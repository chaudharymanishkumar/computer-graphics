#Moving Car Annimation
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
def Round(n):
	return int(n+0.5)	
def setpix(xcor,ycor):
	glBegin(GL_POINTS)	
	glVertex2f(xcor,ycor)
	glEnd()
	glFlush()
def cir(t,tt):
	global r,cx,cy
	r=20
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
def cirb(m,mm):
	global r,cx,cy
	r=20
	cx=m
	cy=mm
	li(m,mm)
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
	r=20
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
	
	


def car(lt,lttt):
	
	glBegin(GL_LINES)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(lt+20*math.cos(180*3.14/180),60+20*math.sin(180*3.14/180))
	glVertex2f(lt+20*math.cos(180*3.14/180)-20,60)
	glVertex2f(lt+20*math.cos(180*3.14/180)-20,60)
	glVertex2f(lt+20*math.cos(180*3.14/180)-20,160)

	glVertex2f(lttt+20*math.cos(0*3.14/180),60+20*math.sin(0*3.14/180))
	glVertex2f(lttt+20*math.cos(0*3.14/180)+20,60)
	glVertex2f(lttt+20*math.cos(0*3.14/180)+20,60)
	glVertex2f(lttt+20*math.cos(0*3.14/180)+20,160)
	glVertex2f(lttt+20*math.cos(0*3.14/180)+20,160)
	glVertex2f(lt+20*math.cos(180*3.14/180)-20,160)
	glVertex2f(lt+20*math.cos(0*3.14/180),60+20*math.sin(0*3.14/180))
	glVertex2f(lttt+20*math.cos(180*3.14/180),60+20*math.sin(180*3.14/180))
	
	
	glEnd()
	glFlush()
def carr(lt,lttt):
	
	glBegin(GL_LINES)
	glColor3f(0.0,1.0,1.0)
	glVertex2f(lt+20*math.cos(180*3.14/180),60+20*math.sin(180*3.14/180))
	glVertex2f(lt+20*math.cos(180*3.14/180)-20,60)
	glVertex2f(lt+20*math.cos(180*3.14/180)-20,60)
	glVertex2f(lt+20*math.cos(180*3.14/180)-20,160)

	glVertex2f(lttt+20*math.cos(0*3.14/180),60+20*math.sin(0*3.14/180))
	glVertex2f(lttt+20*math.cos(0*3.14/180)+20,60)
	glVertex2f(lttt+20*math.cos(0*3.14/180)+20,60)
	glVertex2f(lttt+20*math.cos(0*3.14/180)+20,160)
	glVertex2f(lttt+20*math.cos(0*3.14/180)+20,160)
	glVertex2f(lt+20*math.cos(180*3.14/180)-20,160)
	glVertex2f(lt+20*math.cos(0*3.14/180),60+20*math.sin(0*3.14/180))
	glVertex2f(lttt+20*math.cos(180*3.14/180),60+20*math.sin(180*3.14/180))
	
	
	glEnd()
	glFlush()	

def keyboard(key, x, y):
	#  Allows us to quit by pressing 'Esc' or 'q'
	if key == chr(27):
		sys.exit()
	key= str(raw_input())
	if key == "q":
		sys.exit() 		
def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	i=0
	lt=50
	ltt=60
	lttt=200
	while True:
		
		car(lt,lttt)	
		cir(lt,ltt)
		cir(lttt,60)
		l(lt,ltt)
		l(lttt,60)
		lin(lt,ltt)
		lin(lttt,60)
		time.sleep(0.2)
		l(lt,ltt)
		l(lttt,60)
		cirr(lt,ltt)
		cirr(lttt,60)
		carr(lt,lttt)
		l(lt,ltt)
		l(lttt,60)
		#cirb(100,60)
		lt=lt+10
		lttt=lttt+10
	
		
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE| GLUT_RGB | GLUT_DEPTH )
	glutInitWindowSize(800,800)
	glutInitWindowPosition(10,10)
	glutCreateWindow("clock")
	
	glutDisplayFunc(Display)
	glutKeyboardFunc(keyboard)
	init()
	glutMainLoop()

main()
	
