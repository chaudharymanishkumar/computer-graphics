from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from gen_dda_import import lineDDA

def ROUND(a):
	return int(a+0.5)

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)

def readinputs():
	global x1,y1,x2,y2
	x1=input('x1 coordinate:')
	y1=input('y1 coordinate:')
	x2=input('x2 coordinate:')
	y2=input('y2 coordinate:')
	
def Display1():
	glClear(GL_COLOR_BUFFER_BIT)
	lineDDA(x1,y1,x2,y1)
	lineDDA(x2,y1,x2,y2)
	lineDDA(x1,y1,x1,y2)
	lineDDA(x1,y2,x2,y2)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Rectangle")
	readinputs()
	glutDisplayFunc(Display1)
	init()
	glutMainLoop()	

main()
