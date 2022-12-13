from manim import *

class Pointers(Scene):
  def construct(self):
    code = ImageMobject(os.getcwd() + "/media/assets/koodi.png")
    code.scale(1.2)
    code.to_edge(RIGHT, buff=1)

    title1 = Text("Variables").scale(0.5)
    title2 = Text("Objects in Memory").scale(0.5)
    title3 = Text("Output:").scale(0.5)
    title1.to_edge(LEFT, buff=1).to_edge(UP, buff=1)
    title2.next_to(title1, RIGHT).shift(RIGHT * 2)
    title3.next_to(title1, DOWN).shift(DOWN * 5)

    # Create line to indicate current position in code
    currentLine = Rectangle(RED, 0.25, 4)
    currentLine.next_to(code, UP)
    currentLine.shift(DOWN * 1).shift(RIGHT * 0.25)
    currentLine.set_opacity(0.5)
    currentLine.set_fill(RED, opacity=0.1)

    self.play(FadeIn(code))
    self.play(Write(title1))
    self.play(Write(title2))
    self.play(Write(title3))

    self.wait(2)

    self.play(Create(currentLine))

    self.wait(2)

    var1 = Text("cat1").scale(0.5).next_to(title1, DOWN)
    self.play(Write(var1))
    obj1 = textbox("Tane").scale(0.5).next_to(title2, DOWN).shift(UP * 0.15)
    self.play(Create(obj1))
    arrow1 = Arrow(start=LEFT, end=RIGHT * 2.25, color=GRAY).next_to(var1)
    self.play(Create(arrow1))

    shift_code(self, currentLine)
    change_output(self, "Tane says meow!", title3)
    shift_code(self, currentLine)

    var2 = Text("cat2").scale(0.5).next_to(var1, DOWN).shift(DOWN * 0.25)
    self.play(Write(var2))
    obj2 = textbox("Papu").scale(0.5).next_to(obj1, DOWN)
    self.play(Create(obj2))
    arrow2 = Arrow(start=LEFT, end=RIGHT * 2.25, color=GRAY).next_to(var2)
    self.play(Create(arrow2))

    shift_code(self, currentLine)
    change_output(self, "Papu says meow!", title3)
    shift_code(self, currentLine)

    var3 = Text("cat3").scale(0.5).next_to(var2, DOWN).shift(DOWN * 0.25)
    self.play(Write(var3))
    arrow3 = Arrow(start=LEFT, end=RIGHT * 2.5, color=GRAY).next_to(var3).rotate(0.37).shift(UP * 0.55).shift(LEFT * 0.1)
    self.play(Create(arrow3))

    shift_code(self, currentLine)
    change_output(self, "Tane says meow!", title3)
    self.wait(3)

    shift_code(self, currentLine)

    arrow4 = Arrow(start=LEFT, end=RIGHT * 2.35, color=GRAY).next_to(var2).rotate(0.22).shift(UP * 0.2)
    self.play(Transform(arrow2, arrow4))

    self.wait(3)

    self.play(obj2.animate.set_color(RED))
    self.play(FadeOut(obj2))

    shift_code(self, currentLine)
    change_output(self, "Tane says meow!", title3)

    self.wait(10)

def textbox(string):
  result = VGroup() # create a VGroup
  box = Rectangle(  # create a box
      height=1, width=2, stroke_color=WHITE
  )
  text = Text(string).move_to(box.get_center()) # create text
  result.add(box, text) # add both objects to the VGroup
  return result

def shift_code(self, rect):
  self.play(rect.animate.shift(DOWN * 0.235))

def change_output(self, text, title):
  text_obj = Text(text).scale(0.5).next_to(title)
  self.play(Write(text_obj))
  self.wait(1)
  self.play(FadeOut(text_obj))
