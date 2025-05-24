import random

class Grid:

    def __init__(self , n , m):
        self.n = n
        self.m = m 
        self.flags = m
        #grid1 - stores the location of mines 
        #grid2 - used to display the grid to the player
        self.grid_1 = []
        self.grid_2 = []
        self.populate()

    def reset_grid(self):
        for i in range(self.n):
            for j in range(self.n):
                self.grid_2[i][j] = '■'
        
    # ■ 🚩 □
    def populate(self):
        
        for i in range(self.n):
            row = []
            trow = []
            for j in range(self.n):
                row.append(0)
                trow.append('■')
                

            self.grid_1.append(row)
            self.grid_2.append(trow)
        
        for i in range(self.m):
            i = random.randint(0,self.n-1)
            j = random.randint(0,self.n-1)
            self.grid_1[i][j] = '*'
        
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

    def is_empty(self,x,y):
        if self.grid_2[y][x] == '■' or self.grid_2[y][x] == '⚐':
            return False
        return True    
                
    def place_flag(self,x,y):
        if self.grid_2[y][x] == '⚐':
            return False 
        
        self.grid_2[y][x] = '⚐'
        self.flags -= 1
        return True

    
    def remove_falg(self,x,y):
        if self.grid_2[y][x] != '⚐':
            return False
        
        self.grid_2[y][x] = '■'
        self.flags += 1
        return True

    def check_flag(self,x,y):
        if self.grid_2[y][x] == '⚐':
            return True
        
        return False
    def display(self):
        
        # for i in range(self.n):
        #     print('------'*(self.n-4)+'-----')
        #     print('|',end = '')
        #     for j in range(self.n):
        #         print(f' {self.grid_1[i][j]} |',end = '')
        #     print("")
        # print('------'*(self.n-4)+'-----')

        
        #print('\n\n GRID 2:')
        print('    ',end='')
        for i in range(self.n):
            print(f'{i+1:^3} ',end = "")
        print()
        for i in range(self.n):
            print('   ' + ('+---') * self.n + '+')
            print(f'{i+1:^3}|',end = '')
            for j in range(self.n):
                print(f'{self.grid_2[i][j]:^3}|', end='')
            print("")
        print('   ' + ('+---') * self.n + '+')

    def reveal(self,x,y):
        if self.grid_2[y][x] != '■':
            return True 
        
        if self.grid_1[y][x] == '*':
            self.grid_2[y][x] = '💥'
            return False
        
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
        
        self.grid_2[y][x] = self.grid_1[y][x]
        return True

    def check_win(self):

        count = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.grid_2[i][j] in ('■','⚐'):
                    count += 1
        
        #all safe cells are revealed 
        if count == self.m:
            for i in range(self.n):
                for j in range(self.n):
                    if self.grid_2[i][j] in ('■','⚐'):
                        self.grid_2[i][j] = '*'
                    
            return True
        
        return False
                


        
       



        


if __name__ == '__main__':      
    g = Grid(30,20)
    g.display()
        

        