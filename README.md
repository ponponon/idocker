# idocker

<p align="center">
    <!-- <a href="https://github.com/ponponon/idocker/actions/workflows/tests.yml" target="_blank">
        <img src="https://github.com/ponponon/idocker/actions/workflows/tests.yml/badge.svg" alt="Tests coverage"/>
    </a>
    <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/lancetnik/idocker" target="_blank">
        <img src="https://coverage-badge.samuelcolvin.workers.dev/lancetnik/idocker.svg" alt="Coverage">
    </a> -->
    <a href="https://pypi.org/project/idocker" target="_blank">
        <img src="https://img.shields.io/pypi/v/idocker?label=pypi%20package" alt="Package version">
    </a>
    <a href="https://pepy.tech/project/idocker" target="_blank">
        <img src="https://static.pepy.tech/personalized-badge/idocker?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" alt="downloads"/>
    </a>
    <br/>
    <a href="https://pypi.org/project/idocker" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/idocker.svg" alt="Supported Python versions">
    </a>
    <a href="https://github.com/ponponon/idocker/blob/master/LICENSE" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/github/license/ponponon/idocker?color=%23007ec6">
    </a>
</p>

[简体中文](./README.zh-CN.md) | [English](./README.md)

## Introduce

This tool is a supplement to docker's official command line tool and can output container information in a human-friendly way to increase readability

⭐️ 🌟 ✨ ⚡️ ☄️ 💥

## Installation

Package is uploaded on PyPI: [idocker](https://pypi.org/project/idocker/)

You can install it with pip:

```shell
pip install idocker
```

## Requirements

- Python : 3.8 and newer
- Make sure you have docker installed on your machine

## Documentation

📄 Intensified preparation in progress

## Example

### View container running information

Enter the command in the terminal: `idocker ps`

The following output is obtained

```shell
There is a total of 17 container
| id           | status     | name                 | memory    |   cpu (%) |
|:-------------|:-----------|:---------------------|:----------|----------:|
| f96ba3157d97 | ⭕️ exited  | mystifying_kapitsa   | 0.0 MB    |     0     |
| 1647f82f4f5d | ⭕️ exited  | hardcore_benz        | 0.0 MB    |     0     |
| d34a102050d3 | ⭕️ exited  | minikube             | 0.0 MB    |     0     |
| 62e74fb7138e | ⭕️ exited  | nginx                | 0.0 MB    |     0     |
| 21b45572fd50 | ⭕️ exited  | thirsty_stonebraker  | 0.0 MB    |     0     |
| 3a7729ee272b | ⭕️ exited  | sad_lalande          | 0.0 MB    |     0     |
| 16e49729de2d | ⭕️ exited  | twitter_redis        | 0.0 MB    |     0     |
| 98df9168bbd5 | ⭕️ exited  | rustdesk-hbbr        | 0.0 MB    |     0     |
| bf19958f710f | ⭕️ exited  | rustdesk-hbbs        | 0.0 MB    |     0     |
| 874838b6335d | ⭕️ exited  | twitter_mysql8       | 0.0 MB    |     0     |
| 57469356f55b | ⭕️ exited  | heuristic_northcutt  | 0.0 MB    |     0     |
| 6fd8b4c901f1 | ⭕️ exited  | competent_ritchie    | 0.0 MB    |     0     |
| cb0ef103c8f6 | ✅ running | twitter_memcahed     | 5.57 MB   |     0.007 |
| aa291a307aac | ✅ running | rebloom              | 8.65 MB   |     0.098 |
| 1e08693fdcfd | ✅ running | public_minio         | 108.28 MB |     0.055 |
| 7b411cf33283 | ✅ running | rabbitmq3-management | 144.1 MB  |     0.556 |
| c50ca07d3d41 | ✅ running | mysql8               | 282.34 MB |     0.339 |
```

> By default, the sorting is in ascending order of memory usage

If you want to change the default sorting, you can see the help information 'idocker ps --help'

```shell
Usage: python -m idocker.cli.main ps [OPTIONS]

  view all container

Options:
  --id              Sort by id
  --status          Sort by id
  --name            Sort by name
  --cpu             Sort by cpu stats usage
  --mem             Sort by memory stats usage  [default: True]
  -i, --image_name  Show Image name
  --help            Show this message and exit.

```

For example, if you want to know which containers are using the most cpu, you can type 'idocker ps --cpu' and it will be sorted in ascending order of cpu usage

```shell
There is a total of 17 container
| id           | status     | name                 | memory    |   cpu (%) |
|:-------------|:-----------|:---------------------|:----------|----------:|
| f96ba3157d97 | ⭕️ exited  | mystifying_kapitsa   | 0.0 MB    |     0     |
| d34a102050d3 | ⭕️ exited  | minikube             | 0.0 MB    |     0     |
| 62e74fb7138e | ⭕️ exited  | nginx                | 0.0 MB    |     0     |
| 57469356f55b | ⭕️ exited  | heuristic_northcutt  | 0.0 MB    |     0     |
| 16e49729de2d | ⭕️ exited  | twitter_redis        | 0.0 MB    |     0     |
| 21b45572fd50 | ⭕️ exited  | thirsty_stonebraker  | 0.0 MB    |     0     |
| 1647f82f4f5d | ⭕️ exited  | hardcore_benz        | 0.0 MB    |     0     |
| 3a7729ee272b | ⭕️ exited  | sad_lalande          | 0.0 MB    |     0     |
| bf19958f710f | ⭕️ exited  | rustdesk-hbbs        | 0.0 MB    |     0     |
| 6fd8b4c901f1 | ⭕️ exited  | competent_ritchie    | 0.0 MB    |     0     |
| 874838b6335d | ⭕️ exited  | twitter_mysql8       | 0.0 MB    |     0     |
| 98df9168bbd5 | ⭕️ exited  | rustdesk-hbbr        | 0.0 MB    |     0     |
| cb0ef103c8f6 | ✅ running | twitter_memcahed     | 5.57 MB   |     0.007 |
| 1e08693fdcfd | ✅ running | public_minio         | 107.95 MB |     0.054 |
| aa291a307aac | ✅ running | rebloom              | 8.63 MB   |     0.098 |
| c50ca07d3d41 | ✅ running | mysql8               | 281.5 MB  |     0.338 |
| 7b411cf33283 | ✅ running | rabbitmq3-management | 143.62 MB |     0.553 |
```

Note that cpu 100% does not mean that 100% of the whole machine is consumed, but 100% of the single core

### View container port information

Enter the command in the terminal: `idocker port`

The following output is obtained

```shell
There is a total of 3 container
elk-kibana-7
    Host     -> Container
    5601     -> 5601
    5601     -> 5601

elk-elasticsearch-7
    Host     -> Container
    9200     -> 9200
    9200     -> 9200
    9300     -> 9300
    9300     -> 9300

rebloom
    Host     -> Container
    6379     -> 6379
    6379     -> 6379
```
