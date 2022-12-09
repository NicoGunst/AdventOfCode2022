puzzle_input=open('data/data5.txt').read().splitlines()

piles = [[0]]
done = False
for line in puzzle_input:
    if not line: #si c'est la ligne vide, on passe
        continue
    if not done and line[1] != '1':#parsing des piles de bases
        for i in range(1, len(line), 4):
            idx = i // 4 + 1
            if len(piles) <= idx:#si la pile n'existe pas encore on la crée
                piles.append([line[i]])
            else:#sinon on ajoute sur la pile existante
                piles[idx].append(line[i])
    elif not done and line[1] == '1':#on arrive à la fin du parsing
        done = True
        for i, stack in enumerate(piles):
            stack = stack[::-1]#on remet les piles dans le bon sens
            piles[i] = stack
            while piles[i] and piles[i][-1] == ' ':
                piles[i].pop()#on enlève les cases vides
    else:#mouvements
        step = line.split()
        move, fro, to = map(int, [step[1], step[3], step[5]])
        # Partie 1
        # for i in range(move):
        #     c = piles[fro].pop()
        #     piles[to].append(c)
        # Partie 2
        crates = piles[fro][-move:]
        piles[fro] = piles[fro][:-move]
        piles[to].extend(crates)
res = ''
piles = piles[1:]
for elem in piles:
    res += elem.pop()
print(res)