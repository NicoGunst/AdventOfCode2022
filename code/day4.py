import re
 
def inclut(min1: int, max1: int, min2: int, max2: int) -> bool:
    return any([min1 >= min2 and max1 <= max2, min2 >= min1 and max2 <= max1])  

def intersection(min1: int, max1: int, min2: int, max2: int) -> bool:
    return not any([min1 > max2, max1 < min2])
    
puzzle_input = open("data/data4.txt", "r").read().rstrip().split()
pattern = re.compile(r'\d+')
data = [[int(n) for n in re.findall(pattern, line)]
            for line in puzzle_input]

#partie1
nb_pairs: int = 0
for pair in data:
    if inclut(*pair):
        nb_pairs += 1
print(nb_pairs)
 
#partie2
nb_intersection: int = 0
for pair in data:
    if intersection(*pair):
        nb_intersection += 1
print(nb_intersection)
