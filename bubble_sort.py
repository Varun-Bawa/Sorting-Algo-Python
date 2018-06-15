
#This is modified version of bubble sort and it decreases the number of loops and the time consumption for execution
#Can check this by executing both codes with time functions

def bubbleSort_custom(list,swaps,count):
    for i in range(len(list)-1, 0, -1):
        swaps_loc=swaps
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                swaps+=1
            count += 1
        count+=1
        if swaps_loc == swaps:
            break
    print("Swaps=%d , Total loops=%d" % (swaps, count))

list=[5,9,3,1,2,8,4,7,6]
count=0
swaps=0
bubbleSort_custom(list,swaps,count)
print(list)



#This is the generic bubble sort algorithm with higher time consumption
def bubbleSort(alist,aswaps,acount):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                aswaps+=1
            acount+=1
    print("ASwaps=%d , Total Aloops=%d" % (aswaps, acount))

aswaps=0
acount=0
alist=[5,9,3,1,2,8,4,7,6]
bubbleSort(alist,aswaps,acount)
print(alist)