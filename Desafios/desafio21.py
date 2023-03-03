#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

#Correção

import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
pygame.event.wait()
