#!/usr/bin/env python3

# gtts is a library that uses Google's Text-to-Speech API to generate an audio file with spoken text.
from gtts import gTTS
# pydub is a library for manipulating audio files. It provides a high-level API for working with audio files
from pydub import AudioSegment
from pydub.playback import play



def text_to_speech(text):
    """ This function to convert text to audio save it and then play it """
    # convert to text 
    tts = gTTS(text=text, lang='en')
    tts.save("simo.mp3")
    # play the audio 
    sound = AudioSegment.from_file("simo.mp3", format="mp3")
    play(sound)
    
# Type what do you want your computer to say  
text = input("Enter text...\n")
# Let the magic happen 
text_to_speech(text)
