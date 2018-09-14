from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
	
def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(xcoordinate,ycoordinate)
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

