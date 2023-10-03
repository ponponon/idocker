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

## 介绍

这个工具是 docker 官方命令行工具的补充版本，可以人类友好的方式输出容器信息，增加可读性

⭐️ 🌟 ✨ ⚡️ ☄️ 💥

## 安装

软件包已经上传到 PyPI: [idocker](https://pypi.org/project/idocker/)

可以直接使用 pip 安装:

```shell
pip install idocker
```

## 依赖

- Python : 3.8 及以上
- 确保你的机器已经安装了 docker

## 文档

📄 暂无

## 示例

### 查看容器运行状态

可以在终端输入: `idocker ps`

输出如下：

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

> 默认按照内存占用升序排序

如果你想修改默认的排序方式，可以查看帮助信息 `idocker  ps --help`

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

比如你希望知道哪些容器占用的 cpu 最多，可以输入 `idocker ps --cpu`, 这样就会按照 cpu 使用率升序排序

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

> 注意, cpu 100% 并不是表示消耗了整机的 100%，而是单核的 100%

有的时候，我们好像知道容器对应的镜像名称，可以加上 `-i` 或者 `--image_name` 参数来同时显示镜像名称

```shell
╰─➤  idocker ps -i
There is a total of 21 container
| id           | status     | name                 | memory    |   cpu (%) | image                                    |
|:-------------|:-----------|:---------------------|:----------|----------:|:-----------------------------------------|
| 16e49729de2d | ⭕️ exited  | twitter_redis        | 0.0 MB    |     0     | redis:latest                             |
| 62e74fb7138e | ⭕️ exited  | nginx                | 0.0 MB    |     0     | nginx:latest                             |
| 3a7729ee272b | ⭕️ exited  | sad_lalande          | 0.0 MB    |     0     | 192.168.31.245:8081/python:3.10-buster   |
| 98df9168bbd5 | ⭕️ exited  | rustdesk-hbbr        | 0.0 MB    |     0     | rustdesk/rustdesk-server:1.1.6           |
| d34a102050d3 | ⭕️ exited  | minikube             | 0.0 MB    |     0     | kicbase/stable:v0.0.36                   |
| 1647f82f4f5d | ⭕️ exited  | hardcore_benz        | 0.0 MB    |     0     | ubuntu:latest                            |
| 6fd8b4c901f1 | ⭕️ exited  | competent_ritchie    | 0.0 MB    |     0     | ubuntu:latest                            |
| 874838b6335d | ⭕️ exited  | twitter_mysql8       | 0.0 MB    |     0     | mysql:8.0                                |
| f96ba3157d97 | ⭕️ exited  | mystifying_kapitsa   | 0.0 MB    |     0     | sha256:b7fb33a5a7bb                      |
| 57469356f55b | ⭕️ exited  | heuristic_northcutt  | 0.0 MB    |     0     | 192.168.31.245:8081/python:3.10-buster   |
| 21b45572fd50 | ⭕️ exited  | thirsty_stonebraker  | 0.0 MB    |     0     | sha256:b7fb33a5a7bb                      |
| bf19958f710f | ⭕️ exited  | rustdesk-hbbs        | 0.0 MB    |     0     | rustdesk/rustdesk-server:1.1.6           |
| cb0ef103c8f6 | ✅ running | twitter_memcahed     | 2.09 MB   |     0.008 | memcached:latest                         |
| aa291a307aac | ✅ running | rebloom              | 5.74 MB   |     0.104 | redislabs/rebloom:latest                 |
| 84ef73971e0d | ✅ running | zilliz_attu          | 75.91 MB  |     0.022 | zilliz/attu:v2.2.7                       |
| 75f08019e787 | ✅ running | milvus-etcd          | 77.74 MB  |     0.688 | quay.io/coreos/etcd:v3.5.5               |
| 98c1082f8e5b | ✅ running | milvus-minio         | 87.07 MB  |     0.098 | minio/minio:RELEASE.2022-03-17T06-34-49Z |
| 78e26a299331 | ✅ running | public_minio         | 133.05 MB |     0.11  | minio/minio:RELEASE.2023-09-04T19-57-37Z |
| 7b411cf33283 | ✅ running | rabbitmq3-management | 156.2 MB  |     0.477 | rabbitmq:3-management                    |
| e2618c7ec2ec | ✅ running | milvus-standalone    | 317.84 MB |     4.369 | milvusdb/milvus:v2.2.9                   |
| c50ca07d3d41 | ✅ running | mysql8               | 739.54 MB |     1.026 | mysql:8                                  |
```

### 查看容器绑定的端口信息

可以在终端输入: `idocker port`

输出如下：

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
