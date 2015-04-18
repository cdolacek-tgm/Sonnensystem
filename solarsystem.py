import interaction

__author__ = "Carina Dolacek"

from planet import *
from textur import *
from licht import *
from interaction import *

class Solarsystem(Planet, Textur):
    def __init__(self):
        """
        Initialisierung der Attribute und Objekte
        """
        self.sonne = None
        self.erde = None
        self.mond = None
        self.light = True

        self.bol = True
        self.stateT = True
        self.stateL = True
        self.geschw = True
        self.geschws = 0
        self.geschwp = 0
        self.geschwl = True
        self.stop = True

        Planet.__init__(self)
        Textur.__init__(self)
        Licht.__init__(self)
        #Interaction.__init__(self)

    def InitGL(self, Width, Height):
        """
        Einmalige Einstellungen der Anzeige

        :param Width: Breite des Fensters
        :param Height: Höhe des Fensters
        """
        self.sonne = Textur.LoadTextures(self, "Resources/textures/sun.gif")
        self.erde = Textur.LoadTextures(self, "Resources/textures/erde.jpg")
        self.mond = Textur.LoadTextures(self, "Resources/textures/mond.jpg")
        self.rosa = Textur.LoadTextures(self, "Resources/textures/rosa.jpg")

        glClearColor(0.0, 0.0,0.0, 0.0)

        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()
        gluPerspective(45, float(640) / float(480), 0.1, 100.0)
        gluLookAt(2, 0, 4, 0, 0, 0, 0, 1, 1)
        glMatrixMode(GL_MODELVIEW)

        Licht.light(self)

    def refresh(self):
        """
        Die Methode übernimmt die Mauseingabe für den Perspektivenwechsel

        :return:
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, float(640) / float(480), 0.1, 100.0)

        if self.bol is False:
            gluLookAt(0, 5, 1, 0, 0, 0, 0, 1, 0)

        elif self.bol is True:
             gluLookAt(0, 0, 4, 0, 0, 0, 0, 1, 0)

        glMatrixMode(GL_MODELVIEW)

        glLoadIdentity()

    def showPlanets(self):
        """
        Die Methode gibt alle Planeten aus und ruft die refresh Methode auf
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()  # reset position

        Solarsystem.refresh(self)

        glPushMatrix()

        if self.geschw is False:
            Planet.sonne(self, 0.2, 0.0, 0.0, 0.0, 0.01 + self.geschws, self.sonne)
            Planet.erde_mond(self, 0.1, 0.8, 0.0, 0.0, 0.03 + self.geschws, self.erde)
            Planet.erde_mond(self, 0.03, 1.0, 0.0, 0.0, 0.0 + self.geschws, self.mond)
            Planet.venus(self, 0.1, 1.5, 0.0, 0.5, 0.02 + self.geschws, self.rosa)

        elif self.geschwl is False:
            Planet.sonne(self, 0.2, 0.0, 0.0, 0.0, 0.01 - self.geschws, self.sonne)
            Planet.erde_mond(self, 0.1, 0.8, 0.0, 0.0, 0.03 - self.geschws, self.erde)
            Planet.erde_mond(self, 0.03, 1.0, 0.0, 0.0, 0.0 - self.geschws, self.mond)
            Planet.venus(self, 0.1, 1.5, 0, 0.5, 0.02 - self.geschws, self.rosa)

        elif self.stop is False:
            Planet.sonne(self, 0.2, 0.0, 0.0, 0.0, 0.0, self.sonne)
            Planet.erde_mond(self, 0.1, 0.8, 0.0, 0.0, 0.0, self.erde)
            Planet.erde_mond(self, 0.03, 1.0, 0.0, 0.0, 0.0, self.mond)
            Planet.venus(self, 0.1, 1.5, 0.0, 0.5, 0.0, self.rosa)

        elif self.stop is True:
            Planet.sonne(self, 0.2, 0.0, 0.0, 0.0, 0.01, self.sonne)
            Planet.erde_mond(self, 0.1, 0.8, 0.0, 0.0, 0.03, self.erde)
            Planet.erde_mond(self, 0.03, 1.0, 0.0, 0.0, 0.0, self.mond)
            Planet.venus(self, 0.1, 1.5, 0.0, 0.5, 0.02, self.rosa)

        glPopMatrix()
        glutSwapBuffers()

    def keyPressed(self, key, x, y):
        """
        Methode für die Tastatureneingabe

        :param key: Taste
        :param x:
        :param y:
        """

        #print ("Taste wurde gedrueckt: %c \n", key);

        #Kamera ändern
        if key == b'c':
            if self.bol is True:
                self.bol = False
            elif self.bol is False:
                self.bol = True
                self.stateC = True

        #Geschwindigkeit schneller
        if key == b'd':
           self.geschw = False
           self.geschws = self.geschws + 0.002

        #Geschwindigkeit langsamer
        if key == b'a':
           self.geschL = False
           self.geschws = self.geschws - 0.002

        #Animation stoppen
        if key == b's':
            if self.stop is True:
                self.stop = False
                self.geschw = True
                self.geschL = True

            elif self.stop is False:
                self.stop = True
                self.geschw = False
                self.geschL = False

        #Solarsystem schließen
        if key == b'q':
            glutDestroyWindow(glutGetWindow())

    def mouse(self, button, state, x, y):
        """
        Methode für die Mauseingabe

        :param button: Maustaste
        :param state: Status
        :param x: x-Koordinate
        :param y: y-Koordinate
        """

        #Licht einschalten
        if self.stateL is True:
            if (button == GLUT_LEFT_BUTTON):
                if state == GLUT_DOWN:
                    glEnable(GL_LIGHTING)

                    self.stateL = False

        #Licht ausschalten
        elif self.stateL is False:
            if (button == GLUT_LEFT_BUTTON):
                if state == GLUT_DOWN:
                    glDisable(GL_LIGHTING)

                    self.stateL = True

        #Textur einschalten
        if self.stateT is True:
            if (button == GLUT_RIGHT_BUTTON):
                if state == GLUT_DOWN:
                    glEnable(GL_TEXTURE_2D)

                    self.stateT = False

        #Textur ausschalten
        elif self.stateT is False:
            if (button == GLUT_RIGHT_BUTTON):
                if state == GLUT_DOWN:
                    glDisable(GL_TEXTURE_2D)

                    self.stateT = True

    def main(self):
        """
        Übergibt den Methoden alle Parameter zum Aufruf
        """
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(800, 600)

        window = glutCreateWindow(b'Solarsystem by OEZER & DOLACEK | Press q to quit the application')

        glutIdleFunc(self.showPlanets)
        glutKeyboardFunc(self.keyPressed)
        glutMouseFunc(self.mouse)

        self.InitGL(800, 600)
        glutMainLoop()