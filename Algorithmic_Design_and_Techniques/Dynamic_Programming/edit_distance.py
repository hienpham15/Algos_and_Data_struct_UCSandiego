# python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)
    
    d = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, n+1):
        d[0][i] = i
    
    for j in range(1, m+1):
        d[j][0] = j
    
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = d[j][i-1] + 1
            deletion = d[j-1][i] + 1
            mismatch = d[j-1][i-1] + 1
            match = d[j-1][i-1]
            if s[i-1] == t[j-1]:
                d[j][i] = min(insertion, deletion, match)
            else:
                d[j][i] = min(insertion, deletion, mismatch)
    return d[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))