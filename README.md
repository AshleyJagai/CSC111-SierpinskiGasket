# CSC111-SierpinskiGasket

# Assignment 08

Due: Wednesday 11/24 before 11:59 PM

## Drawing a Sierpinski Gasket with turtle

You will use recursion and the turtle module to draw a Sierpinski Gasket.

# Gasket Description:

The Gasket is drawn by the following procedure:

The triangle parts mentioned below:

![sierpinski-points](sierpinski-points.png)

  1. Given a turtle reference ```tur```, a triangle ```length```, and a ```depth```:
    1. If the current drawing depth is 0 (the triangle to be drawn is the smallest), then:
        1. Starting at the bottom left corner of a triangle and facing ```0 degrees``` ( Right / East), draw a triangle by moving straight a distance ```length```, turn ```left``` ```120``` degrees, and repeat twice until you are at the starting position facing the initial orientation (```0 degrees```)
    1. Otherwise (depth is not 0): 
        1. call the function recursively three times, each with a length of ```length/2``` and a depth of ```depth-1```: once for the subtriangle on the bottom left side (Triangle ```ABC```, starting at point ```A```, ```0 degrees```), once for the sub-triangle on the bottom right (Triangle ```BDE```, starting at point ```B```, ```0 degrees```), and once for the sub-triangle on the top (Triangle ```CEF```, starting at point ```C```, ```0 degrees```).
        2. Return to point ```A``` facing right.

## Notes:

Remember to go to the starting position and orientation of each subtriangle BEFORE doing the recursive call!

## Grading:

1. The code MUST compile: 50%
2. The top triangle is drawn: 10%
3. sub triangle ABC is drawn: 10%
4. sub triangle BDE is drawn: 10%
5. sub triangle CEF is drawn: 10%
6. The code MUST be commented: 10%

