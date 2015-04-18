from unittest import TestCase
from textur import *

__author__ = 'Cafer Özer'

class TestTextur(TestCase):
    def test_LoadTextures(self):
        """
        Überprüft, ob der Pfad einer Textur richtig angegeben wird
        """
        test = Textur()
        glutInit(sys.argv)

        window = glutCreateWindow(b'Testing')

        pfad = "Resources/textures/rosa.jpg"
        #Parameters like this: LoadTextures("Resources/textures/sun.gif")
        self.assertRaises(Exception, test.LoadTextures(5))
        self.assertRaises(Exception, test.LoadTextures(pfad))