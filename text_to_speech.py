from elevenlabs import generate, play, set_api_key, RateLimitError, UnauthenticatedRateLimitError
import os
from dotenv import load_dotenv
import gpt
import speech_to_text
import pyttsx3

load_dotenv()

set_api_key(os.getenv("ELEVEN_LABS_API_KEY"))

os.environ['PATH'] += os.pathsep + os.getenv('FFMPEG_PATH')


def speak_elevenlabs (gpt_text) :
  audio = generate(
    text= gpt_text,
    voice="Marcus",
    model="eleven_multilingual_v1"
  )

  play(audio)


def speak_pytts (gpt_text) :
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[3].id)
  engine.say(gpt_text)
  engine.runAndWait()


speak_pytts(str(gpt.response))
while True :

    speech_to_text.user_prompt = speech_to_text.recognize()

    gpt.response = gpt.chatgpt_prompt()

    speak_pytts(str(gpt.response))