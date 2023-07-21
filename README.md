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
    <a href="https://pypi.org/project/fast-depend" target="_blank">
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
There is a total of 23 container
container id   status     container name                   memory          cpu
bab1089dc3df   running    elasticsearch_exporter         12.45 MB        0.00%
a561837b3640   running    elk-cerebro                   448.05 MB        0.86%
f0f9bff03341   running    elk-elasticsearch-7              5.3 GB       16.75%
21d022734daf   running    elk-kibana-7                   319.3 MB        3.58%
751467051c58   running    gitlab                           8.2 GB       41.65%
c594dcd36a14   running    grafana                        56.31 MB        0.13%
717ab36294e0   running    milvus-etcd                    92.39 MB        1.16%
856bb706d9e8   running    milvus-minio                  145.28 MB        0.29%
4a73f5df0bc9   running    milvus-standalone               1.37 GB        9.50%
6c8e1058bd57   running    minikube                      343.43 MB        0.08%
b768a2a4d9af   running    mongo-express                  41.08 MB        0.03%
cfe1ae642072   running    mongodb                       150.66 MB        1.11%
85fd1dcf90cb   running    mysql8                        417.11 MB        0.59%
e4a84961e1d7   running    prometheus                     51.49 MB        0.19%
8641438e3b4d   running    public_minio                    1.92 GB        0.24%
b4aec98ee394   running    rabbitmq3-management           122.4 MB        2.64%
e0f2cbb05d47   running    rebloom                        13.14 MB        0.23%
1cd01a299204   running    zilliz_attu                   112.78 MB        0.02%
```

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
