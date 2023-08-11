from elevenlabs import generate, play, set_api_key
import os
from dotenv import load_dotenv
import gpt

load_dotenv()

set_api_key(os.getenv("ELEVEN_LABS_API_KEY"))

os.environ['PATH'] += os.pathsep + 'C:\\ffmpeg'

audio = generate(
  text= str(gpt.response),
  voice="Marcus",
  model="eleven_multilingual_v1"
)

play(audio)