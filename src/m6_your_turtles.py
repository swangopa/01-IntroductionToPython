"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Paige Swango.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('teal', 10)
blue_turtle.speed= 20

size=200
for k in range (20):
    blue_turtle.draw_square(size)
    blue_turtle.pen_up()
    blue_turtle.right(90)
    blue_turtle.forward(30)
    blue_turtle.left(90)
    blue_turtle.pen_down()
    size = size - 20

window.tracer(100)
another_turtle = rg.SimpleTurtle('circle')
another_turtle.pen = rg.Pen('green', 30)
another_turtle.backward(20)


