from turtle import *
import colorsys
bgcolor('black')
tracer(500)
def draw():
    h=0
    for i in range(100):
        c=colorsys.hls_to_rgb(h,1,1)
        h +=0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor(c)
        begin_fill()
        rt(100)
        circle(i,15)
        fd(290)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j,299,steps=5)
            end_fill()
draw()
done()
