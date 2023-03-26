## Creating Grid
width = 3
height = 3
grid = [None for x in range(width * height)]

currentPlayer = "X"

def print_grid():
    for i in range(len(grid)):
        val = grid[i]

        # print the value or cell number
        if val is None:
            print(i, end=" ")
        else:
            print(val, end=" ")

        # do a line break
        if i%3==2:
            print()

def is_input_valid(user_input):

    if user_input not in range(0, 9):
        return False

    if grid[user_input] is not None:
        return False

    return True

def get_player_input():
    user_input = input("Player {} enter your move space: ".format(currentPlayer))

    valid_input = False
    while valid_input == False:
        try:
            user_input = int(user_input)
            if is_input_valid(user_input):
                valid_input = True
            else:
                user_input = input("Invalid input, please try again: ")
        except:
            user_input = input("Invalid input, please try again: ")
    
    return user_input


def alternate_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def update_grid(user_input):
    global grid
    grid[user_input] = currentPlayer

def is_win():  
    return (grid[0] == grid[1] == grid[2] != None or
            grid[1] == grid[4] == grid[7] != None or
            grid[3] == grid[4] == grid[5] != None or
            grid[6] == grid[4] == grid[2] != None or
            grid[0] == grid[3] == grid[6] != None or
            grid[0] == grid[4] == grid[8] != None or
            grid[2] == grid[5] == grid[8] != None or
            grid[6] == grid[7] == grid[8] != None)

def take_turns():

    for i in range(len(grid)):
        user_input = get_player_input()
        update_grid(user_input)
        if is_win():
            print("Player "+currentPlayer+" wins!")
            return
        print_grid()
        alternate_player()

    print("tie")


def main(): 
    take_turns()


main()