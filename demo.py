from typing import List, Dict
from concurrent.futures.thread import ThreadPoolExecutor
import json
import docker
from docker.models.containers import Container

client = docker.from_env()

containers = client.containers.list()

containers_info: List[List[str]] = []

pool = ThreadPoolExecutor(max_workers=10)


def get_container_info(container: Container):
    container_stats: Dict = container.stats(decode=True).__next__()

    mb = container_stats['memory_stats']['usage']/1024/1024

    if mb < 1024:
        memory_stats__usage: str = f'{round(mb,2)} MB'
    else:
        memory_stats__usage: str = f'{round(mb/1024,2)} GB'

    short_id: str = container.short_id
    status: str = container.attrs['State']['Status']
    name: str = container.attrs['Name']

    containers_info.append(
        [
            short_id,
            status,
            name.ljust(25, " "),
            memory_stats__usage.rjust(10, " "),
        ]
    )


for container in containers[:]:
    pool.submit(get_container_info, container)

pool.shutdown(wait=True)

for container_info in containers_info:
    print('   '.join(container_info))
