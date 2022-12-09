import sys

puzzle_input = open("data/data7.txt", "r").read().split('\n')[1:]
filesystem = {"": 0}
pwd = ""

for line in puzzle_input:
    if '..' in line:
        pwd = pwd[:pwd.rindex('/')]
    elif '$ cd' in line:
        pwd = pwd + '/' + line[5:]
        filesystem[pwd] = 0
    elif line.split(' ')[0].isnumeric():
        filesystem[""] += int(line.split(' ')[0])
        cur = pwd
        while cur:
            filesystem[cur] += int(line.split(' ')[0])
            cur = cur[:cur.rindex('/')] if '/' in cur else ""

print(sum([v for v in filesystem.values() if v <= 100000]))
minimum_to_free = filesystem[""] + 30000000 - 70000000
print([x for x in sorted(filesystem.values()) if x - minimum_to_free > 0][0])