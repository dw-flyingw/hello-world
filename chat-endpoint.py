import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = ()
load_dotenv(dotenv_path)
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")


# Geneva PCAI Llama3 NIM-LLAMA endpoint
model = "meta/llama-3.1-8b-instruct"
openai_api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk0NzI4MDAsImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI2NGU1MTQxMS00NWQ3LTQwZDgtYjhmNy01ZTFlOWFlOGMzZDQiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.arhTzvRI4xECeqNKVSFVJFHX_gzFQPanDzrwdw1yq6nolss2zLoVXoDtM6v4aQTopdmTVznOcpkjrcSPH8edigBFt67hrzd8VaSgO_PpgDUCFLZQ7vfcajxuCxtj58Ue6thcIDPqt8IS5c1KyL790s5WYy2EEcFvuwH_wlN29ivzzUsfzPlS_4oaQf8g1uG6zhFmnvcIRA5A0dApU7UM75oblN9nJTI0UGPrRbAq2nhik8hsmYk-USNr5H-uKptMS3_c8C5X_s33cAf--U0ZYK3EsSsXeGDIqePpo0gSMwq1tC9u3fbkZbrD0oDczGMxNEaM4mBYjXIKYPU_pi5naA"
openai_api_base = "https://llama-31-nim-predictor-jordan-nanos-hp-d222129e.hpepcai-ingress.pcai.hpecic.net/v1"


# Geneva PCAI vllm-base-2 endpoint
model = "microsoft/phi-4"
openai_api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk0ODgwNTUsImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI0NGY0N2VmYi05OGI3LTQ5YjMtYTY1OS0zODdlZGVmYmE0NjEiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.mIFdUSo0lQUFhY1IfwZhnXX3OrtX0K-Sh6YMmfZ9cmYgVy-yhSnqJkbG-g66FUD3d1BPKl6sU9p--jS2IcrqKbPxBRkq_Twn9OQB-SvM3eqPjoPxJpddN5EsXBQw_SZHqceDB6JJV6gG0o4939tv-PAvJPmK_u145seo8Mk55x068D3zuqxPjJAmYWFqBGgjLRhMi1k19VTSphSUDfXgL2Q9EImQeGeWLeb2WJnWoOdrm_fyQkyImowlXw8q3bGxd0DQz0FchW3uEm1KaDwo7ozdOmwLWtUoRpsJAyBLMpbpEJU-GS9cfjzP1pbXiuk8fhpX4vVMYp14JcITeQqXQQ"
openai_api_base = "https://vllm-base-deployment-test-predictor-dave-wright-hpe-054bd22f.hpepcai-ingress.pcai.hpecic.net/v1"


# Geneva PCAI vllm-base-2 package and vllm-base-deployment 
model = "microsoft/phi-4"
openai_api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk1NTU3NTksImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI0OWRhOGI4YS01Zjg4LTRlOGMtOTExMS0wNGNjNGExOGUwYTgiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.SEp4teyU6ea4QjmLVXH3jiuKaoMTfHNTmbuWti0x0FOjttKA2wI7Nqbp3GVjnnWKC4n6cKKUqqEohrRDVpQCvZZcQaPVrL9uJ3awJbmDcMue14SBrsFOhR1-bfLSVkfN96_kFxaHUZsrhmg4cxX0EdgN-YBMMk5j4_QolHwfaEeSler92birGifQkg91hlZ5ipMVcavgOYd-9IuEFnJ0dATRdforKEqLQsIOXMhRTGz_GYWLVbI0qllE7n2a8yZA_JiGXupm7XnA44Nr_Kiz8OgCV-ZhL075WhwjOeCbwJyHA_mkGSkOeJVMhFVRn8jR4fr8aBfTjfUizEv3qxkcZw"
openai_api_base = "/v1"


# Geneva PCAI vllm-base-2 package and vllm-base-deployment 
model = "microsoft/phi-2"
openai_api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk1NTMzNzAsImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiJhNzZkOTU1ZC0wYjNlLTRhMTYtYWViOS1lNWQ2YzdmZTdhNWQiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.GfGfyPq2slg7_Hvaa2nkeIRcmJ7RyLKi-J4wTUNY4U1CzLpxkaQCg7anX0_iZiSpHNepmXoTLDHW96P91z0YaCqw6N34sTvKpoY4b-vI4TEwldKXJwzUg3G0YHS40PeppkhK3QVpnQtOpqkSLQR7t8_4tMgZB1lWUjFWWnvWbr6AJ02NdmZg79gaPfcpMXD7O1b4go4TxDOTUx9e-7QgRKSBj_Q67ohxOBQES30bA1MjtmZVdfV4FJX4aVR8UMaVsYv7SedhhHyHfjf4J_5sDvSi0TFDXLcHu8td_DQuogbSuAZf4nNAxbiWLlPmp9YH13RrxsbTmqumllDhfX4fRA"
openai_api_base = "/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

def chat():
    # Initialize conversation history
    messages = []
    
    print("Chat with "+model+"! Type 'quit' to exit.")
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for quit command
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Add user message to history
        messages.append({"role": "user", "content": user_input})
        
        try:
            # Get model response using chat completion
            response = client.chat.completions.create(
                model=model,
                messages=messages
            )
            
            # Extract assistant's message
            assistant_message = response.choices[0].message.content
            
            # Add assistant's response to history
            messages.append({"role": "assistant", "content": assistant_message})
            
            # Print the response
            print("\nAssistant:", assistant_message)
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            
if __name__ == "__main__":
    chat()

