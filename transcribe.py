import whisper

# Read audio files from "audio-files" dir 
model = whisper.load_model("base")
result = model.transcribe("audio-files/audio.mp3")
print(result["text"])
