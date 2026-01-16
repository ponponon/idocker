from typing import List, Dict, Optional
from concurrent.futures.thread import ThreadPoolExecutor
import click
import docker
from rich.console import Console
from docker.models.containers import Container


def removeprefix(s: str, prefix: str) -> str:
    if s.startswith(prefix):
        return s[len(prefix):]
    else:
        return s


console = Console()


@click.group()
def idocker_cli():
    pass


@idocker_cli.command()
@click.option('--id', type=bool, is_flag=True,  show_default=True, default=False, help='Sort by id')
@click.option('--status', type=bool, is_flag=True,  show_default=True, default=False, help='Sort by id')
@click.option('--name', type=bool, is_flag=True, show_default=True, default=False, help='Sort by name')
@click.option('--cpu', type=bool, is_flag=True, show_default=True, default=False, help='Sort by cpu stats usage')
@click.option('--mem', type=bool, is_flag=True,  show_default=True, default=False, help='Sort by memory stats usage')
@click.option('-i', '-a', '--image_name', type=bool, is_flag=True,  show_default=True, default=False, help='Show Image name')
def ps(
    id: bool = False,
    status: bool = False,
    name: bool = True,
    cpu: bool = False,
    mem: bool = False,
    image_name: bool = False,
):
    """ view all container """
    if not status and not name and not cpu and not mem:
        mem = True

    def get_container_info(container: Container):
        short_id: str = container.short_id
        status: str = container.attrs['State']['Status']
        name: str = container.attrs['Name']
        restart_count: str = container.attrs['RestartCount']

        from docker.models.images import Image

        image: Image = container.image

        image_name = image.tags[0] if image.tags else image.short_id

        stats_stream = container.stats(decode=True)
        _ = stats_stream.__next__()
        container_stats: Dict = stats_stream.__next__()

        if not container_stats['memory_stats'].get('usage', None):
            mb = 0
        else:
            mb = float(container_stats['memory_stats']['usage'])-float(
                container_stats['memory_stats']['stats']['inactive_file'])

        if status == 'running':
            status = '✅ '+status
            cpu_stats = container_stats['cpu_stats']
            cpu_total_usage = cpu_stats['cpu_usage']['total_usage']
            cpu_system_usage = cpu_stats['system_cpu_usage']

            precpu_stats = container_stats['precpu_stats']
            precpu_total_usage = precpu_stats['cpu_usage']['total_usage']
            precpu_system_usage = precpu_stats['system_cpu_usage']

            nb_core = container_stats['cpu_stats']['online_cpus']
            cpu_delta = cpu_total_usage - precpu_total_usage
            system_cpu_delta = cpu_system_usage - precpu_system_usage

            cpu_usage = (cpu_delta / system_cpu_delta) * nb_core * 100.0

            cpu_stats__usage: float = round(cpu_usage, 3)
        else:
            status = '⭕️ '+status
            cpu_stats__usage = 0

        if restart_count > 0:
            status = f'{status}({restart_count})'

        containers_info.append(
            [
                short_id,
                status,
                removeprefix(name, '/'),
                mb,
                cpu_stats__usage,
                image_name
            ]
        )

    client = docker.from_env()

    containers = client.containers.list(all=True)

    console.print(f'There is a total of {len(containers)} container')

    containers_info: List[List[str]] = []

    pool = ThreadPoolExecutor(max_workers=30)

    for container in containers[:]:
        pool.submit(get_container_info, container)

    pool.shutdown(wait=True)

    if id:
        containers_info.sort(key=lambda x: x[0])
    if status:
        containers_info.sort(key=lambda x: x[1])
    if name:
        containers_info.sort(key=lambda x: x[2])
    if mem:
        containers_info.sort(key=lambda x: x[3])
    if cpu:
        containers_info.sort(key=lambda x: x[4])

    from tabulate import tabulate

    for ci in containers_info:
        mb = ci[3]/1024/1024
        if mb < 1024:
            memory_stats__usage: str = f'{round(mb,2)} MB'
        else:
            memory_stats__usage: str = f'{round(mb/1024,2)} GB'
        ci[3] = memory_stats__usage
    if image_name:
        print(tabulate(containers_info, headers=[
            "id", "status", "name", 'memory', 'cpu (%)', 'image'], tablefmt="pipe"))
    else:
        print(tabulate([i[:-1] for i in containers_info], headers=[
            "id", "status", "name", 'memory', 'cpu (%)'], tablefmt="pipe"))


@idocker_cli.command()
def port():
    client = docker.from_env()

    containers: List[Container] = client.containers.list(all=True)

    console.print(f'There is a total of {len(containers)} container')

    for container in containers:
        try:
            container_info = client.containers.get(container.id)
            # ports like:
            # - {'3000/tcp': [{'HostIp': '0.0.0.0', 'HostPort': '8000'}, {'HostIp': '::', 'HostPort': '8000'}]}
            # - {'2379/tcp': None, '2380/tcp': None}
            ports = container_info.attrs['NetworkSettings']['Ports']

            ports: Dict[str, Optional[List[Dict[str, str]]]]

            console.print(container.name, style="#c2a064")

            if not ports:
                console.print("    no network config", style='#c85662')
                continue

            console.print(
                f"    {'Host'.ljust(8, ' ')} -> {'Container'.ljust(8, ' ')}", style='#62ae90')
            for port in ports:
                mappings = ports.get(port, [])
                if not mappings:
                    # console.print("    no port bind")
                    continue
                for mapping in mappings:
                    host_port = f"{mapping['HostPort']}".ljust(8, ' ')
                    container_port = f"{mapping['HostPort']}".ljust(8, ' ')
                    console.print(f"    {host_port} -> {container_port}")

        finally:
            print()


@idocker_cli.command()
@click.argument('container_name', type=str)
@click.option('--tail', type=int, default=300, show_default=True, help='Number of lines to show from the end')
@click.option('--no-follow', 'follow', is_flag=True, default=True, help='Do not follow output')
def logs(container_name: str, tail: int = 300, follow: bool = True):
    """View container logs (default: show last 300 lines and follow)"""
    client = docker.from_env()

    try:
        container = client.containers.get(container_name)
    except docker.errors.NotFound:
        console.print(
            f"Container '{container_name}' not found", style='#c85662')
        return

    console.print(
        f"Showing logs for container: [bold]{container.name}[/bold]", style='#62ae90')

    logs_stream = container.logs(
        stream=True,
        follow=follow,
        tail=tail
    )

    for line in logs_stream:
        print(line.decode('utf-8').rstrip())


cli = click.CommandCollection(sources=[idocker_cli])

if __name__ == '__main__':
    cli()
