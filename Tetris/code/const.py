class BlockType:
    RED=0
    ORANGE=1
    YELLOW=2
    GREEN=3
    CYAN=4
    BLUE=5
    PURPLE=6
    BLOCKMAX=7

BLOCK_RES={
    BlockType.RED:"G:\\Tetris\\pic\\red.png",
    BlockType.ORANGE:"G:\\Tetris\\pic\\orange.png",
    BlockType.YELLOW:"G:\\Tetris\\pic\\yellow.png",
    BlockType.GREEN:"G:\\Tetris\\pic\\green.png",
    BlockType.CYAN:"G:\\Tetris\\pic\\green.png",
    BlockType.BLUE:"G:\\Tetris\\pic\\cyan.png",
    BlockType.PURPLE:"G:\\Tetris\\pic\\purple.png",
}

GAME_ROW=17
GAME_COL=10

BLOCK_SHAPE=[
    [(0,0),(0,1),(1,0),(1,1)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,1),(1,0),(1,1),(1,2)],
]