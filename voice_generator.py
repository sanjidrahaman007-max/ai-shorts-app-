from gtts import gTTS

def generate_voice(text):
    tts = gTTS(text)
    tts.save("voice.mp3")
    return "voice.mp3"
