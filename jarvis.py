import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
 


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
       engine.say(audio) 

       engine.runAndWait() 
def wishme():

       hour = int(datetime.datetime.now().hour)
       if hour>=0 and hour<12:
             speak("Good Morning Sir!")

       elif hour>=12 and hour<18:
             speak("Good Afternoon Master!")

       else:
             speak("Good Evening Master!")

       speak("I am Jarvis. Please tell me how may I help you")

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
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mayureshbhosale999@gmail.com', 'cjnxxulgsqdzoagi')
    server.sendmail('mayureshbhosale999@gmail.com', to, content)
    server.close()
 



if __name__=="__main__" :
    wishme()
    while True:
     #if 1:
        query = takeCommand().lower() 

        
        if 'wikipedia' in query:  
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2) 
           speak("According to Wikipedia")
           print(results)
           speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'L:\Alpha\Playlists'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Mayuresh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open my documents' in query:
             docpath="C:\\Users\\Mayuresh\\OneDrive\\Desktop"
             os.startfile(docpath)

        elif 'who are you' in query:
             speak(f"Im your Personal Assistant Jarvis,Sir")

        elif 'what can you do for me' in query:
             speak(f" I can assist you to access your applications for you"         )
             
             
        elif 'email to Mayur' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mayureshbhosale008@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Im Sorry Sir.I am not able to send this email")    
            
        
             
       


















    
