from unittest import TestCase
from splashscreen import *

__author__ = 'Cafer Özer'

class TestSplashscreen(TestCase):
    def test_text_objects(self):
        """
        Überprüft die Eingaben --> Datentypen
        """
        test = Splashscreen()
        black = (0, 0, 0)
        smallfont = pygame.font.SysFont("cambria", 18)
        #Parameters like this: self.text_objects(text, self.smallfont, self.black)
        self.assertRaises(Exception, test.text_objects(5, smallfont, black))

    def test_button(self):
        """
        Überprüft die Eingaben --> Datentypen
        """
        test = Splashscreen()
        black = (0, 0, 0)
        white = (255, 255, 255)
        #Parameters like this: self.button("Back to Menu", 350, 500, 110, 30, self.gray, self.white, self.solar_splashscreen)
        self.assertRaises(Exception, test.button(4, 520, "hallowelt", 50, 20, black, white, None))

    def test_solar_splashscreen(self):
        """
        Überprüft ob das Objekt "Test" wirklich ein Objekt der Klasse Splashscreen ist
        """
        test = Splashscreen()
        self.assertRaises(Exception)

    def test_solar_controls(self):
        """
        Überprüft ob das Objekt "Test" wirklich ein Objekt der Klasse Splashscreen ist
        """
        test = Splashscreen()
        self.assertIsInstance(test, Splashscreen)

    def test_solar_system(self):
        """
        Überprüft ob das Objekt "Test" wirklich ein Objekt der Klasse Splashscreen ist
        """
        test = Splashscreen()
        self.assertIsInstance(test, Splashscreen)

    def test_main(self):
        """
        Überprüft ob das Objekt "Test" wirklich ein Objekt der Klasse Splashscreen ist
        """
        test = Splashscreen()
        self.assertIsInstance(test, Splashscreen)