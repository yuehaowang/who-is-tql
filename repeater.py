import pyttsx3
import sys

name = sys.stdin.read()

speaker = pyttsx3.init()

print(name)

while True:
	speaker.say("%s TQL!" % name)
	speaker.runAndWait()