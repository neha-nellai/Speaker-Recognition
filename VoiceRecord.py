import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
engine = pyttsx3.init()

fs = 44100  # Sample rate
seconds = 5  # Duration of recording

engine.say('Record your voice for 5 seconds')
engine.runAndWait()
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('Rohit_test16.wav', fs, myrecording)
