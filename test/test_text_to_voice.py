# test_voice_to_text.py
import unittest
import os
import wave
import json
import speech_recognition as sr
import sys
import base64
import io
from pydub import AudioSegment
from pydub.playback import play
# Add the directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

# Now you can import the module
from text_to_voice import rwtv

def decode_and_play_audio(encoded_audio):
    """Decode Base64 encoded audio and play it."""
    try:
        audio_bytes = base64.b64decode(encoded_audio)
        audio_buffer = io.BytesIO(audio_bytes)
        
        # Load and play audio
        audio = AudioSegment.from_file(audio_buffer, format="wav")
        play(audio)
    except Exception as e:
        print(f"Error playing audio: {e}")
        
class TestRWTVFunction(unittest.TestCase):
    def setUp(self):
        # Ask user for an audio file path
        text = input("Enter the text wants to convert to voice: ")
        self.text = text
    
    def test_valid_audio(self):
        encoded_audio = rwtv(self.text, True)
        print("Test Response (Valid Audio):", encoded_audio)   
        if encoded_audio:
            print("\n🔹 Base64 Encoded Audio:", encoded_audio[:10] + "...")  # Print only first 10 chars
            print("\n▶ Playing audio now...\n")
            decode_and_play_audio(encoded_audio)

if __name__ == "__main__":
    unittest.main()
