import math

import clear

def check(game, did_update):
    for i in range(9):
        for j in range(9):
            if isinstance(game[i][j], list):
                for k in game[i]:
                    if isinstance(k, int) and isinstance(game[i][j], list) and k in game[i][j]:
                        game[i][j].remove(k)
                        if len(game[i][j]) == 1:
                            game[i][j] = game[i][j][0]
                            result = clear.run(game, did_update)
                            game = result['new_game']
                            did_update = result['did_update']

                for k in range(9):
                    if isinstance(game[k][j], int) and isinstance(game[i][j], list) and game[k][j] in game[i][j]:
                        game[i][j].remove(game[k][j])
                        if len(game[i][j]) == 1:
                            game[i][j] = game[i][j][0]
                            result = clear.run(game, did_update)
                            game = result['new_game']
                            did_update = result['did_update']

                i_quarter = math.floor(i / 3) * 3
                j_quarter = math.floor(j / 3) * 3

                for m in range(i_quarter, i_quarter + 3):
                    for n in range(j_quarter, j_quarter + 3):
                        if isinstance(game[m][n], int) and isinstance(game[i][j], list) and game[m][n] in game[i][j]:
                            game[i][j].remove(game[m][n])
                            if len(game[i][j]) == 1:
                                game[i][j] = game[i][j][0]
                                result = clear.run(game, did_update)
                                game = result['new_game']
                                did_update = result['did_update']
    return clear.run(game, did_update)
