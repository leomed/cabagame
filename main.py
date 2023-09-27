import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("Caba Barrios")
image = "descarga_50.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("barrios.csv")
"""First it's better to convert the data into a list, so as to
    manipulate it more efficiently
    
    data.barrio is a SERIES in panda structure
 """
barrios = data.barrio.to_list()
# How to look for in row
# print(data[data.barrio == "Mataderos"].x)
# print(data[data.barrio == "Mataderos"].y)

barrios_adivinados = []

while len(barrios_adivinados) < len(barrios):
    answer_barrio = screen.textinput(title=f"Adivina el barrio {len(barrios_adivinados)}/{len(barrios)}",prompt="Que barrio se te ocurre rey/reina?").title()

    """Esta manera esta hecho con list comprehension"""
    if answer_barrio == "Exit":
        barrios_sin_adivinar = [barrio for barrio in barrios if barrio not in barrios_adivinados]
        new_data = pd.DataFrame(barrios_sin_adivinar)
        new_data.to_csv("Barrios_por_conocer.csv")
        break

    """Esta manera esta hecho con sin list comprehension"""

    # if answer_barrio == "Exit":
    #     barrios_sin_adivinar = []
    #     """Si quedaron barrios sin adivinar,se appendea a una nueva lista
    #     """
    #     for barrio in barriose:
    #         if barrio not in barrios_adivinados:
    #             barrios_sin_adivinar.append(barrio)
    #     new_data = pd.DataFrame(barrios_sin_adivinar)
    #     new_data.to_csv("Barrios_por_conocer.csv")
    #     break

    if answer_barrio in barrios:
        barrios_adivinados.append(answer_barrio)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        """Barrio_data is a row"""
        barrio_data = data[data.barrio == answer_barrio]
        t.goto(int(barrio_data.x), int(barrio_data.y))
        t.color("green")
        """Item just grabs the first element"""
        # barrio_data.barrio.item()
        t.write(answer_barrio, font=("Courier", 12, "bold"))


