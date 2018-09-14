from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glutWireTeapot(0.5)
	#glutWireSphere(0.75,25,25)
	#glutWireCube(1.0)
	#glutSolidCube(1.0)
	glFlush()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(250,250)
glutInitWindowPosition(200,200)
glutCreateWindow("My first OGL program")
glutDisplayFunc(draw)
glutMainLoop()
