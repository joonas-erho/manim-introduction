from manim import *

class Examples(Scene):
  def construct(self):
    circle = Circle()  # create a circle
    circle.set_fill(PINK, opacity=0.5)  # set color and transparency

    square = Square()  # create a square
    square.rotate(PI / 4)  # rotate a certain amount

    self.play(Create(square))  # animate the creation of the square
    self.play(Transform(square, circle))  # interpolate the square into the circle
    self.play(square.animate.shift(LEFT * 5))

    text = Tex("\LaTeX", font_size=72)
    self.play(Write(text))
    self.play(text.animate.shift(RIGHT * 5))

    G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                  layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                          4: [1, 0, 0], 5: [2, 0, 0]}
                  )
    self.play(Create(G))
    self.play(G.animate.change_layout("circular"))
    self.wait("Moi kaikki KOTEP-opiskelijat :)")
