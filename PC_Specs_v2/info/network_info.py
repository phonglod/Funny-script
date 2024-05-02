import psutil
import wmi
from shared.bytes import get_size
from shared.print_header import print_section_header

def get_network_info():
    network_interface_addresses = psutil.net_if_addrs()
    wmi_service = wmi.WMI()
    net_io = psutil.net_io_counters()

    return (network_interface_addresses,
            wmi_service.Win32_NetworkAdapter(NetEnabled=True),
            wmi_service.Win32_NetworkAdapterConfiguration(IPEnabled=True)[0].IPAddress[0],
            net_io)

def print_network_info(network_info):
    print()
    print_section_header("Network Information")

    for interface_name, interface_addresses in network_info[0].items():
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

    network_adapter_info = network_info[1]
    network_adapter_info_list = []
    for network_adapter in network_adapter_info:
        network_adapter_info_list.append(
            (network_adapter.Name, network_adapter.Description,
             network_adapter.MACAddress, network_adapter.Speed))

    print()
    print("Network Adapter Information: ")
    print()
    for network_adapter in network_adapter_info_list:
        print("  Name:", network_adapter[0])
        print("  Description:", network_adapter[1])
        print("  MAC Address:", network_adapter[2])
        print("  Speed:", get_size(int(network_adapter[3])))

    print("  Internet IP address:", network_info[2])

    net_io = network_info[3]
    print(f"  Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"  Total Bytes Received: {get_size(net_io.bytes_recv)}")
