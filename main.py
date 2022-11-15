#----------------------------------------------
#        Name: Ashley Jagai
# Course Info: CSC111 - Fall 2021
# Description: Assignment 08
#        Date: 11/22/21
# -----------------------------------------------
# INSTRUCTIONS draw a Sierpinski Gasket recursively using turtle


import turtle

def main():
  window = turtle.Screen()
  window.setup(400, 400)
  t = turtle.Turtle()
  t.speed(0)
  #### start: moves starting position
  t.penup()
  t.goto(-window.window_width()/4, -window.window_height()/4)
  t.pendown()
  #### end: moves starting position

  length = 200
  initial_depth = 3
  draw_sierpinski(t, length, initial_depth)


# TODO: modify draw_sierpinski:
def draw_sierpinski(t, length, depth):
  # TODO: add base case
  if depth==0:
    for i in range(3):
      t.fd(length)
      t.left(120)
  else:
    #draws 1 triangle set on the bottom left
    draw_sierpinski(t, length/2, depth-1)
    t.fd(length/2)
    #draws  second trangle set right next to it
    draw_sierpinski(t, length/2, depth-1)
    t.left(120)
    t.fd(length/2)
    t.right(120)
    #draws third trangle seton top
    draw_sierpinski(t, length/2, depth-1)
    t.right(120)
    t.fd(length/2)
    t.left(120)


if __name__ == "__main__":
    main()






