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
openai_api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk1NTU3NTksImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI0OWRhOGI4YS01Zjg4LTRlOGMtOTExMS0wNGNjNGExOGUwYTgiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.SEp4teyU6ea4QjmLVXH3jiuKaoMTfHNTmbuWti0x0FOjttKA2wI7Nqbp3GVjnnWKC4n6cKKUqqEohrRDVpQCvZZcQaPVrL9uJ3awJbmDcMue14SBrsFOhR1-bfLSVkfN96_kFxaHUZsrhmg4cxX0EdgN-YBMMk5j4_QolHwfaEeSler92birGifQkg91hlZ5ipMVcavgOYd-9IuEFnJ0dATRdforKEqLQsIOXMhRTGz_GYWLVbI0qllE7n2a8yZA_JiGXupm7XnA44Nr_Kiz8OgCV-ZhL075WhwjOeCbwJyHA_mkGSkOeJVMhFVRn8jR4fr8aBfTjfUizEv3qxkcZw"

#model = "microsoft/phi-2"
#openai_api_base = "https://microsoft-phi-2-predictor-dave-wright-hpe-2dc7f199.hpepcai-ingress.pcai.hpecic.net/v1"
#openai_api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk1NTgxOTUsImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiJkZWI3ZGUxZi1lNDNkLTRkMzgtOGI1Zi05NTU3MGJlMDA2MTciLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.gflA1_KtZmYuT1D1pgRFuBUilxBbuRLn_tCfelElgqMvsjs-FGglIHNTupMnRxh3tb9vB0PuSLPKbXPimylK63OpIxaE48lrO2Ql_5wIgGqsYhqQqVWi7GEE6xmxoWvh4QgBGnMrfiYqLXCqQ-IHz4uyMRr5F9MGDFOOCeoRCwWDEQlGkFlB3Lp1lAftsRf7sddIwWlu7l08TxQVHm6TwZYTpJd3S2cxAgYcJS_6pjVs8B6nA4LdCatO77IAfeYPxtkCDBRiMfJaHhyZ2pH-MBWOlyIody19P4Yb7M4No24PEZQbbGIFeImqJDOV3tuRYvyz9vWs_qocpTGqNZJGPQ"

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

