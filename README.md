# COMP9001-Minesweeper 💣 
Classic Minesweeper reimagined in Python as a interactive command-line input game. Find all the hidden mines in the board to win the game. 

## FEATURES
- Random and independent palcement of mines in the grid
- Terminal refreshes for each action ensuring a clean gameplay experience
- Clean view of the grid with coordinates on the side for ease of comfort
- Score is calculated as the time taken to beat the game
- Mutiple difficulty choices (Easy|Medium|Hard|Expert)
- No additional libraries required other than time and random 

## GAME INSTRUCTIONS
Once the game starts and displays the grid, you can enter your command or action in the following format:   
`<x coordinate> <y coordinate> <action>`
  
Valid commands : 
| Command |        Description        | Format   | Example |
|---------|---------------------------|----------|----------|
| f       | Place a flag (⚑) at (x,y) | x y  f   | 1 2 f    |
| r       | Reveal the tile (x,y)     | x y r    | 4 5 r    |
| rf      | Remove a placed flag      | x y rf   | 3 6 rf   |
| q       | Quit the game             | q        | q        |
| help    | Show instructions         | help     | help     |

The main objective of the game is to find all the mines.
## HOW TO RUN
- Clone the Git repository
- Run driver.py
  
Requires `Python3.x`    
No external libraries required

## PROJECT STRUCTURE
```
Minesweeper/
├── driver.py   # Main script to run the game 
├── mines.py    # Classes and grids
└── README.md   # Project documentation
```
Source Code available at : https://github.com/rahul-361/COMP9001-Minesweeper
