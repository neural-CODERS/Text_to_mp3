from gtts import gTTS 
from playsound import playsound
mytext = 'Welcome to neural coders!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
playsound("welcome.mp3")
