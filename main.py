import turtle as t
import random




screen = t.Screen()
tim = t.Turtle(visible=False)
t.colormode(255)
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122),
              (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202),
              (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95),
              (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

number_of_dots = 100
for dot_count in range(1,number_of_dots + 1):
   tim.forward(50)
   tim.dot(20, random.choice(color_list))
   if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen.mainloop()
screen.exitonclick()