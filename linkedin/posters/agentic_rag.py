from manim import *

class AgenticRAGPoster_0(Scene):
    def construct(self):
        title = Text("Agentic AI RAG Workflow", font_size=60).to_edge(UP)
        self.add(title)

        llm_box = Rectangle(width=4, height=1).set_stroke(width=2).next_to(title, DOWN, buff=1)
        llm_text = Text("LLM Layer", font_size=32).move_to(llm_box.get_center())

        sim_box = Rectangle(width=4, height=2).set_stroke(width=2).next_to(llm_box, DOWN, buff=1)
        sim_text = Text("Similarity Search\n[Relational DB | Blob DB]", font_size=24).move_to(sim_box.get_center())

        emb_box = Rectangle(width=4, height=2).set_stroke(width=2).next_to(sim_box, DOWN, buff=1)
        emb_text = Text("Embeddings\n[Sentence | Paragraph | Recursive]", font_size=24).move_to(emb_box.get_center())

        tools = VGroup(*[Rectangle(width=3, height=1).set_stroke(width=2) for _ in range(4)])
        tools.arrange(DOWN, buff=0.5).to_edge(RIGHT).shift(UP * 0.5)
        labels = ["Search Tool", "LLM Calling Tool", "Vector Store Tool", "Code Interpreter Tool"]
        tool_texts = VGroup(*[Text(label, font_size=24).move_to(box.get_center()) for label, box in zip(labels, tools)])

        agent = Circle(radius=0.3).to_edge(RIGHT).shift(UP * 3)
        agent_label = Text("Agent", font_size=18).next_to(agent, RIGHT)
        user = Circle(radius=0.3).to_edge(RIGHT).shift(DOWN * 3)
        user_label = Text("User", font_size=18).next_to(user, RIGHT)

        self.add(
            llm_box, llm_text,
            sim_box, sim_text,
            emb_box, emb_text,
            tools, tool_texts,
            agent, agent_label,
            user, user_label
        )

        arrows = [
            Arrow(llm_box.get_bottom(), sim_box.get_top(), buff=0.1),
            Arrow(sim_box.get_bottom(), emb_box.get_top(), buff=0.1),
            Arrow(sim_box.get_right(), tools[0].get_left(), buff=0.1),
            Arrow(tools[0].get_bottom(), tools[1].get_top(), buff=0.1),
            Arrow(tools[1].get_bottom(), tools[2].get_top(), buff=0.1),
            Arrow(tools[2].get_bottom(), tools[3].get_top(), buff=0.1),
            Arrow(agent.get_bottom(), tools[0].get_top(), buff=0.5),
            Arrow(user.get_top(), tools[1].get_left(), buff=0.5)
        ]

        self.play(*(GrowArrow(a) for a in arrows))
        self.wait(2)

from manim import *

