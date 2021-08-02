'''
faça um programa em python que abra e reproduza um audio de um mp3.

'''
import pygame
pygame.init()
pygame.mixer.music.load("desafio021.mp3")
pygame.mixer.music.play("desafio021.mp3")
pygame.event.wait()


