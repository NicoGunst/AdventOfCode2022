directions = {
    "R" : lambda x, y : (x + 1, y),
    "D" : lambda x, y : (x, y + 1),
    "L" : lambda x, y : (x - 1, y),
    "U" : lambda x, y : (x, y - 1)
}

puzzle_input = open("data/data9.txt", "r").read().rstrip().splitlines()
data = (((y := x.split(" "))[0], int(y[1])) for x in puzzle_input)
rope = [(0,0) for x in range(11)]
prev_rope = [set() for x in range(11)]

for direction, steps in data:
    print("start move ",direction)
    for i in range(steps):
        print("start enum ",i)
        for e, z in enumerate(rope):
            print(e," ",z," ",rope[e])
            if e==0:#début de la corde
                rope[e] = directions[direction](*rope[e])
                prev_rope[e].add(rope[e])
                print("go to ",*rope[e])
            else:#on suit la corde
                x = rope[e - 1][0] - rope[e][0]#diff en x avec le bout juste avant
                y = rope[e - 1][1] - rope[e][1]#diff en y avec le bout juste avant
                if abs(x) > 1 or abs(y) > 1:
                    x //= abs(x or 1)
                    y //= abs(y or 1)
                    new_x = rope[e][0]+x
                    new_y = rope[e][1]+y
                    rope[e] = (new_x,new_y)
                    print(rope[e])
                prev_rope[e].add(rope[e])
print(len(prev_rope[1]))
print(len(prev_rope[9]))