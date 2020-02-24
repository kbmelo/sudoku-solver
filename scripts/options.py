import math

import clear

def filterIsolated(game, did_update):
    for i in range(9):
        amount = {}
        for j in range(9):
            if isinstance(game[i][j], list):
                for k in game[i][j]:
                    if str(k) in amount:
                        amount[str(k)] += 1
                    else:
                        amount[str(k)] = 1
        for key in amount:
            if amount[key] == 1:
                for k in range(9):
                    if isinstance(game[i][k], list) and int(key) in game[i][k]:
                        game[i][k] = int(key)
                        result = clear.run(game, True)
                        game = result['new_game']
                        did_update = result['did_update']

    result = clear.run(game, did_update)

    game = result['new_game']
    did_update = result['did_update']

    for j in range(9):
        amount = {}
        for i in range(9):
            if isinstance(game[i][j], list):
                for k in game[i][j]:
                    if str(k) in amount:
                        amount[str(k)] += 1
                    else:
                        amount[str(k)] = 1
        for key in amount:
            if amount[key] == 1:
                for k in range(9):
                    if isinstance(game[k][j], list) and int(key) in game[k][j]:
                        game[k][j] = int(key)
                        result = clear.run(game, True)
                        game = result['new_game']
                        did_update = result['did_update']

    result = clear.run(game, did_update)

    game = result['new_game']
    did_update = result['did_update']

    return clear.run(game, did_update)
