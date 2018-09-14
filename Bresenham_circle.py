#@MKchaudhary 15th sept 2018
#Bresenham's circle drawing python opengl program

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)

def readinput_circle():
	global xcenter,ycenter,radius
	xcenter=input('xCenter:')
	ycenter=input('yCenter:')
	radius=input('Radius:')

def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2f(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def Brescircle(xcenter,ycenter,radius):
	x=0
	y=radius
	p=3-2*radius
	circlePlotpoints(xcenter,ycenter,x,y)
	while x <= y:
		x+=1
		if p<0:
			p=p+4*x+6
		else:
			y-=1
			p= p+ 4*(x-y) + 10
		circlePlotpoints(xcenter,ycenter,x,y)

def circlePlotpoints(xcenter,ycenter,x,y):
	setPixel(xcenter + x , ycenter + y)
	setPixel(xcenter + x , ycenter - y)
	setPixel(xcenter - x , ycenter + y)
	setPixel(xcenter - x , ycenter - y)
	setPixel(xcenter + y , ycenter + x)
	setPixel(xcenter + y , ycenter - x)
	setPixel(xcenter - y , ycenter + x)
	setPixel(xcenter - y , ycenter - x)

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	Brescircle(xcenter,ycenter,radius)	

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("2D Transformation")
	readinput_circle()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
