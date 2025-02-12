
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = ('/home/dave.wright-hpe.com/dave-wright-hpe-5f2c6f61/.env')
load_dotenv(dotenv_path)
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")


client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

completion = client.completions.create(model="meta/llama-3.1-8b-instruct",
                                      prompt="Panama is a")
print("Completion result:", completion)



client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)



