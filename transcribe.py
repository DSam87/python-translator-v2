import whisper
from datetime import datetime

# Get current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Open file  
text_output = open("text-files/transcribe.txt", "a")

# Read audio files from "audio-files" dir 
model = whisper.load_model("base")
result = model.transcribe("audio-files/audio.mp3")

# Append to file
text_output.write(f"\n{current_time}\n")
text_output.write(result["text"] + "\n")
text_output.close()
