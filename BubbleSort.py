import random
import statistics
from timeit import default_timer as timer

amount = 1280

ordered = list(range(amount))

mean = []

def average():
    c = 0
    while 10 > c:
        unordered = list(range(amount))
        random.shuffle(unordered)
        mean.insert(c, sort(unordered))
        c += 1    
    return sum(mean) / len(mean)

def stdev():
    x = (statistics.stdev(mean))
    y = round(x, 2)
    return y

def sort(list):
    comparisons = 0
    i = 0
    start = timer()
    while i < len(list):
        if i + 1 == len(list):
            i = 0
        if list[i] > list[i + 1]:
            comparisons += 1
        if list[i] > list[i + 1]:
            swap(list, i, i+1)
            comparisons += 1
        i += 1
        if list == ordered:
            break
    end = timer()
    print(end - start)
    return comparisons

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

print("Mean = " + str(average()))
print("std = "  + str(stdev()))