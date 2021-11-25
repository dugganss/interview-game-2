#SCREEN SIZE VARIABLES
WINDOW_W = 800
WINDOW_H = 600

# ~ The 2D array that is used for positioning of of the sprites on screen

# KEY:
# 1 = Block
# 2 = SPACE THAT CANNOT BE SEEN ON SCREEN DUE TO OFFSET FOR ISOMETRIC EFFECT
# 3 = Player
# 4 = Platform
# 5 = Enemy

layout =[
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2],
  [0,0,1,1,3,1,1,1,1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2],
  [0,0,1,1,1,1,1,1,1,4,4,0,4,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,1,1,1,1,0,0,0,0,4,4,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,1,1,0,0,0,0,0,0,4,4,0,0,0,0,0,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,4,0,0,0,0,0,0,0,0,4,1,1,0,0,0,0,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,2,2,2,2,2,2,2],
  [0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,2,2,2,2,2,2],
  [0,0,0,0,1,4,0,0,0,0,0,0,0,0,0,5,1,0,0,0,0,0,0,0,2,2,2,2,2],
  [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,2,2,2,2],
  [2,0,0,0,1,1,1,1,5,1,1,1,4,0,4,1,1,0,0,0,0,0,0,0,0,0,2,2,2],
  [2,2,0,0,0,0,0,0,0,0,0,4,0,0,0,0,1,4,4,4,0,0,0,0,0,0,0,2,2],
  [2,2,2,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,2,2],
  [2,2,2,2,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,2,2],
  [2,2,2,2,2,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,2],
  [2,2,2,2,2,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2],
  [2,2,2,2,2,2,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2],
  [2,2,2,2,2,2,2,2,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,2,2],
  [2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,2,2],
  [2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,4,4,0,0,0,0,0,0,4,1,5,1,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,4,0,0,0,0,0,0,4,0,1,1,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,4,4,4,0,0,4,4,4,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,1,1,1,1,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,1,1,1,1,1,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2],
  ]

TEMPLATE =[
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
  [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,2,2],
  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2],
]