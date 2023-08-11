from elevenlabs import generate, play, set_api_key
import os
from dotenv import load_dotenv
import gpt
import speech_to_text

load_dotenv()

set_api_key(os.getenv("ELEVEN_LABS_API_KEY"))

os.environ['PATH'] += os.pathsep + os.getenv('FFMPEG_PATH')


def speak (gpt_text) :
  audio = generate(
    text= gpt_text,
    voice="Marcus",
    model="eleven_multilingual_v1"
  )

  play(audio)

speak(str(gpt.response))
while True :

    speech_to_text.user_prompt = speech_to_text.recognize()

    gpt.response = gpt.chatgpt_prompt()

    # gpt_text_response = str(gpt.response)

    speak(str(gpt.response))