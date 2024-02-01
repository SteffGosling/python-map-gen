from PIL import Image
import numpy as np
import random
import config as cfg

w = cfg.width
h = cfg.height
buffer_percentage = cfg.buffer_percentage
node_bumper = [int(w/3), int(h/3)]
border = cfg.border_height
initial_nodes = cfg.initial_nodes
data = np.zeros((h, w, 3), dtype=np.uint8)
cycles = int(w*h/initial_nodes)
q,r = 0,0
data[:,:] = cfg.water_colour


def pick_direction(x, y):
    x += random.randint(-1,1)
    y += random.randint(-1,1)
    return x,y

# colour tile
def colour_tile(x, y, colour):
    data[x][y] = colour

# check if eligible to colour tile
def check_limits(x, y, limits):
    random_element = random.randint(0,limits[0])
    return False if x < w-(limits[0]-random_element) and x > (limits[0]-random_element) and y < h-(limits[1]-random_element) and y > (limits[1]-random_element) else True

def already_coloured(x, y, colour):
    return True if data[x][y] == colour else False

def next_tile(x, y, limits, reset_location):
    if check_limits(x, y, limits):
        return reset_location
    else:
        return pick_direction(x, y)


"""
while x < initial_nodes:
    initial_node_location = [random.randint(node_bumper[0],w-node_bumper[0]),random.randint(node_bumper[1],h-node_bumper[1])]
    rand_x ,rand_y = initial_node_location
    x,y = create_land_mass(rand_x, rand_y, cfg.land_colour,initial_node_location)
    for i in range(0, cycles):
        print(i) if i % 10000 == 0 else None
        img = Image.fromarray(data, 'RGB')
        img.save('my.png')
        img.show()
        x,y = create_land_mass(x, y, cfg.land_colour,initial_node_location)
"""     

while q < initial_nodes:
    initial_node_location = [random.randint(node_bumper[0],w-node_bumper[0]),random.randint(node_bumper[1],h-node_bumper[1])]
    rand_x = random.randint(node_bumper[0],w-node_bumper[0])
    rand_y = random.randint(node_bumper[1],h-node_bumper[1])
    data[rand_x,rand_y] = cfg.hill_colour
    x,y = rand_x,rand_y
    for i in range(0, cycles):
        data[x][y] = cfg.hill_colour
        x,y = next_tile(x, y, border, initial_node_location)
    img = Image.fromarray(data, 'RGB')
    img.save(f'map_{q}.png')
    img.show()
    q+=1
    
##create_land_mass(256, 256)

img = Image.fromarray(data, 'RGB')
img.save('map_final.png')
img.show()