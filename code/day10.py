puzzle_input = open("data/data10.txt", "r").read().rstrip().split()
X=1
part1=0
part2 = ''
for i, value in enumerate(puzzle_input):
    part1 += (i+1) * X if i%40==19 else 0
    
    part2 += '#' if abs(i%40 - X) < 2 else '.'
    if i%40==0 :
        part2 += '\n'
    if (value[0] != 'a' and value[0] != 'n'):#si c'est un nombre
        X+=int(value)
    
    
print(part1)
print(part2)