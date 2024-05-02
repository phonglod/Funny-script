import psutil
from shared.bytes import get_size
from shared.print_header import print_section_header

def get_memory_info():
    return psutil.virtual_memory(), psutil.swap_memory(), psutil.disk_partitions(), psutil.disk_io_counters()

def print_memory_info(vmem):
    print()
    print_section_header("Memory Information")
    print(f"  Total: {get_size(vmem.total)}")
    print(f"  Available: {get_size(vmem.available)}")
    print(f"  Used: {get_size(vmem.used)}")
    print(f"  Percentage: {vmem.percent}%")

def print_swap_info(swap):
    print()
    print_section_header("SWAP Information")
    print(f"  Total: {get_size(swap.total)}")
    print(f"  Free: {get_size(swap.free)}")
    print(f"  Used: {get_size(swap.used)}")
    print(f"  Percentage: {swap.percent}%")

def print_disk_info(partitions, disk_io):
    print()
    print_section_header("Disk Information")

    print("  Partitions and Usage:")
    for partition in partitions:
        print()
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")

    print()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")
