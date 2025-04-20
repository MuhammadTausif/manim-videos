# Command to run MANIM

### Run Simple file
`manim poster.py LinkedInPoster -p -s -r 1200,628`
`manim poster.py LinkedInPoster -p -s -r 628,1200`
`manim poster.py LinkedInPoster -p -r 628,1200`


### Converting MP4 to PNG

`ffmpeg -i complete_path\manim-videos\linkedin\posters\media\videos\poster_simple\1080p60\LinkedInPoster.mp4  -vf "fps=15,scale=1200:628:flags=lanczos"     complete_path\manim-videos\linkedin\posters\media\videos\poster_simple\LinkedInPoster.gif
`
