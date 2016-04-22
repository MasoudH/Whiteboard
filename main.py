# Copyright of Masoud Harati 2015
# White Board for jotting down ideas

from pygame import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from math import hypot

root = Tk()
root.withdraw()

screen = display.set_mode((1000, 750))
screen.fill((255, 255, 255))
display.set_caption("White Board")
display.set_icon(image.load("whiteboard.png"))

radius = 1
mx, my = 0, 0

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False 
        if e.type == MOUSEBUTTONDOWN: 
        	if e.button == 4: # Increases the radius of the drawing utensil
        		radius += 1
        	if e.button == 5 and radius > 1: # Decreases the radius of the drawing utensil
        		radius -= 1
        if e.type == KEYDOWN:
            running = False

    keyboard = key.get_pressed()
    ox, oy = mx, my
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    if keyboard[K_LCTRL] and keyboard[K_o]:
        fileName = askopenfilename(parent=root,title="Open Image:") # gets which directory it needs to open the image froma
        screen.blit(image.load(fileName), (0, 0))

    if keyboard[K_LCTRL] and keyboard[K_s]:
    	copy = screen.copy()
    	name = asksaveasfilename(parent=root,title="Save the image as...") # gets file name to save image
    	image.save(copy, name + ".jpg")

    if mb[0] == 1: # pencil
        if mx == ox and my == oy: #Checks if mouse was stable
            draw.circle(screen, (0, 0, 0), (ox,oy), radius//2) #draws a circle at the mouses position
        else:
            dx = mx-ox #distance between mx and ox
            dy = my-oy #distance between my andoy
            dist = hypot(dx, dy) # distance between old mouse pos and new mouse pos
            x = dx/dist
            y = dy/dist
            for i in range(int(dist)):
                draw.circle(screen, (0, 0, 0), (int(ox+i*x), int(oy+i*y)), radius//2) # drawing the circle at every pixel

    if mb[2] == 1: # Eraser
        if mx == ox and my == oy: #Checks if mouse was stable
            draw.circle(screen, (255, 255, 255), (ox,oy), radius//2) #draws a circle at the mouses position
        else:
            dx = mx-ox #distance between mx and ox
            dy = my-oy #distance between my andoy
            dist = hypot(dx, dy) # distance between old mouse pos and new mouse pos
            x = dx/dist
            y = dy/dist
            for i in range(int(dist)):
                draw.circle(screen, (255, 255, 255), (int(ox+i*x), int(oy+i*y)), radius//2) # drawing the circle at every pixel

    display.flip()
quit()
