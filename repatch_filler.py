import os, subprocess, shutil

shutil.rmtree("./filler")
os.mkdir("./filler")

for i, file in enumerate(os.listdir('./tmp')):
    full_path = os.path.abspath(f"./tmp/{file}")

    subprocess.run(["ffmpeg", "-i", full_path, "-c:v", "libx264", "-crf", "23", "-preset", "veryfast", "-c:a", "aac", "-b:a", "128k", os.path.abspath(f"./filler/ex_{i}.mp4")])