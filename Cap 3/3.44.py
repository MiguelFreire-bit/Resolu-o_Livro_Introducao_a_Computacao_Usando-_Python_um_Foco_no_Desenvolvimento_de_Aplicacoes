import turtle
import math

# Cria uma tartaruga
t = turtle.Turtle()

def centro(n):
    lado = 100
    d = lado / 2

    # mover o turtle para que o centro do hexágono fique no centro da tela
    t.speed(0)
    distancia = (lado / 2) * 1 / math.sin(math.pi / n)
    t.penup()
    t.goto(-d, -distancia)
    t.pendown()

def poligono(n):
    while n < 3:
        n = int(input("Digite N maior ou igual a 3 "))
    centro(n)
    # Os ângulos internos de um polígono regular de n lados podem ser calculados
    # através da fórmula: Ângulo interno = (n - 2) * 180 / n
    angulo_externo = 180 - ((n - 2) * 180) / n

    # Desenha um polígono
    for i in range(n):
        t.forward(100)
        t.left(angulo_externo)

    # Mantém a janela aberta
    turtle.done()

poligono(7)