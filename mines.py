import random

'''
Class Grid generates an object that stores the minesweeper grid and multiple 
helper functions to run the game. Member functions are used to fill mines in the grid
at random postions, place and remove flags, reveal cells and multiple cells using recursion and
all other functionalities of a Minesweeper game
'''

class Grid:

    def __init__(self , n , m):
        '''
        Initialises an object if class Grid
        Makes a grid of size = n*n
        Number of mines = m
        Number of flags = m
        Two empty matrix grid_1 and grid_2 of n*n
        '''
        self.n = n
        self.m = m 
        self.flags = m

        #grid1 - stores the location of mines 
        #grid2 - used to display the grid to the player
        self.grid_1 = []
        self.grid_2 = []
        self.populate()
    #end of init

    def reset_grid(self):
        '''
        Resets the grid for restarting a game
        '''    
        for i in range(self.n):
            for j in range(self.n):
                self.grid_2[i][j] = '■'
    #end of reset_grid

    def populate(self):
        '''
        Generates a n*n grid , and places m mines in it uniformly at random using random.sample
        grid_1 will have location of the mines and the neighbouting mines count = meant for internal use
        grid_2 wil only have cells which are used to display the grid to the player
        placing mines in grid_1 unifromly at random using random.sample
        this eliminates duplicates and ensures unifromly independent distribution
        takes m (x,y) postions from the list of all postions to place mines in (randomly)
        '''
        all_pos = []
        for i in range(self.n):
            row = []
            trow = []
            for j in range(self.n):
                all_pos.append((i,j))
                row.append(0)
                trow.append('■')

            self.grid_1.append(row)
            self.grid_2.append(trow)
        
        #placing mines at random
        mine_pos = random.sample(all_pos,self.m)
        for i,j in mine_pos:
            self.grid_1[i][j] = '*'
      
        #generating neighbouring mines count for grid_1
        neighbours = (-1,0,1)
        for i in range(self.n):
            for j in range(self.n):
                if self.grid_1[i][j] == '*':
                    continue
                count = 0
                for l in neighbours:
                    for k in neighbours:
                        x = i + l
                        y = j + k
                        if x in range(self.n) and y in range(self.n):
                            if self.grid_1[x][y] == '*':
                                count += 1
                self.grid_1[i][j] = count
    #end of populate


    def is_empty(self,x,y):
        '''
        Checks is a cell in grid_2 has already been revelaed by the player
        '''
        if self.grid_2[y][x] == '■' or self.grid_2[y][x] == '⚑':
            return False
        return True    
    #end of is_empty


    def place_flag(self,x,y):
        '''
        Places a flag ⚑ at cell at (x,y)
        '''
        if self.grid_2[y][x] == '⚑':
            return False 
        
        self.grid_2[y][x] = '⚑' 
        self.flags -= 1
        return True
    #end of place_flag

    
    def remove_falg(self,x,y):
        '''
        Removes the flag at (x,y) if present
        '''
        if self.grid_2[y][x] != '⚑':
            return False
        
        self.grid_2[y][x] = '■'
        self.flags += 1
        return True
    #end of remove_flag


    def check_flag(self,x,y):
        '''
        Checks if a flag is placed at (x,y)
        '''
        if self.grid_2[y][x] == '⚑':
            return True
        return False
    #end of check_flag


    def no_flags_left(self):
        '''
        Checks if there are any more flags left to use
        '''
        if self.flags == 0:
            return True
        return False
    #end of no_flags_left


    def display(self):
        '''
        This function diplays grid_2 to the player
        It will diaply the grif along with the x and y axis on the side for easy reference 
        '''
        print(f'Flags Left: {self.flags}\n')
        print('    ',end='')
        #x coordinates
        for i in range(self.n):
            print(f'{i+1:^3} ',end = "")
        print()
        
        #priting grid
        print('   ┌' + '───┬' * (self.n - 1) + '───┐')
        for i in range(self.n):
            print(f'{i+1:^3}│', end='')
            for j in range(self.n):
                print(f'{self.grid_2[i][j]:^3}│', end='')
            print()
            if i < self.n - 1:
                print('   ├' + '───┼' * (self.n - 1) + '───┤')
        print('   └' + '───┴' * (self.n - 1) + '───┘')
        
    #end of display


    def reveal(self,x,y):
        '''
        This function will reveal the cell at (x,y) if it is hidden (■)
        Returns Flase when a bomb is reveled causing an explosion
        Returns True in all other cases
        If an empty cell with 0 neighbours is revealed, the function will recursively call itself 
        to revel more cells 
        If a cell with a neighbour count is revealed, only that one is revealed
        '''
        #to stop the recursion if it encounters a flag
        if self.grid_2[y][x] != '■':
            return True 
        
        #mine explosion
        if self.grid_1[y][x] == '*':
            self.grid_2[y][x] = '💥'
            return False
        
        #recursion to reveal multiple cell in case of 0 neighbours
        neighbours = (-1,0,1)
        if self.grid_1[y][x] == 0 :
            self.grid_2[y][x] = ' '
            for l in neighbours:
                    for k in neighbours:
                        n_x = x + l
                        n_y = y + k
                        if n_x in range(self.n) and n_y in range(self.n) and not(l==0 and k==0):
                            if self.grid_1[n_y][n_x] != '*' and self.grid_2[n_y][n_x] == '■':
                                self.reveal(n_x,n_y)
            return True
        
        #single cell reveal 
        self.grid_2[y][x] = self.grid_1[y][x]
        return True
    #end of reveal


    def check_win(self):
        '''
        Checks for the winning condition
        A player wins the game if the number of hidden cells (including flags) is equla to the 
        number of mines placed in the grid ,i.e, all the safe cells have been revealed 
        '''
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.grid_2[i][j] in ('■','⚑'):
                    count += 1
        
        #all safe cells are revealed 
        if count == self.m:
            for i in range(self.n):
                for j in range(self.n):
                    if self.grid_2[i][j] in ('■','⚑'):
                        self.grid_2[i][j] = '*'
                    
            return True
        
        return False
    #end of check_win        

if __name__ == '__main__':
    #debugging       
    g = Grid(30,20)
    g.display()
        

        
