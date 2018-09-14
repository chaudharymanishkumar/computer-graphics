#Midpoint Algorithm to draw ellipse.
#Ellipse is symmetrical about  quadrants.
#We need to consider about 1st quadrant of ellipse.All other three pixel we can get from corresponding pixel in 1st quadrant
#@Mkchaudhary 14th Sept 2018
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def ROUND(a):
	return int(a+0.5)

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-640.0,640.0,-480.0,480.0)
	
def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2f(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def readinput():
	global xcenter,ycenter,rx,ry
	xcenter=input('xCenter:')
	ycenter=input('yCenter:')
	rx=input('Radius_x:')
	ry=input('Radius_y:')
	
def ellipseMidpoint(xcenter,ycenter,rx,ry):
	x=0
	y=ry
	px=0
	py=2*y*rx*rx
	p=ROUND(ry*ry- (rx*rx*ry) + (0.25*rx*rx))
	while px < py:
		x+=1
		px+=2*ry*ry
		if p < 0:
			p +=ry*ry+px
		else:
			y-=1
			py -= 2*rx*rx
			p+=ry*ry+px-py
		ellipsePlotpoint(xcenter,ycenter,x,y)

	p= ROUND(ry*ry*(x+0.5)*(x+0.5)+rx*rx*(y-1)*(y-1) - rx*rx*ry*ry)
	while y > 0:
		y=y-1
		py-=2*rx*rx
		if p>0:
			p +=rx*rx - py
		else:
			x=x+1
			px+=2*ry*ry
			p+=rx*rx+px-py
		ellipsePlotpoint(xcenter,ycenter,x,y)
	
def ellipsePlotpoint(xcenter,ycenter,x,y):
	setPixel(xcenter + x , ycenter + y)
	setPixel(xcenter + x , ycenter - y)
	setPixel(xcenter - x , ycenter + y)
	setPixel(xcenter - x , ycenter - y)
	

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	ellipseMidpoint(xcenter,ycenter,rx,ry)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Midpoint Ellipse Algorithm")
	readinput()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
