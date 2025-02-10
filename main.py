print ("Hello World")

import platform
import psutil
import cpuinfo
import GPUtil
import os

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
    #print(f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz")
    
    # Memory Information
    print("\n=== Memory Information ===")
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024**3):.2f} GB")
    print(f"Available Memory: {memory.available / (1024**3):.2f} GB")
    print(f"Memory Usage: {memory.percent}%")
    
    # GPU Information
    print("\n=== GPU Information ===")
    try:
        gpus = GPUtil.getGPUs()
        for i, gpu in enumerate(gpus):
            print(f"\nGPU {i + 1}:")
            print(f"Name: {gpu.name}")
            print(f"Driver: {gpu.driver}")
            print(f"Memory Total: {gpu.memoryTotal} MB")
            print(f"Memory Used: {gpu.memoryUsed} MB")
            print(f"Memory Free: {gpu.memoryFree} MB")
            print(f"GPU Load: {gpu.load * 100}%")
    except Exception as e:
        print("No GPU information available")

if __name__ == "__main__":
    get_system_info()
