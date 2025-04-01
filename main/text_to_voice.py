import base64
import io
from gtts import gTTS
from pydub import AudioSegment
import logging

def rwtv(text, diagnostics=False):
    """Convert text to speech and return Base64 encoded audio."""
    if diagnostics:
        logging.basicConfig(filename='rwtv_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    
    def log_event(message, error_message=None):
        if diagnostics:
            if error_message:
                logging.error(f"{message} - Error: {error_message}")
            else:
                logging.info(message)
    
    try:
        log_event("Starting rwtv function")
        
        tts = gTTS(text=text, lang="en")
        log_event("Generated TTS audio")

        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        log_event("Written TTS audio to buffer")

        # Convert MP3 to WAV for consistency
        audio = AudioSegment.from_file(audio_buffer, format="mp3")
        wav_buffer = io.BytesIO()
        audio.export(wav_buffer, format="wav")
        log_event("Converted MP3 to WAV")

        # Encode WAV file to Base64
        encoded_audio = base64.b64encode(wav_buffer.getvalue()).decode("utf-8")
        log_event("Encoded WAV to Base64")
        
        return encoded_audio
    except Exception as e:
        log_event("Error in TTS", error_message=str(e))
        print(f"Error in TTS: {e}")
        return None
