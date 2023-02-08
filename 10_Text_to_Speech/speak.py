#!/usr/bin/env python3 

import sys 
import pyttsx3

# Initialize the TTS engine. 
tts = pyttsx3.init() 


print("""Text-to-speech using the pyttsx3 module, which in turn uses'
the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows), or
eSpeak (on Linux) speech engines.\n""")

print("Enter the text to speak, or QUIT to quit.")
print("Type q to quit ")

while True:
    text = input("Enter your text")
    
    # In case the user want to quit  
    if text.lower() == 'q':
        sys.exit()

    # convert the text to speech usisng TTS engine 
    tts.say(text) 
    # Make my computer (The TTS engine)say it. 
    tts.runAndWait()
    


