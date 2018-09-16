from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
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
	global p,m
	n=input("Enter no of control points: ")
	p=[[0 for x in range(2)] for y in range(n)]
	m=[0 for x in range(n)]
	for i in range(n):
		p[i][0]=input("Enter control point_x: ")
		p[i][1]=input("Enter control point_y: ")
		m[i]=input("Enter slope at control point: ")

def draw_cubic_spline():	
	while True:
		read_controlpoint()
		n=len(p)
		for i in range(n-1):
			hermite(p[i],p[i+1],m[i],m[i+1])
		print("Enter a decimal no other than 0 to continue")
		check=int(input("Enter 0 to exit: "))
		if check == 0:
			break
		else:
			pass

def hermite(p1,p2,m1,m2):
	u=0.0	
	while u <= 1.0:	
		H0_u=2*u*u*u -3*u*u +1
		H1_u=-2*u*u*u + 3*u*u
		H2_u=u*u*u -2*u*u + u
		H3_u=u*u*u - u*u
		x=H0_u*p1[0] + H1_u*p2[0] + H2_u*m1 + H3_u*m2 
		y=H0_u*p1[1] + H1_u*p2[1] + H2_u*m1 + H3_u*m2
		setPixel(x,y)		
		u+=0.001
		

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_cubic_spline()

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
