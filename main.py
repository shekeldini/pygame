import pygame
from classes.game.game import Game


if __name__ == "__main__":
    pygame.font.init()
    game = Game()
    game.play()

