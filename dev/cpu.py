import docker
import json
from docker.models.containers import Container


def get_cpu_usage(container_id):
    client = docker.from_env()
    container: Container = client.containers.get(container_id)

    # Get container stats
    stats_stream = container.stats()
    next(stats_stream)
    try:
        while True:
            # Retrieve the first data point (current stats)
            stats_data = next(stats_stream)

            # Decode bytes to string and load JSON
            stats_data_str = stats_data.decode('utf-8')
            stats_data_json = json.loads(stats_data_str)

            # print('>>>',calculate_cpu_percent2(stats_data_json))

            # Extract CPU usage information
            cpu_stats = stats_data_json['cpu_stats']
            cpu_total_usage = cpu_stats['cpu_usage']['total_usage']
            cpu_system_usage = cpu_stats['system_cpu_usage']

            # Extract CPU usage information
            precpu_stats = stats_data_json['precpu_stats']
            precpu_total_usage = precpu_stats['cpu_usage']['total_usage']
            precpu_system_usage = precpu_stats['system_cpu_usage']

            cpu_delta = cpu_total_usage - precpu_total_usage
            system_cpu_delta = cpu_system_usage - precpu_system_usage

            nb_core = 16

            # Calculate CPU usage percentage
            cpu_usage = (cpu_delta / system_cpu_delta) * nb_core * 100.0
            # print(stats_data_json['precpu_stats'])
            print(f"CPU Usage of Container {container_id}: {cpu_usage:.2f}%")
    finally:
        # Close the stream when done
        stats_stream.close()


# this is taken directly from docker client:
#   https://github.com/docker/docker/blob/28a7577a029780e4533faf3d057ec9f6c7a10948/api/client/stats.go#L309
def calculate_cpu_percent(d):
    cpu_count = len(d["cpu_stats"]["cpu_usage"]["percpu_usage"])
    cpu_percent = 0.0
    cpu_delta = float(d["cpu_stats"]["cpu_usage"]["total_usage"]) - \
        float(d["precpu_stats"]["cpu_usage"]["total_usage"])
    system_delta = float(d["cpu_stats"]["system_cpu_usage"]) - \
        float(d["precpu_stats"]["system_cpu_usage"])
    if system_delta > 0.0:
        cpu_percent = cpu_delta / system_delta * 100.0 * cpu_count
    return cpu_percent

# again taken directly from docker:
#   https://github.com/docker/cli/blob/2bfac7fcdafeafbd2f450abb6d1bb3106e4f3ccb/cli/command/container/stats_helpers.go#L168
# precpu_stats in 1.13+ is completely broken, doesn't contain any values


def calculate_cpu_percent2(d, previous_cpu, previous_system):
    # import json
    # du = json.dumps(d, indent=2)
    # logger.debug("XXX: %s", du)
    cpu_percent = 0.0
    cpu_total = float(d["cpu_stats"]["cpu_usage"]["total_usage"])
    cpu_delta = cpu_total - previous_cpu
    cpu_system = float(d["cpu_stats"]["system_cpu_usage"])
    system_delta = cpu_system - previous_system
    online_cpus = d["cpu_stats"].get("online_cpus", len(
        d["cpu_stats"]["cpu_usage"].get("percpu_usage", [None])))
    if system_delta > 0.0:
        cpu_percent = (cpu_delta / system_delta) * online_cpus * 100.0
    return cpu_percent, cpu_system, cpu_total


# Example usage
container_id = "2351c2dbe9c7"
cpu_usage = get_cpu_usage(container_id)
print(f"CPU Usage of Container {container_id}: {cpu_usage:.2f}%")