class AgenticRAGPoster1(Scene):
    def construct(self):
        title = Text("Agentic AI RAG Workflow", font_size=60).to_edge(UP)
        self.add(title)

        llm_box = Rectangle(width=4, height=1).set_stroke(width=2).next_to(title, DOWN, buff=1)
        llm_text = Text("LLM Layer", font_size=32).move_to(llm_box.get_center())

        sim_box = Rectangle(width=4, height=2).set_stroke(width=2).next_to(llm_box, DOWN, buff=1)
        sim_text = Text("Similarity Search\n[Relational DB | Blob DB]", font_size=24).move_to(sim_box.get_center())

        emb_box = Rectangle(width=4, height=2).set_stroke(width=2).next_to(sim_box, DOWN, buff=1)
        emb_text = Text("Embeddings\n[Sentence | Paragraph | Recursive]", font_size=24).move_to(emb_box.get_center())

        tools = VGroup(*[Rectangle(width=3, height=1).set_stroke(width=2) for _ in range(4)])
        tools.arrange(DOWN, buff=0.5).to_edge(RIGHT).shift(UP * 0.5)
        labels = ["Search Tool", "LLM Calling Tool", "Vector Store Tool", "Code Interpreter Tool"]
        tool_texts = VGroup(*[Text(label, font_size=24).move_to(box.get_center()) for label, box in zip(labels, tools)])

        agent = Circle(radius=0.3).to_edge(RIGHT).shift(UP * 3)
        agent_label = Text("Agent", font_size=18).next_to(agent, RIGHT)
        user = Circle(radius=0.3).to_edge(RIGHT).shift(DOWN * 3)
        user_label = Text("User", font_size=18).next_to(user, RIGHT)

        self.add(
            llm_box, llm_text,
            sim_box, sim_text,
            emb_box, emb_text,
            tools, tool_texts,
            agent, agent_label,
            user, user_label
        )

        arrows = [
            Arrow(llm_box.get_bottom(), sim_box.get_top(), buff=0.1),
            Arrow(sim_box.get_bottom(), emb_box.get_top(), buff=0.1),
            Arrow(sim_box.get_right(), tools[0].get_left(), buff=0.1),
            Arrow(tools[0].get_bottom(), tools[1].get_top(), buff=0.1),
            Arrow(tools[1].get_bottom(), tools[2].get_top(), buff=0.1),
            Arrow(tools[2].get_bottom(), tools[3].get_top(), buff=0.1),
            Arrow(agent.get_bottom(), tools[0].get_top(), buff=0.5),
            Arrow(user.get_top(), tools[1].get_left(), buff=0.5)
        ]

        dashed_arrows = [DashedVMobject(a, num_dashes=12).set_stroke(width=2) for a in arrows]
        self.play(*[Create(d) for d in dashed_arrows])
        self.play(*[d.animate.shift(a.get_unit_vector() * 0.5) for d, a in zip(dashed_arrows, arrows)],
                  rate_func=linear, run_time=2)
        self.wait(2)


from manim import *

class AgenticRAGPoster(Scene):
    def construct(self):
        # title = Text("Agentic AI RAG Workflow", font_size=48).to_edge(UP)
        # self.add(title)

        # left_box = Rectangle(width=4, height=1.5).set_stroke(width=2).to_edge(LEFT).shift(DOWN)
        # left_label = Text("LLM Layer", font_size=24).move_to(left_box.get_center())
        # left_group = VGroup(left_box, left_label)

        # right_box = Rectangle(width=4, height=1.5).set_stroke(width=2).to_edge(RIGHT).shift(DOWN)
        # right_label = Text("Search Tool", font_size=24).move_to(right_box.get_center())
        # right_group = VGroup(right_box, right_label)

        arrow = Arrow(left_box.get_right(), right_box.get_left(), buff=0.9)
        dashed_arrow = DashedVMobject(arrow, num_dashes=10).set_stroke(width=2)

        self.add(left_group, right_group)
        self.play(Create(dashed_arrow))
        # Animate the dash pattern moving along the path without changing endpoints
        self.play(dashed_arrow.animate.set(dash_offset=100), run_time=10, rate_func=linear)
        self.wait(2)


from manim import *

class SingleArrowScene(Scene):
    def construct(self):
        # Draw an arrow from left to right
        arrow = Arrow(start=LEFT * 3, end=RIGHT * 3, buff=0)
        self.add(arrow)
        # Hold on screen for 2 seconds
        self.wait(2)

from manim import *

class SingleDottedArrowScene(Scene):
    def construct(self):
        # Create a dotted arrow
        arrow = DashedVMobject(
            Arrow(start=LEFT * 3, end=RIGHT * 3, buff=0),
            num_dashes=30
        ).set_stroke(width=2)
        # Add it directly (no animation on entry)
        self.add(arrow)
        # Hold on screen so you can see the dots
        self.wait(2)


from manim import *

class MovingDottedArrowScene(Scene):
    def construct(self):
        # 1) Create a regular arrow
        arrow = Arrow(start=LEFT * 3, end=RIGHT * 3, buff=0)

        # 2) Turn it into a dashed (dotted) arrow
        dotted = DashedVMobject(arrow, num_dashes=30).set_stroke(width=2)

        # 3) Add it to the scene
        self.add(dotted)

        # 4) Updater to slide the dash pattern along the path
        def flow_dots(mob, dt):
            mob.dash_offset += dt * 2  # tweak the multiplier for speed

        dotted.add_updater(flow_dots)

        # 5) Hold for 10 s so you can see the motion
        self.wait(10)

