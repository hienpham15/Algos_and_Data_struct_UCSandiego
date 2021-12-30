# Uses python3
import sys

inf = 999999999


def get_change(m):
    coins = [4, 3, 1]
    MinNumCoins = [inf]*(m+1)
    MinNumCoins[0] = 0
    
    for i in range(1, m+1):
        for j in range(len(coins)):
            if i >= coins[j]:
                NumCoins = MinNumCoins[i - coins[j]] + 1
                
                if NumCoins < MinNumCoins[i]:
                    MinNumCoins[i] = NumCoins
    return MinNumCoins[m]
        

#ans = get_change(34)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
