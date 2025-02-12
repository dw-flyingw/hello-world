pip install psutil py-cpuinfo GPUtil pynvml --no-warn-script-location 
clear
PATH=$PATH:~/.local/bin
python ./hello-world/main.py 
nvidia-smi
export NGC_API_KEY="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"

#helm fetch https://helm.ngc.nvidia.com/nim/nvidia/charts/nvidia-nim-llama-32-nv-embedqa-1b-v2-1.3.0.tgz --username='$oauthtoken' --password=$NGC_API_KEY

