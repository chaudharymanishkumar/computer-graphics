

'''A triangle PQR has its vertices located at P(80,50), Q(60,10),R(100,10). It is desired toobtain its reflection about an axis parallel to Y axis and passing through poit A(30,10). Write
program do this transformation'''
#@ Mk chaudhary

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

matrix=[[0 for x in range(1)] for y in range(3)]
composite_matrix=[[0 for x in range(3)]for y in range(3)]

def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-window_x/2,window_x/2,-window_y/2,window_y/2)
	
def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def readinput_polygon():
	global vertex_x,vertex_y
	n=input("Enter no of vertices: ")
	vertex_x=[0 for x in range(n)]
	vertex_y=[0 for x in range(n)]
	for i in range(n):
		vertex_x[i]=input("Enter x_coordinate: ")
		vertex_y[i]=input("Enter y_coordinate: ")

def draw_axis():
	glColor3f(0.0,0.0,0.0)
	lineBres(30,-window_y,30,window_y)
	glColor3f(0.0,1.0,1.0)
	lineBres(-window_x,0,window_x,0)
	lineBres(0,-window_y,0,window_y)

def lineBres(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	if delta_x !=0:
		m=delta_y/delta_x
	else:
		m=4000   			

	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)

	if dy >= dx:				
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

	p=2*t1 - t2    			         

	if t0 > tEnd:				
		x=xEnd
		y=yEnd
	else:
		x=x0
		y=y0

	setPixel(x,y)
	for k in range(int(steps)):
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

def matrix_set_identity(m):
	for i in range(3):
		for j in range(3):
			if i==j:
				m[i][j]=1

def matrix_multiply(matrix_a,matrix_b):
	temp_matrix=[[0 for x in range(len(matrix_b[0]))] for y in range(len(matrix_a))]
	for i in range(len(matrix_a)):
		for j in range(len(matrix_b[0])):
			for k in range(len(matrix_a)):
				temp_matrix[i][j]+=matrix_a[i][k]*matrix_b[k][j]

	for i in range(len(matrix_b)):
		for j in range(len(matrix_b[0])):
			matrix_b[i][j]=temp_matrix[i][j]

def translate(tx,ty):
	m=[[0 for x in range(3)] for y in range(3)]
	matrix_set_identity(m)
	m[0][2]=tx
	m[1][2]=ty
	matrix_multiply(m,composite_matrix)

def reflection():
	m1=[[0 for x in range(3)] for y in range(3)]
	matrix_set_identity(m1)
	m1[0][0]=-1
	matrix_multiply(m1,composite_matrix)

def drawpolygon(vertex_x,vertex_y):
	glColor3f(1.0,0.0,0.0)
	n= len(vertex_x)
	for i in range(n-1):
		lineBres(vertex_x[i],vertex_y[i],vertex_x[i+1],vertex_y[i+1])
	lineBres(vertex_x[n-1],vertex_y[n-1],vertex_x[0],vertex_y[0])
	
def transformation():
	matrix_set_identity(composite_matrix)
	
	drawpolygon(vertex_x,vertex_y)
	translate(-30,0)
	reflection()
	translate(30,0)
	
	for i in range(len(vertex_x)):
		matrix[0][0]=vertex_x[i]
		matrix[1][0]=vertex_y[i]
		matrix[2][0]=1
		matrix_multiply(composite_matrix,matrix)		
		vertex_x[i]=matrix[0][0]
		vertex_y[i]=matrix[1][0]
	drawpolygon(vertex_x,vertex_y)

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_axis()
	transformation()
def main():
	global window_x,window_y
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE |GLUT_RGB)
	window_x=int(input("Enter window_x: "))
	window_y=int(input("Enter window_y: "))
	glutInitWindowPosition(50,50)
	glutInitWindowSize(window_x,window_y)
	glutCreateWindow("Reflection")
	readinput_polygon()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
