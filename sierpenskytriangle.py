#Mkchaudhary 6th oct 2018
#Sierpensky triangle

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def ROUND(a):
	return int(a+0.5)
k=0
def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,600.0,0.0,600.0)

def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2i(x,y)
	glEnd()
	glFlush()

def readvertices():
	global n,x0,y0,x1,y1,x2,y2
	x0=input("Enter 1st_x: ")
	y0=input("Enter 1st_y: ")
	x1=input("Enter 2nd_x: ")
	y1=input("Enter 2nd_y: ")
	x2=input("Enter 3rd_x: ")
	y2=input("Enter 3rd_y: ")
	n=input("Enter level of sierpensky: ")

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
	setPixel(ROUND(x),ROUND(y))
	
	for k in range(steps):
		if delta_x >= 0:  
			x+=change_x
		else:
			x-=change_x
		if delta_y >= 0:
			y+=change_y
		else:
			y-=change_y
		setPixel(ROUND(x),ROUND(y))


def draw_triangle(x0,y0,x1,y1,x2,y2):
	lineDDA(x0,y0,x1,y1)
	lineDDA(x1,y1,x2,y2)
	lineDDA(x0,y0,x2,y2)
	
def sierpensky(x0,y0,x1,y1,x2,y2,k):
	k+=1
	if k>n:
		return
	mx0=(x0+x1)/2
	my0=(y0+y1)/2
	mx1=(x1+x2)/2
	my1=(y1+y2)/2
	mx2=(x2+x0)/2
	my2=(y2+y0)/2
	glColor3f(1.0,1.0,1.0)
	draw_triangle(mx0,my0,mx1,my1,mx2,my2)
	sierpensky(x0,y0,mx0,my0,mx2,my2,k)
	sierpensky(mx0,my0,x1,y1,mx1,my1,k)
	sierpensky(mx1,my1,x2,y2,mx2,my2,k)
	

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	draw_triangle(x0,y0,x1,y1,x2,y2)
	sierpensky(x0,y0,x1,y1,x2,y2,k)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Seirpensky Triangle")
	readvertices()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
