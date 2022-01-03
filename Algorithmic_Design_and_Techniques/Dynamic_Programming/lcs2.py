# python3

import sys

def lcs2(a, b):
    n = len(a)
    m = len(b)
    
    d = [[0 for i in range(n+1)] for j in range(m+1)]
    
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = d[j][i-1] 
            deletion = d[j-1][i] 
            mismatch = d[j-1][i-1] 
            match = d[j-1][i-1] + 1
            if a[i-1] == b[j-1]:
                d[j][i] = max(insertion, deletion, match)
            else:
                d[j][i] = max(insertion, deletion, mismatch)
    return d[m][n]


#a = [2, 7, 8, 3]
#b = [5, 2, 8, 7]

#ans = lcs2(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))