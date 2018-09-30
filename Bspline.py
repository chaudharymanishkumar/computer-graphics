'''30 sept 2018 @Mkchaudhary'''
#Nonuniform Bspline curve using python opengl
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from time import *
import sys
t=[0 for i in range(20)]

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glPointSize(3.0)
	gluOrtho2D(0,599,0,599)
		
def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2f(xcoordinate,ycoordinate)
	glEnd()
	glFlush()


def read_controlpoint():
	global px,py,no_controlpoint,k
	no_controlpoint=input("Enter no of control points: ")
	k=input("Enter order of curve: ")
	px=[0 for x in range(no_controlpoint)]
	py=[0 for y in range(no_controlpoint)]
	for i in range(no_controlpoint):
		px[i]=input("Enter control point_x: ")
		py[i]=input("Enter control point_y: ")
		setPixel(px[i],py[i])

def calc_knot_value():				#to calculate knot vectors
	n=no_controlpoint-1
	for i in range(n+k+1):
		if i<k:
			t[i]=0
		elif k<=i<=n:
			t[i]=i-k+1
		elif i>n:
			t[i]=n-k+2

def bsplinefun(i,k,u):
	result=0
	if k==1:
		if t[i]<=u and u<=t[i+1]:
			return 1
		else:
			return 0
	if (t[i+k-1] - t[i])!=0:
		result+=float(((u-t[i])*bsplinefun(i,k-1,u))/(t[i+k-1]-t[i]))
	if (t[i+k] - t[i+1])!=0:
		result+=float(((t[i+k]-u)*bsplinefun(i+1,k-1,u))/(t[i+k]-t[i+1]))
	return result

def Bspline():
	n=no_controlpoint-1
	calc_knot_value()
	u=0.0
	while u<=n-k+2:
		x=0.0
		y=0.0
		for i in range(no_controlpoint):
			x+=bsplinefun(i,k,u)*px[i]
			y+=bsplinefun(i,k,u)*py[i]
		setPixel(x,y)
		u+=0.0005

def draw_Bspline_curve():
	while True:
		read_controlpoint()
		Bspline()
		print("Enter any decimal to continue")
		check=int(input("Enter 0 to exit: "))
		if check==0:
			sleep(5)
			sys.exit()
		else:
			pass
def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_Bspline_curve()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Bspline curve")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
