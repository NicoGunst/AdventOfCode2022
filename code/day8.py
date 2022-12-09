puzzle_input = open("data/data8.txt", "r").read().rstrip().split()
arbres = tuple([tuple(map(int, list(row.strip())))
                       for row in puzzle_input])
#partie1
visibles = 0

for i, row in enumerate(arbres):
    for j, col in enumerate(row):
        element = arbres[i][j]

        haut = list([element > row[j] for row in arbres[:i]])
        gauche = list([element > col for col in arbres[i][:j]])
        droite = list([element > col for col in arbres[i][j + 1:]])
        bas = list([element > row[j] for row in arbres[i + 1:]])

        if any([all(haut), all(gauche), all(droite), all(bas)]):
            visibles += 1

print(visibles)
    
#partie2
scores = []

for i, row in enumerate(arbres):
    for j, col in enumerate(row):
        element = arbres[i][j]

        haut = tuple(reversed([element > row[j] for row in arbres[:i]]))
        gauche = tuple(reversed([element > col for col in arbres[i][:j]]))
        droite = tuple([element > col for col in arbres[i][j + 1:]])
        bas = tuple([element > row[j] for row in arbres[i + 1:]])

        h = haut.index(False) + 1 if (False in haut) else len(haut)
        g = gauche.index(False) + 1 if (False in gauche) else len(gauche)
        d = droite.index(False) + 1 if (False in droite) else len(droite)
        b = bas.index(False) + 1 if (False in bas) else len(bas)

        score = h * g * d * b
        scores.append(score)

print(max(scores))