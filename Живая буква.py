import turtle
import tkinter

t = turtle.Pen()
def вывод_буквы():
    t.pencolor("Violet")
    turtle.bgcolor("Black")
    t.write("К", font = ("Arial", 12))

def Смена(event):
    t.clear()
    t.pencolor("Orange")
    turtle.bgcolor("Black")
    t.write("К", font = ("Arial", 36))
def Смена1(event):
    t.clear()
    t.pencolor("Violet")
    turtle.bgcolor("Black")
    t.write("К", font = ("Arial", 12))

вывод_буквы()
root = tkinter.Tk()
root.bind("<Button-1>", Смена)
root.bind("<Button-2>", Смена1)


turtle.mainloop()
