from elevenlabs import generate, play, set_api_key
import os
from dotenv import load_dotenv
import gpt
import speech_to_text

load_dotenv()

set_api_key(os.getenv("ELEVEN_LABS_API_KEY"))

os.environ['PATH'] += os.pathsep + 'C:\\ffmpeg'


def speak (gpt_text) :
  audio = generate(
    text= gpt_text,
    voice="Marcus",
    model="eleven_multilingual_v1"
  )

  play(audio)

continuer = input("Voulez-vous continuer ? (y/n) : ").lower()
while continuer == "y":
    speech_to_text.user_prompt = speech_to_text.recognize()
    gpt.response = ""
    gpt.response = gpt.chatgpt_prompt()
    speak(str(gpt.response))

    continuer = input("Voulez-vous continuer ? (y/n) : ").lower()
    while continuer not in ["y", "n"]:
        print("Répondez avec 'y' pour Oui ou 'n' pour Non.")
        continuer = input("Voulez-vous continuer ? (y/n) : ").lower()

speak("Au revoir !")