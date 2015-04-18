from unittest import TestCase
from licht import *

__author__ = 'Cafer Özer'


class TestLicht(TestCase):
    def test_light(self):
        """
        Überprüft ob das Objekt "Test" wirklich ein Objekt der Klasse Licht ist
        """
        test = Licht()
        self.assertIsInstance(test, Licht)