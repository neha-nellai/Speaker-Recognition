import librosa
import matplotlib.pyplot as plt
import librosa.display

audio_path = 'Voice_Samples_Training/Neha-001/Neha_audio1.wav'
x , sr = librosa.load(audio_path)
print(type(x), type(sr))
librosa.load(audio_path, sr=44100)
plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)
