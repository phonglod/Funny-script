'''
WARNING: Before you run this script you need to run the command below in cmd to use properly

Command: <"pip install psutil GPUtil py-cpuinfo wmi setuptools tabulate datetime requests geocoder>"
'''
import subprocess, sys, platform, os
import psutil, GPUtil, cpuinfo, wmi, distutils.core, setuptools, requests, geocoder
from datetime import datetime
from tabulate import tabulate

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
print("\n* Copyright of Phong, 2024                                     *")
print("\n* https://www.youtube.com/@BruceLee19991                       *")
print("\n****************************************************************")

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print()
print("="*40, "System Information", "="*40, "\n")
uname = platform.uname()
print(f"  System: {uname.system}")
print(f"  Device Name: {uname.node}")
print(f"  Release: {uname.release}")
print(f"  Version: {uname.version}")
print(f"  Machine: {uname.machine}")
print(f"  Processor: {cpuinfo.get_cpu_info()['brand_raw']}")
print(f"  CPU Version: {cpuinfo.get_cpu_info()['cpuinfo_version_string']}")
print(f"  IPv4 Address: {requests.get('https://api.ipify.org').text}")
print(f"  IPv6 Address: {requests.get('https://api6.ipify.org').text}")

print()
print("="*40, "Location Information", "="*40, "\n")
g = geocoder.ip('me')
latitude = g.latlng[0]
longitude = g.latlng[1]
lat_dir = 'N' if latitude >= 0 else 'S'
long_dir = 'E' if longitude >= 0 else 'W'
lat_deg, lat_remainder = divmod(abs(latitude), 1)
lat_min, lat_sec = divmod(lat_remainder * 60, 1)
lat_sec *= 60
long_deg, long_remainder = divmod(abs(longitude), 1)
long_min, long_sec = divmod(long_remainder * 60, 1)
long_sec *= 60
cordness = f"{int(lat_deg)}° {int(lat_min)}' {lat_sec:.2f}\" {lat_dir}, {int(long_deg)}° {int(long_min)}' {long_sec:.2f}\" {long_dir}"
isp = g.org
hostname = g.hostname
country = g.country
region = g.state
city = g.city
timezone = datetime.now().astimezone().tzinfo
location_info = {
    'ISP': isp,
    'Hostname': hostname,
    'Country': country,
    'Region/State': region,
    'City': city,
    'Latitude': latitude,
    'Longitude': longitude,
    'Coordinates': cordness,
    'Timezone': timezone,
}
print("  Location Information:")
for key, value in location_info.items():
    print(f"  {key}: {value}")

print()
print("="*40, "Boot Time", "="*40, "\n")
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"  Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

print()
print("="*40, "CPU Information", "="*40, "\n")
print("  Physical cores:", psutil.cpu_count(logical=False))
print("  Total cores:", psutil.cpu_count(logical=True))
print(f"  CPU Arch: {cpuinfo.get_cpu_info()['arch']}")
print(f"  CPU Bits: {cpuinfo.get_cpu_info()['bits']}")
cpufreq = psutil.cpu_freq()
print(f"  Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"  Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"  Current Frequency: {cpufreq.current:.2f}Mhz")
print("  CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"  Core {i}: {percentage}%")
print(f"  Total CPU Usage: {psutil.cpu_percent()}%")

print()
print("="*40, "Memory Information", "="*40, "\n")
svmem = psutil.virtual_memory()
print(f"  Total: {get_size(svmem.total)}")
print(f"  Available: {get_size(svmem.available)}")
print(f"  Used: {get_size(svmem.used)}")
print(f"  Percentage: {svmem.percent}%")
print()
print("="*40, "SWAP Information", "="*40, "\n")
swap = psutil.swap_memory()
print(f"  Total: {get_size(swap.total)}")
print(f"  Free: {get_size(swap.free)}")
print(f"  Used: {get_size(swap.used)}")
print(f"  Percentage: {swap.percent}%")

print()
print("="*40, "Disk Information", "="*40, "\n")
print("  Partitions and Usage:")
partitions = psutil.disk_partitions()
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
disk_io = psutil.disk_io_counters()
print()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")

print()
print("="*40, "Network Information", "="*40, "\n")
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")

network_adapter_info = wmi.WMI().Win32_NetworkAdapter(NetEnabled=True)
network_adapter_info_list = []
for network_adapter in network_adapter_info:
    network_adapter_name = network_adapter.Name
    network_adapter_description = network_adapter.Description
    network_adapter_mac_address = network_adapter.MACAddress
    network_adapter_speed = network_adapter.Speed
    network_adapter_info_list.append((network_adapter_name, network_adapter_description, network_adapter_mac_address, network_adapter_speed))
print()
print("Network Adapter Information: ")
print()
for network_adapter in network_adapter_info_list:
    print("  Name:", network_adapter[0])
    print("  Description:", network_adapter[1])
    print("  MAC Address:", network_adapter[2])
    print("  Speed:", get_size(int(network_adapter[3])))

wmi_service = wmi.WMI()
ip_address = wmi_service.Win32_NetworkAdapterConfiguration(IPEnabled=True)[0].IPAddress[0]
print("  Internet IP address:", ip_address)

net_io = psutil.net_io_counters()
print(f"  Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"  Total Bytes Received: {get_size(net_io.bytes_recv)}")

print()
print("="*40, "GPU Information", "="*40, "\n")
gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:
    gpu_id = gpu.id
    gpu_name = gpu.name
    gpu_load = f"{gpu.load*100}%"
    gpu_free_memory = f"{gpu.memoryFree}MB"
    gpu_used_memory = f"{gpu.memoryUsed}MB"
    gpu_total_memory = f"{gpu.memoryTotal}MB"
    gpu_temperature = f"{gpu.temperature} °C"
    gpu_uuid = gpu.uuid
    list_gpus.append((
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
        gpu_total_memory, gpu_temperature, gpu_uuid
    ))
print(tabulate(list_gpus, headers=("ID", "Name", "Load", "Free Memory", "Used Memory", "Total Memory","Temperature", "UUID")))
if list_gpus == None:
    print("*Note*: None physical GPU detected! \n")

#debug section
#print(f"Processor: {cpuinfo.get_cpu_info()}")

input("\nPress enter to close \n>>>")
