import os
import openai
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def record_voice():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file
    return 'output.wav'

def transcribe_audio(audio_file):
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]

def get_response(text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text}
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message["content"]

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    print("You: ")
    audio_file = record_voice()
    text = transcribe_audio(audio_file)
    response = get_response(text)
    speak_text(response)
    print("Assistant:", response)
    user_choice = input("Continue? (y/n): ")
    if user_choice.lower()!= "y":
        print("Glad to help! Bye!")
        break