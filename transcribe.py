import sys
import whisper

# arguments
audio_file = sys.argv[1] if len(sys.argv) >= 2 else "./recordings/output.wav"

# transcribe
model = whisper.load_model("base")
result = model.transcribe(audio_file)

# print result
print(result["text"])