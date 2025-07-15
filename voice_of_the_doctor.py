#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text,output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text="Hi this is an AI with Darshana!"
#text_to_speech_with_gtts(input_text=input_text,output_filepath="gtts_testing.mp3")

#Step 1B: Setup Text to speech-TTS-Model with ElevenLbas

import os
from elevenlabs import generate, save, set_api_key
from dotenv import load_dotenv

load_dotenv()
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def text_to_speech_with_elevenlabs_old(text, output_filepath):
    audio = generate(
        text=text,
        voice="Aria",  
        model="eleven_monolingual_v1"
    )
    save(audio, output_filepath)
    print(f"✅ Audio saved to {output_filepath}")

text = "Hello Darshana, this is your AI voice assistant."
#text_to_speech_with_elevenlabs(text, "elevenlabs_testing.mp3")


#Step 2: Use Model for Text ouput to voice

import subprocess
import platform

def text_to_speech_with_gtts(input_text,output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    print("✅ Audio file saved successfully.")

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(f'start "" "{output_filepath}"', shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text="Hi this is Ai with Darshana, autoplay testing!"
#text_to_speech_with_gtts(input_text=input_text,output_filepath="gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(text, output_filepath):
    audio = generate(
        text=text,
        voice="Aria",  
        model="eleven_monolingual_v1"
    )
    save(audio, output_filepath)
    print(f"✅ Audio saved to {output_filepath}")
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(f'start "" "{output_filepath}"', shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text = "Hello Darshana, this is your AI voice assistant autoplay testing."
text_to_speech_with_elevenlabs(text, "elevenlabs_testing_autoplay.mp3")


