import os
import requests
import tempfile
from playsound import playsound
from time import sleep
import google.generativeai as genai

class TTS:
    def __init__(self, path: str = None):
        """
        Initializes the WireTTS class.

        Args:
            path (str, optional): The path to save the generated audio to. Defaults to None.

        If path is None, the generated audio will be saved to a temporary directory.
        """
        self.path = path or os.path.join(tempfile.gettempdir(), "generated.mp3")

    def say(self, text: str = "Hello World!", voice_model: str = "Jenny"):
        """
        Generates an audio file based on the given text and plays it.

        Args:
            text (str, optional): The text to generate audio from. Defaults to "Hello World!".
            voice_model (str, optional): The voice model to use. Defaults to "Jenny".
        """
        payload = {
            "userId": "public-access",
            "platform": "landing_demo",
            "ssml": f"<speak><p>{text}</p></speak>",
            "voice": f"en-US-{voice_model}Neural",
            "narrationStyle": "Neural",
            "method": "file"
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'Content-Type': 'application/json'
        }

        # Sends a POST request to the API endpoint with the payload and headers
        response = requests.post('https://play.ht/api/transcribe', json=payload, headers=headers)

        if response.ok:
            content = response.json()
            if "file" in content:
                self._download(content["file"]) # Downloads the audio file from the API response
                sleep(0.5)
                playsound(self.path)
                return
            else:
                print(f"Error: {content}")
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")

    def _download(self, url: str):
        """
        Downloads the audio file from the given URL.

        Args:
            url (str): The URL of the audio file to download.
        """
        response = requests.get(url)

        if response.ok:
            with open(self.path, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download file from {url}: {response.status_code} - {response.text}")


class AIChat:
    def __init__(self, model: str = 'gemini-1.5-flash', api_key: str = None):
        """
        Initializes an AI chat.

        Args:
            model (str, optional): The name of the model to use. Defaults to 'gemini-1.5-flash'.
            api_key (str, optional): The API key to use. Defaults to None.

        If no API key is provided, the AI will not be able to generate responses.
        """
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.chat = genai.GenerativeModel(model).start_chat(history=[])
        self.tts = TTS()

    def start(self, exit_code: str = 'ai.exit'):
        """
        Starts the AI chat.

        Args:
            exit_code (str, optional): The string to type to exit the chat. Defaults to 'ai.exit'.
        """
        print("Type 'ai.exit' to exit the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == exit_code:
                print("Exiting chat.")
                break
            
            response = self.chat.send_message(
                user_input,
                generation_config=genai.types.GenerationConfig(
                    stop_sequences=['x'], # Adjust the stop sequence as needed
                    max_output_tokens=100, # Adjust the maximum output length as needed
                    temperature=0.7 # Adjust the temperature as needed
                )
            ).text
            
            self.tts.say(response, voice_model="Jenny")
            print(f"AI: {response}")


if __name__ == "__main__":
    # ensure the environment variable is set before running
    API_KEY = os.getenv("GOOGLE_API_KEY")
    if API_KEY is None:
        print("Error: GOOGLE_API_KEY environment variable not set.")
    else:
        ai_chat = AIChat(api_key=API_KEY)
        ai_chat.start()
