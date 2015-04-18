from unittest import TestCase
from planet import *
from textur import *

__author__ = 'Cafer Özer'

class TestPlanet(TestCase):
    def test_sonne(self):
        """
        Überprüft die Eingaben --> Datentypen
        """
        test = Planet()
        glutInit(sys.argv)

        window = glutCreateWindow(b'Testing')
        sonne = Textur.LoadTextures(self, "Resources/textures/sun.gif")
        #Parameters like this: Planet.sonne(self, 0.2, 0.0, 0.0, 0.0, 0.01 + self.geschws, self.sonne)
        self.assertRaises(Exception, test.sonne("falsche Eingabe", 1.0, 2.0, 3.0, 5.0, sonne))

    def test_erde_mond(self):
        """
        Überprüft die Eingaben --> Datentypen
        """
        test = Planet()
        glutInit(sys.argv)

        window = glutCreateWindow(b'Testing')
        erde = Textur.LoadTextures(self, "Resources/textures/erde.jpg")
        #Parameters like this: Planet.erde_mond(self, 0.1, 0.8, 0.0, 0.0, 0.03 + self.geschws, self.erde)
        self.assertRaises(Exception, test.erde_mond(0.1, 1.0, 2.0, 3.0, 5.0, erde)) #Fehler ausgeben

    def test_venus(self):
        """
        Überprüft die Eingaben --> Datentypen
        """
        test = Planet()
        glutInit(sys.argv)

        window = glutCreateWindow(b'Testing')
        venus = Textur.LoadTextures(self, "Resources/textures/rosa.jpg")
        #Parameters like this: Planet.venus(self, 0.1, 1.5, 0.0, 0.5, 0.02 + self.geschws, self.rosa)
        self.assertRaises(Exception, test.venus(2.0, 1.0, 2.0, 3.0, 5.0, venus))