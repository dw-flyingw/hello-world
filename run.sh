conda create -n terminal --yes
conda env list
conda activate terminal
pip install psutil py-cpuinfo GPUtil --no-warn-script-location
python ./hello-world/main.py 
