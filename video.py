import os
import moviepy
from moviepy.video.fx import Resize
from tkinter import filedialog
import random

gap = 5

def get_filler():
    videos = os.listdir("./filler")
    return f"./filler/{random.choice(videos)}"

def generate_video(path: str, output_path: str):
    if not os.path.exists(path):
        return

    if path.endswith('.mp4'):
        content = moviepy.VideoFileClip(path)
    elif path.endswith('.png') or path.endswith('.jpg'):
        content = moviepy.ImageClip(path).with_duration(10)
    else:
        return

    reaction = moviepy.VideoFileClip(get_filler())

    while reaction.duration < content.duration:
        clip_path = moviepy.VideoFileClip(get_filler())
        next_idle = moviepy.VideoFileClip("./coreclips/idle.mp4").with_duration(random.random())
        clip_path = moviepy.concatenate_videoclips([clip_path, next_idle])
        already_idle = False
        if clip_path.duration + reaction.duration > content.duration:
            clip_path = moviepy.VideoFileClip("./coreclips/idle.mp4")
            already_idle = True
        if not already_idle and random.random() < 0.1:
            clip_path = moviepy.VideoFileClip("./coreclips/idle.mp4").with_duration(random.random())
        reaction = moviepy.concatenate_videoclips([reaction, clip_path])

    reaction = reaction.with_duration(content.duration)

    content = content.with_effects([Resize(width=640)]).with_position(("center", 0))
    reaction = reaction.with_effects([Resize(width=640)]).with_position(("center", content.h + gap))

    content = moviepy.CompositeVideoClip([content, reaction], size=(content.w, content.h + reaction.h + gap))

    content.write_videofile(output_path, fps=24)

if __name__ == '__main__':
    generate_video(filedialog.askopenfilename())