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
@click.option('--mem', type=bool, is_flag=True,  show_default=True, default=True, help='Sort by memory stats usage')
@click.option('-i', '--image_name', type=bool, is_flag=True,  show_default=True, default=False, help='Show Image name')
def ps(
    id: bool = False,
    status: bool = False,
    name: bool = True,
    cpu: bool = False,
    mem: bool = False,
    image_name: bool = False,
):
    """ view all container """
    def get_container_info(container: Container):
        short_id: str = container.short_id
        status: str = container.attrs['State']['Status']
        name: str = container.attrs['Name']

        from docker.models.images import Image

        image: Image = container.image

        image_name = image.tags[0] if image.tags else image.short_id

        container_stats: Dict = container.stats(decode=True).__next__()

        if not container_stats['memory_stats'].get('usage', None):
            mb = 0
        else:
            mb = float(container_stats['memory_stats']['usage'])

        if status == 'running':
            status = '✅ '+status
            cpu_usage = container_stats['cpu_stats']['cpu_usage']['total_usage']
            system_cpu_usage = container_stats['cpu_stats']['system_cpu_usage']
            cpu_percent = (cpu_usage / system_cpu_usage) * 100
            cpu_count = container_stats['cpu_stats']['online_cpus']
            cpu_stats__usage: float = round(cpu_percent*cpu_count, 3)
        else:
            status = '⭕️ '+status
            cpu_stats__usage = 0

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


cli = click.CommandCollection(sources=[idocker_cli])

if __name__ == '__main__':
    cli()
