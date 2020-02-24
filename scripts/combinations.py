import clear

def find(game, did_update):
    for i in range(9):
        combinations = {}
        for j in range(9):
            if isinstance(game[i][j], list):
                word = ''
                for letter in game[i][j]:
                    word += str(letter)
                if word in combinations:
                    combinations[word][0] += 1
                    combinations[word][1].append(j)
                else:
                    combinations[word] = [1, [j]]
        for key in combinations:
            if combinations[key][0] == len(key):
                for k in range(9):
                    if isinstance(game[i][k], list) and k not in combinations[key][1]:
                        for l in key:
                            if int(l) in game[i][k]:
                                game[i][k].remove(int(l))
                                result = clear.run(game, did_update)
                                game = result['new_game']
                                did_update = result['did_update']
                                did_update = True
                                did_update = True

    for j in range(9):
        combinations = {}
        for i in range(9):
            if isinstance(game[i][j], list):
                word = ''
                for letter in game[i][j]:
                    word += str(letter)
                if word in combinations:
                    combinations[word][0] += 1
                    combinations[word][1].append(i)
                else:
                    combinations[word] = [1, [i]]
        for key in combinations:
            if combinations[key][0] == len(key):
                for k in range(9):
                    if isinstance(game[k][j], list) and k not in combinations[key][1]:
                        for l in key:
                            if int(l) in game[k][j]:
                                game[k][j].remove(int(l))
                                result = clear.run(game, did_update)
                                game = result['new_game']
                                did_update = result['did_update']
                                did_update = True
                                did_update = True

    for i in range(2):
        for j in range(2):
            i_quarter = i * 3
            j_quarter = j * 3

            combinations = {}
            for m in range(i_quarter, i_quarter + 3):
                for n in range(j_quarter, j_quarter + 3):
                    if isinstance(game[m][n], list):
                        word = ''
                        for letter in game[m][n]:
                            word += str(letter)
                        if word in combinations:
                            combinations[word][0] += 1
                            combinations[word][1].append([m, n])
                        else:
                            combinations[word] = [1, [[m, n]]]
            for key in combinations:
                if combinations[key][0] == len(key):
                    for o in range(i_quarter, i_quarter + 3):
                        for p in range(j_quarter, j_quarter + 3):
                            if isinstance(game[o][p], list) and [o, p] not in combinations[key][1]:
                                for l in key:
                                    if int(l) in game[o][p]:
                                        game[o][p].remove(int(l))
                                        result = clear.run(game, did_update)
                                        game = result['new_game']
                                        did_update = result['did_update']
                                        did_update = True
    return clear.run(game, did_update)
