#execute this file to run the game

from mines import Grid
import os

#calling this function will clear the terminal  
#great for showing real time changes in the grid
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == '__main__':



    diff_levels = {'easy':(10,10),'medium':(15,40),'hard':(20,60),'expert':(20,85)}
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t+-------------------------------------+')
    print('\t|      Welcome to MINESWEEPER 💣      |')
    print('\t+-------------------------------------+')
    print('\nYou can choose a difficulty from the table below')
    print('The difficultyyou choose will determine the size of your grid and the number of mines in it')
    print('''
    +------------+----------------------------+
    | Difficulty | Description                |
    +------------+----------------------------+
    | Easy       | 10x10 Grid with 10 mines   |
    | Medium     | 15x15 Grid with 40 mines   |
    | Hard       | 20x20 Grid with 60 mines   |
    | Expert     | 20x20 Grid with 85 mines   |
    +------------+----------------------------+''')

    
    chances = 4
    while chances:
        difficulty = input("\nChoose your difficulty: ").strip().lower()
        if difficulty not in diff_levels.keys():
            print('Please choose one of the 4 given choices :)')
            chances -= 1
            continue
        break

    if chances == 0:
        difficulty = 'easy'
        print('\nDefault Difficulty set: Easy')
        input("\nPRESS ENTER TO CONTINUE ")
    else:
        print(f'\nYou have chosen {difficulty} difficulty.')
        input("\nPRESS ENTER TO CONTINUE ")

    n = diff_levels[difficulty][0]
    m = diff_levels[difficulty][1]
    
    mine_map = Grid(n,m)
    #mine_map.display()
    clear_terminal()
    print('\t\t+-------------------------------------+')
    print('\t\t|      Welcome to MINESWEEPER 💣      |')
    print('\t\t+-------------------------------------+\n')
    print(f'A {n}x{n} grid has been generated with {m} mines placed in it randomly at arbitrary positions\n')
    valid_cmd = {'f':'Flag','r':'Revealing','rf':'Remove Flag'}
    print('Instructions: Enter the coordinates and action in the following format: <x> <y> <action>\n')
    instructions = '''                        Valid Actions
    +------+-------------------------+-----------------+---------------+
    | Cmd  | Description             | Format          | Example       |
    +------+-------------------------+-----------------+---------------+
    | f    | Place a flag at (x,y)   | <x> <y> f       | 1 2 f         |
    | r    | Reveal the cell (x,y)   | <x> <y> r       | 4 5 r         |
    | rf   | Remove a placed flag    | <x> <y> rf      | 3 6 rf        |
    | q    | Quit the game           | q               | q             |
    | help | Show instructions       | help            | help          |
    +------+-------------------------+-----------------+---------------+
    
Other than the flag and reveal options, you dont need to enter coordinates for the rest'''
    print(instructions)
    input("\nPRESS ENTER START THE GAME ")
    while True:
        clear_terminal()
        mine_map.display()
        print('\nIf you need help, type \'help\'')
        command = input('Enter your next move <x> <y> <action>: ').strip().lower()
        print("")
        args = command.split()
        if len(args) != 3:
            try:
                args[0]
            except IndexError:
                print('Seems like you did not enter any commands.If you need help, type \'help\'')
                input("\nPRESS ENTER TO CONTINUE ")
                continue

            if args[0] == 'q':
                print('Exiting the game!!\n')
                break

            if args[0] == 'help':
                print(instructions)
                input("\nPRESS ENTER TO CONTINUE ")
                continue

            print('Oops! Wrong command. Seems like you are missing a few things. If you need help, type \'help\'')
            input("\nPRESS ENTER TO CONTINUE ")
            continue

        try:
            #lists in python are 0 indexed, but since we are diplaying the grid from  1 for user convenience 
            x = int(args[0]) -1
            y = int(args[1]) -1
        except ValueError:
            print('Oops. Please enter numerical coordinates. If you need help, type \'help\' ')
            input("\nPRESS ENTER TO CONTINUE ")
            continue
        if x not in range(n) and y not in range(n):
            print(f'Oops. It seems like the coordinates are invalid. Try to enter coordinates in the range (0 to {n}).\nIf you need help, type \'help\' ')
            input("\nPRESS ENTER TO CONTINUE ")
            continue
        
        act = args[2]
        if act not in valid_cmd.keys():
            print('Invalid action.If you need help, type \'help\'  ')
            input("\nPRESS ENTER TO CONTINUE ")
            continue

        if mine_map.is_empty(x,y):
            print('This cell is already reveled. Please try another cell')
            input("\nPRESS ENTER TO CONTINUE ")
            continue
        
        if act == 'f':
            if mine_map.place_flag(x,y):
                clear_terminal()
                mine_map.display()
                print(f'Placed a flag at ({x+1},{y+1}).')
                input("\nPRESS ENTER TO CONTINUE ")
                continue
            else:
                print(f'Flag already placed at ({x+1},{y+1})')
                input("\nPRESS ENTER TO CONTINUE ")
                continue

        if act == 'rf':
            if mine_map.remove_falg(x,y):
                clear_terminal()
                mine_map.display()
                print(f'Falg at ({x+1},{y+1}) has been removed.')
                input("\nPRESS ENTER TO CONTINUE ")
                continue
            else:
                print(f'No flag palced at ({x+1},{y+1})')
                input("\nPRESS ENTER TO CONTINUE ")
                continue

        if act == 'r':
            if mine_map.check_flag(x,y):
                print(f'\nA flag is placed at ({x+1},{y+1})')
                print('Please remove the flag using the \'rf\' command first.')
                input("\nPRESS ENTER TO CONTINUE ")
                continue
            if mine_map.reveal(x,y):
                #reveal returns True for all cases excpet a mine epxlosion
                if mine_map.check_win():
                    clear_terminal()
                    mine_map.display()
                    print('\n!!!!CONGRATULATIONS!!!!')
                    print('You have won the game')
                    try_again = input("\nDo you want to play again (y/n):  ").strip().lower()
                    if try_again == 'y':
                        mine_map = Grid(n,m)
                        print(f'\nGenerated a {n}x{n} grid with new mine posttions.')
                        input("\nPRESS ENTER TO RESTART ")
                        continue
                    else:
                        print('\nExiting the game. Hope to see you again.\n')
                        break

            else:
                #reaveal return False when a mine has exploded
                clear_terminal()
                mine_map.display()
                print(f'\nMINE EXPLODED AT ({x+1},{y+1})')
                print('**** GAME OVER ****')
                try_again = input("\nDo you want to try again (y/n):  ").strip().lower()
                if try_again == 'y':
                    try_again = input("\nDo you the same grid? (y/n):  ").strip().lower()
                    if try_again == 'n':
                        mine_map = Grid(n,m)
                        print(f'\nGenerated a {n}x{n} grid with new mine posttions.')
                        input("\nPRESS ENTER TO RESTART ")
                        continue
                    else:
                        mine_map.reset_grid()
                        print('\nRestarting with the same grid.')
                        input("\nPRESS ENTER TO RESTART ")
                        continue
                        
                else:
                    print('\nExiting the game. Hope to see you again.\n')
                    break
        
        # print('That is an invalid move. If you need help, type \'help\' ')
        # input("\nPRESS ENTER TO CONTINUE ")
        # continue


        
        
        



        
    


 
