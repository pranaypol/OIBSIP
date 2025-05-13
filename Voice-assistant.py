import speech_recognition as sr 
import pyttsx3 
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    """"speak the given text"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """listen to user voice and convert into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am listening ")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        speak("Sorry, there was a problem with the service.")
        return ""

def main():
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")

        elif "your name" in command:
            speak("I am your simple Python voice assistant.")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")

        elif "open youtube" in command:
            print("Command recognized: open youtube")
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            print("Command recognized: open google")
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            
        elif "exit" in command:
            speak("Thank you for using me,Goodbye!")
            break
        elif command:
            speak("You said: " + command)

#Run the assistant  
main()
