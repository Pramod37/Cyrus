import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer
try:
    engine = pyttsx3.init()
except ImportError:
    print('Imported Drive is not found..')
except RuntimeError:
    print('Driver failed to initialise..')

voices = engine.getProperty('voices')
# for voice in voices:
#     print (voice.id)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_10.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)
# engine.say('Hello Sir, This is Cyrus...')
engine.runAndWait()

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    print('Listening...')
    with sr.Microphone() as source :
        audio = speech.listen(source)
    try :
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError :
        pass
    except sr.RequestError:
        print ('Network Error')
    return voice_text

if __name__ == '__main__':
    speak_text_cmd("Hello Mr. Singh.. This is Cyrus as Your AI Robo..")

    while True:
        voice_note = read_voice_cmd()
        print('cmd:()'.format(voice_note))

        if 'hello' in voice_note :
            speak_text_cmd('Hello Sir ,How Can I help you.')
            continue
        elif 'open' in voice_note :
            os.system('explorer C:\\ {}'.format(voice_note.replace('Open ', '')))
            continue
        elif 'bye' in voice_note :
            speak_text_cmd('Bye Mr. Singh. Happy to help you. Good Bye.. ')
            exit()




