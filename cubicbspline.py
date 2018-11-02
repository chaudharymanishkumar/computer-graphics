from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from time import *

k=3
t=[0 for i in range(20)]
def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glPointSize(2.0)
	glColor3f(1.0,0.0,0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,20.0,0.0,20.0)

def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def read_controlpoint():
	global px,py,no_controlpoint
	no_controlpoint=input("Enter no of control point: ")
	px=[0 for x in range(no_controlpoint)]
	py=[0 for y in range(no_controlpoint)]
	for i in range(no_controlpoint):
		px[i]=input("Enter control_x: ")
		py[i]=input("Enter control_y: ")
		#setPixel(px[i],py[i])

def cal_knot_value():
	n=no_controlpoint -1
	for i in range(n+k+1):
		if i<k:
			t[i]=0
		elif k<=i<=n:
			t[i]=i-k+1
		elif i>n:
			t[i]=n-k+2

def Bspline(i,k,u):
	result=0
	if k==1:
		if u>=t[i] and u<=t[i+1]:
			return 1
		else:
			return 0
	if (t[i+k-1] -t[i]) !=0:
		result+=float((u-t[i])*Bspline(i,k-1,u)/(t[i+k-1]-t[i]))
	if (t[i+k] - t[i+1])!=0:
		result+=float((t[i+k]-u)*Bspline(i+1,k-1,u)/(t[i+k]-t[i+1]))
	return result 

def bspline():
	cal_knot_value()
	n=no_controlpoint -1
	u=0.0
	while u<=n-k+2:
		x=0.0
		y=0.0
		for i in range(no_controlpoint):
			x+=Bspline(i,k,u)*px[i]
			y+=Bspline(i,k,u)*py[i]
		setPixel(x,y)
		u+=0.0005
	
def draw_Bspline_curve():
	while True:
		read_controlpoint()
		bspline()
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
	#read_controlpoint()
	glutCreateWindow("Bspline")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
