import turtle
#červené dlaždice 150*150, bílé spáry mezi nimi 5, bílá 4 okénka uvnitř (54*54),
#spáry mezi nimi 14

#red tile 150*150 inside till is 4 white square 54*54 and white chink 14 px

#tile (dlaždice)

#settings
Nada = turtle.Turtle()
Nada.up()
#start position (x, y)
Nada.goto(-300, 250)
Nada.down()
Nada.pensize(2)
Nada.speed(4)

#big square (150*150) - no colored
def square():
    for i in range(4):
        Nada.forward(150)
        Nada.right(90)

#position between big tile
def position():
    Nada.up()
    Nada.forward(155)
    Nada.down()

#small square (54*54)
def small_square_inside_big_square(): 
    for i in range (4):
        Nada.forward(54)
        Nada.right(90)

#position in big tile - move right
def move_right():
    Nada.forward(54)
    Nada.up()
    Nada.forward(14)
    Nada.down()   

#colored big tile (square 150*150 + colors)
def colored_big_tile():
    Nada.color("black")
    Nada.begin_fill()
    Nada.fillcolor("red")
    square()
    Nada.end_fill()

#starting position in big tile (small square - left top corner)
def left_top_corner():
    Nada.up()
    Nada.right(90)
    Nada.forward(68)
    Nada.right(90)
    Nada.forward(68)
    Nada.left(180)
    Nada.down()

#white square in tile
def white_square():
    Nada.begin_fill()
    Nada.fillcolor("white")
    small_square_inside_big_square()
    Nada.end_fill()

#start white square in tile
def start_white_square():
    Nada.up()
    Nada.right(90)
    Nada.forward(14)
    Nada.left(90)
    Nada.forward(14)
    Nada.down()


######
######
######

# 1 tile (black line - red fill)
colored_big_tile()

#starting position in big square - top small square
start_white_square()

#small top left square inside tile (black line - white fill)
white_square()

#position on tile - move right
move_right()

#small top right square inside tile (black line - white fill)
white_square()

#starting position in tile (small down left square - left top corner)

left_top_corner()

#small down left square inside tile (black - white fill)
white_square()

#position on tile - move right
move_right()

#small down right square inside tile (white fill)
white_square()

#movement on new (other) tile (turle is at top left big tile point)
Nada.up()
Nada.left(90)
Nada.forward(82)
Nada.right(90)
Nada.forward(73)
Nada.down()

###
###
###

#2 till
#till (black line - red fill)
colored_big_tile()

#starting position in big tile - top small square
start_white_square()

#small top left square (inside big square (white fill))
white_square()

#position on big tile - move right (on left small square)
move_right()

#small top right square (inside big tile (white fill))
white_square()

#starting position in big tile (small square - left top corner)
left_top_corner()

#small down left square inside big square (black - white fill)
white_square()

#position in big tile - move right
move_right()

#small down right square inside big tile (white fill)
white_square()

#movement on new (other) tile (turle is at top left big tile point)
Nada.up()
Nada.left(90)
Nada.forward(82)
Nada.right(90)
Nada.forward(73)
Nada.down()





#Nada.hideturtle()
turtle.exitonclick()
