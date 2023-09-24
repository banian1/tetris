class BlockType:
    RED=0
    ORANGE=1
    YELLOW=2
    GREEN=3
    CYAN=4
    BLUE=5
    PURPLE=6
    BLOCKMAX=7

class BlockGroupType:
    FIXED=0
    DROP=1

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

BLOCK_SIZE_W=32
BLOCK_SIZE_H=32


BLOCK_SHAPE=[
    #方形
    [((0,0),(0,1),(1,0),(1,1)),],
    #长条
    [((0,0),(0,1),(0,2),(0,3)),((0,0),(1,0),(2,0),(3,0))],
    #z字形
    [((0,0),(0,1),(1,1),(1,2)),((0,1),(1,0),(1,1),(2,0))],
    #飞机形
    [((0,1),(1,0),(1,1),(1,2)),
     ((0,1),(1,1),(1,2),(2,1)),
     ((1,0),(1,1),(1,2),(2,1)),
     ((0,1),(1,0),(1,1),(2,1))],
]