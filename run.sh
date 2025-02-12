pip install dotenv psutil py-cpuinfo GPUtil pynvml --no-warn-script-location 
clear
PATH=$PATH:~/.local/bin
python ./hello-world/main.py 
nvidia-smi
ld -v
export NGC_API_KEY="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"

