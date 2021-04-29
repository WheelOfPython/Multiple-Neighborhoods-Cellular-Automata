import numpy as np
import pygame as pg
import copy
np.random.seed(0)

neighborhood_pattern_1 = [[0,0,1,1,1,0,0],
                          [0,1,0,0,0,1,0],
                          [1,0,1,1,1,0,1],
                          [1,0,1,0,1,0,1],
                          [1,0,1,1,1,0,1],
                          [0,1,0,0,0,1,0],
                          [0,0,1,1,1,0,0]]

neighborhood_pattern_2 = [[0,0,0,0,0,1,1,1,0,0,0,0,0],
                          [0,0,0,1,1,1,1,1,1,1,0,0,0],
                          [0,0,1,1,1,1,1,1,1,1,1,0,0],
                          [0,1,1,1,1,0,0,0,1,1,1,1,0],
                          [0,1,1,1,0,0,0,0,0,1,1,1,0],
                          [1,1,1,0,0,0,0,0,0,0,1,1,1],
                          [1,1,1,0,0,0,0,0,0,0,1,1,1],
                          [1,1,1,0,0,0,0,0,0,0,1,1,1],
                          [0,1,1,1,0,0,0,0,0,1,1,1,0],
                          [0,1,1,1,1,0,0,0,1,1,1,1,0],
                          [0,0,1,1,1,1,1,1,1,1,1,0,0],
                          [0,0,0,1,1,1,1,1,1,1,0,0,0],
                          [0,0,0,0,0,1,1,1,0,0,0,0,0]]

neighborhood_pattern_3 = [
[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
[0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0],
[0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0],
[1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1],
[0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0],
[0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0],
[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
[0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]]



size = width, height = (30, 30)
coordinates = [(x,y) for x in range(width) for y in range(height)]

Pixels = {} # {(0,0):np.random.randint(100), ...}
for cell in coordinates:
    Pixels[cell] = np.random.random()

def Sum_(pixel, neighborhood_pattern, Pixels):
    hei, wid = len(neighborhood_pattern), len(neighborhood_pattern[0])
    hei_hlf, wid_hlf = int(hei/2), int(wid/2)
    suma = 0
    pixel_x = pixel[0]
    pixel_y = pixel[1]
    for x in range(-wid_hlf, wid_hlf+1):
        for y in range(-hei_hlf, hei_hlf+1):
            if pixel_x + x >= 0 and pixel_y + y >= 0 and pixel_x + x < width and pixel_y + y < height:
                neigthbor = (pixel_x + x, pixel_y + y)
                mana = Pixels[neigthbor]
                weight = neighborhood_pattern[hei_hlf+y][wid_hlf+x]
                suma += mana * weight
    return suma


pg.init()
screen = pg.display.set_mode([width, height])

n=0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255, 255, 255))
    
    Pixels2 = copy.deepcopy(Pixels)

    for pixel in coordinates:
        suma1 = Sum_(pixel, neighborhood_pattern_1, Pixels2)
        suma2 = Sum_(pixel, neighborhood_pattern_2, Pixels2)
        suma3 = Sum_(pixel, neighborhood_pattern_3, Pixels2)
        if suma1 > 13 or suma1 < 5:
             Pixels2[pixel] -= 0.03
        elif suma2 > 9 and suma2 < 21:
             Pixels2[pixel] -= 0.04
        if suma3 > 78 and suma3 < 89:
            Pixels2[pixel] -= 0.05
        elif suma3 > 108:
            Pixels2[pixel] = 0.1
        else:
            Pixels2[pixel] = np.random.random()

    Pixels = Pixels2

    for pixel in coordinates:
        P = Pixels[pixel]
        if P > 0:
            P = int(P*100000)
            pg.draw.circle(screen, (int(abs(P%255-0.33*P%255)),0,P%255), (pixel[0], pixel[1]), 1)
        else:
            pg.draw.circle(screen, (255,255,255), (pixel[0], pixel[1]), 1)
    
    
    # fname = "circle_blue"+str(n)+".png"
    # pg.image.save(screen, fname)
    # print("file {} has been saved".format(fname))

    pg.display.flip()
    n += 1

pg.quit()