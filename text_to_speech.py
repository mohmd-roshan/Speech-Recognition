import pyttsx3
txt_sp=pyttsx3.init()
txt=input('enter the text : \n')
voices=txt_sp.getProperty('voices')
for voice in voices:
    print('ID : ',voice.id)
txt_sp.setProperty('voice',voices[0].id)
txt_sp.say(txt)
txt_sp.runAndWait()