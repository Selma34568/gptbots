
# Chat with GPT

Chat with GPT is a Python application that provides a simple interface to chat with OpenAI's GPT models. This project aims to showcase how to interact with OpenAI's API to create conversational AI applications.

## Features

- Chat with GPT using a simple text interface.
- Uses the latest GPT models for improved response quality.
- Basic session management to maintain conversation context.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- An OpenAI API key

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/pbrudny/gptbots.git
cd gptbots
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

Before running the application, you need to set up your OpenAI API key. The recommended way is to use an environment variable. Create a `.env` file in the root of your project directory with the following content:

```
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

### Running the Application

To start the application, run:

```bash
python gpt.py
```

Follow the on-screen instructions to chat with GPT.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
