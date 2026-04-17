Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import math
import random

print("Monte-Carlo pi approximator")

number_of_iterations = int(input("Enter the total number of iterations: "))
display_step = int(input("Enter the display step: "))

number_of_steps = int(number_of_iterations/display_step)

inside = 0   # number of points inside the circle
outside = 0  # number of points outside the circle

for i in range(number_of_steps):
  for j in range(display_step):
    x = random.random()   # random position coordinates
    y = random.random()   # random position coordinates
    d = math.sqrt(x**2 + y**2)  # the distance from the origin to the point (x,y) 
    if d < 1:   # checking if the point (x,y) is inside the circle
      inside += 1
    else:
      outside +=1
    all = inside + outside
  pi = 4*(inside/all)
  print(str(display_step*(i+1)),":", pi)

print("The calculated final value is:",pi)
print("Python math.pi equals:",math.pi)
