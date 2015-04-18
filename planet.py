__author__ = 'Carina Dolacek, Cafer Özer'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

class Planet(object):
    def __init__(self):
        """
        Der Konstruktor initialisiert die Attribute für das Rotieren der Planeten
        """
        self.yplanet = 0.0
        self.yplanet1 = 0.0
        self.rot = 0.0

    def sonne(self, radius, x, y, z, angle, txt):
        """
        Methode für den Zentralstern

        :param radius:  Radius des Planetens
        :param x: x-Koordinate
        :param y: y-Koordinate
        :param z: z-Koordinate
        :param txt: Textur
        """
        if type(radius) is float and type(x) is float and type(y) is float and type(z) is float and type(angle) is float:
            glLoadIdentity()

            glTranslatef(x, y, z)

            self.rot = self.rot + angle
            glRotate(self.rot, 0, 1, 0)

            glBindTexture(GL_TEXTURE_2D, txt)

            quadratic = gluNewQuadric()
            gluQuadricNormals(quadratic, GLU_SMOOTH)
            gluQuadricTexture(quadratic, GL_TRUE)

            gluSphere(quadratic, radius, 32, 32)
        else:
            print("Eingaben überprüfen")

    def erde_mond(self, radius, x, y, z, angle, txt):
        """
        Methode für den Planeten mit Mond

        :param radius:  Radius des Planetens
        :param x: x-Koordinate
        :param y: y-Koordinate
        :param z: z-Koordinate
        :param angle: Geschwindigkeit
        :param txt: Textur
        """
        if type(radius) is float and type(x) is float and type(y) is float and type(z) is float and type(angle) is float:
            glLoadIdentity()

            self.yplanet1 = self.yplanet1 + angle
            glRotate(self.yplanet1, 0, 1, 0)

            glTranslate(x,y,z)
            glBindTexture(GL_TEXTURE_2D, txt)

            quadratic = gluNewQuadric()
            gluQuadricNormals(quadratic, GLU_SMOOTH)
            gluQuadricTexture(quadratic, GL_TRUE)

            gluSphere(quadratic, radius, 32, 32)
        else:
            print("Eingaben überprüfen")

    def venus(self, radius, x, y, z, angle1, txt):
        """
        Methode für den Planeten Venus

        :param radius:  Radius des Planetens
        :param x: x-Koordinate
        :param y: y-Koordinate
        :param z: z-Koordinate
        :param angle: Geschwindigkeit
        :param txt: Textur
        """
        if type(radius) is float and type(x) is float and type(y) is float and type(z) is float and type(angle1) is float:
            glLoadIdentity()

            self.yplanet = self.yplanet + angle1
            glRotate(self.yplanet, 0, 1, 0)

            glTranslate(x, y, z)
            glBindTexture(GL_TEXTURE_2D, txt)

            quadratic = gluNewQuadric()
            gluQuadricNormals(quadratic, GLU_SMOOTH)
            gluQuadricTexture(quadratic, GL_TRUE)

            gluSphere(quadratic, radius, 32, 32)  #Planet mit der Textur
        else:
            print("Eingaben überprüfen")