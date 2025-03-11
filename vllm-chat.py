from openai import OpenAI

# Dave WRight pod Geneva PCAI
model = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
openai_api_base = "https://smollm2-1-7b-vllm-predictor-dave-wright-hpe-1073f7cd.hpepcai-ingress.pcai.hpecic.net/v1"
openai_api_key =  "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mzk5MzgzMzAsImlzcyI6ImFpb2xpQGhwZS5jb20iLCJzdWIiOiI5MjNhM2JhOC1mMGU4LTQxOTQtODNkMS05ZWY4NzNjZGYxOWYiLCJ1c2VyIjoiZGF2ZS53cmlnaHQtaHBlLmNvbSJ9.YwH9gGPxTWxy4RSdjnQA9-U3_u7P0OIcarqw25DV8bOiftU1L4IvvyERHspj2lMGtZWbff1F3uh84wjAePHaHDcDTLoGtq6gJYwo_qRU03xV8Q2lwBetCCLUE4OHqS608gjJ-j1SLyqwxFxlXkqMOtnBY5_nswlAwCzHV28P8u8XxxfWuXFmoJpSA1egCWVVfEoTuK8CTz9kUJJ5opSp6m8qdqJmC2qxH0igcpKmL2H_MZ-62UHfEf240VRtc0DRNlOjeCoDM79aVPs3SjCtGeVkeEHimJwJbfGFIcu3LibX3QjbABUzWb5BPPZjzyEYUVM5ak12_sJ8j1mUW-r0sA"


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

