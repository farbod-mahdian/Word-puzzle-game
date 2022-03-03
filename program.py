# program: Assignment1.py
# author:  Farbod Mahdian
# date:    July 3, 2021
# purpose: python main( ) program for PRG550 Summer 2021 Assignment #1

import string


def generateGameBoard(nRows, nCols):
    board = []

    for i in range(nRows):
        tmp = []
        for j in range(nCols):
            tmp.append('.')
        board.append(tmp)

    return board


def loadWord(boardData, nRows, nCols, coord, word, dir):
    mapping_ = {}
    x = coord[0]
    y = coord[1]

    if nRows > nCols:
        index = nRows
    else:
        index = nCols

    for i in range(index - 9):
        mapping_[string.ascii_uppercase[i]] = (i + 10)
        if x == string.ascii_uppercase[i]:
            x = mapping_[x]
        if y == string.ascii_uppercase[i]:
            y = mapping_[y]
    x = int(x) - 1
    y = int(y) - 1

    if dir == 'H':
        for i in range(len(word)):
            boardData[x][y + i] = word[i]

    else:  # V
        for i in range(len(word)):
            boardData[x + i][y] = word[i]
    return boardData


def checkCoord(nRows, nCols, coord):
    mapping_ = {}

    if len(coord) != 2:
        return False

    else:
        if coord[0] in string.ascii_lowercase or coord[1] in string.ascii_lowercase:
            return False
        else:
            x = coord[0]
            y = coord[1]

        if nRows > nCols:
            index = nRows
        else:
            index = nCols

        for i in range(index - 9):
            mapping_[string.ascii_uppercase[i]] = (i + 10)
            if x == string.ascii_uppercase[i]:
                x = mapping_[x]
            if y == string.ascii_uppercase[i]:
                y = mapping_[y]
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return False

        if x <= nRows and y <= nCols:
            return True
        else:
            return False


def updateGameBoard(boardData, boardMask, nRows, nCols, coord, score, lastMove):

    if checkCoord(nRows, nCols, coord):
        mapping_ = {}
        x = coord[0]
        y = coord[1]

        if nRows > nCols:
            index = nRows
        else:
            index = nCols

        for i in range(index - 9):
            mapping_[string.ascii_uppercase[i]] = (i + 10)
            if x == string.ascii_uppercase[i]:
                x = mapping_[x]
            if y == string.ascii_uppercase[i]:
                y = mapping_[y]
        x = int(x) - 1
        y = int(y) - 1

        if boardData[x][y] != '.' and boardData[x][y] != '-':
            boardMask[x][y] = boardData[x][y]
            score += 5
            lastMove = "FOUND '" + boardData[x][y] + \
                "' at [" + coord[0] + "," + coord[1] + "]"

            a = 1
            while (y+a) < nCols and boardData[x][y+a] != '.' and boardMask[x][y+a] == '.':
                boardMask[x][y+a] = boardData[x][y+a]
                score += 5
                a += 1
            a = 1
            while (y-a) >= 0 and boardData[x][y-a] != '.' and boardMask[x][y-a] == '.':
                boardMask[x][y-a] = boardData[x][y-a]
                score += 5
                a += 1

            a = 1
            while (x+a) < nRows and boardData[x+a][y] != '.' and boardMask[x+a][y] == '.':
                boardMask[x+a][y] = boardData[x+a][y]
                score += 5
                a += 1
            a = 1
            while (x-a) >= 0 and boardData[x-a][y] != '.' and boardMask[x-a][y] == '.':
                boardMask[x-a][y] = boardData[x-a][y]
                score += 5
                a += 1
        else:
            if boardData[x][y] != '-':
                boardMask[x][y] = '~'
            lastMove = "NO letter FOUND at [" + coord[0] + "," + coord[1] + "]"

    else:
        lastMove = "[" + coord[0] + "," + \
            coord[1] + "] is an INVALID COORDINATE"

    print("Python Crossword Puzzle...")
    print("  ", end="")
    for i in range(1, 10):
        print(i, end="")
    for i in range(nCols - 9):
        print(string.ascii_uppercase[i], end="")
    print()

    for i in range(1, 10):
        print(str(i) + '|', end="")
        for j in range(nCols):
            print(boardMask[i-1][j], end="")
        print('|')
    for i in range(nRows - 9):
        print(string.ascii_uppercase[i] + '|', end="")
        for j in range(nCols):
            print(boardMask[i+9][j], end="")
        print('|')

    print("Current Score: " + "%04d" % score, end="  ")
    print("Last Move: " + lastMove)

    return (boardData, boardMask, score, lastMove)


def main():
    score = 0
    coords = ["25", "2A", "XL", "9Q", "1D", "6J", "93", "B4", "AF"]
    lastMove = ""
    board = generateGameBoard(20, 26)
    mask = generateGameBoard(20, 26)

    # loading words onto game board
    board = loadWord(board, 20, 26, "29", "HELLO", "H")
    board = loadWord(board, 20, 26, "1D", "NO", "V")
    board = loadWord(board, 20, 26, "2A", "EXAMINE", "V")
    board = loadWord(board, 20, 26, "5J", "AREA", "V")
    board = loadWord(board, 20, 26, "6H", "NORTH", "H")
    board = loadWord(board, 20, 26, "93", "PYTHON", "H")
    board = loadWord(board, 20, 26, "AD", "PUZZLE", "H")
    board = loadWord(board, 20, 26, "B4", "7-SEAS", "H")
    board = loadWord(board, 20, 26, "AF", "ZOO", "V")

    for coord in coords:
        (board, mask, score, lastMove) = updateGameBoard(
            board, mask, 20, 26, coord, score, lastMove)
        print()


if __name__ == "__main__":
    main()
