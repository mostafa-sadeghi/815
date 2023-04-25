# import random

# my_number = random.randrange(10, 101)
# print(my_number)

# my_list = ["rock","paper","scissors"]
# print(random.choice(my_list))

# تمرین بازی سنگ کاغذ و قیچی پیاده سازی کنید

import turtle

s = turtle.Screen()
p = turtle.Pen()
p.shape('turtle')
p.color("red", "purple")
p.shapesize(2)
p.pensize(4)
p.begin_fill()
for i in range(4):
    p.forward(100)
    p.left(90)
p.end_fill()

p.circle(50)

s.exitonclick()

# exercise:
# کشیدن مثلث
# کشیدن پنجضلعی
# rotated squares