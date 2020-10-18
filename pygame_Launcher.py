#TEAM MEMBER
'''

KOUADIO YAO INNOCENT JUNIOR
SANJEET MAISNAM


Contributions:

    the maze_solver.py code: Sanjeet
    pygame_Launcher.py and other PyGame related materials: Junior Yao
=======================================================================================
The code can be run in the terminal of appropriate directory by using the command:

python pygame_Launcher.py matrix.txt

where matrix.txt represents your input file.
=======================================================================================
'''

import pygame as pg
import GameSetting
import sys
import maze_solver
import numpy as np
import argparse

#Put your
parser = argparse.ArgumentParser(description = 'Enter the txt file matrix  ')
parser.add_argument('Matrix')
args = parser.parse_args()


def main(m):

    Global_collector = []
    #get the matrix dimension then , set the surface accordingly to avoid gap
    maze = GameSetting.Read_map(m)

    #generate the surface
    window = GameSetting.initializing_surface()
    frame = pg.time.Clock()

    #get path solution
    obj = maze_solver.Mazesolver(m)


    def get_dimension():
        return len(maze) , len(maze[0])


    #external setting
    block_number_height ,block_number_wide = get_dimension()
    blockwidth  = round(GameSetting.width/block_number_wide)
    blockheight = round(GameSetting.height/block_number_height)


    def refresh_screen () :
        global walkcount

        #fill the screen with the picture background
        #player.Charater_move_animation(window)

        pg.display.update()

    def get_color(x):
    #get the proper image
        if x == '1':
            return GameSetting.block
        elif x == '0' :
            return GameSetting.path
        elif x=='s':
            return GameSetting.player
        elif x=='e':
            return GameSetting.end
        elif x=='g':
            return GameSetting.rdoor
        elif x=='f':
            return GameSetting.rkey
        elif x=='c':
            return GameSetting.gdoor
        elif x=='d':
            return GameSetting.gkey
        elif x=='i':
            return GameSetting.bdoor
        elif x=='h':
            return GameSetting.bkey
        elif x=='b':
            return GameSetting.ydoor
        elif x=='a':
            return GameSetting.ykey
        else :
            return GameSetting.ghost


    def vertical_up (time , coor_i_j , textmap ):
        w = coor_i_j[0] -1
        for i in range(int(time)-1):
            if textmap[w][coor_i_j[1]] == '1'  :
                break
            else :
                Global_collector.append((w,coor_i_j[1]))
                window.blit(GameSetting.pink_cell,((coor_i_j[1]*blockwidth,w*blockheight )) )
                w-=1

    def horizontal_right (time , coor_i_j , textmap):
        w = coor_i_j[1] + 1
        for i in range(int(time)-1):
            if textmap[coor_i_j[0]][w] == '1'  :
                break
            else :
                Global_collector.append((coor_i_j[0] , w))
                window.blit(GameSetting.pink_cell,((w*blockwidth,coor_i_j[0]*blockheight )) )
                w+=1


    def vertical_down (time , coor_i_j , textmap):
        w = coor_i_j[0] + 1
        for i in range(int(time)-1):
            if textmap[w][coor_i_j[1]] == '1'  :
                break
            else :
                Global_collector.append ((w ,coor_i_j[1] ) )
                window.blit(GameSetting.pink_cell,((coor_i_j[1]*blockwidth,w*blockheight )) )
                w+=1

    def horizontal_left(time , coor_i_j , textmap):
        w = coor_i_j[1] - 1
        for i in range(int(time)-1):
            if textmap[coor_i_j[0]][w] == '1'  :
                break
            else :
                Global_collector.append( (coor_i_j[0] ,w ) )
                window.blit(GameSetting.pink_cell,((w*blockwidth,coor_i_j[0]*blockheight )) )
                w-=1
    def diagonal_up_right (time , coor_i_j , textmap):
        ii= coor_i_j[0] +1
        j = coor_i_j[1] -1
        w = coor_i_j[0] -1
        x = coor_i_j[1] +1
        for i in range(int(time)-1):
            if textmap[ii][j] == '1'  or ( textmap[w][coor_i_j[1]] == '1' and textmap[coor_i_j[0]][x] == '1'   ) :
                break
            else :
                Global_collector.append( (ii,j))
                window.blit(GameSetting.pink_cell,((j*blockwidth,ii*blockheight )) )
                ii+=1
                j-=1
                w-=1
                x+=1
    def diagonal_up_left (time , coor_i_j , textmap):
        ii = coor_i_j[0] -1
        j = coor_i_j[1]  -1
        w =  coor_i_j[0] -1
        x = coor_i_j[1] - 1
        for i in range(int(time)-1):
            if textmap[ii][j] == '1' or (  textmap[w][coor_i_j[1]] == '1'      and    textmap[coor_i_j[0]][x] == '1'   )  :
                break
            else :
                Global_collector.append( (ii,j))
                window.blit(GameSetting.pink_cell,((j*blockwidth,ii*blockheight )) )
                ii-=1
                j-=1
                w-=1
                x-=1
    def diagonal_down_right (time , coor_i_j , textmap):
        ii =coor_i_j[0] +1
        j = coor_i_j[1] +1
        w = coor_i_j[1] +1
        x = coor_i_j[0] +1
        for i in range(int(time)-1):
            if textmap[ii][j] == '1'  or  (textmap[coor_i_j[0]][w] == '1' and textmap[x][coor_i_j[1]] == '1')    :
                break
            else :
                Global_collector.append( (ii,j))
                window.blit(GameSetting.pink_cell,((j*blockwidth,ii*blockheight )) )
                ii+=1
                j+=1
                x+=1
                w+=1

    def diagonal_down_left (time , coor_i_j , textmap):
        ii= coor_i_j[0] -1
        j = coor_i_j[1] +1
        w = coor_i_j[1] -1
        x = coor_i_j[0] +1
        for i in range(int(time)-1):
            if textmap[ii][j] == '1' or ( textmap[coor_i_j[0]][w] == '1'  and  textmap[x][coor_i_j[1]] == '1' ) :
                break
            else :
                Global_collector.append( (ii,j))
                window.blit(GameSetting.pink_cell,((j*blockwidth,ii*blockheight )) )
                ii-=1
                j+=1
                x+=1
                w-=1

    def get_pink_cell(collection,textmap):
        for i in  collection.keys():

            #perform the 8 condictions

            vertical_up(i , collection[i] , textmap)
            vertical_down (i , collection[i] , textmap)
            horizontal_right(i , collection[i] , textmap)
            horizontal_left(i , collection[i] , textmap)

            diagonal_down_right(i , collection[i] , textmap)
            diagonal_up_left(i , collection[i] , textmap)
            diagonal_up_right(i , collection[i] , textmap)
            diagonal_down_left(i , collection[i] , textmap)


    def Print_map_cor(window , textmap):
        gost_collector  = {}

        #get the ghost position
        for i , row in enumerate(textmap ) :
            for j , title in enumerate(row):
                if textmap[i][j] == '2' :
                    gost_collector['2'] = (i,j)
                    pass
                elif  textmap[i][j] == '3' :
                    gost_collector['3'] = (i,j)
                    pass
                elif  textmap[i][j] == '4' :
                    gost_collector['4'] = (i,j)
                    pass
                k=get_color(textmap[i][j])
                window.blit(k,((j*blockwidth,i*blockheight )))

        #get pink cell, Gosh number id :  2,3,4
        get_pink_cell(gost_collector,textmap)

    #################################
    Print_map_cor(window,maze)

    count = 0
    backClean = 0
    a = 0
    b = 0
    # display the path
    print("The path is : ")
    print(obj.Path_tracer())
    w = obj.Path_tracer()
    while True:

        if count >= len(w):
            count = 0
        e = w[count]
        if backClean == 0 :
            backClean = 1
        elif ((b,a) == w[-1]) :
            Print_map_cor(window,maze)
            frame.tick(1)
        else :
            window.blit(get_color('0'),((a*blockwidth,b*blockheight )))

        for event in pg.event.get():
            if event.type == pg.QUIT :#close the game
                pg.quit()
                sys.exit()
        window.blit(get_color('s'),((e[1]*blockwidth,e[0]*blockheight )))

        #clear the screen
        a = e[1]
        b = e[0]
        count += 1
        refresh_screen ()
        frame.tick(5)

if __name__ == '__main__' :
    main(args.Matrix)
