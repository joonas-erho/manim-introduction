from manim import *

class Sieve(Scene):
  def construct(self):
    squares = VGroup(*[Square() for i in range(100)]).arrange_in_grid(10,10).scale(0.25).shift(LEFT * 2)
    self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.005))
   
    numbers = VGroup(*[Text(str(i+1)) for i in range(100)]).scale(0.4).shift(LEFT * 2)
    for n in range(0,100):
      numbers[n].move_to(squares[n])
    self.play(AnimationGroup(*[FadeIn(n) for n in numbers], lag_ratio=0.005))

    self.wait(0.5)

    self.play(numbers[0].animate.set_color(GRAY), run_time=0.3)
    
    self.wait(5)

    self.play(numbers[1].animate.set_color(GOLD), run_time=0.3)

    self.wait(5)

    self.play(AnimationGroup(*[n.animate.set_color(RED) for n in numbers[3::2]], lag_ratio=0.01))

    self.wait(1)

    primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97  ]
    colors = [ BLUE, GREEN, PURPLE, PINK ]
    counter = 0

    for i in primes[1:5]:
      a = i - 1
      self.play(numbers[a].animate.set_color(GOLD), run_time=0.3)
      self.wait(1)
      self.play(AnimationGroup(*[n.animate.set_color(colors[counter]) for n in numbers[i+a::i]], lag_ratio=0.01))
      counter = counter + 1
      self.wait(1)

    self.wait(1)
    text = Text('11*11 = 121\r121 > 100')
    text.shift(RIGHT * 3)
    self.add(text)
    self.wait(2)

    for i in range(0,100):
      if (i not in primes):
        self.play(numbers[i-1].animate.set_color(GRAY), run_time=0.0005)
      else:
        self.play(numbers[i-1].animate.set_color(GOLD), run_time=0.0025)

    self.wait(10)