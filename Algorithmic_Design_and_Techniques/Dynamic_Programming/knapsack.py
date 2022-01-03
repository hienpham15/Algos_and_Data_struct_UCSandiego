# python3
import sys

def optimal_weight(W, golds):
    weight = [[0 for _ in range(W+1)] for _ in range(len(golds)+1)]
    
    for i in range(W+1):
        weight[0][i] = 0
    
    for j in range(len(golds)+1):
        weight[j][0] = 0
    
    for j in range(1, len(golds)+1):
        for w_i in range(1, W+1):
            weight[j][w_i] = weight[j-1][w_i]
            if w_i >= golds[j-1]:
                new_weight = weight[j-1][w_i - golds[j-1]] + golds[j-1]
                weight[j][w_i] = max(new_weight, weight[j][w_i])
            
    return weight[len(golds)][W]

#W = 10
#golds = [4, 1, 8]
#ans = optimal_weight(W, golds)
    
if __name__ == '__main__':
    W, n, *w = list(map(int, sys.stdin.read().split()))
    print(optimal_weight(W, w))