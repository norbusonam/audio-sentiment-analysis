import sys
import sounddevice as sd
from scipy.io.wavfile import write

# arguments
fs = 44100  
seconds = int(sys.argv[1]) if len(sys.argv) >= 2 else 10
filename = sys.argv[2] if len(sys.argv) == 3 else "output.wav"
filename = filename if filename.endswith(".wav") else filename + ".wav"
filename = "./recordings/" + filename

# record and save file
myrecording = sd.rec(seconds * fs, samplerate=fs, channels=1)
write(filename, fs, myrecording)  # Save as WAV file 