#Moving Man
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import math
import sys

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glPointSize(2)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,800.0,0.0,800.0)

def setpix(xcor,ycor):
	glBegin(GL_POINTS)
	
	glVertex2f(xcor,ycor)
	glEnd()
	glFlush()
def head(t,tt):
	global r,cx,cy
	r=20
	cx=t
	cy=tt
	for i in range(361):
		
		m=int(r*math.cos(i*3.14/180.0))+cx
		n=int(r*math.sin(i*3.14/180.0))+cy
		glBegin(GL_POINTS)
	
		glVertex2f(m,n)
		glEnd()
	glFlush()

	
def hand1():
	glBegin(GL_LINES)
	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-20)
	glVertex2f(cx+r*math.cos(270*3.14/180)+20,cy+r*math.sin(270*3.14/180)-30) #right straight

	glVertex2f(cx+r*math.cos(270*3.14/180)+20,cy+r*math.sin(270*3.14/180)-30)
	glVertex2f(cx+r*math.cos(270*3.14/180)+5,cy+r*math.sin(270*3.14/180)-40) #right bend

	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-20)
	glVertex2f(cx+r*math.cos(270*3.14/180)-20,cy+r*math.sin(270*3.14/180)-30) #left straight

	glVertex2f(cx+r*math.cos(270*3.14/180)-20,cy+r*math.sin(270*3.14/180)-30)
	glVertex2f(cx+r*math.cos(270*3.14/180)-5,cy+r*math.sin(270*3.14/180)-40) #left bend
	glEnd()
	glFlush()

def hand2():
	glBegin(GL_LINES)
	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-20)
	glVertex2f(cx+r*math.cos(270*3.14/180)+10,cy+r*math.sin(270*3.14/180)-50) #right straight

	glVertex2f(cx+r*math.cos(270*3.14/180)+10,cy+r*math.sin(270*3.14/180)-50)
	glVertex2f(cx+r*math.cos(270*3.14/180)+5,cy+r*math.sin(270*3.14/180)-70) #right bend

	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-20)
	glVertex2f(cx+r*math.cos(270*3.14/180)-10,cy+r*math.sin(270*3.14/180)-50) #right straight

	glVertex2f(cx+r*math.cos(270*3.14/180)-10,cy+r*math.sin(270*3.14/180)-50)
	glVertex2f(cx+r*math.cos(270*3.14/180)-5,cy+r*math.sin(270*3.14/180)-70) #left bend
	glEnd()
	glFlush()
def leg1():
	glBegin(GL_LINES)
	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-80)
	glVertex2f(cx+r*math.cos(270*3.14/180)+30,cy+r*math.sin(270*3.14/180)-100) #right leg

	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-80)
	glVertex2f(cx+r*math.cos(270*3.14/180)-30,cy+r*math.sin(270*3.14/180)-100)
	glEnd()
	glFlush()
def leg2():
	glBegin(GL_LINES)
	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-80)
	glVertex2f(cx+r*math.cos(270*3.14/180)+15,cy+r*math.sin(270*3.14/180)-100)

	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-80)
	glVertex2f(cx+r*math.cos(270*3.14/180)-15,cy+r*math.sin(270*3.14/180)-100)
	glEnd()
	glFlush()
		
def body(t,tt):
	cx=t
	cy=tt
	glBegin(GL_LINES)
	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180))
	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180)-80) #body		
	glEnd()
	glFlush()
		
def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	varcenx=100
	varceny=200
	while True:
		glColor3f(1.0,0.0,0.0)
		head(varcenx,varceny)
		body(varcenx,varceny)
		hand1()
		leg1()
		time.sleep(0.5)
		glColor3f(0.0,1.0,1.0)
		hand1()
		leg1()
		glColor3f(1.0,0.0,0.0)
		hand2()
		leg2()
		time.sleep(0.5)
		glColor3f(0.0,1.0,1.0)
		hand2()
		leg2()
		head(varcenx,varceny)
		body(varcenx,varceny)
		varcenx=varcenx+10
			
		
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE| GLUT_RGB | GLUT_DEPTH )
	glutInitWindowSize(800,800)
	glutInitWindowPosition(10,10)
	glutCreateWindow("Moving Man")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
	
