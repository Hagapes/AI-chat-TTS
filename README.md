# AI Voice Chatbot

This project is a simple AI Voice Chatbot that integrates Google Generative AI with Text-to-Speech (TTS) capabilities. The chatbot uses the Google Generative AI model to generate text responses and converts them into speech using the `play.ht` API. The generated speech is played back in real-time, making the conversation more interactive.

## Features
- **AI-powered Chatbot**: The bot uses a Google Generative AI model for text-based responses.
- **Text-to-Speech**: Converts the AI responses into speech and plays the audio.
- **Interactive Chat**: Allows you to type messages, hear responses, and see the AI-generated text.
- **Exit command**: Type `ai.exit` to end the chat.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Hagapes/AI-chat-TTS.git
```

2. Create a virtual environment (optional, but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the Google API key:

Make sure to set the `GOOGLE_API_KEY` environment variable before running the script. This API key is used to access Google Generative AI services.

- **On Windows**:

```bash
set GOOGLE_API_KEY=your-api-key
```

- **On Linux/Mac**:

```bash
export GOOGLE_API_KEY=your-api-key
```

5. Run the script:

```bash
python chatbot.py
```

## Usage
When you run the script, the chatbot will start and prompt you to type your message. The AI will respond with text and play the speech output. To end the session, type `ai.exit`.

## Requirements
- Python 3.8 or higher
- A Google Generative AI API key (set it in the environment variable `GOOGLE_API_KEY`)

## Notes
- This project uses the `play.ht` API for Text-to-Speech. The `voice_model` parameter in the `say` method can be adjusted to use different voices available in the API.

## Troubleshooting
- **Error: `GOOGLE_API_KEY environment variable not set`**:
    - Make sure the `GOOGLE_API_KEY` environment variable is correctly set with your Google API key.

- **Audio not playing**:
    - Ensure that the `playsound` library is installed correctly. You may need additional libraries depending on your OS (`pygame` or `pyaudio` can be used as alternatives).

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
