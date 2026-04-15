import os
import uuid

AUDIO_FOLDER = "static/audio"

def speak(text, emotion):
    os.makedirs(AUDIO_FOLDER, exist_ok=True)

    filename = str(uuid.uuid4())
    aiff_path = f"{AUDIO_FOLDER}/{filename}.aiff"
    mp3_path = f"{AUDIO_FOLDER}/{filename}.mp3"

    # Voice + Rate (Pitch Simulation)
    if emotion == "very_positive":
        voice = "Samantha"
        rate = 210
        volume = 2.0   
    elif emotion == "positive":
        voice = "Samantha"
        rate = 200
        volume = 1.5
    elif emotion == "neutral":
        voice = "Alex"
        rate = 170
        volume = 1.0
    elif emotion == "negative":
        voice = "Daniel"
        rate = 140
        volume = 0.8
    elif emotion == "very_negative":
        voice = "Daniel"
        rate = 120
        volume = 0.6
    else:
        voice = "Alex"
        rate = 170
        volume = 1.0

    print(f"Voice: {voice}, Rate: {rate}, Volume: {volume}")

    # Generate speech
    
    os.system(f'say -v {voice} -r {rate} -o "{aiff_path}" "{text}"')

    # Convert to MP3 + adjust volume
    
    os.system(f'ffmpeg -y -i "{aiff_path}" -filter:a "volume={volume}" "{mp3_path}"')

    os.remove(aiff_path)

    return mp3_path