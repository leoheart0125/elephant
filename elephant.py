#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

from turtle import *

def body():
    #身體和四肢
    
    #身軀
    width(3)
    color("#000000","#AAAAAA")
    begin_fill()
    left(90)
    forward(50)
    circle(-50,90)
    forward(400)
    right(180)
    circle(50,-90)
    right(180)
    forward(400)
	
    #四肢
    right(90)
    forward(70)
    right(90)
    forward(60)
    left(90)
    forward(70)
    left(90)
    forward(60)
    right(90)
    forward(70)
    right(90)
    forward(60)
    left(90)
    forward(70)
    left(90)
    forward(60)
    right(90)
    forward(70)
    right(90)
    forward(60)
    left(90)
    forward(70)
    left(90)
    forward(60)
    right(90)
    forward(70)
    right(90)
    forward(60)
    left(90)
    forward(10)
    right(90)
    forward(300)
    end_fill()
    
    #將角度重置
    right(90)
	
	
def ear_and_nose(radius,length):
    
        #重製至(0,0)開始畫頭
    up()
    goto(0,0)
    down()
    width(3)
    
         #畫兩個耳朵
    color("#000000","#AAAAAA")
    begin_fill()
    circle(radius,360)
    right(90)
    circle(radius,360)
    end_fill()
    right(-300)
    
	#畫鼻子
    width(100)
    color("#AAAAAA")
    begin_fill()
    forward(length)
    up()    
    right(90)
    forward(50)
    down()
    width(3)
    begin_fill()
    
	#鼻子的彎曲處
    left(90)
    circle(100,180)
    left(90)
    forward(20)
    end_fill()

def head():
        #頭部
    up()
    forward(75)
    left(90)
    forward(10)
    up()
    backward(420)
    right(90)
    forward(75)
    down()
    begin_fill()
    color("#AAAAAA")
    circle(150,360)
    end_fill()
    
	#眉毛+眼睛
    color("#000000")
    up()
    left(90)
    forward(70)
    right(90)
    forward(50)
    down()
    circle(30,60)
    up()
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    down()
    circle(30,60)
    up()
    left(90)
    forward(30)
    right(90)
    forward(5)
    down()
    color("#000000","#000000")
    begin_fill()
    circle(20,360)
    end_fill()
    up()
    forward(100)
    right(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(15)
    left(90)
    down()
    begin_fill()
    circle(20,360)
    end_fill()
    
	#左象牙
    up()
    left(60)
    forward(170)
    right(30)
    down()
    color("#000000","#FFFFF0")
    begin_fill()
    circle(100,30)
    left(130)
    circle(100,30)
    end_fill()
    
	#右象牙
    up()
    right(50)
    forward(150)
    right(90)
    forward(30)
    down()
    begin_fill()
    circle(100,30)
    left(130)
    circle(100,30)
    forward(10)
    end_fill()

def main():
    reset()
    body()
    ear_and_nose(120,200)
    head()
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
