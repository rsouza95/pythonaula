#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

