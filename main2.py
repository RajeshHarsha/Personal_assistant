import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime 
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine  = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id )

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("I'm listening... ")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'lucy' in command:
                command =  command.replace('lucy','')
                print(command)
    except:
        pass
    return command

def run_lucy():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play', '')
        talk('Ok wait a minute!'+ song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datatime.datatime.now().strftime('%H:%M:%S %p')
        print("samayam: "+time)
        talk("samayam: "+time)
        
    elif 'what is ' in command:
        person = command.replace("what is  ",'')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'single' in command:
        talk("Sorry! I'm in a relationship with WIFI  ")

    elif 'i love you' in command:
        talk("I Love You too.!")
    else:
        talk("Please say the command again.!")

    
while True: 
    run_lucy()
