import sounddevice as sd
import numpy as np
import wavio

# Function to callback when audio is received
def callback(indata, frames, time, status):
    if status:
        print(f"Error: {status}")

    # Append the new audio data to the existing data
    audio_data.append(indata.copy())

# Set the sample rate and duration for recording
sample_rate = 44100
duration = 5  # in seconds

# Initialize an empty list to store audio data
audio_data = []

# Start recording using the callback function
print("Speak! We are recording. ")
with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
    sd.sleep(duration * 1000)

# Convert the list of audio data to a numpy array
full_audio_data = np.concatenate(audio_data, axis=0)

# Save the audio data to a WAV file
wavio.write("recorded_audio.wav", full_audio_data, sample_rate, sampwidth=3)

print("Recording saved to 'recorded_audio.wav'")
