__author__ = 'Cafer Özer'

import pygame

from solarsystem import *

class Splashscreen():
    pygame.init()

    #Farben definieren
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (190, 190, 190)
    red = (255, 0, 0)
    green = (0, 155, 0)

    #Hintergrund definieren
    bg = pygame.image.load("Resources/bg/bg.jpg")
    controls = pygame.image.load("Resources/bg/controls.jpg")

    #Fenstergröße definieren
    display_width = 800
    display_height = 600

    solarDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Solarsystem by OEZER & DOLACEK")

    #icon = pygame.image.load("Resources/icon.png")
    #pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    smallfont = pygame.font.SysFont("cambria", 18)

    def text_objects(self, text, font, color):
        """
        Diese Methode rendert uns einen String, um es in einem PyGame-Element einbetten zu können

        :param text: Buttonnamen als String
        :param font: Schriftart
        :param color: Farbe
        """
        if type(text) is str:
            textSurface = font.render(text, True, color)
            return textSurface, textSurface.get_rect()
        else:
            pygame.display.quit()
            print ("Eingaben überprüfen")

    def button(self, text, x, y, w, h, inactive, active, action = None):
        """
        Diese Methode erstellt uns Menüpunkte im Splashscreen

        :param text: Buttonnamen als String
        :param x: x-Koordinate für das Rechteck
        :param y: y-Koordinate für das Rechteck
        :param w: Breite des Rechtecks
        :param h: Höhe des Rechtecks
        :param inactive: Farbe für inactive angeben
        :param active: Farbe für active angeben
        :param action: Aufruf einer Methode
        :return:
        """
        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()
        if type(text) is str and type(x) is int and type(y) is int and type(w) is int and type(h) is int:
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(self.solarDisplay, active, (x, y, w, h))
                if click[0] == 1 and action != None:
                    action()
            else:
                pygame.draw.rect(self.solarDisplay, inactive, (x, y, w, h))

            textSurf, textRect = self.text_objects(text, self.smallfont, self.black)
            textRect.center = ((x + (w / 2)), (y + (h / 2)))
            self.solarDisplay.blit(textSurf, textRect)
        else:
            pygame.display.quit()
            print("Eingaben überprüfen")


    def solar_splashscreen(self):
        """
        Solarsystem Splashscreen
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

            self.solarDisplay.blit(self.bg, [0, 0])

            self.button("Solar", 350, 240, 80, 30, self.gray, self.green, self.solar_system)
            self.button("Controls", 350, 310, 80, 30, self.gray, self.white, self.solar_controls)
            self.button("Quit", 350, 380, 80, 30, self.gray, self.red, quit)

            pygame.display.update()

    def solar_controls(self):
        """
        Erstellt eine Anzeige mit der Benutzersteuerung unseres Solarsystems
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.solarDisplay.blit(self.controls, [0, 0])

            self.button("Back to Menu", 350, 500, 110, 30, self.gray, self.white, self.solar_splashscreen)
            pygame.display.update()

    def solar_system(self):
        """
        Schließt als erstes das Menü-Fenster und ruft anschließend Solarsystem auf
        """
        pygame.display.quit()
        s = Solarsystem()
        s.main()

    def main(self):
        """
        Führt den Splashscreen aus
        """
        self.solar_splashscreen()