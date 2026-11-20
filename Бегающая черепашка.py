import turtle
import time


t = turtle.Pen()
t.shape("turtle")
t.setheading(45)
for i in range(50):
  t.forward(10)
  time.sleep(0.1)
t.write("Салам, братка!", font = ("Arial", 14))

time.sleep(10)
