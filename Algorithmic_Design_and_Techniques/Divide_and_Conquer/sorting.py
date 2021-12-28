# python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    m1, m2 = l, l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            a[m2+1], a[i] = a[i], a[m2+1]
            a[m2+1], a[m1] = a[m1], a[m2+1]
            m1 += 1
            m2 += 1
        elif a[i] == x:
            a[m2+1], a[i] = a[i], a[m2+1]
            m2 += 1         
    return m1, m2

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    #k = 0
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);

#a = [5, 2, 7, 6, 1, 4, 5, 5]
#randomized_quick_sort(a, 0, len(a) - 1)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')