from manim import *

class MovingDashedLine(Scene):
    def construct(self):
        # Define the start and end points of the line
        start_point = LEFT * 3
        end_point = RIGHT * 3

        # Create the dotted line
        dashed_line = DashedLine(start_point, end_point, dash_length=0.2)
        self.add(dashed_line)

        # Define a path for the line to move along
        path = Line(LEFT * 3, RIGHT * 3)

        # Create the animation
        self.play(MoveAlongPath(dashed_line, path), run_time=2)

        self.wait()
        
        
from manim import *

class ContinuousDashedLine(Scene):
    def construct(self):
        # Define the start and end points
        start_point = LEFT * 3
        end_point = RIGHT * 3

        # Create the dotted line
        dashed_line = DashedLine(start_point, end_point, dash_length=0.2)
        self.add(dashed_line)

        # Create a ValueTracker to control the movement
        value_tracker = ValueTracker(0)

        # Add an updater to update the line's end points
        dashed_line.add_updater(lambda line, alpha: line.put_start_and_end_on(
            start_point + (end_point - start_point) * value_tracker.get_value(),
            start_point + (end_point - start_point) * (1 - value_tracker.get_value())
        ))

        # Animate the ValueTracker (which will update the line)
        self.play(value_tracker.animate.set_value(1), run_time=2)
        self.wait()

        # Optional: Animate the ValueTracker back to 0
        self.play(value_tracker.animate.set_value(0), run_time=2)
        self.wait()        
        

from manim import *

class MoveAlongPathExample1(Scene):
    def construct(self):
        d1 = Dot().set_color(ORANGE)
        l1 = Line(LEFT, RIGHT)
        l2 = VMobject()
        self.add(d1, l1, l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)        
        
   

class MoveAlongPathExample(Scene):
    def construct(self):
        
        # Define the start and end points of the line
        start_point = LEFT * 3
        end_point = RIGHT * 3

        # Create the dotted line
        dashed_line = DashedLine(start_point, end_point, dash_length=0.5)
        # self.add(dashed_line)

        
        d1 = Dot().set_color(ORANGE)
        # l1 = Line(LEFT, RIGHT)
        l1 = Line(start_point, end_point)
        l2 = VMobject()
        self.add(d1, l2)
        l2.add_updater(lambda x: x.become(DashedLine(start_point, d1.get_center(), dash_length=0.5).set_color(WHITE)))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)        
        

from manim import *

class MovingDashedLine(Scene):
    def construct(self):
        # 1) Create a static straight line
        line = Line(LEFT * 3, RIGHT * 3, stroke_width=2)

        # 2) Turn it into a dashed line
        dashed = DashedVMobject(line, num_dashes=40)

        # 3) Add it to the scene
        self.add(dashed)

        # 4) Updater: slide the dash pattern along the path
        def flow_dots(mob, dt):
            mob.dash_offset += dt * 3  # speed: increase or decrease multiplier

        dashed.add_updater(flow_dots)

        # 5) Hold on screen (e.g. 10s) to see the movement
        self.wait(10)

# Ten Moving Lines Animation in Manim

class TenMovingLines(Scene):
    def construct(self):
        speed = 2  # units per second

        # Spawner for a single short line
        def spawn_line():
            line = Line(LEFT * 3, LEFT * 2.5, stroke_width=10)
            self.add(line)
            # Updater: moves the line to the right continuously
            line.add_updater(lambda m, dt: m.shift(RIGHT * speed * dt))

        # Spawn and start moving 10 lines, one every 0.5 seconds
        for _ in range(10):
            spawn_line()
            self.wait(0.5)

        # Let all lines keep moving for 5 more seconds
        self.wait(5)

class WrappingLinesScene(Scene):
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
