#!/usr/bin/python
#coding: utf-8
""" -- Solsystemet - Opprettet 24.03.16 --
    Dette programmet begynte med at eg
     bare hadde tenkt til å rendere lys 
      på en realistisk måte, men eksalerte til
       å bli en presentasjon av solsystemet.  
        --------------- Jonas --------- """

from turtle import Turtle, Screen


s = Screen()
s.delay(0)
s.bgcolor('black')


class Sola():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.farge = 'yellow'

        self.t = Turtle()
        self.t.speed(0)
        self.t.penup()
        self.t.setpos(x, y)
        self.t.shape("circle")
        self.t.color(self.farge)
        self.t.shapesize(3)
        self.t.stamp()

    def render_light(self):

        s.colormode(255)
        self.t.width(10)
        self.t.ht()
        farge = 255
        self.t.color(farge, farge, 0)
        x = 0
        x_des = 0
        count = 0
        for i in range(36):
            spacing = i*8
            self.t.rt(90)
            self.t.fd(spacing)
            self.t.lt(90)
            self.t.pendown()
            self.t.circle(spacing)
            self.t.penup()
            self.t.goto(self.x, self.y)

            farge -= 11
            farge += x
            print('farge', farge)
            count += 1
            x_des += 0.25
            print('x_des', x_des)
            if x_des % 1 == 0: 
                x += 1
            print('x', x)
            print('i', i)
            self.t.color(farge, farge, 0)
        self.t.color(self.farge)
        self.t.goto(self.x, self.y)
        self.t.st()


class Planet():
    def __init__(self, radius=100, size=2):
        self.t = Turtle()
        self.radius = radius
        self.t.color('black')
        self.t.shape('circle')
        self.t.speed(1)
        self.t.penup()
        self.t.rt(90)
        self.t.forward(radius)    # <-- Radius!
        self.t.lt(90)
        self.t.shapesize(size)    # <--- Size !

    def folg_bane(self, hastighet=2):
        self.t.circle(self.radius, hastighet) # <--- hastighet


sol = Sola()
sol.render_light()

s.delay(0.1)

merkur = Planet(50, 1)  # Planet(radius, size)
venus = Planet(100, 2)
jorda = Planet(150, 3)
jupiter = Planet(250, 5)

while True:
    merkur.folg_bane(8) # folg_bane(grader)
    venus.folg_bane(6)
    jorda.folg_bane(5)
    jupiter.folg_bane(2)

s.mainloop()


