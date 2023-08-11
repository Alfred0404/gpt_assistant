import openai
import os
from dotenv import load_dotenv
import speech_to_text

load_dotenv()

def chatgpt_prompt() :
    # store the API key (better to store in a .env file)
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # get user input and the chatgpt's personnality
    personnality = "Tu es un assistant vocal. Tu dois repondre a toute les questions de maniere claire et precise, afin d'aider du mieux que tu peux. Tu es professionnel et informé meme si le prompt que tu recois est en anglais, reponds en francais tout le temps."
    user_input = speech_to_text.user_prompt

    # create a list of instructions for the gpt
    instructions = [{'role' : 'system', 'content' : personnality}]
    instructions.append({"role" : 'user', 'content' : user_input})

    # create a gpt response
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = instructions
    )

    # store the gpt response
    gpt_response = completion.choices[0].message.content

    return gpt_response

response = chatgpt_prompt()
print(response)