list=[]
k=0
with open('dataset_3363_4.txt',encoding='utf-8') as file:
    tmp=file.readline().strip()
    while tmp:
        list+=tmp.split()
        tmp = file.readline().strip()
        k+=1
print(list)
res=[0]*(k+1)
med=[0]*3
n=0
for j in range(k):
    for i in list[j].split(';'):
        if (i.isdigit()) and (n==0):
            res[j]+=int(i)
            med[0]+=int(i)
            n+=1
            continue
        if (i.isdigit()) and (n==1):
            res[j]+=int(i)
            med[1]+=int(i)
            n+=1
            continue
        if (i.isdigit()) and (n==2):
            res[j]+=int(i)
            med[2]+=int(i)
            n=0
            continue
    res[j]/=3
    print(round(res[j],9))
    last=''
for i in range(3):
    med[i]/=k
    last+=str(round(med[i],9))+' '
print(last)
with open('dataset_3363_4.txt','w') as file:
    for i in range(k):
        file.write(str(round(res[i],9)))
        file.write('\n')
    file.write(last)

