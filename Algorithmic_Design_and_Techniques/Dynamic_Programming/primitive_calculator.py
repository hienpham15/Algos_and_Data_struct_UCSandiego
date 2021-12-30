# python3

import sys

"""
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n%3 != 0:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n - 1
    return reversed(sequence)
"""
inf = 999999999999

def optimal_sequence(n):
    sequence = []
    count = [inf] * (n+1)
    parents = [0]* (n+1)
    count[0] = 0
    count[1] = 0
    
    for i in range(2, n+1):
        if i%2 != 0 and i%3 != 0:
            count[i] = count[i-1] + 1
            parents[i] = i - 1
            
        elif i%2 == 0 and i%3 != 0:
            min_ops = min(count[i-1], count[i//2])
            count[i] = min_ops + 1
            parents[i] = i//2 if min_ops == count[i//2] else i - 1
            
        elif i%3 == 0 and i%2 != 0:
            min_ops = min(count[i-1], count[i//3])
            count[i] = min_ops + 1
            parents[i] = i//3 if min_ops == count[i//3] else i - 1
            
        elif i%2 == 0 and i%3 == 0:
            min_ops = min(count[i-1], count[i//2], count[i//3])
            count[i] = min_ops + 1
            if min_ops == count[i//3]:
                parents[i] = i//3
            elif min_ops == count[i//2]:
                parents[i] = i//2
            else:
                parents[i] = i - 1
    
    k = n
    while k > 0:
        sequence.append(k)
        k = parents[k]
    
    return sequence
    
#seq = optimal_sequence(96234)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
