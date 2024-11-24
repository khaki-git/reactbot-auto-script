# reactbotify
a small script i wrote that generates reactbot reactions, based off of those [spammy yt short channels](<https://www.youtube.com/watch?v=dr4a3Cwyfag>).  
i recommend you read this entire `README.md` document if you're planning to use this script
### how to reactbot
open `interface.py` and then press the `Select Video` button to choose which video for reactbot to react to, then just press render and look at the terminal for progress updates on rendering
### project structure
`reactbot.ico` - window icon  
`repatch_filler.py` - fixes metadata and headers in the video files in `tmp`, and then exports them to `filler`, if you're going to add more reactbot reactions, you should save the videos to the `tmp` directory and then run the `repatch_filler.py` script to patch the `filler` directory.  
`video.py` - module for generating the actual video  
`interface.py` - main file that you should open when launching the program, holds the gui interface for the app  
`requirements.txt` - once you've download the repository, you should run `pip install -r requirements.txt` to install dependencies.  
`coreclips` - hold clips that are required for the script, mainly the reactbot idle animation  
`filler` - holds all of the patched reactbot reactions after executing `repatch_filler.py`  
`tmp` - where you should save ALL of your reactbot reactions, then run `repatch_filler.py` to properly patch them
### more dependencies
you MUST have the `ffmpeg` cli tool if you're going to add more reactions and then patch them, you can download [here](https://ffmpeg.org/), make sure you add it to PATH