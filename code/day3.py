data = open("data/data3.txt", "r").read().rstrip().split()


        
def toPriority(elem):
    num=ord(elem)
    if num<123 and num >96:
        num=num-96
    elif num<91 and num >64 :
        num=num-64+26
    return num

sum=0
for i in range(0,len(data),3):
    line1,line2,line3=set(data[i]),set(data[i+1]),set(data[i+2])
    for item in (line1 & line2 & line3):
        print(item)
        print(toPriority(item))
        sum+=toPriority(item)
    print(sum)

print(sum)
