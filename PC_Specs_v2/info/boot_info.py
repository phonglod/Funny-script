import psutil
from datetime import datetime
from shared.print_header import print_section_header

def get_boot_info() -> datetime:
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return bt

def print_boot_info(boot_info: datetime):
    print()
    print_section_header("Boot Time")
    bt = boot_info
    print(f"  Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
