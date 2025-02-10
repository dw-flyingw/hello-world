conda create -n terminal
conda env list
conda activate terminal
pip install psutil py-cpuinfo GPUtil --no-warn-script-location
python ./hello-world/main.py 
