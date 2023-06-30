# idocker

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
