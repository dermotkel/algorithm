# https://www.pythoncentral.io/selection-sort-implementation-guide/
import time
def selectionSort(alist):

   for i in range(len(alist)):

      # Find the minimum element in remaining
       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
                
       # Swap the found minimum element with minPosition       
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist


x = [3,4,7,4,2,1,6,3,7,4,3]

print(selectionSort(x))

