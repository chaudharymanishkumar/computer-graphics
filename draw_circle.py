# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 22:46:37 2018

@author: Ajay
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from drawDDA import setPixel
from drawDDA import myInit
import numpy
import math
sys.setrecursionlimit(4000)

def plotfunc(x,y):

	theta=0
	step=0.001

	glBegin(GL_POINTS)
	glVertex2f(0.0, 0.0)
	r=0.03
	glEnd()



	while theta<=2*math.pi:
		x += r*math.cos(theta)
		y += r*math.sin(theta)
		glBegin(GL_POINTS)
		glVertex2f(x,y)
		glEnd()
		glFlush()
		theta+=step


def circle_input():
	global x1,y1,x2,y2
	x1,y1= list(map(float,input("Enter the coordinates of the point to be boundary filled:").split()))
	x2,y2=list(map(float,input("Enter the coordinates of the circle to be flood filled:").split()))

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	print("Plotting circle")
	plotfunc(x1,y1)
	plotfunc(x2,y2)
	boundary_fill(xb,yb,[[[1.0,0.0,0.0]]],[[[0.0,1.0,0.0]]])
	flood_fill(xf,yf,[[[0.0,0.0,0.0]]])

def boundary_fill_input():

	global xb, yb
	xb,yb=list(map(float,input("Enter the boundary fill coordinates").split()))




def boundary_fill(x,y,fill_color,boundary_color):



	numpy_pixel=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT,None,float)
	string_pixels=numpy_pixel.tolist()



	glColor3f(1.0,0.0,0.0)
	if (string_pixels!= boundary_color) and (string_pixels!=fill_color):

		setPixel(x,y)
		boundary_fill(x+1,y,fill_color,boundary_color)
		boundary_fill(x,y+1,fill_color,boundary_color)
		boundary_fill(x-1,y,fill_color,boundary_color)
		boundary_fill(x,y-1,fill_color,boundary_color)

		return


def flood_input():
	global xf, yf
	xf,yf=list(map(float,input("Enter the flood fill coodinates").split()))


def flood_fill(x, y, interior_color):
	numpy_pixel = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT, None, float)
	target_color = numpy_pixel.tolist()
	glColor3f(1.0, 0.0, 0.0)
	if (target_color == interior_color):
		setPixel(x, y)
		flood_fill(x + 1, y, interior_color)
		flood_fill(x, y + 1, interior_color)
		flood_fill(x - 1, y, interior_color)
		flood_fill(x, y - 1, interior_color)


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(700,700)
	glutInitWindowPosition(50,50)
	glutCreateWindow("circle flood fill Algorithm")
	circle_input()
	boundary_fill_input()
	flood_input()
	glutDisplayFunc(Display)
	myInit()
	glutMainLoop()


main()