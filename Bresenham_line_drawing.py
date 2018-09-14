
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
	

def readinput():
	global x0,y0,xEnd,yEnd
	x0=input('x0 coordinate:')
	y0=input('y0 coordinate:')
	xEnd=input('xEnd coordinate:')
	yEnd=input('yEnd coordinate:')
	
def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def lineBres(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	if delta_x !=0:
		m=delta_y/delta_x
	else:
		m=4000   			# a random value for undefined slope

	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)

	if dy >= dx:				# to set general values for both slope [0, )
		steps=dy
		t0=y0
		tEnd=yEnd
		t1=dx
		t2=dy
	else:
		steps=dx
		t0=x0
		tEnd=xEnd
		t1=dy
		t2=dx

	p=2*t1 - t2    			         # initial decision parameter

	if t0 > tEnd:				#to decide starting point
		x=xEnd
		y=yEnd
	else:
		x=x0
		y=y0

	setPixel(x,y)
	for k in range(steps):
		if dy >= dx:
			y=y+1
		else:
			x=x+1
		if p < 0 :
			p+=2*t1
		else:
			if dy >= dx:
				if m >= 0:
					x+=1
				if m < 0:
					x-=1
			else:
				if m >=0:
					y+=1
				if m < 0:
					y-=1
			p=p+2*t1-2*t2
		setPixel(x,y)			

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	lineBres(x0,y0,xEnd,yEnd)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("DDA Line Algorithm")
	readinput()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
