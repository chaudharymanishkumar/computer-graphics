#Mkchaudhary 17sept 2018
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from time import *
import sys

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-10.0,10.0,-10.0,10.0)
		
def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2f(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def read_controlpoint():
	global p
	n=input("Enter no of control points: ")
	p=[[0 for x in range(2)] for y in range(n)]
	for i in range(n):
		p[i][0]=input("Enter control point_x: ")
		p[i][1]=input("Enter control point_y: ")

def factorial(n):
	if n==0:
		return 1
	else:
		n=n*factorial(n-1) 
	return n

def Binomial_coefficient(n,k):
	result=float(factorial(n)/(factorial(n-k)*factorial(k)))
	return result

def Bezier():
	n=len(p)
	u=0.0
	while u <= 1.0:	
		x=0.0
		y=0.0
		for k in range(n-1):
			blend=Binomial_coefficient(n,k)*pow(u,k)*pow(1-u,n-k)
			x+=blend*p[k][0]
			y+=blend*p[k][1]						
		setPixel(x,y)		
		u+=0.0001
		
def draw_Bezier_curve():
	while True:
		read_controlpoint()
		Bezier()
		print("Enter any decimal to continue")
		check=int(input("Enter 0 to exit: "))
		if check==0:
			sleep(5)
			sys.exit()
		else:
			pass
def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_Bezier_curve()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Cubic spline")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
