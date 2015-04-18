__author__ = 'Carina Dolacek'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Licht(object):
    def light(self):
        """
        Setzt das Licht für die Planeten
        :return:
        """
        zeros = (0.2, 0.2, 0.2, 1)
        ones = (1.0, 1.0, 1.0, 1)
        half = (0.5, 0.5, 0.5, 1)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)

        glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
        glLightfv(GL_LIGHT0, GL_SPECULAR, half)

        glLightfv(GL_LIGHT0, GL_POSITION, (0, 0.3, 1, 1))	# Position The Light
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)

        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)