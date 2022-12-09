f = open("data/data2.txt", "r")

sum = 0
for line in f:
    adversaire,moi = line.strip().split(' ')
    #calcul de mon elemnt
    if moi=='X':
        if adversaire=='A':
            moi='C'
        elif adversaire=='B':
            moi='A'
        elif adversaire=='C':
            moi='B'
    elif moi=='Y':
        moi = adversaire
    elif moi=='Z':
        if adversaire=='A':
            moi='B'
        elif adversaire=='B':
            moi='C'
        elif adversaire=='C':
            moi='A'
    #calcul du score
    if moi=="A" :
        sum+=1
    elif moi=="B":
        sum+=2
    else:
        sum+=3
    if (moi=='A' and adversaire=='A'):
        sum+=3
    elif (moi=='B' and adversaire=='B'):
        sum+=3
    elif (moi=='C' and adversaire=='C'):
        sum+=3
    elif (moi=='A' and adversaire=='C'):
        sum+=6
    elif (moi=='B' and adversaire=='A'):
        sum+=6
    elif (moi=='C' and adversaire=='B'):
        sum+=6
print(sum)
