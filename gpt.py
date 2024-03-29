import openai
import os
from dotenv import load_dotenv

# Load the environment variables from a .env file
load_dotenv()

# Retrieve the API key from an environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt, chat_history=[]):
    try:
        # Adjusting to the new API call structure
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}] + chat_history,
            temperature=0.7,
            max_tokens=50,
            stop=["\n", "User:", "Assistant:"],
            frequency_penalty=0,
            presence_penalty=0.6,
        )

        # Append the current prompt to the chat history
        chat_history.append({"role": "user", "content": prompt})
        # Extract and append the response to the chat history
        chat_history.append({"role": "assistant", "content": response.choices[0].message["content"]})

        return response.choices[0].message["content"].strip(), chat_history
    except Exception as e:
        print(f"An error occurred: {e}")
        return "", chat_history  # Return an empty string and the current chat history on error

if __name__ == "__main__":
    chat_history = []  # Initialize an empty chat history

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response, chat_history = chat_with_gpt(user_input, chat_history)
        print("ChatGPT:", response)
