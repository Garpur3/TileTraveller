#We assign each (v)ertival and (h)orizontal wall to a boolean value in these arrays
#In both arrays we index left to right and down to up
v_walls = [[False, False, False], [False, True, True], [False, False, True], [False, False, False]]
h_walls = [[False, False, False], [True, True, True], [True, False, True], [False, False, False]]

x = 1
y = 1

#Function to print " or" if direction is not the first available direction
def not_first(is_it):
    if is_it:
        print(" or", end=" ")

#Direction printer, checks if each wall is true
def print_directions(x, y, h_walls, v_walls):
    next_dir = False
    print("You can travel: ", end="")
    if h_walls[y][x-1]:
        print("(N)orth", end="")
        next_dir = True
    if v_walls[x][y-1]:
        not_first(next_dir)
        print("(E)ast", end ="")
        next_dir = True
    if h_walls[y-1][x-1]:
        not_first(next_dir)
        print("(S)outh", end="")
        next_dir = True
    if v_walls[x-1][y-1]:
        not_first(next_dir)
        print("(W)est", end="")
        next_dir = True
    print(".")

#Decentralized wall-checkers
def check_north(x, y, h_walls, v_walls):
    return h_walls[y][x-1]

def check_east(x, y, h_walls, v_walls):
    return v_walls[x][y-1]

def check_south(x, y, h_walls, v_walls):
    return h_walls[y-1][x-1]

def check_west(x, y, h_walls, v_walls):
    return v_walls[x-1][y-1]


#Returns x and y variables whether they were updated or not
def move(x, y, h_walls, v_walls):
    move_char = input("Direction: ").lower()
    if move_char == "n" and check_north(x, y, h_walls, v_walls):
        y += 1
    elif move_char == "e" and check_east(x, y, h_walls, v_walls):
        x += 1
    elif move_char == "s" and check_south(x,y, h_walls, v_walls):
        y -= 1
    elif move_char == "w" and check_west(x, y, h_walls, v_walls):
        x -= 1
    else:
        print("Not a valid direction!")
    return x, y

while True:

    print_directions(x, y, h_walls, v_walls)

    #These are used to check whether the x and y values were actually updated
    x0 = x
    y0 = y

    while x0 == x and y0 == y:
        x, y = move(x, y, h_walls, v_walls)

    #Victory case
    if x == 3 and y == 1:
        print("Victory!")
        break