f = open("data/data1.txt", "r")
max1=0
max2=0
max3 = 0
cpt = 0
for line in f:
    if not line.strip():
        if cpt>max3:
            if (cpt>max1):
                max3=max2
                max2=max1
                max1=cpt
            elif cpt>max2:
                max3=max2
                max2=cpt
            else:
                max3=cpt
        cpt=0
    else:
        cpt+= int(line.strip()) 
print("max : "+str(max1+max2+max3))
