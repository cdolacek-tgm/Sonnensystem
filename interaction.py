__author__ = 'Cafer Özer'

from OpenGL.GLUT.special import glutKeyboardFunc
from PIL.Image import *
from PIL.OleFileIO import key
from planet import *
from textur import *
from licht import *
import string

class Interaction(object):
    def __init__(self):
        """
        Konstruktor der Klasse Interaction
        """

        self.bol = True
        self.stateT = True
        self.stateL = True
        self.geschw = True
        self.geschws = 0
        self.geschwp = 0
        self.geschwl = True
        self.stop = True

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
                self.bol= True
                self.stateC=True

        #Geschwindigkeit schneller
        if key == b'd':
           self.geschw = False
           self.geschws = self.geschws + 0.005
           self.geschwp = self.geschwp + 0.0005

        #geschwindigkeit langsamer
        if key == b'a':
           self.geschL = False
           self.geschws = self.geschws - 0.005
           self.geschwp = self.geschwp - 0.0005

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

    def mouse(self, button, state, x, y):
        """
        Methode für die Mauseingabe

        :param button: Maustaste
        :param state: Status
        :param x:
        :param y:
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