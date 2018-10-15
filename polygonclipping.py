#@MKchaudhary 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)

def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def window_input():
	global x_min,y_min,x_max,y_max
	x_min=input("Enter lower x coordinate: ")
	y_min=input("Enter lower y coordinate: ")
	x_max=input("Enter higher x coordinate: ")
	y_max=input("Enter higher y coordinate: ")
def window_draw():
	lineBres(x_min,y_min,x_min,y_max)
	lineBres(x_min,y_max,x_max,y_max)
	lineBres(x_max,y_max,x_max,y_min)
	lineBres(x_max,y_min,x_min,y_min)

def polygon_input():
	global x_vertex,y_vertex
	x_vertex=[]
	y_vertex=[]
	n=input("Enter no of vertices: ")
	for i in range(n):
		x_vertex.append(input("Enter x_coordinate: "))
		y_vertex.append(input("Enter y_coordinate: "))
	

def SHC(x_vertex,y_vertex):
	global x_new,y_new,x_newr,y_newr,x_newb,y_newb,x_newt,y_newt
	x_new=[]
	y_new=[]
	x_newr=[]
	y_newr=[]
	x_newb=[]
	y_newb=[]
	x_newt=[]
	y_newt=[]
	n=len(x_vertex)
	for i in range(n-1):
		clipl(x_vertex[i],y_vertex[i],x_vertex[i+1],y_vertex[i+1]) 
	clipl(x_vertex[n-1],y_vertex[n-1],x_vertex[0],y_vertex[0]) 	
	#drawpolygon(x_new,y_new)
	
	n=len(x_new)
	for i in range(n-1):
		clipr(x_new[i],y_new[i],x_new[i+1],y_new[i+1]) 
	clipr(x_new[n-1],y_new[n-1],x_new[0],y_new[0]) 
	#drawpolygon(x_newr,y_newr)
	
	n=len(x_newr)
	for i in range(n-1):
		clipb(x_newr[i],y_newr[i],x_newr[i+1],y_newr[i+1]) 
	clipb(x_newr[n-1],y_newr[n-1],x_newr[0],y_newr[0]) 
	#drawpolygon(x_newb,y_newb)

	n=len(x_newb)
	for i in range(n-1):
		clipt(x_newb[i],y_newb[i],x_newb[i+1],y_newb[i+1]) 
	clipt(x_newb[n-1],y_newb[n-1],x_newb[0],y_newb[0]) 
	drawpolygon(x_newt,y_newt)
	
def clipl(x1,y1,x2,y2):
		
	if x2 - x1 !=0 :
		m=(y2 - y1)/(x2 - x1)
	else:
		m=4000
	if x1 >= x_min and x2 >= x_min:
		
		x_new.append(x2)
		y_new.append(y2)
		
	elif x1 < x_min and x2 >= x_min:
		
		x_new.append(x_min)
		y_new.append(y1+ m*(x_min - x1))
		x_new.append(x2)
		y_new.append(y2)

	elif x1 >= x_min and x2 < x_min :
		
		x_new.append(x_min)
		y_new.append(y1 + m*(x_min - x1))
	
def clipr(x1,y1,x2,y2):
	if x2 - x1 !=0 :
		m=(y2 - y1)/(x2 - x1)
	else:
		m=4000

	if x1 <= x_max and x2 <= x_max:
		
		x_newr.append(x2)
		y_newr.append(y2)
		
	elif x1 > x_max and x2 <= x_max:
		
		x_newr.append(x_max)
		y_newr.append(y1+ m*(x_max - x1))
		x_newr.append(x2)
		y_newr.append(y2)

		
	elif x1 <= x_max and x2 > x_max :
		x_newr.append(x_max)
		y_newr.append(y1 + m*(x_max - x1))
	

def clipt(x1,y1,x2,y2):
	if (y2-y1)!=0:
		m=(x2-x1)/(y2-y1)
	else:
		m=4000
	if y1 <= y_max and y2<= y_max:
		x_newt.append(x2)
		y_newt.append(y2)
	elif y1 > y_max and y2 <= y_max:
		x_newt.append(x1+m*(y_max-y1))
		y_newt.append(y_max)
		x_newt.append(x2)
		y_newt.append(y2)

	elif y1 <= y_max and y2 > y_max:
		x_newt.append(x1+m*(y_max -y1))
		y_newt.append(y_max)


def clipb(x1,y1,x2,y2):
	if (y2-y1)!=0:
		m=(x2-x1)/(y2-y1)
	else:
		m=4000
	if y1 >= y_min and y2>= y_min:
		x_newb.append(x2)
		y_newb.append(y2)
	elif y1 < y_min and y2 >= y_min:
		x_newb.append(x1+m*(y_min-y1))
		y_newb.append(y_min)
		x_newb.append(x2)
		y_newb.append(y2)

	elif y1 >= y_min and y2 < y_min:
		x_newb.append(x1+m*(y_min -y1))
		y_newb.append(y_min)

def drawpolygon(x_vertex,y_vertex):
	n=len(x_vertex)	
	for i in range(n-1):
		lineBres(x_vertex[i],y_vertex[i],x_vertex[i+1],y_vertex[i+1])
	lineBres(x_vertex[n-1],y_vertex[n-1],x_vertex[0],y_vertex[0])	

		
def lineBres(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	if delta_x !=0:
		m=delta_y/delta_x
	else:
		m=4000   			# a random value for undefined slope

	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)

	if dy >= dx:				# to set general values for both slope [0, )
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

	p=2*t1 - t2    			         # initial decision parameter

	if t0 > tEnd:				#to decide starting point
		x=xEnd
		y=yEnd
	else:
		x=x0
		y=y0

	setPixel(x,y)
	for k in range(steps):
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
def clipping():
	while(True):
		print("Enter details of window")
		window_input()
		window_draw()
		SHC(x_vertex,y_vertex)
		iterator=input("y for continue and n for exit")
		if iterator == 'y':
			pass
		else:
			break
		

def Display():
	glClear(GL_COLOR_BUFFER_BIT)	
	clipping()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("polygon clipping")
	polygon_input()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()

