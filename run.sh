#pip install  psutil py-cpuinfo GPUtil pynvml --no-warn-script-location 

#clear
#python ./hello-world/hello-world.py 
#nvidia-smi
#ld -v

#pip install -r hello-world/requirements.txt

PATH=$PATH:~/.local/bin
export NGC_API_KEY="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"
echo "$NGC_API_KEY" | docker login nvcr.io --username '$oauthtoken' --password-stdin

# set up TTS NIM
export NIM_TAGS_SELECTOR=name=fastpitch-hifigan-en-us
docker pull nvcr.io/nim/nvidia/riva-tts:1.3.0

docker run -it --rm --name=riva-tts \
   --runtime=nvidia \
   --gpus '"device=0"' \
   --shm-size=8GB \
   -e NGC_API_KEY \
   -e NIM_HTTP_API_PORT=9000 \
   -e NIM_GRPC_API_PORT=50051 \
   -p 9000:9000 \
   -p 50051:50051 \
   -e NIM_TAGS_SELECTOR \
   nvcr.io/nim/nvidia/riva-tts:1.3.0



