from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from gen_dda_import import *    # for importing lineDDA and ROUND function from gen_dda_import.py pgm

INSIDE = 0 	#0000
LEFT = 1   	#0001
RIGHT = 2  	#0010
BOTTOM = 4 	#0100
TOP = 8    	#1000
def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)

def read_window_input():                        # to taking dimension of rectangular clipping window
	global x_min,y_min,x_max,y_max
	x_min = input("Enter x_min coordinate")
	y_min = input("Enter y_min coordinate")
	x_max = input("Enter  x_max coordinate")
	y_max = input("Enter y_max coordinate")


def multi_line_clip():
	while True:
		x1 = input("Enter 1st x-coordinate")
		y1 = input("Enter 1st y-coordinate")
		x2 = input("Enter 2nd x-coordinate")
		y2 = input("Enter 2nd y-coordinate")
		cohensoutherlandclip(x1,y1,x2,y2)
		print("Enter a decimal no other than 0 to continue")
		check=int(input("Enter 0 to exit: "))
		if check == 0:
			break
		else:
			pass

def lineclipping():
	glClear(GL_COLOR_BUFFER_BIT)
		
	lineDDA(x_min,y_min,x_max,y_min)
	lineDDA(x_max,y_min,x_max,y_max)
	lineDDA(x_min,y_min,x_min,y_max)
	lineDDA(x_min,y_max,x_max,y_max)	
	multi_line_clip()
	

def computecode(x,y):               # to compute region code
	code = INSIDE
	if x < x_min:      
        	code =code | LEFT
	elif x > x_max:    
        	code=code | RIGHT
	if y < y_min:    
	        code =code | BOTTOM
	elif y > y_max:    
		code =code | TOP

	return code
 	
def cohensoutherlandclip(x1,y1,x2,y2):
	code1=computecode(x1,y1)
	code2=computecode(x2,y2)
	accept = False

	while True:
		if code1==0 and code2 == 0:
			accept = True
			break
		elif (code1 & code2) != 0:
			break
		else:
			x=0.0
			y=0.0
			dx=x2-x1
			dy=y2-y1
			if dx != 0:       # for handling divide by 0
				m=dy/dx
					
			if code1 != 0:
				code_out = code1
			else:
				code_out = code2

			if code_out & TOP:
				y = y_max
				if dx == 0:         # when slope of line is infinity or undefined
					x=x1
				else:
					x = x1 + (y_max - y1)/m
			elif code_out & BOTTOM:
				y = y_min
				if dx == 0:	   # when slope of line is infinity or undefined
					x=x1
				else:
					x= x1 + (y_min -y1)/m
			elif code_out & RIGHT:
				x = x_max
				y = y1 + m*(x_max - x1)
			elif code_out & LEFT:
				x = x_min
				y = y1 + m*(x_min - x1)

			if code_out == code1:
				x1=x
				y1=y
				code1=computecode(x1,y1)
			else:
				x2=x
				y2=y
				code2=computecode(x2,y2)
	if accept:
		lineDDA(ROUND(x1),ROUND(y1),ROUND(x2),ROUND(y2))
	else:
		print("Line is rejected")
						
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Plot Points")
	read_window_input()
	glutDisplayFunc(lineclipping)
	init()
	glutMainLoop()

main()
