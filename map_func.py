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
            elif map[i][x] == 'G':
                coords_map[i,x] = 'goal'
    
    return map, coords_map

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