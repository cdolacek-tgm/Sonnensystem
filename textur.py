__author__ = 'Carina Dolacek'

from PIL.Image import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Textur(object):
    def LoadTextures(self, pic):
        """
        Texturen werden aufgerufen und für das Objekt vorbereitet

        :param pic: Der Name der gewünschten Textur

        :return:  Die Textur für das Objekt
        """
        if type(pic) is str:
            try:
                image = open(pic)   #Sonnentextzur öffnen

                ix_s = image.size[0]
                iy_s = image.size[1]

                image = image.convert("RGBA").tostring("raw", "RGBA")
                texture = glGenTextures(1)
                glBindTexture(GL_TEXTURE_2D,texture)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
                gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix_s, iy_s, GL_RGBA, GL_UNSIGNED_BYTE, image)

                glEnable(GL_TEXTURE_2D)

                return texture
            except:
                raise("Konnte Textur nicht laden")
        else:
            print("Eingabe überprüfen")