# GPT Chatbot with OpenAI
This project demonstrates how to create a simple chatbot using OpenAI's GPT (Generative Pre-trained Transformer) model. The chatbot interacts with users by generating responses based on the input provided.

## Installation
To run the chatbot locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

## Usage
Run the `chat_with_gpt.py` script to start the chatbot. You will be prompted to enter a message, and the chatbot will respond accordingly.

## Configuration
Before running the script, make sure to set your OpenAI API key in the `openai.api_key` variable.
openai.api_key = "YOUR_API_KEY_HERE"

# Dependencies
OpenAI: Python package for accessing OpenAI's GPT models.

# Attributes:
# model: The GPT model to use for generating responses. Default is "text-davinci-002".
# messages: A list of messages containing user input and previous messages. Default is an empty list.
# max_tokens: The maximum number of tokens in the response. Default is 50.
# temperature: Controls the randomness of the response. Default is 0.7.
# stop: A list of strings indicating when to stop generating the response. Default is ["\n", "User:", "Assistant:"].
# frequency_penalty: Controls how much the model avoids repeating words. Default is 0.
# presence_penalty: Controls how much the model avoids generating unlikely words. Default is 0.6.
# custom_instructions: Custom instructions for the model. Default is "You are a helpful assistant.".



