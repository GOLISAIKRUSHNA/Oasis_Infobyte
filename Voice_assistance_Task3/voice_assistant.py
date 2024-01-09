import speech_recognition as sr  #module's are speech recognition,pyttsx3,dateandtime and webbrowser
import pyttsx3  #module         SIMPLE ASSISTANCE IN PYTHON
from datetime import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you repeat?")
        return ""

def main():
    speak("Hello! How can I assist you today?")

    while True:
        query = recognize_speech()

        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "time" in query:
            current_time = datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
        elif "date" in query:
            current_date = datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {current_date}")
        elif "search" in query:
            search_term = query.replace("search", "").strip()
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.open(url)
            speak(f"Searching the web for {search_term}")
        elif "exit" in query or "bye" in query:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm sorry, I didn't understand that command. Can you please repeat?")

if __name__ == "__main__":
    main()
