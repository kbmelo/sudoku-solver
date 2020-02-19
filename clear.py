import math


def run(game, did_update):
    shouldRerun = False

    for i in range(9):
        numbers = []
        for j in range(9):
            if isinstance(game[i][j], int):
                numbers.append(game[i][j])
        for k in range(9):
            for n in numbers:
                if isinstance(game[i][k], list):
                    if n in game[i][k]:
                        game[i][k].remove(n)
                        did_update = True
                        if len(game[i][k]) == 1:
                            game[i][k] = game[i][k][0]
                            shouldRerun = True
    for j in range(9):
        numbers = []
        for i in range(9):
            if isinstance(game[i][j], int):
                numbers.append(game[i][j])
        for k in range(9):
            for n in numbers:
                if isinstance(game[k][j], list):
                    if n in game[k][j]:
                        game[k][j].remove(n)
                        did_update = True
                        if len(game[k][j]) == 1:
                            game[k][j] = game[k][j][0]
                            shouldRerun = True

    for i in range(3):
        for j in range(3):

            i_quarter = i * 3
            j_quarter = j * 3

            for m in range(i_quarter, i_quarter + 3):
                numbers = []
                for n in range(j_quarter, j_quarter + 3):
                    if isinstance(game[m][n], int):
                        numbers.append(game[m][n])
                for m in range(i_quarter, i_quarter + 3):
                    for n in range(j_quarter, j_quarter + 3):
                        for num in numbers:
                            if isinstance(game[m][n], list):
                                if num in game[m][n]:
                                    game[m][n].remove(num)
                                    if len(game[m][n]) == 1:
                                        game[m][n] = game[m][n][0]
                                        shouldRerun = True

    if shouldRerun:
        return run(game, did_update)

    return {
        'new_game': game,
        'did_update': did_update,
    }