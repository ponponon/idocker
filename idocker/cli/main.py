
from typing import List, Dict
from concurrent.futures.thread import ThreadPoolExecutor
import click
import docker
from docker.models.containers import Container


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

        containers_info.append(
            [
                short_id,
                status.ljust(8, " "),
                name.ljust(25, " "),
                memory_stats__usage.rjust(10, " "),
            ]
        )

    client = docker.from_env()

    containers = client.containers.list(all=True)

    print(f'There is a total of {len(containers)} container')

    containers_info: List[List[str]] = []

    pool = ThreadPoolExecutor(max_workers=10)

    for container in containers[:]:
        pool.submit(get_container_info, container)

    pool.shutdown(wait=True)

    containers_info.sort(key=lambda x: x[2])

    for container_info in containers_info:
        print('   '.join(container_info))


cli = click.CommandCollection(sources=[idocker_cli])

if __name__ == '__main__':
    cli()
