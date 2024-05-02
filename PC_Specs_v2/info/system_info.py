import platform
import requests
from typing import TypeAlias, Any
from shared.print_header import print_section_header

SystemInfo: TypeAlias = dict[str, platform.uname_result | str]

def get_system_info() -> SystemInfo:
    uname: platform.uname_result = platform.uname()
    ipv4_address: str = requests.get('https://api.ipify.org').text
    ipv6_address: str = requests.get('https://api6.ipify.org').text

    return {
        "uname": uname,
        "ipv4": ipv4_address,
        "ipv6": ipv6_address
    }

def print_system_info(system_info: SystemInfo, cpu_info: dict[str, Any]):
    print()
    print_section_header("System Information")

    uname = system_info['uname']
    print(f"  System: {uname.system}")
    print(f"  Device Name: {uname.node}")
    print(f"  Release: {uname.release}")
    print(f"  Version: {uname.version}")
    print(f"  Machine: {uname.machine}")

    print(f"  Processor: {cpu_info['brand_raw']}")
    print(f"  CPU Version: {cpu_info['cpuinfo_version_string']}")

    print(f"  IPv4 Address: {system_info['ipv4']}")
    print(f"  IPv6 Address: {system_info['ipv6']}")
