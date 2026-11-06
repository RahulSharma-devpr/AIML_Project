# # import pyjokes
# # joke = pyjokes.get_joke()
# # print(joke)

# #practice set
# import pyttsx3
# engine = pyttsx3.init()

# engine.say("chal na")
# engine.runAndWait() 

# google to text to speak much better

from gtts import gTTS
import os

text = "John Chal Bahar Ghummi Ghummi ,,Billi Billi chuha agya"
speech = gTTS(text=text, lang='hi') #hi =hindi
speech.save("output.mp3")
os.system("start output.mp3")
