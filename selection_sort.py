list=[5,9,3,1,2,8,4,7,6]
min = list[0]
index=0
count=0
for i in range(0, len(list)-1):
    min = list[i]
    for j in range(i+1, len(list)):
        if list[j]<min:
            min=list[j]
            index=j
        count+=1
    if min < list[i]:
        temp = list[i]
        list[i] = min
        list[index] = temp
print(count)
print(list)

def selectionSort(alist,counta):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
           counta+=1
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
   print(counta)

alist = [5,9,3,1,2,8,4,7,6]
selectionSort(alist,0)
print(alist)