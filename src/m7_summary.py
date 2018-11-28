"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Paige Swango.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
#
# TODO: 2.
#   Write code that accomplishes the following (and ONLY the following),
#   in the order listed:
#
#    - Constructs a SimpleTurtle with a  'blue'  Pen.
#
#    - Makes the SimpleTurtle go straight UP 200 pixels.
#
#    - Makes the SimpleTurtle lift its pen UP
#         (so that the next movements do NOT leave a "trail")
#         HINT: Use the "dot trick" to figure out how to do this.
#
#    - Makes the SimpleTurtle go to the Point at (100, -40).
#
#    - Makes the SimpleTurtle put its pen DOWN
#         (so that the next movements will return to leaving a "trail").
#
#    - Makes the SimpleTurtle's pen have color 'green' and thickness 10.
#
#    - Makes the SimpleTurtle go 150 pixels straight DOWN.
#
#   Don't forget to:
#     - import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     - ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#   As always, test by running the module.
#   As always, COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(20)

tom=rg.SimpleTurtle()
tom = rg.SimpleTurtle('turtle')
tom.pen = rg.Pen('blue', 20)
tom.right(-90)
tom.forward(200)
tom.right(90)
tom.pen_up()
tom.forward(100)
tom.right(-90)
tom.forward(40)
tom.pen_down()
tom.pen=rg.Pen('green',10)
tom.backward(150)
window.close_on_mouse_click()