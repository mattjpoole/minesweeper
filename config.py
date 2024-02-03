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
ICON_BADFLAG = "bad-flag"
ICON_MINE = "mine"
ICON_TIMER = "timer"
ICONS = [ICON_ONE, ICON_TWO, ICON_THREE, ICON_FOUR, ICON_FIVE, 
        ICON_SIX, ICON_SEVEN, ICON_EIGHT, ICON_FLAG, ICON_BADFLAG,
        ICON_MINE, ICON_TIMER]
ICONS_PATH = "./images/"
ICON_EXT = ".png"
ICON_STATE_CLOSED = "closed"
ICON_STATE_EMPTY = "empty"
ICON_STATE_OUTOFBOUNDS = "outofbounds"

# text
WINDOW_CAPTION = "MINESWEEPER"
LEVEL_EASY = "Easy"
LEVEL_MEDIUM = "Medium"
LEVEL_HARD = "Hard"

# debug
DEBUG_ON = False
DEBUG_MINE_LOCATIONS_EASY = {"12": 12, "23": 23, "25": 25, "31": 31, "34": 34, "40": 40,
                         "43": 43, "47": 47, "50": 50, "56": 56}
DEBUG_MINE_LOCATIONS_MEDIUM = {
  "7": 7, "12": 12, "21": 21, "34": 34, "42": 42, "51": 51, "63": 63, "74": 74, "81": 81, "92": 92,
  "103": 103, "114": 114, "126": 126, "132": 132, "145": 145, "157": 157, "164": 164, "172": 172, "181": 181, "194": 194,
  "4": 4, "19": 19, "28": 28, "38": 38, "46": 46, "55": 55, "67": 67, "73": 73, "85": 85, "97": 97,
  "101": 101, "111": 111, "123": 123, "134": 134, "142": 142, "155": 155, "163": 163, "176": 176, "184": 184, "196": 196
}
DEBUG_MINE_LOCATIONS_HARD = {
  "12": 12, "23": 23, "37": 37, "41": 41, "52": 52, "65": 65, "72": 72, "85": 85, "90": 90,
  "103": 103, "115": 115, "126": 126, "137": 137, "148": 148, "159": 159, "160": 160, "171": 171, "182": 182,
  "193": 193, "204": 204, "210": 210, "221": 221, "232": 232, "243": 243, "254": 254, "265": 265, "276": 276,
  "287": 287, "298": 298, "301": 301, "312": 312, "323": 323, "334": 334, "345": 345, "356": 356, "367": 367,
  "378": 378, "389": 389, "14": 14, "25": 25, "36": 36, "47": 47, "58": 58, "69": 69, "80": 80,
  "91": 91, "102": 102, "113": 113, "124": 124, "135": 135, "146": 146, "157": 157, "168": 168, "179": 179,
  "190": 190, "201": 201, "212": 212, "223": 223, "234": 234, "245": 245, "256": 256, "267": 267, "278": 278,
  "289": 289, "300": 300, "311": 311, "322": 322, "333": 333, "344": 344, "355": 355, "366": 366, "377": 377,
  "388": 388, "399": 399, "13": 13, "24": 24, "35": 35, "46": 46, "57": 57, "68": 68, "79": 79,
  "92": 92, "105": 105, "118": 118, "131": 131, "142": 142, "153": 153, "164": 164, "175": 175, "186": 186,
  "197": 197, "208": 208, "219": 219, "230": 230, "241": 241, "252": 252, "263": 263, "274": 274, "285": 285
}
