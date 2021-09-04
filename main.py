import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from pipwin import command


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def talk(text):

  engine.say(text)
  #engine.say('What can I do for you')
  engine.runAndWait()
def take_command():
  try:
      with sr.Microphone() as source:
          print('listning...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          command =command.lower()
          if 'alex' in command:
              command = command.replace('alex', '')
              print(command)
  except:
         pass
  return command

def run_alex():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
       time = datetime.datetime.now().strftime('%I:%M %p')
       print(time)
       talk('Current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    else:
        talk('please say again,')


while True:
    run_alex()