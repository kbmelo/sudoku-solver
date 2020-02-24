import numpy as np

import options
import combinations
import clear

game = [
    [0, 3, 7, 6, 2, 0, 0, 0, 0],
    [9, 5, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 2, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 3, 0, 0, 0],
    [8, 0, 0, 1, 0, 4, 9, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 1, 4, 0, 0, 0, 0, 2, 6],
]

# game = [
#     [3, 7, 9, 0, 0, 0, 0, 0, 5],
#     [0, 6, 0, 0, 0, 0, 0, 7, 0],
#     [0, 0, 0, 2, 3, 0, 0, 0, 1],
#     [0, 9, 0, 0, 2, 0, 0, 5, 0],
#     [7, 0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 2, 6, 0, 8, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 0, 3],
#     [0, 3, 8, 0, 0, 0, 6, 0, 0],
#     [0, 0, 0, 0, 0, 0, 4, 0, 9],
# ]

# game = [
#     [0, 3, 0, 0, 7, 2, 0, 0, 6],
#     [0, 0, 4, 0, 0, 0, 2, 0, 9],
#     [6, 0, 0, 0, 1, 3, 0, 0, 8],
#     [0, 0, 0, 5, 0, 6, 4, 0, 0],
#     [0, 8, 0, 0, 9, 0, 0, 6, 0],
#     [0, 0, 2, 1, 0, 7, 0, 0, 0],
#     [2, 0, 0, 6, 4, 0, 0, 0, 7],
#     [9, 0, 6, 0, 0, 0, 8, 0, 0],
#     [8, 0, 0, 2, 5, 0, 0, 1, 0],
# ]

initial = 0

for i in range(9):
    for j in range(9):
        if not game[i][j]:
            initial += 1
            game[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


gameStatus = True

print('0%')

while gameStatus:
    did_update = False

    result = clear.run(game, did_update)
    game = result['new_game']
    did_update = result['did_update']

    result = options.filterIsolated(game, did_update)
    game = result['new_game']
    did_update = result['did_update']

    result = combinations.find(game, did_update)   
    game = result['new_game']
    did_update = result['did_update']

    current = 0

    for i in range(9):
        for j in range(9):
            if isinstance(game[i][j], list):
                current += 1
    progress = round((initial - current) * 100 / initial)

    print(f'{str(progress)}%')

    if not did_update or progress == 100:
        gameStatus = False

message = 'Win'

for i in range(9):
    for j in range(9):
        if isinstance(game[i][j], list):
            game[i][j] = 0
            message = 'Lose'

print(message)
print(np.matrix(game))
