def insertion_sort(array):
    for i in range(1,len(array)):
        cv=array[i]
        cp=i
        while cp>0 and array[cp-1]>cv:
            array[cp]=array[cp-1]
            cp=cp-1
            array[cp]=cv