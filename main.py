import platform
import psutil
import GPUtil
import subprocess

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

    # GPU
    try:
        gpus = GPUtil.getGPUs()
        gpu_info = []
        for i, gpu in enumerate(gpus):
            gpu_info.append({
                'GPU {}'.format(i+1): {
                    'Name': gpu.name,
                    'Total Memory': f"{gpu.memoryTotal / (1024 ** 3):.2f} GB",
                    'Used Memory': f"{gpu.memoryUsed / (1024 ** 3):.2f} GB",
                    'Free Memory': f"{gpu.memoryFree / (1024 ** 3):.2f} GB",
                    'Load': f"{gpu.load * 100:.2f}%"
                }
            })
        info['gpus'] = gpu_info
    except ImportError:
        info['gpus'] = "GPUtil library not found."
    except Exception as e:
        info['gpus'] = f"Error getting GPU information: {e}"

    # vGPU (Placeholder - Difficult without nvidia-smi)
    info['vgpu_present'] = "Unknown (vGPU detection without nvidia-smi is challenging)" 

    return info

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
    print(f"  - Free: {server_info['free_memory']}")
    print(f"\nGPU:")
    if isinstance(server_info['gpus'], list):
        for gpu_dict in server_info['gpus']:
            for gpu_name, gpu_details in gpu_dict.items():
                print(f"  - {gpu_name}:")
                for key, value in gpu_details.items():
                    print(f"    - {key}: {value}")
    else:
        print(f"  - {server_info['gpus']}")
    print(f"\nvGPU Presence: {server_info['vgpu_present']}")