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
    # texte = ""

    try :
        audio = get_audio()

        texte = r.recognize_google(audio, language="fr-FR")
        print(texte)

        if texte == "stoppe":
            exit()

        return texte

    except sr.UnknownValueError :
        print("Google Speech Recognition could not understand audio")
        return recognize()

    except sr.RequestError as e :
        print(f"Error : {e}")

user_prompt = recognize()