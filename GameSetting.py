import pygame as pg 

height = 1
width  = 1

def resolution():
    global height,width
    return width , height

#read map 

def Read_map (maptext):
    global height , width 
    
    with open (maptext,'r') as file :
        matrice_map = file.readlines()
    matrice_map =  [ row.strip() for row in matrice_map] 
    maze = [i.split(' ') for i in matrice_map]
 
    height , width = 53*len(maze) , 53*len(maze[0])
    
    return maze

    
#initializing surface 

def initializing_surface():
    pg.init()
#set the dimention for the display setting up resolution 
    l , p = resolution()
#create a surface
    window =  pg.display.set_mode((l,p))
#set a caption 
    pg.display.set_caption("Challenge game ")
    return window



#colors 

Red= (178,34,34)


# background image 
player = pg.image.load('run/pacman.png')
block=pg.image.load('run/block.png')
path=pg.image.load('run/path.png')
end=pg.image.load('run/reward.png')
rdoor = pg.image.load('run/red_door.png')
rkey=pg.image.load('run/red_key.png')
bdoor=pg.image.load('run/blue_door.png')
bkey=pg.image.load('run/blue_key.png')
gdoor=pg.image.load('run/green_door.png')
gkey=pg.image.load('run/green_key.png')
ydoor=pg.image.load('run/yellow_door.png')
ykey=pg.image.load('run/yellow_key.png')
ghost=pg.image.load('run/ghost.png')
pink_cell = pg.image.load('run/pink_cell.png')


