from PIL import Image
import numpy as np
import random

w, h = 1024, 1024
buffer_percentage = 25
node_bumper = [int(w / buffer_percentage), int(h / buffer_percentage)]
data = np.zeros((h, w, 3), dtype=np.uint8)
x,y = 0,0
initial_nodes = 3
land_colour = [141,253,135]
hill_colour = [123,255,159]
cycles = int(w*h*initial_nodes)
data[:,:] = [153, 255, 255]


def create_land_mass(x, y, colour):
    if x < 0 or x > w-1 or y < 0 or y > h-1:
        return False
    data[x][y] = colour
    choose = random.randint(1,5)
    if choose == 1:
        create_land_mass(x+1, y,colour)
    elif choose == 2:
        create_land_mass(x-1, y,colour)
    elif choose == 3:
        create_land_mass(x, y+1,colour)
    elif choose == 4:
        create_land_mass(x, y-1,colour)
    else:
        return False
    
while x < initial_nodes:
    rand_x = random.randint(node_bumper[0],w-node_bumper[0])
    rand_y = random.randint(node_bumper[1],h-node_bumper[1])
    data[rand_x,rand_y] = land_colour
    
    for i in range(0, cycles):
        rand_x += random.randint(-1,1)
        rand_y += random.randint(-1,1)
        if create_land_mass(rand_x, rand_y,land_colour):
            i=cycles
    x+=1

while y < initial_nodes:
    rand_x = random.randint(node_bumper[0],w-node_bumper[0])
    rand_y = random.randint(node_bumper[1],h-node_bumper[1])
    data[rand_x,rand_y] = hill_colour
    
    for i in range(0, cycles):
        rand_x += random.randint(-1,1)
        rand_y += random.randint(-1,1)
        if create_land_mass(rand_x, rand_y, hill_colour):
            i=cycles
    y+=1
    
##create_land_mass(256, 256)

img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()