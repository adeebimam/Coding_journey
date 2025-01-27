from turtle import Turtle, Screen

addi_turtle = Turtle()
addi_turtle.shape("turtle")
addi_turtle.color("blue")

for i in range(4):
    addi_turtle.forward(100)
    addi_turtle.right(90)   
 



screen = Screen()
screen.exitonclick()