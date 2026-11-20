import turtle
import time


t = turtle.Pen()
t.shape("turtle")
Поле = turtle.Screen()
Ширина = turtle.Screen().window_width()	
Высота = turtle.Screen().window_height()
x = Ширина / 2
y = Высота / 2
h = 0 
print(Ширина, Высота)
while(h != 5):
	a = t.xcor()
	if(a > -x + 20 and a < x - 20):
		t.forward(10)
		time.sleep(0.1)
	else:
		t.left(180)
		h = h + 1
