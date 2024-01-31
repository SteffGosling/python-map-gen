from PIL import Image
import numpy as np
import random
import config as cfg

w = cfg.width
h = cfg.height
buffer_percentage = cfg.buffer_percentage
node_bumper = [int(w / buffer_percentage), int(h / buffer_percentage)]
initial_nodes = cfg.initial_nodes
data = np.zeros((h, w, 3), dtype=np.uint8)
cycles = int(w*h*initial_nodes)
x,y = 0,0
data[:,:] = cfg.water_colour


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
    initial_node_location = [random.randint(node_bumper[0],w-node_bumper[0]),random.randint(node_bumper[1],h-node_bumper[1])]
    rand_x ,rand_y = initial_node_location
    data[rand_x,rand_y] = cfg.land_colour
    
    for i in range(0, cycles):
        rand_x += random.randint(-1,1)
        rand_y += random.randint(-1,1)
        create_land_mass(rand_x, rand_y, cfg.land_colour)
    x+=1

while y < initial_nodes:
    rand_x = random.randint(node_bumper[0],w-node_bumper[0])
    rand_y = random.randint(node_bumper[1],h-node_bumper[1])
    data[rand_x,rand_y] = cfg.hill_colour
    
    for i in range(0, cycles):
        rand_x += random.randint(-1,1)
        rand_y += random.randint(-1,1)
        if create_land_mass(rand_x, rand_y, cfg.hill_colour):
            i=cycles
    y+=1
    
##create_land_mass(256, 256)

img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()