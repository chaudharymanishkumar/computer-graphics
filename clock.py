#MKchaudhary 13th october 2018

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from datetime import *
from time import *
import sys

xcenter=0
ycenter=0
radius=200
hradius=100
mradius=140
sradius=170

def ROUND(a):
	return int(a+0.5)

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glPointSize(4.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-300.0,300.0,-300.0,300.0)

def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def lineDDA(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)
	x,y=x0,y0
	steps=dx if dx>dy else dy
	if steps !=0:
		change_x=dx/float(steps)
		change_y=dy/float(steps)
	else:
		change_x=0
		change_y=0
	setPixel(x,y)
	
	for k in range(int(steps)):
		if delta_x >= 0:  
			x+=change_x
		else:
			x-=change_x
		if delta_y >= 0:
			y+=change_y
		else:
			y-=change_y
		setPixel(x,y)


def read_circle_input():
	global xcenter,ycenter,radius
	xcenter=input("Enter x_center: ")
	ycenter=input("Enter y_center: ")
	radius=input("Enter radius: ")

def draw_circle(xcenter,ycenter,radius):
	glColor(1.0,0.0,0.0)
	theta=0
	while theta <=360:
		angle=(3.14*theta)/180
		x=xcenter+radius*cos(angle)
		y=ycenter+radius*sin(angle)
		setPixel(x,y)
		theta+=0.5

def glut_print( x,  y,  font,  text, r,  g , b , a):

    blending = False 
    if glIsEnabled(GL_BLEND) :
        blending = True

    glEnable(GL_BLEND)
    glRasterPos2f(x,y)
    for ch in text :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )
    if not blending :
        glDisable(GL_BLEND) 
        
def Draw():
    glColor3f(0,1,1)
    glut_print( 95+(-5) ,-165+(-5) , GLUT_BITMAP_9_BY_15 , "5" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(165+(-5),-95+(-5), GLUT_BITMAP_9_BY_15 , "4" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(190+(-5),-7 , GLUT_BITMAP_9_BY_15 , "3" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(165+(-7),95+(-7) , GLUT_BITMAP_9_BY_15 , "2" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(95+(-5),165+(-10), GLUT_BITMAP_9_BY_15 , "1" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-3,190+(-10), GLUT_BITMAP_9_BY_15 , "12" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-95+(0),165+(-10), GLUT_BITMAP_9_BY_15 , "11" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-165+(-2),95+(-10), GLUT_BITMAP_9_BY_15 , "10" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-190+(-3),-7 , GLUT_BITMAP_9_BY_15 , "9" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-165+(-5),-95+(-3) , GLUT_BITMAP_9_BY_15 , "8" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-95+(-5),-165+(-5), GLUT_BITMAP_9_BY_15 , "7" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-6,-190+(-5), GLUT_BITMAP_9_BY_15 , "6" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( -35 ,-250, GLUT_BITMAP_9_BY_15 , ":" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( 0 ,-250, GLUT_BITMAP_9_BY_15 , ":" , 1.0 , 1.0 , 1.0 , 1.0 )
    glFlush()

def get_time():
	global hr,mint,sec
	currentT=datetime.now()
	hr=currentT.hour
	if hr > 12:
		hr=hr- 12
	mint=currentT.minute
	sec=currentT.second
	
def second_niddle(sec):
	glColor(0.0,0.0,0.0)
	lineDDA(0,0,-18.164716180901422, 169.02675257505038)
	sx=sradius*cos((90-sec*6+6)*3.14/180) 
	sy=sradius*sin((90-sec*6+6)*3.14/180)
	lineDDA(0,0,sx,sy)
	glColor(1.0,1.0,1.0)
	sx=sradius*cos((90-sec*6)*3.14/180) 
	sy=sradius*sin((90-sec*6)*3.14/180)
	lineDDA(0,0,sx,sy)



def minute_niddle(mint):
	glColor(0.0,0.0,0.0)
	mx=mradius*cos((90-mint*6+6)*3.14/180)
	my=mradius*sin((90-mint*6+6)*3.14/180)
	lineDDA(0,0,mx,my)
	glColor(1.0,1.0,0.0)
	mx=mradius*cos((90-mint*6)*3.14/180) 
	my=mradius*sin((90-mint*6)*3.14/180)
	lineDDA(0,0,mx,my)

def hour_niddle(hr):
	glColor(0.0,0.0,0.0)
	hx=hradius*cos((90-hr*30+30)*3.14/180)
	hy=hradius*sin((90-hr*30+30)*3.14/180)
	lineDDA(0,0,hx,hy)
	glColor(1.0,0.0,1.0)
	hx=hradius*cos((90-hr*30)*3.14/180)
	hy=hradius*sin((90-hr*30)*3.14/180)
	lineDDA(0,0,hx,hy)

def clock():
	get_time()
	while True:
		get_time()
		if sec ==0:
			s=60
			mi=mint-1
		else:
			s=sec-1
			mi=mint
		if mint==0:
			h=hr-1
		else:
			h=hr
		glColor3f(0,0,0)
		glut_print(10 ,-250, GLUT_BITMAP_9_BY_15 ,str(s), 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( 10 ,-250, GLUT_BITMAP_9_BY_15 , str(sec) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(0,0,0)
		glut_print( -20 ,-250, GLUT_BITMAP_9_BY_15 , str(mi) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( -20 ,-250, GLUT_BITMAP_9_BY_15 , str(mint) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(0,0,0)
		glut_print( -50 ,-250, GLUT_BITMAP_9_BY_15 , str(h) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( -50 ,-250, GLUT_BITMAP_9_BY_15 , str(hr) , 1.0 , 1.0 , 1.0 , 1.0 )
		second_niddle(sec)
		minute_niddle(mint)
		hour_niddle(hr)

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_circle(xcenter,ycenter,radius)
	Draw()
	glut_print(-50 ,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().day), 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(-30 ,-280, GLUT_BITMAP_9_BY_15 ,"-", 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(-20,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().month), 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(0 ,-280, GLUT_BITMAP_9_BY_15 ,"-", 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(10 ,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().year), 1.0 , 1.0 , 1.0 , 1.0 )
	clock()
	

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Clock")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
