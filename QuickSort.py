import random
import statistics
from timeit import default_timer as timer

amount = 1280

totalComp = []

time = []

mean = []

def quickSort():    
    unordered = list(range(amount))
    random.shuffle(unordered)
    quickSort2(unordered, 0, len(unordered) - 1)
    return sum(totalComp)

def quickSort2(list, low, hi):
    if low < hi:
        p = partition(list, low, hi)
        quickSort2(list, low, p-1)
        quickSort2(list, p+1, hi)

def get_Pivot(list, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if list[low] < list[mid]:
        if list[mid] < list[hi]:
            pivot = mid
    elif list[low] < list[hi]:
        pivot = low
    return pivot

def partition(list, low, hi):
    comparisons = 0
    pivotIndex = get_Pivot(list, low, hi)
    pivotValue = list[pivotIndex]
    swap(list, pivotIndex, low)
    border = low
    for i in range(low, hi + 1):
        if list[i] < pivotValue:
            border += 1
            swap(list, i, border)
            comparisons += 1
    swap(list, low, border)
    comparisons += 1
    totalComp.insert(len(totalComp), comparisons)
    return border

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def average():
    return sum(time) / len(time)

def scoreAvg():
    return sum(mean) / len(mean)

def stdev():
    x = (statistics.stdev(mean))
    y = round(x, 2)
    return y

for i in range(0,10):
    totalComp = []
    start = timer()
    x = quickSort() 
    mean.insert(i, x)
    end = timer()
    dur = end - start
    time.insert(i, dur)

print("mean time = " + str(average()))
print("mean score = " + str(scoreAvg()))
print("stdev = " + str(stdev()))