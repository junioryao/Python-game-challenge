Global_collector = []

def vertical_up(time, coor_i_j, textmap):
    w = coor_i_j[0] - 1
    for i in range(int(time) - 1):
        if textmap[w][coor_i_j[1]] == '1':
            break
        else:
            #print(w, coor_i_j[1])
            Global_collector.append((w, coor_i_j[1]))
            w -= 1


def horizontal_right(time, coor_i_j, textmap):
    w = coor_i_j[1] + 1
    for i in range(int(time) - 1):
        if textmap[coor_i_j[0]][w] == '1':
            break
        else:
            #print(coor_i_j[0], w)
            Global_collector.append((coor_i_j[0], w))
            w += 1


def vertical_down(time, coor_i_j, textmap):
    w = coor_i_j[0] + 1
    for i in range(int(time) - 1):
        if textmap[w][coor_i_j[1]] == '1':
            break
        else:
            #print(w, coor_i_j[1])
            Global_collector.append((w, coor_i_j[1]))
            w += 1


def horizontal_left(time, coor_i_j, textmap):
    w = coor_i_j[1] - 1
    for i in range(int(time) - 1):
        if textmap[coor_i_j[0]][w] == '1':
            break
        else:
            #print(coor_i_j[0], w)
            Global_collector.append((coor_i_j[0], w))
            w -= 1


def diagonal_up_right(time, coor_i_j, textmap):
    ii = coor_i_j[0] + 1
    j = coor_i_j[1] - 1
    w = coor_i_j[0] - 1
    x = coor_i_j[1] + 1
    for i in range(int(time) - 1):
        if textmap[ii][j] == '1' or (textmap[w][coor_i_j[1]] == '1' and textmap[coor_i_j[0]][x] == '1'):
            break
        else:
            #print(ii, j)
            Global_collector.append((ii, j))
            ii += 1
            j -= 1
            w -= 1
            x += 1


def diagonal_up_left(time, coor_i_j, textmap):
    ii = coor_i_j[0] - 1
    j = coor_i_j[1] - 1
    w = coor_i_j[0] - 1
    x = coor_i_j[1] - 1
    for i in range(int(time) - 1):
        if textmap[ii][j] == '1' or (textmap[w][coor_i_j[1]] == '1' and textmap[coor_i_j[0]][x] == '1'):
            break
        else:
            #print(ii, j)
            Global_collector.append((ii, j))
            ii -= 1
            j -= 1
            w -= 1
            x -= 1


def diagonal_down_right(time, coor_i_j, textmap):
    ii = coor_i_j[0] + 1
    j = coor_i_j[1] + 1
    w = coor_i_j[1] + 1
    x = coor_i_j[0] + 1
    for i in range(int(time) - 1):
        if textmap[ii][j] == '1' or (textmap[coor_i_j[0]][w] == '1' and textmap[x][coor_i_j[1]] == '1'):
            break
        else:
            #print(ii, j)
            Global_collector.append((ii, j))
            ii += 1
            j += 1
            x += 1
            w += 1


def diagonal_down_left(time, coor_i_j, textmap):
    ii = coor_i_j[0] - 1
    j = coor_i_j[1] + 1
    w = coor_i_j[1] - 1
    x = coor_i_j[0] + 1
    for i in range(int(time) - 1):
        if textmap[ii][j] == '1' or (textmap[coor_i_j[0]][w] == '1' and textmap[x][coor_i_j[1]] == '1'):
            break
        else:
            #print(ii, j)
            Global_collector.append((ii, j))
            #window.blit(GameSetting.pink_cell, ((j * blockwidth, ii * blockheight)))
            ii -= 1
            j += 1
            x += 1
            w -= 1


def get_pink_cell(collection, textmap):
    for i in collection.keys():
        # perform the 8 condictions

        vertical_up(i, collection[i], textmap)
        vertical_down(i, collection[i], textmap)
        horizontal_right(i, collection[i], textmap)
        horizontal_left(i, collection[i], textmap)

        diagonal_down_right(i, collection[i], textmap)
        diagonal_up_left(i, collection[i], textmap)
        diagonal_up_right(i, collection[i], textmap)
        diagonal_down_left(i, collection[i], textmap)

    return Global_collector
