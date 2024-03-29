import openai

openai.api_key = "##3##43#532332###"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="text-davinci-002",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,  
        temperature=0.7,  
        stop=["\n", "User:", "Assistant:"],  
        frequency_penalty=0, 
        presence_penalty=0.6,   
        custom_instructions="You are a helpful assistant." 
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You:")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("ChatGPT:", response)
