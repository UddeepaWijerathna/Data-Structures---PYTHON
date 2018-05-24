def selectionSort(lst):
    for j in range(0,len(lst)):
        max=0
        for i in range (1,len(lst)-j):
            if lst[i]>lst[max]:
                max=i
            lst[max],lst[len(lst)-1-j]=lst[len(lst)-1-j],lst[max]


    return lst
print(selectionSort([3 , 6 ,23 ,1 ,89,45, 67]))
            
            
    
