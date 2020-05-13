import random
import statistics
from timeit import default_timer as timer

amount = 1280

mean = []

def average():
    c = 0
    while 10 > c:
        unordered = list(range(amount))
        random.shuffle(unordered)
        mean.insert(c, insertionSort(unordered))
        c += 1
    return sum(mean) / len(mean)

def stdev():
    x = (statistics.stdev(mean))
    y = round(x, 2)
    return y

def insertionSort(list):
    comparisons = 0
    start = timer()
    for i in range(1, len(list)):
        j = i-1
        while list[j] > list[j+1] and j >= 0:
            swap(list, j, j+1)
            comparisons += 1
            j -= 1
    end = timer()
    print(end - start)
    return comparisons    

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


print("mean = " + str(average()))
print("std = "  + str(stdev()))
