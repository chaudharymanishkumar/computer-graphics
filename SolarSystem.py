#Solar System
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import math
from  math import *
import numpy
import sys
sys.setrecursionlimit(8000000)
def init():
	glClearColor(0.0,0.0,0.0,0.0)
	
	glPointSize(3)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,800.0,0.0,800.0)

def setpixn(xcor,ycor):
	glBegin(GL_POINTS)	
	glVertex2i(xcor,ycor)
	glEnd()
	glFlush()
def circle(cx,cy,r):
	for i in range(361):
		m=r*math.cos(i*3.14/180)+cx
		n=r*math.sin(i*3.14/180)+cy
		glBegin(GL_POINTS)
		
		glVertex2f(m,n)
		glEnd()
	glFlush()
	
def eclps(rx,ry,cx,cy):
	the=0
	redd=10
	for i in range(9):
		

		for i in range(361):
			m=rx*math.cos(i*3.14/180)+cx
			n=ry*math.sin(i*3.14/180)+cy
			glBegin(GL_POINTS)
	
			glVertex2f(m,n)
			glEnd()
		glFlush()
		circle(cx+rx*math.cos(the*3.14/180),cy+ry*math.sin(the*3.14/180),redd)
		rx=rx+40
		ry=ry+20		
		the=the+30
		redd=redd+2

def rotatecircle(aa):
	the=aa
	redd=10
	rx=30
	ry=20
	for i in range(9):
		circle(400+rx*math.cos(the*3.14/180),400+ry*math.sin(the*3.14/180),redd)
		rx=rx+40
		ry=ry+20		
		the=the+30
		redd=redd+2

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	eclps(30,20,400,400)
	circle(400,400,10)
	k=0
	while True:
		glColor3f(1.0,0.0,0.0)
		rotatecircle(k)
		time.sleep(1)
		glColor3f(0.0,0.0,0.0)
		rotatecircle(k)
		k=k+10
		
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(800,800)
	glutInitWindowPosition(10,10)
	glutCreateWindow("Solar System")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()
main()
