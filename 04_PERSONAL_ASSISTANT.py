import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(f"I am Friday. Please tell me how may I help you")       

def takeCommand():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
          
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

  

        elif 'play music' in query:
            music_dir = 'C:\\Users\\ayush\\Music'
            songs = os.listdir(music_dir)
            print(songs)   
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'video' in query:
            videos_dir = 'C:\\Users\\ayush\\Videos\\Movies'
            videos = os.listdir(videos_dir)
            print(videos)   
            os.startfile(os.path.join(videos_dir, videos[1]))

        elif 'random song' in query:
            music_dir = 'C:\\Users\\ayush\\Music'
            songs = os.listdir(music_dir)
            print(songs)   
            randsong = random.randint(0, 7)
            os.startfile(os.path.join(music_dir, songs[randsong]))

        elif 'random video' in query:
            videos_dir = 'C:\\Users\\ayush\\Videos\\Movies'
            videos = os.listdir(music_dir)
            randvideo = random.randint(1, 7)
            print (randvideo)
            os.startfile(os.path.join(videos_dir, videos[randvideo]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'thanks' in query:
            speak('pleasure is mine.')
            print ('pleasure is mine...')
            break

        elif 'thank you' in query:
            speak("you're welcome!")
            print ("you're welcome")
            break

        elif "nickname" in query:
            print ('''I got some nicknames for you
                      1. Tubelight
                      2. Puchchi
                      3. Sweety
                      4. Baby
                      5. Kachori  ''')

            speak ('I got some nicknames for you, tubelight, puchchi, sweety, baby, kachori')
        elif "stop" in query:
            speak("hope you liked my services! Please come again, I'll be waiting for you")
            break

        
        