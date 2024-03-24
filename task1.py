import speech_recognition as sr
import webbrowser
import datetime

def voice_assistant():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")

        if "hello" in command:
            print("Hello! How can I assist you?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(f"The current time is {current_time}")
        elif "search" in command:
            query = command.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            print("I didn't understand that command.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your voice.")
    except sr.RequestError:
        print("Sorry, there was an issue connecting to the Google API.")

voice_assistant()
