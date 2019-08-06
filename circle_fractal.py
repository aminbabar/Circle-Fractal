"""
 *****************************************************************************
   FILE:  circle_fractal.py

   AUTHOR:  Amin Babar

   ASSIGNMENT: Project 7: circle_fractal

   DATE: 10/20/17

   DESCRIPTION: This program takes in the input for level and radius from user,
   and creates a fractal recursively based on that information

 *****************************************************************************
"""

import turtle

t = turtle.Turtle()
t.speed(0)
r = int(input("Please enter the radius: "))
level = int(input("Please enter the level: "))


def circle_draw(r):
    """ Draws a circle with radius r """

    # Ensures the same start and end postion for the turtle. Also, results in
    # the correct center for the circle
    t.up()
    t.right(90)
    t.forward(r)
    t.left(90)
    t.down()
    t.circle(r)
    t.up()
    t.left(90)
    t.forward(r)
    t.right(90)


def circle_fractal(t, r, level):
    """ Takes in the input of radius and level from the user, and draws a
    fractal based on that information """
    # CITE: Worked with professor Helmuth on the recursion part
    # Base case for level 0
    if level == 0:
        circle_draw(r)

    # if level is greater than 0, the turtle draws 3 circles recursively on the
    # circumference of each circle it draws. The total number of circles depend
    # on the level entered in by the user.
    if level > 0:
        circle_draw(r)
        t.up()
        t.forward(r)
        t.down()
        circle_fractal(t, r / 2, level - 1)

        t.right(180)
        t.forward(r)
        t.right(60)
        t.forward(r)
        circle_fractal(t, r / 2, level - 1)

        t.right(180)
        t.forward(r)
        t.right(60)
        t.forward(r)
        circle_fractal(t, r / 2, level - 1)

        # Ensures that the turtle returns back to the center after its done
        # drawing a circle
        t.left(180)
        t.forward(r)
        t.right(60)


def main():

    # corrects the heading for the turtle to vertical before the turtle
    # begins to draw
    t.setheading(90)
    circle_fractal(t, r, level)

    turtle.mainloop()


if __name__ == "__main__":
    main()
