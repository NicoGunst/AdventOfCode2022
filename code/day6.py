puzzle_input = open("data/data6.txt").read()
for length in 4,14:
    for i in range(len(puzzle_input)):
        if(len(set(puzzle_input[i:i+length])) == length):
            print(i+length)
            break