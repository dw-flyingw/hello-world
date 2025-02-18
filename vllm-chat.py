import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = ()
load_dotenv(dotenv_path)
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")

model = "microsoft/phi-4"
openai_api_base = "https://microsoft-phi-4-predictor-dave-wright-hpe-2dc7f199.hpepcai-ingress.pcai.hpecic.net/v1"
openai_api_key =  "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk1NTU3NTksImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI0OWRhOGI4YS01Zjg4LTRlOGMtOTExMS0wNGNjNGExOGUwYTgiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.SEp4teyU6ea4QjmLVXH3jiuKaoMTfHNTmbuWti0x0FOjttKA2wI7Nqbp3GVjnnWKC4n6cKKUqqEohrRDVpQCvZZcQaPVrL9uJ3awJbmDcMue14SBrsFOhR1-bfLSVkfN96_kFxaHUZsrhmg4cxX0EdgN-YBMMk5j4_QolHwfaEeSler92birGifQkg91hlZ5ipMVcavgOYd-9IuEFnJ0dATRdforKEqLQsIOXMhRTGz_GYWLVbI0qllE7n2a8yZA_JiGXupm7XnA44Nr_Kiz8OgCV-ZhL075WhwjOeCbwJyHA_mkGSkOeJVMhFVRn8jR4fr8aBfTjfUizEv3qxkcZw"

# Jordan Nanos pod on Geneva PCAI
model = "meta/llama-3.1-8b-instruct"
openai_api_base = "https://llama-31-nim-predictor-jordan-nanos-hp-d222129e.hpepcai-ingress.pcai.hpecic.net/v1"
openai_api_key =  "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk0NzI4MDAsImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI2NGU1MTQxMS00NWQ3LTQwZDgtYjhmNy01ZTFlOWFlOGMzZDQiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.arhTzvRI4xECeqNKVSFVJFHX_gzFQPanDzrwdw1yq6nolss2zLoVXoDtM6v4aQTopdmTVznOcpkjrcSPH8edigBFt67hrzd8VaSgO_PpgDUCFLZQ7vfcajxuCxtj58Ue6thcIDPqt8IS5c1KyL790s5WYy2EEcFvuwH_wlN29ivzzUsfzPlS_4oaQf8g1uG6zhFmnvcIRA5A0dApU7UM75oblN9nJTI0UGPrRbAq2nhik8hsmYk-USNr5H-uKptMS3_c8C5X_s33cAf--U0ZYK3EsSsXeGDIqePpo0gSMwq1tC9u3fbkZbrD0oDczGMxNEaM4mBYjXIKYPU_pi5naA"


# Geun Tak Roh pod on Geneva PCAI
model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
openai_api_base = "https://ds-r1-distill-qwen-1-5b-predictor-geun-tak-roh-hp-38c6cdee.hpepcai-ingress.pcai.hpecic.net/v1"
openai_api_key =  "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk4OTY1MDQsImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI4OWU3YmJkOC1iMGNjLTQ1OTQtOWQ2My1iMGViYmU4M2UyODMiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.OL9jlJvSzCwxAY4d5AsJxDY-C45gmabOM_E3Z9vr4h3CQQf-bXqffPKCzMKbQAXCsMALU3XVlkP10vqvfynKmqbsGdrhLZsea2UxJK70oQwTzTxML6OlgcnzI46N51hwTvmNzE-CBA8D9ybH7_yvweaaZzfVV7SLaCT1QWh2ad24nDXQKpAJNO62VJfsQYmUSLxgrbyWvuk-o6AEcD17yw5PAHHODGCeCBxae5RSo12lTWL9Ar-_XBV-psHgCbfyti6UWVVBHIbf7doD0dVdFOFHTV-0wqAe_krTrpFXKEcOOIlCGx3G503BIB4TDHTRX0TWdTtGJhlSuVtOgl4DqA"




# create OpenAI client interface
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

