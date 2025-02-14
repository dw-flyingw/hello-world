
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = ()
load_dotenv(dotenv_path)
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")

model = "meta/llama-3.1-8b-instruct"  

# Geneva PCAI Llama3 NIM-LLAMA endpoint
openai_api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk0NzI4MDAsImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI2NGU1MTQxMS00NWQ3LTQwZDgtYjhmNy01ZTFlOWFlOGMzZDQiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.arhTzvRI4xECeqNKVSFVJFHX_gzFQPanDzrwdw1yq6nolss2zLoVXoDtM6v4aQTopdmTVznOcpkjrcSPH8edigBFt67hrzd8VaSgO_PpgDUCFLZQ7vfcajxuCxtj58Ue6thcIDPqt8IS5c1KyL790s5WYy2EEcFvuwH_wlN29ivzzUsfzPlS_4oaQf8g1uG6zhFmnvcIRA5A0dApU7UM75oblN9nJTI0UGPrRbAq2nhik8hsmYk-USNr5H-uKptMS3_c8C5X_s33cAf--U0ZYK3EsSsXeGDIqePpo0gSMwq1tC9u3fbkZbrD0oDczGMxNEaM4mBYjXIKYPU_pi5naA"
openai_api_base = "https://llama-31-nim-predictor-jordan-nanos-hp-d222129e.hpepcai-ingress.pcai.hpecic.net/v1"



client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

completion = client.completions.create(model=model,
                                      prompt="Panama is a")
print("Completion result:", completion)


client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)



