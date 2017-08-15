# -*- coding: utf-8 -*-
import pygame
import random
from sys import exit
# use sys.exit to closed

pygame.init()
# Initialize pygame
screen = pygame.display.set_mode((450, 800), 0, 32)
# Create 450 * 800 window
pygame.display.set_caption("Hit plane")
# Set title


class Plane:

    def restart(self):
        self.x = 200
        self.y = 600

    def __init__(self):
        self.restart()
        self.image = pygame.image.load('plane.png').convert_alpha()
        # load plane image

    def move(self):
        x, y = pygame.mouse.get_pos()
        # get x,y from plane top left corner
        x -= self.image.get_width() / 2
        y -= self.image.get_height() / 2
        self.x = x
        self.y = y
plane = Plane()


class Bullet:

    def __init__(self):
        self.x = 0
        self.y = -1
        # Initialize location of the bullet
        self.image = pygame.image.load('bullet.png').convert_alpha()
        # load bullet image
        self.active = False

    def move(self):
        if self.active:
            # move when active == True
            self.y -= 1
        if self.y < 0:
            self.active = False
        # if bullet's location out of windows,active = False

    def restart(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX-self.image.get_width()/2
        self.y = mouseY-self.image.get_height()/2
        self.active = True
        # active bullet


class Enemy:

    def __init__(self):
        self.restart()
        self.image = pygame.image.load('enemy.png').convert_alpha()

    def restart(self):
        self.x = random.randint(50, 400)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.1

    def move(self):
        if self.y < 800:
            self.y += self.speed
        else:
            self.restart()


def checkHit(enemy, bullet):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        enemy.restart()
        bullet.active = False
        return True
    return False


def checkCrash(enemy, plane):
    if (plane.x + 0.7*plane.image.get_width() > enemy.x) and (plane.x + 0.3*plane.image.get_width() < enemy.x + enemy.image.get_width()) and (plane.y + 0.7*plane.image.get_height() > enemy.y) and (plane.y + 0.3*plane.image.get_height() < enemy.y + enemy.image.get_height()):
        return True
    return False


pic = 'bg.jpg'
background = pygame.image.load(pic).convert()
# load image
boom = pygame.image.load('boom.png').convert_alpha()

bullets_list = []
# Create bullets_list
for i in range(10):
    bullets_list.append(Bullet())
# Add Bullet in bullets_list
count_b = len(bullets_list)
# Bullet Numbers
index_b = 0
# Shoot Bullet's ID
interval_b = 0
# Shoot interval
enemie_list = []
for i in range(5):
    enemie_list.append(Enemy())
gameover = False
score = 0
font = pygame.font.Font(None, 32)
while True:
    # Main
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit Game
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Change background on MouseClick
            if pic == 'bg2.jpg':
                pic = 'bg.jpg'
            else:
                pic = 'bg2.jpg'
            background = pygame.image.load(pic).convert()
    screen.blit(background, (0, 0))
    # draw background
    interval_b -= 1
    if interval_b < 0:
        bullets_list[index_b].restart()
        # Shoot bullet
        interval_b = 100
        index_b = (index_b+1) % count_b
    for b in bullets_list:
        if b.active:
            b.move()
            screen.blit(b.image, (b.x, b.y))
            # Move bullet
            for e in enemie_list:
                if checkHit(e, b):
                    score += 1
                    # Get score when the bullet hit the enemie
    for e in enemie_list:
        e.move()
        screen.blit(e.image, (e.x, e.y))
    if not gameover:
        for e in enemie_list:
            if checkCrash(e, plane):
                gameover = True
                # Gameover when the plane crash the enemie
            e.move()
            screen.blit(e.image, (e.x, e.y))

        text = font.render("Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(text, (0, 0))
        # Show socre
        plane.move()
        screen.blit(plane.image, (plane.x, plane.y))
        # Move plane
    else:
        interval_b = float("inf")
        text = font.render("Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(boom, (plane.x, plane.y))
        screen.blit(text, (190, 400))
    if gameover and event.type == pygame.MOUSEBUTTONUP:
        plane.restart()
        for e in enemie_list:
            e.restart()
        for b in bullets_list:
            b.active = False
        score = 0
        gameover = False
        interval_b = 0
        # Restart
    x, y = pygame.mouse.get_pos()
    # Get mouse coordinates
    pygame.display.set_caption("X:"+str(x)+","+"Y:" + str(y))
    pygame.display.update()
    # Redraw
