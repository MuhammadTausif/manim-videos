from manim import *


class ContinuesLine(Scene):
    def construct(self):
        speed = 2             # movement speed (units/sec)
        spawn_interval = 0.5  # time between spawns
        line_length = 0.5     # length of each short line

        left_edge = LEFT * 3
        right_edge = RIGHT * 3

        for _ in range(10):
            # Create a short line at the left edge
            start = left_edge
            end = left_edge + RIGHT * line_length
            line = Line(start, end, stroke_width=4)
            self.add(line)

            # Store its original center to reset later
            original_center = line.get_center()

            # Updater: move right, then wrap around when past right_edge
            def move_and_wrap(mob, dt, orig_center=original_center):
                mob.shift(RIGHT * speed * dt)
                if mob.get_start()[0] > right_edge[0]:
                    mob.move_to(orig_center)

            line.add_updater(move_and_wrap)

            # Wait before spawning the next line
            self.wait(spawn_interval)

        # Let all lines keep moving for 5 seconds
        self.wait(5)


class DashedLineScene(Scene):
    def construct(self):
        # Create a dashed line from left to right
        dashed_line = DashedLine(start=LEFT, end=RIGHT, dash_length=0.2, dashed_ratio=0.5)
        self.add(dashed_line)

from manim import *

class AlternatingDashedLine(Scene):
    def construct(self):
        # Dashed line 1 (starts with visible dashes)
        dashed_line1 = DashedLine(start=LEFT * 5, end=RIGHT * 5, dash_length=0.4, dashed_ratio=0.5, color=WHITE)

        # Dashed line 2 (inverted pattern)
        # dashed_line2 = DashedLine(start=LEFT * 5, end=RIGHT * 5, dash_length=0.4, dashed_ratio=0.5, color=WHITE)
        # Dashed line 2 — shifted exactly one dash length to the right
        dashed_line2 = DashedLine(start=LEFT * 5 + RIGHT * 0.4, end=RIGHT * 5 + RIGHT * 0.4, dash_length=0.4, dashed_ratio=0.5, color=WHITE)
        dashed_line2.shift(UP * 0.001)  # Slight offset to avoid z-fighting

        # Flip the phase of second line so its white appears in first line's black
        dashed_line2.set_dash_offset(0.2)  # half of dash_length * dashed_ratio = 0.4 * 0.5 = 0.2

        # Initially show only line 1
        self.add(dashed_line1)

        # Alternate appearance every 0.1 second for a few seconds
        for _ in range(20):
            self.wait(0.1)
            self.remove(dashed_line1)
            self.add(dashed_line2)

            self.wait(0.1)
            self.remove(dashed_line2)
            self.add(dashed_line1)

        self.wait(1)
