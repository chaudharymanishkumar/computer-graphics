from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import math
import sys

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glPointSize(4)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,800.0,0.0,800.0)

def setpix(xcor,ycor):
	glBegin(GL_POINTS)
	glVertex2f(xcor,ycor)
	glEnd()
	glFlush()
def cir(t,tt):
	global r,cx,cy
	r=50
	cx=t
	cy=tt
	li(t,tt)
	for i in range(361):
		glColor3f(1.0,0.0,0.0)
		m=int(r*math.cos(i*3.14/180.0))+cx
		n=int(r*math.sin(i*3.14/180.0))+cy
		glBegin(GL_POINTS)
		glVertex2f(m,n)
		glEnd()
	glFlush()
def cirr(t,tt):
	global r,cx,cy
	r=50
	cx=t
	cy=tt
	li(t,tt)
	for i in range(361):
		glColor3f(0.0,1.0,1.0)
		m=int(r*math.cos(i*3.14/180.0))+cx
		n=int(r*math.sin(i*3.14/180.0))+cy
		glBegin(GL_POINTS)
		glVertex2f(m,n)	
		glEnd()
	glFlush()
	
def li(t,tt):
	cx=t
	cy=tt
	glPointSize(4)
	glBegin(GL_LINES)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(45*3.14/180),cy+r*math.sin(45*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(135*3.14/180),cy+r*math.sin(135*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(225*3.14/180),cy+r*math.sin(225*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(315*3.14/180),cy+r*math.sin(315*3.14/180))
	glEnd()
	glFlush()
def lin(t,tt):
	cx=t
	cy=tt
	glBegin(GL_LINES)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(0*3.14/180),cy+r*math.sin(0*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(90*3.14/180),cy+r*math.sin(90*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(180*3.14/180),cy+r*math.sin(180*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180))
	glEnd()
	glFlush()
def l(t,tt):
	cx=t
	cy=tt
	glBegin(GL_LINES)
	glColor3f(0.0,1.0,1.0)
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(0*3.14/180),cy+r*math.sin(0*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(90*3.14/180),cy+r*math.sin(90*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(180*3.14/180),cy+r*math.sin(180*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(270*3.14/180),cy+r*math.sin(270*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(45*3.14/180),cy+r*math.sin(45*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(135*3.14/180),cy+r*math.sin(135*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(225*3.14/180),cy+r*math.sin(225*3.14/180))
	glVertex2f(cx,cy)
	glVertex2f(cx+r*math.cos(315*3.14/180),cy+r*math.sin(315*3.14/180))
	
	glEnd()
	glFlush()
	
	
def circlea():
	li()
	for i in range(361):
		if(i>=0 and i<=45):
			glColor3f(1.0,0.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		elif(i>=90 and i<=120):
			glColor3f(1.0,0.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		elif(i>=180 and i<=240):
			glColor3f(1.0,0.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		elif(i>=300 and i<=330):
			glColor3f(1.0,0.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		else:
			glColor3f(0.0,1.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)

def circleb():
	lin()
	for i in range(361):
		if(i>=0 and i<=45):
			glColor3f(0.0,1.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		elif(i>=90 and i<=120):
			glColor3f(0.0,1.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		elif(i>=180 and i<=240):
			glColor3f(0.0,1.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		elif(i>=300 and i<=330):
			glColor3f(0.0,1.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		else:
			glColor3f(1.0,0.0,0.0)
			m=int(200*math.cos(i*3.14/180.0))+400
			n=int(200*math.sin(i*3.14/180.0))+400
			setpix(m,n)
		
def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	i=0
	lt=400
	ltt=400
	while True:	
		#circlea()
		cir(lt,ltt)
		l(lt,ltt)
		lin(lt,ltt)
		time.sleep(0.2)
		l(lt,ltt)
		cirr(lt,ltt)
		l(lt,ltt)
		lt=lt+10
		
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE| GLUT_RGB | GLUT_DEPTH )
	glutInitWindowSize(800,800)
	glutInitWindowPosition(10,10)
	glutCreateWindow("Wheel")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
	
