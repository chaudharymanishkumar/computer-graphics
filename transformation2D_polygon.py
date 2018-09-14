''' 13 sept 2018 @M.k.chaudhary'''
#Basic 2D transformation for polygon by using homogenous coordinate representation.
#Concatenated transformation for different order and parameter.
#Translation ,rotation with respect to pivot point ,scaling with respect to pivot point for polygon
#DDA line drawing algorithm has been used to draw line.

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from gen_dda_import import *			#lineDDA() function has been imported through this file
import sys
from math import * 
matrix=[[0 for x in range(1)] for y in range(3)]    # 3*1 matrix to store homogenious point (x,y)
composite_matrix=[[0 for x in range(3)] for y in range(3)]  # 3*3 composite matrix
def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)

def readinput_polygon():
	global vertex_x,vertex_y
	n=input("Enter no of vertices: ")
	vertex_x=[0 for x in range(n)]
	vertex_y=[0 for x in range(n)]
	for i in range(n):
		vertex_x[i]=input("Enter x_coordinate: ")
		vertex_y[i]=input("Enter y_coordinate: ")

def drawpolygon(vertex_x,vertex_y):
	n=len(vertex_x)
	for i in range(n-1):
		lineDDA(vertex_x[i],vertex_y[i],vertex_x[i+1],vertex_y[i+1])
	lineDDA(vertex_x[n-1],vertex_y[n-1],vertex_x[0],vertex_y[0])

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

def scale(sx,sy,refpoint_x,refpoint_y):
	tx=refpoint_x - 0
	ty=refpoint_y - 0
	translate(-tx,-ty)
	m=[[0 for x in range(3)] for y in range(3)]
	matrix_set_identity(m)
	m[0][0]=sx
	m[1][1]=sy
	matrix_multiply(m,composite_matrix)
	translate(tx,ty)

def rotate(theta,refpoint_x,refpoint_y):
	tx=refpoint_x - 0
	ty=refpoint_y - 0
	translate(-tx,-ty)
	m=[[0 for x in range(3)] for y in range(3)]
	matrix_set_identity(m)
	m[0][0]=cos(theta)
	m[0][1]=-sin(theta)
	m[1][0]=sin(theta)
	m[1][1]=cos(theta)
	matrix_multiply(m,composite_matrix)
	translate(tx,ty)

def transformation_polygon():
	matrix_set_identity(composite_matrix)
	while(True):
		print("1.Translation \n2.scaling with respect to pivot point \n3.rotation with respect to pivot point \n4.To show final image")
		choose_transformation=input("Select transformation: ")
		if choose_transformation==1:
			tx=input("Enter tx: ")
			ty=input("Enter ty: ")
			translate(tx,ty)
		elif choose_transformation==2:
			sx=input("Enter sx: ")
			sy=input("Enter sy: ")
			refpoint_x=input("Enter reference point_x: ")
			refpoint_y=input("Enter reference point_y: ")
			scale(sx,sy,refpoint_x,refpoint_y)
		elif choose_transformation==3:
			print("1.Anticlockwise rotation \n2.clockwise rotation")
			direction=input("Select direction")
			theta=input("Enter theta: ")
			refpoint_x=input("Enter reference point_x: ")
			refpoint_y=input("Enter reference point_y: ")
			if direction==1:
				rotate(theta,refpoint_x,refpoint_y)
			elif direction==2:
				rotate(-theta,refpoint_x,refpoint_y)
		elif choose_transformation==4:
			break
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
	drawpolygon(vertex_x,vertex_y)
	transformation_polygon()
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("2D Transformation")
	readinput_polygon()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()
main()
