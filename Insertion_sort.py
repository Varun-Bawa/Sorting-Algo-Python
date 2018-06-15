list=[5,9,3,1,2,8,4,7,6]
count=0

for i in range(1, len(list)):
    #num=list[i]
    cur=list[i]
    index=i
    while index>0 and cur<list[index-1]:
        list[index]=list[index-1]
        index-=1
    list[index]=cur
    count+=1
print(list)