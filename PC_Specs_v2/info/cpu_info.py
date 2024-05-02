import psutil
import cpuinfo
from typing import TypeAlias, Any
from shared.print_header import print_section_header

CPUInfo: TypeAlias = tuple[dict[str, Any], float, float, float, int, int, list[float], float]

def get_cpu_info() -> CPUInfo:
    cpu_info: dict[str, Any] = cpuinfo.get_cpu_info()
    cpufreq = psutil.cpu_freq(percpu=False)
    num_physical_cores: int = psutil.cpu_count(logical=False)
    num_total_cores: int = psutil.cpu_count(logical=True)
    usage_per_core: list[float] = psutil.cpu_percent(percpu=True, interval=1)
    total_usage: float = psutil.cpu_percent()

    return (cpu_info, cpufreq.max, cpufreq.min, cpufreq.current,
            num_physical_cores, num_total_cores, usage_per_core, total_usage)


def print_cpu_info(cpu_info: CPUInfo):
    print()
    print_section_header("CPU Information")
    
    print("  Physical cores:", cpu_info[4])
    print("  Total cores:", cpu_info[5])

    print(f"  CPU Arch: {cpu_info[0]['arch']}")
    print(f"  CPU Bits: {cpu_info[0]['bits']}")

    print(f"  Max Frequency: {cpu_info[1]:.2f}Mhz")
    print(f"  Min Frequency: {cpu_info[2]:.2f}Mhz")
    print(f"  Current Frequency: {cpu_info[3]:.2f}Mhz")

    print("  CPU Usage Per Core:")
    for i, percentage in enumerate(cpu_info[6]):
        print(f"  Core {i}: {percentage}%")
    print(f"  Total CPU Usage: {cpu_info[7]}%")
