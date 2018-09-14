''' 
Midpoint circle drawing algorithm with given center and radius.
Circle is symmetrical about its octant.so we need to consider about only one octant.from each pixel in that octant we can get all
other corresponding seven pixels.'''
#@MKchaudhary 27Aug 2018 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)
def readinput():
	global xcenter,ycenter,radius
	xcenter=input('xCenter:')
	ycenter=input('yCenter:')
	radius=input('Radius:')
	
def circleMidpoint(xcenter,ycenter,radius):
	x=0
	y=radius
	p=1 - radius
	circlePlotpoints(xcenter,ycenter,x,y)
	while x < y:
		x+=1
		if p<0:
			p=p+2*x+1
		else:
			y-=1
			p= p+ 2*(x-y) + 1
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
	circleMidpoint(xcenter,ycenter,radius)
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Midpoint circle Algorithm")
	readinput()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
