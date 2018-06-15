list=[5,9,3,1,2,8,4,7,6]
count=0
loops=int(len(list)/2)
print(loops)

for i in range(1,loops+1):
    print("Pair of %d" %(i*2))
    for j in range(0, len(list) - 1, i*2):


for i in range(0,len(list)-1,2):
    if list[i]>list[i+1]:
        temp=list[i]
        list[i]=list[i+1]
        list[i+1]=temp
print("HEAP-1: {}".format(list))
