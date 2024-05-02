from typing import TypeAlias, Any

import GPUtil
from tabulate import tabulate

from shared.print_header import print_section_header

GPU_Info: TypeAlias = list[tuple[Any, str, str, str, str, str, str, Any]]

def get_gpu_info() -> GPU_Info:
    list_gpus = []
    gpus = GPUtil.getGPUs()

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load * 100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    return list_gpus

def print_gpu_info(gpu_list: GPU_Info):
    print()
    print_section_header("GPU Information")

    if gpu_list is None or len(gpu_list) == 0:
        print("*Note*: None physical GPU detected! \n")

    else:
        print(tabulate(gpu_list,
                       headers=("ID", "Name", "Load", "Free Memory", "Used Memory",
                                "Total Memory", "Temperature", "UUID")))
