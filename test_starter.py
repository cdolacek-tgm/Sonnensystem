from unittest import TestCase
from starter import *

__author__ = 'Cafer Özer'

class TestStarter(TestCase):
    def test_main(self):
        """
        Überprüft ob das Objekt "Test" wirklich ein Objekt der Klasse Starter ist
        """
        test = Starter()
        self.assertRaises(Exception)