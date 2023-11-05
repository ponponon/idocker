from typing import List, Dict, Optional
from concurrent.futures.thread import ThreadPoolExecutor
import click
import docker
from rich.console import Console
from docker.models.containers import Container
import json


def get_container_info(container: Container):
    short_id: str = container.short_id
    status: str = container.attrs['State']['Status']
    name: str = container.attrs['Name']

    from docker.models.images import Image

    image: Image = container.image

    image_name = image.tags[0] if image.tags else image.short_id

    container_stats: Dict = container.stats(decode=True).__next__()

    # print(json.dumps(container_stats, indent=4))


client = docker.from_env()


container = client.containers.get('1ed0dc5ac54e')

get_container_info(container)

# print(json.dumps(container.attrs,indent=4,ensure_ascii=False))

# print(container.client)
# print(container.collection)
# print(json.dumps(container.client,indent=4,ensure_ascii=False))
# print(json.dumps(container.collection,indent=4,ensure_ascii=False))
