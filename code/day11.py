class Singe:
    def __init__(self, x):
        _, a, b, c, d, e = x.split('\n')
        self.items = [int(i) for i in a[18:].split(',')]
        self.operation = b[19:]
        self.div = int(c[20:])
        self.true = int(d[28:])
        self.false = int(e[29:])
        self.action = 0

        
puzzle_input = open("data/data11.txt").read().split('\n\n')
singes = [*map(Singe,puzzle_input) ]

modulo=1
for i in (s.div for s in singes):
    modulo *= i
    
for i in range(10000):
    for s in singes:
        for worry in s.items:
            old = worry
            worry = eval(s.operation) % modulo
            #Partie 1 seulement
            #worry //=3
            dest = s.false if worry % s.div else s.true
            singes[dest].items.append(worry)
            s.action += 1
        s.items = []
        
actions_singes = [s.action for s in singes]
first = max(actions_singes)
actions_singes.remove(first)
second = max(actions_singes)
print(first * second)