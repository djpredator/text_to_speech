# Import the gTTs module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'My name is predator. I love Programming.'
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("speech.mp3") 
  
# Play the converted file 
os.system("start speech.mp3")
