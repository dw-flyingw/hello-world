#print ("Hello World")

import platform
import psutil
import cpuinfo
import torch
#import GPUtil

def get_system_info():
    # Operating System Information
    print("\n=== Operating System Information ===")
    print(f"OS Name: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"OS Release: {platform.release()}")
    print(f"Machine Architecture: {platform.machine()}")
    
    # CPU Information
    print("\n=== CPU Information ===")
    cpu_info = cpuinfo.get_cpu_info()
    print(f"CPU Brand: {cpu_info['brand_raw']}")
    print(f"CPU Cores (Physical): {psutil.cpu_count(logical=False)}")
    print(f"CPU Cores (Logical): {psutil.cpu_count(logical=True)}")
    
    # Memory Information
    print("\n=== Memory Information ===")
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024**3):.2f} GB")
    print(f"Available Memory: {memory.available / (1024**3):.2f} GB")
    print(f"Memory Usage: {memory.percent}%")
    
def get_gpu_info():
    # GPU Information
    print("\n=== GPU Information ===")
    gpu_names = []
    if torch.cuda.is_available():
        for i in range(torch.cuda.device_count()):
            gpu_names.append(torch.cuda.get_device_name(i))
    return gpu_names


if __name__ == "__main__":
    get_system_info()
    

    gpu_names = get_gpu_info()
    if gpu_names:
        print("Available GPUs:")
    for i, gpu_name in enumerate(gpu_names):
        print(f"  GPU {i}: {gpu_name}")
    else:
        print("No GPU available.")