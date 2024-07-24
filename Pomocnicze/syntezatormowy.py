import pyttsx3 as synt

sayengine = synt.init()

texttosay = "hello, what's up to you Bartek"

sayengine.say(texttosay)

sayengine.runAndWait()