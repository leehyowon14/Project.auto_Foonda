'''
symbols:
    . = blank
    o = disk
    x = block
    /, \ = reflector
    R,L,r,l= one-way reflector(up-Right, up-Left, down-Right, down-Left)
    - = gap
    _ = hole
    F = Foonda
    G = goal

var
    Foonda_location = [x,y]
    coords_map = {(x,y): symbol}

map v2 coords example(2x2):
    0,0 | 1,0
    0,1 | 1,1
'''

one_way_reflector_spin_order = ["one-way_reflector_down_right", "one-way_reflector_down_left", "one-way_reflector_up_left", "one-way_reflector_up_right"]

def disk(direction, coords):
    global Foonda_location , coords_map

def reflector(direction, coords, is_one_way, is_Foonda): 
    #parameter: direction(Foonda's move direction), coords(reflector's coords), is_one_way(one-way or two-way), is_Foonda(Foonda or disk)
    global Foonda_location , coords_map
    if is_one_way:
        if direction == 'up':
            if coords_map[coords] == 'one-way_reflector_down_right':
                coords_map[coords] = 'one-way_reflector_down_left'
            else:
                coords_map[coords] = 'one-way_reflector_up_left'
            #move Foonda

def move_Foonda(direction):
    global Foonda_location, coords_map # Foonda_location = [x,y]
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

                    return ['disk', 'up', (Foonda_location[0], Foonda_location[1]-1)] #[타입, 방향, 좌표]
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