from typing import List, Dict
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
def ps():
    """ view all container """
    def get_container_info(container: Container):
        short_id: str = container.short_id
        status: str = container.attrs['State']['Status']
        name: str = container.attrs['Name']

        container_stats: Dict = container.stats(decode=True).__next__()

        if not container_stats['memory_stats'].get('usage', None):
            memory_stats__usage = 'None'
        else:
            mb = container_stats['memory_stats']['usage']/1024/1024

            if mb < 1024:
                memory_stats__usage: str = f'{round(mb,2)} MB'
            else:
                memory_stats__usage: str = f'{round(mb/1024,2)} GB'

        cpu_usage = container_stats['cpu_stats']['cpu_usage']['total_usage']
        system_cpu_usage = container_stats['cpu_stats']['system_cpu_usage']
        cpu_percent = (cpu_usage / system_cpu_usage) * 100
        cpu_count = container_stats['cpu_stats']['online_cpus']
        cpu_stats__usage = f"{cpu_percent*cpu_count:.2f}%"

        containers_info.append(
            [
                short_id,
                status.ljust(8, " "),
                removeprefix(name.ljust(27, " "), '/'),
                memory_stats__usage.rjust(10, " "),
                cpu_stats__usage.rjust(10, " "),
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

    containers_info.sort(key=lambda x: x[2])

    containers_info.insert(
        0, [
            'container id',
            'status'.ljust(8, " "),
            removeprefix('container name'.ljust(26, " "), '/'),
            'memory'.rjust(10, " "),
            'cpu'.rjust(10, " "),
        ])

    for container_info in containers_info:
        console.print('   '.join(container_info))


cli = click.CommandCollection(sources=[idocker_cli])

if __name__ == '__main__':
    cli()
