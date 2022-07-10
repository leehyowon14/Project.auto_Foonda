'''
. = blank
o = disk
x = block
/, \ = reflector
R,L,r,l= one-way reflector(up-Right, up-Left, down-Right, down-Left)
- = gap
_ = hole
F = Foonda
G = goal
'''


def make_map():
    size = int(input("Enter the size of the map: "))
    map, coords_map = [], {}
    for i in range(size):
        map.append([input("Enter the map (line "+str(i+1)+"): ")])

    for i in range(len(map)):
        for x in range(len(map[i])):
            if map[i][x] == '.':
                coords_map[i,x] = 'blank'
            elif map[i][x] == 'o':
                coords_map[i,x] = 'disk'
            elif map[i][x] == 'x':
                coords_map[i,x] = 'block'
            elif map[i][x] == '\\':
                coords_map[i,x] = 'reflector_up_right'
            elif map[i][x] == '/':
                coords_map[i,x] = 'reflector_up_left'
            elif map[i][x] == 'R':
                coords_map[i,x] = 'one-way_reflector_up_right'
            elif map[i][x] == 'L':
                coords_map[i,x] = 'one-way_reflector_up_left'
            elif map[i][x] == 'r':
                coords_map[i,x] = 'one-way_reflector_down_right'
            elif map[i][x] == 'l':
                coords_map[i,x] = 'one-way_reflector_down_left'
            elif map[i][x] == '-':
                coords_map[i,x] = 'gap'
            elif map[i][x] == '_':
                coords_map[i,x] = 'hole'
            elif map[i][x] == 'F':
                coords_map[i,x] = 'Foonda'
                Foonda_location = [i,x]
            elif map[i][x] == 'G':
                coords_map[i,x] = 'goal'
    
    return map, coords_map, Foonda_location

def print_map(map):
    print("Map:")
    for i in range(len(map)):
        for x in range(len(map[i])):
            if x != len(map[i])-1:
                print(map[i][x], end="")
            else:
                print(map[i][x], end="\n")
    print('\n')


def update_map(coords_map): #coords_map to map
    map = []
    for i in range(len(coords_map)):
        map.append([])
        for x in range(len(coords_map[i])):
            if coords_map[i,x] == 'blank':
                temp = '.'
            elif coords_map[i,x] == 'disk':
                temp = 'o'
            elif coords_map[i,x] == 'block':
                temp = 'x'
            elif coords_map[i,x] == 'reflector_up_right':
                temp = '\\'
            elif coords_map[i,x] == 'reflector_up_left':
                temp = '/'
            elif coords_map[i,x] == 'one-way_reflector_up_right':
                temp = 'R'
            elif coords_map[i,x] == 'one-way_reflector_up_left':
                temp = 'L'
            elif coords_map[i,x] == 'one-way_reflector_down_right':
                temp = 'r'
            elif coords_map[i,x] == 'one-way_reflector_down_left':
                temp = 'l'
            elif coords_map[i,x] == 'gap':
                temp = '-'
            elif coords_map[i,x] == 'hole':
                temp = '_'
            elif coords_map[i,x] == 'Foonda':
                temp = 'F'
            elif coords_map[i,x] == 'goal':
                temp = 'G'

            map[i].append(temp)
    return map


puzzle_map, coords_map, Foonda_location = make_map()



'''
map v2 coords example(2x2):
    0,0 | 1,0
    0,1 | 1,1
'''

def move_Foonda(direction, coords_map):
    global Foonda_location # Foonda_location = [x,y]
    if direction == 'up':
        while True:
            if Foonda_location[1] > 0:
                if coords_map[Foonda_location[0], Foonda_location[1] -1] == 'blank':
                    Foonda_location[1] -= 1
                elif coords_map[Foonda_location[0], Foonda_location[1] -1] == 'disk':
                    # if coords_map[Foonda_location[0], Foonda_location[1] -2] == 'disk': #디스크 두개 겹친 경우 To-Do = 위에 리플렉터나 블록이 있는 경우
                    #     return False
                    # Foonda_location[1] -= 1

                    # coords_map[Foonda_location[0], Foonda_location[1] + 1] = 'blank'
                    # coords_map[Foonda_location[0], Foonda_location[1] ] = 'Foonda'
                    # coords_map[Foonda_location[0], Foonda_location[1] - 1] = 'disk'

                    # #move disk

                    return 'disk' #디스크 전용 함수로 넘기기
                elif coords_map[Foonda_location[0], Foonda_location[1] -1] == 'reflector_up_right': #왼쪽으로 튕겨나가게
                    return 'reflector_up_right'
                elif coords_map[Foonda_location[0], Foonda_location[1] -1] == 'reflector_up_left':
                    return 'reflector_up_left'
                elif coords_map[Foonda_location[0], Foonda_location[1] -1] == 'one-way_reflector_down_right':
                    return 'one-way_reflector_down_right'
                elif coords_map[Foonda_location[0], Foonda_location[1] -1] == 'one-way_reflector_down_left':
                    return 'one-way_reflector_down_right'
                elif coords_map[Foonda_location[0], Foonda_location[1] -1] == 'block' or coords_map[Foonda_location[0], Foonda_location[1] -1 ] == 'hole' or coords_map[Foonda_location[0], Foonda_location[1] -1 ] == 'one-way_reflector_up_right' or coords_map[Foonda_location[0], Foonda_location[1] -1 ] == 'one-way_reflector_up_left':
                    return False
            else:
                return False
    elif direction == 'down':
        Foonda_location[1] += 1
    elif direction == 'left':
        Foonda_location[0] -= 1
    elif direction == 'right':
        Foonda_location[0] += 1
        return False
    return True