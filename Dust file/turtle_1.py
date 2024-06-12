# import turtle library
import turtle             
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
my_pen.color("black")
my_pen.width(3)
def my_sqrfunc(size):
   for i in range(4):
      my_pen.fd(size)
      my_pen.left(90)
      size = size - 5
i = 200
while i > 0:
   my_sqrfunc(i-20)
   if(i%2)==0:
      my_sqrfunc(30)
      for x in range(6):
         my_sqrfunc(x+40)
   i = i-1