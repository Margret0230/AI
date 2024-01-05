import pyttsx3
import speech_recognition as sr  
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import smtplib
import sys
                                # pip install pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=17:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
        
        
    speak("I am jarvis sir please tell me how may i help you")

def takecommand():
    #it take microphone input from the user and return string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print(e)
        
        print("Say that again please....")
        return "None"
    query = query.lower()
    return query
    
    
if __name__ == "__main__":
    wishme()
    while True:
    
    
         query = takecommand().lower()
         
         if 'wikipedia' in query:
             speak('Searching Wikipedia.....')
             query = query.replace("Wikipedia", "")
             results = wikipedia.summary(query, sentences=4)
             speak("According to Wikipedia")
             print(results)
             speak(results)
             
             
         elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
         elif 'open word' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010"
            os.startfile(npath)
            
         elif 'open excel' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010"
            os.startfile(npath)
            
         elif 'open powerpoint' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010"
            os.startfile(npath)
            
         elif 'open notepad' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(npath)
            
         elif 'open firefox' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\FireFox"
            os.startfile(npath)
            
         elif 'open command prompt' in query:
            npath = "C:\\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
            os.startfile(npath)
            
        
         elif 'open google' in query:
            speak("sir, what should i search on google")
            am = takecommand().lower()
            webbrowser.open(f"{am}")
            
            
         elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        
         elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            
         elif 'open meet' in query:
            webbrowser.open("google meet.com")

         elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            
            
            
         elif 'play music' in query:
            music_dir = 'E:\\Margret photo & video\\Music\\download'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[98]))
            
         elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
         elif 'how are you' in query: 
            speak("I Am Fine Sir!") 
            speak("Whats About YOU?")
        
         elif 'you need a break' in query:
            speak ("Ok Sir, You Can Call Me Anytime !")
            
        
         elif 'bye' in query:
            speak("Ok Sir, Bye")
        
         elif 'hello' in query:
            speak(" hello Sir, how can i help you")
            
            
         elif 'send message' in query:
            kit.sendwhatmsg("+919673712747", "hi ha msg mi ai ni sewnd kela aahe",5,56)
            
         elif 'play song on youtube' in query:
            speak("sir, which song should i search on youtube")
            bm = takecommand().lower()
            kit.playonyt(f"{bm}")
            
         elif 'no thanks' in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
        
         speak("sir, do you have any other work.")
         
         
         
         
      