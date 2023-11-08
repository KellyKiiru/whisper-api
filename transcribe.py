import openai
from docx import Document

audio_file_path = "EarningsCall.wav"

def transcribe_audio("EarningsCall.wav"):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']

print(audio_file_path)