# python3

import sys

def partition3(A, n):
    W = sum(A)//3
    count = 0
    if n < 3:
        return 0
    if sum(A)%3 != 0:
        return 0
    
    value = [[0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, W+1):
            value[i][j] = value[i-1][j]
            if j >= A[i-1]:
                new_value = value[i-1][j - A[i-1]] + A[i-1]
                value[i][j] = max(new_value, value[i][j])
                
            if value[i][j] == W:
                count += 1
    
    if count < 3:
        return 0
    else:
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A, n))
