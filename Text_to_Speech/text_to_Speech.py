from gtts import gTTS
import os

def text_to_speech(text):
    tts=gTTS(text=text,lang='en')
    tts.save("speechoutput.mp3")
    os.system("start output.mp3")
if __name__ =="__main__":
    text =input("Enter the text you want to convert to speech:")
    text_to_speech(text)
