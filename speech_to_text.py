import speech_recognition as sr


# getting the audio
def get_audio() :
    global r
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("say something")
        audio = r.listen(source)
    return audio


# recognize the audio
def recognize() :
    texte = ""
    try :
        audio = get_audio()
        texte = r.recognize_google(audio)
        return texte

    except sr.UnknownValueError :
        print("Oups...Can't understand what you said...")

    except sr.RequestError as e :
        print(f"Error : {e}")

user_prompt = recognize()
print(user_prompt)