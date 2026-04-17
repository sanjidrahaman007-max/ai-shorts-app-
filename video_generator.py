from moviepy.editor import *

def create_video(audio):
    clip = ColorClip(size=(720,1280), color=(0,0,0), duration=10)
    audio_clip = AudioFileClip(audio)
    clip = clip.set_audio(audio_clip)

    clip.write_videofile("output.mp4", fps=24)
    return "output.mp4"
