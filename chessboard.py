import numpy as np
import random

# Author: Brenden Ehlers
# The purpose of this algorithm is to generate a tiling of
# 2x1 dominoes for a chessboard of a given size with 2 missing
# cells.  In the final console, -1 represents the missing square,
# 1 represents the start of a domino, and 2 represents the end
# of a domino.

def mutilated_chessboard(x_size=8, y_size=8):
    arr = np.zeros((x_size, y_size))
    arr[random.randrange(x_size)][random.randrange(y_size)] = -1
    x_rand, y_rand = random.randrange(x_size), random.randrange(y_size)
    while arr[x_rand][y_rand] == -1:
        x_rand, y_rand = random.randrange(x_size), random.randrange(y_size)
    arr[x_rand][y_rand] = -1

    red = True
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == -1:
                print(f"{arr[x][y]}: {'red' if red else 'blue'}")
            red = not red
        red = not red

    # check if the problem is solvable
    # raise exception if it isn't solvable
    if not check_solvable(arr):
        raise Exception("this board is not solvable")
        # return -1

    # create the tiling
    x_i, y_i = 0, 0
    transposed = False
    num_holes = 0

    for x in range(x_i, len(arr[y_i])):
        if arr[y_i][x] == -1:
            num_holes += 1

    if arr[y_i][x_i] == -1:
        x_i += 1

    # if a hole is in an annoying spot, transpose the array so it
    # is no longer in that spot set the transposed variable to
    # True so the program knows to switch the array back
    if num_holes > 0:
        np.transpose(arr)
        transposed = True

    # starting row
    start = True
    for x in range(0, len(arr[y_i])):
        if arr[y_i][x] == -1:
            x += 1
        else:
            arr[y_i][x] = 1 if start else 2
            start = not start

    # middle rows
    forward = False

    for y in range(1, len(arr)-1):
        if not forward:
            for x in range(len(arr[y])-1, 0, -1):
                if arr[y][x] == -1:
                    if x - 1 >= 1:
                        x -= 1
                    else:
                        break
                else:
                    arr[y][x] = 1 if start else 2
                    start = not start
        else:
            for x in range(1, len(arr[y])):
                if arr[y][x] == -1:
                    if x+1 <= len(arr[y]):
                        x += 1
                    else:
                        break
                else:
                    arr[y][x] = 1 if start else 2
                    start = not start
        forward = not forward

    # final row
    for x in range(x_size-1, 0, -1):
        if arr[y_size-1][x] == -1:
            x -= 1
        else:
            arr[y_size-1][x] = 1 if start else 2
            start = not start

    # final column
    for y in range(y_size-1, 0, -1):
        if arr[y][0] == -1:
            y -= 1
        else:
            arr[y][0] = 1 if start else 2
            start = not start

    if transposed:
        np.transpose(arr)

    return arr

# returns true if the array provided is solvable, otherwise returns false
def check_solvable(arr):
    num_red, num_blue = 0, 0
    red = True

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == -1:
                if red:
                    num_red += 1
                else:
                    num_blue += 1
            red = not red
        red = not red
    # print(f"num_red: {num_red}\num_blue: {num_blue}")
    return num_red == num_blue

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = (mutilated_chessboard(8, 8))
    print(arr)
