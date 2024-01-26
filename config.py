"""A list of constants for configuring the game"""

#general settings
WINDOW_BG_COLOUR = [116, 207, 252, 255]
CELL_COLOUR = [116, 207, 252, 255]
ALT_CELL_COLOUR = [69, 186, 245, 255]
CELL_BORDER_HOVER = [12, 140, 204, 255]
CELL_COLOUR_MINE = [250, 132, 142, 255]
CELL_COLOUR_EMPTY = [182, 193, 250, 255]
UI_BG_COLOUR = [12, 140, 204, 252]
UI_HEIGHT = 60

CLOCK_SPEED = 60

# level data
EASY_GRID_SIZE = 8
MEDIUM_GRID_SIZE = 14
HARD_GRID_SIZE = 20

NUM_MINES_EASY = 10
NUM_MINES_MEDIUM = 40
NUM_MINES_HARD = 99

EASY_CELL_SIZE = 50
MEDIUM_CELL_SIZE = 35
HARD_CELL_SIZE = 30

# icons
ICON_ONE = "one"
ICON_TWO = "two"
ICON_THREE = "three"
ICON_FOUR = "four"
ICON_FIVE = "five"
ICON_SIX = "six"
ICON_SEVEN = "seven"
ICON_EIGHT = "eight"
ICON_FLAG = "flag"
ICON_MINE = "mine"
ICONS = [ICON_ONE, ICON_TWO, ICON_THREE, ICON_FOUR, ICON_FIVE, 
        ICON_SIX, ICON_SEVEN, ICON_EIGHT, ICON_FLAG, ICON_MINE]
ICONS_PATH = "./images/"
ICON_EXT = ".png"
ICON_STATE_CLOSED = "closed"
ICON_STATE_PENDING = "pending"
ICON_STATE_EMPTY = "empty"
ICON_STATE_OUTOFBOUNDS = "outofbounds"

# text
WINDOW_CAPTION = "MINESWEEPER"
LEVEL_EASY = "Easy"
LEVEL_MEDIUM = "Medium"
LEVEL_HARD = "Hard"
