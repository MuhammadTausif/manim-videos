from manim import *

class LinkedInPoster(Scene):
    def construct(self):
        # Title
        title = Text("My Project Update", font_size=72)
        subtitle = Text("Built with Manim", font_size=48).next_to(title, DOWN, buff=0.5)

        # Bring them on-screen
        self.play(Write(title))
        self.play(FadeIn(subtitle))

        # Optional: add your logo or QR code
        # logo = ImageMobject("my_logo.png").scale(0.5).to_corner(UR)
        # self.add(logo)


## manim poster.py LinkedInPoster -p -s -r 1200,628
## manim poster.py LinkedInPoster -p -s -r 628,1200
## manim poster.py LinkedInPoster -p -r 628,1200

## ffmpeg -i complete_path\manim-videos\linkedin\posters\media\videos\poster_simple\1080p60\LinkedInPoster.mp4  -vf "fps=15,scale=1200:628:flags=lanczos"     complete_path\manim-videos\linkedin\posters\media\videos\poster_simple\LinkedInPoster.gif
