import platform
import psutil
import subprocess
import pynvml

def get_server_info():
    """
    Gathers information about the server.

    Returns:
        A dictionary containing server information.
    """
    info = {}

    # Operating System
    info['os_name'] = platform.system()
    info['os_release'] = platform.release()
    info['os_version'] = platform.version()
    try:
        info['lsb_release'] = subprocess.run(["lsb_release", "-a"], capture_output=True, text=True).stdout.strip()
    except FileNotFoundError:
        info['lsb_release'] = "lsb_release command not found."

    # CPU
    info['cpu_count'] = psutil.cpu_count()
    info['cpu_cores'] = psutil.cpu_count(logical=False)  # Physical cores

    # Memory
    mem = psutil.virtual_memory()
    info['total_memory'] = f"{mem.total / (1024 ** 3):.2f} GB"
    info['used_memory'] = f"{mem.used / (1024 ** 3):.2f} GB"
    info['free_memory'] = f"{mem.free / (1024 ** 3):.2f} GB"


    # Uptime
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_minutes = uptime_seconds // 60
        uptime_hours = uptime_minutes // 60
        uptime_days = uptime_hours // 24
        uptime_hours = uptime_hours % 24
        uptime_minutes = uptime_minutes % 60
        info['uptime'] = f"{uptime_days}d {uptime_hours}h {uptime_minutes}m"

    # Load Average (from /proc/loadavg)
    with open('/proc/loadavg', 'r') as f:
        load_avg = f.read().split()[:3]
        info['load_avg_1min'] = load_avg[0]
        info['load_avg_5min'] = load_avg[1]
        info['load_avg_15min'] = load_avg[2]
    return info

def get_gpu_info():
    """
    Get basic GPU information including type, memory usage, and utilization.
    Returns a list of dictionaries containing information for each GPU.
    """
    try:
        # Initialize NVML
        pynvml.nvmlInit()
        
        gpu_info = []
        device_count = pynvml.nvmlDeviceGetCount()
        
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            info = {}
            
            # Get GPU name/type
            name = pynvml.nvmlDeviceGetName(handle)
            info['name'] = name.decode() if isinstance(name, bytes) else name
            
            # Get memory info
            memory = pynvml.nvmlDeviceGetMemoryInfo(handle)
            info['memory'] = {
                'total': f"{memory.total / (1024**2):.2f} MB",
                'used': f"{memory.used / (1024**2):.2f} MB",
                'free': f"{memory.free / (1024**2):.2f} MB"
            }
            
            # Get GPU utilization
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
            info['utilization'] = {
                'gpu': f"{utilization.gpu}%",
                'memory': f"{utilization.memory}%"
            }
            
            gpu_info.append(info)
            
    except pynvml.NVMLError as e:
        print(f"Error getting GPU information: {e}")
        return None
        
    finally:
        try:
            pynvml.nvmlShutdown()
        except:
            pass
            
    return gpu_info

def print_gpu_info(gpu_info):
    """
    Print formatted GPU information
    """
    if not gpu_info:
        print("No GPU information available")
        return
        
    for i, gpu in enumerate(gpu_info):
        print(f"\nGPU {i}:")
        print(f"Name: {gpu['name']}")
        print("\nMemory:")
        print(f"  Total: {gpu['memory']['total']}")
        print(f"  Used:  {gpu['memory']['used']}")
        print(f"  Free:  {gpu['memory']['free']}")
        print("\nUtilization:")
        print(f"  GPU:    {gpu['utilization']['gpu']}")
        print(f"  Memory: {gpu['utilization']['memory']}")

if __name__ == "__main__":
    server_info = get_server_info()

    # Print in a more readable format
    print("*** Server Information ***")
    print(f"Operating System:")
    print(f"  - Name: {server_info['os_name']}")
    print(f"  - Release: {server_info['os_release']}")
    print(f"  - Version: {server_info['os_version']}")
    print(f"  - lsb_release: {server_info['lsb_release']}")
    print(f"\nCPU:")
    print(f"  - Cores: {server_info['cpu_count']} (Logical)")
    print(f"  - Physical Cores: {server_info['cpu_cores']}")
    print(f"\nMemory:")
    print(f"  - Total: {server_info['total_memory']}")
    print(f"  - Used: {server_info['used_memory']}")
    print(f"  - Free: {server_info['free_memory']} ")
    print(f"\nUptime: {server_info['uptime']}")
    print(f"\nLoad Average: 1-minute: {server_info['load_avg_1min']}, 5-minute: {server_info['load_avg_5min']}, 15-minute: {server_info['load_avg_15min']}")

    gpu_info = get_gpu_info()
    print_gpu_info(gpu_info)

    