import turtle

# Initialisation de la fenêtre de dessin
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Création du personnage
character = turtle.Turtle()
character.speed(0)  # Vitesse maximale

# Fonction pour dessiner un cercle
def draw_circle(color, radius, x, y):
    character.penup()
    character.goto(x, y)
    character.pendown()
    character.color(color)
    character.begin_fill()
    character.circle(radius)
    character.end_fill()

# Dessin du corps
draw_circle("yellow", 50, 0, 0)

# Dessin de la tête
draw_circle("yellow", 25, 0, 150)

# Dessin des yeux
draw_circle("black", 5, -20, 180)
draw_circle("black", 5, 20, 180)

# Dessin des bras
character.penup()
character.goto(-50, 100)
character.pendown()
character.setheading(60)
character.pensize(10)
character.forward(60)
character.backward(60)

character.penup()
character.goto(50, 100)
character.pendown()
character.setheading(120)
character.forward(60)
character.backward(60)

# Dessin des jambes
character.penup()
character.goto(-30, -50)
character.pendown()
character.setheading(260)
character.pensize(10)
character.forward(80)
character.backward(80)

character.penup()
character.goto(30, -50)
character.pendown()
character.setheading(280)
character.forward(80)
character.backward(80)

# Masquer la tortue
character.hideturtle()

# Garder la fenêtre ouverte
screen.mainloop()
