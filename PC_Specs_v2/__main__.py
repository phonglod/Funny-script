"""
WARNING: Before you run this script you need to run the command below in cmd to use properly

Command: <"python.exe -m pip install psutil GPUtil py-cpuinfo wmi setuptools tabulate datetime requests geocoder>"
"""

import threading ,time ,progressbar
from multiprocessing.pool import ThreadPool

from info.boot_info import get_boot_info, print_boot_info
from info.cpu_info import get_cpu_info, print_cpu_info
from info.gpu_info import print_gpu_info, get_gpu_info
from info.location_info import get_location_info, print_location_info
from info.memory_info import print_memory_info, print_swap_info, get_memory_info, print_disk_info
from info.network_info import print_network_info, get_network_info
from info.system_info import get_system_info, print_system_info

def print_program_header():
    print(f"SYSTEM: Packages ready")
    print(r"""
    CREATOR:
    ██████╗░██╗░░██╗░█████╗░███╗░░██╗░██████╗░  ██╗░░░░░░█████╗░██████╗░
    ██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝░  ██║░░░░░██╔══██╗██╔══██╗
    ██████╔╝███████║██║░░██║██╔██╗██║██║░░██╗░  ██║░░░░░██║░░██║██║░░██║
    ██╔═══╝░██╔══██║██║░░██║██║╚████║██║░░╚██╗  ██║░░░░░██║░░██║██║░░██║
    ██║░░░░░██║░░██║╚█████╔╝██║░╚███║╚██████╔╝  ███████╗╚█████╔╝██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░
    """)
    print("\n****************************************************************")
    print("\n*Creator: phonglod(https://github.com/phonglod)                *")
    print("\n*Contributor: FDIL(https://github.com/FDIL501st)               *")
    print("\n*https://www.youtube.com/@BruceLee19991                        *")
    print("\n****************************************************************")

def loading_animation(event: threading.Event):
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    while not event.is_set():
        time.sleep(0.5)
        bar.update(1)

print_program_header()

loading_done_event: threading.Event = threading.Event()

pool: ThreadPool = ThreadPool(processes=2)

pool.apply_async(func=loading_animation, args=(loading_done_event,))
get_CPU_thread = pool.apply_async(func=get_cpu_info)

CPU_info = get_CPU_thread.get()

loading_done_event.set()

pool.close()
pool.join()
sys_info = get_system_info()
print_system_info(sys_info, CPU_info[0])

loc_info = get_location_info()
print_location_info(loc_info)

bt_info = get_boot_info()
print_boot_info(bt_info)

print_cpu_info(CPU_info)

vmem, swap, disk_partitions, dsk_io = get_memory_info()
print_memory_info(vmem)

print_swap_info(swap)

print_disk_info(disk_partitions, dsk_io)

network_info = get_network_info()
print_network_info(network_info)

gpu_info = get_gpu_info()
print_gpu_info(gpu_info)

# debug section
# print(f"Processor: {cpuinfo.get_cpu_info()}")

input("\nPress enter to close \n>>>")
