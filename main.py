import turtle
import pandas as pd

screen = turtle.Screen()


screen.title("Caba Barrios")
image = "descarga_50.gif"
screen.addshape(image)
turtle.shape(image)



data = pd.read_csv("barrios.csv")
barrios = data.barrio.to_list()




game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Adivina el barrio", prompt="Que barrio se te ocurre rey/reina?")
    if answer_state in barrios:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.barrio == answer_state]
            t.goto(int(state_data.x),int(state_data.y))
            t.color("green")
            t.write(answer_state, font=("Courier",12 ,"bold"))
    else:
        game_is_on = False





screen.exitonclick()