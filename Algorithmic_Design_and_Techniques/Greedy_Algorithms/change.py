# python3
import sys

def get_change(m):
    #if m < 5:
    #    return m
    #if 5 <= m < 10:
    #    return 1 + m -5
        
    count_10, rem_10 = divmod(m, 10)
    count_5, rem_5 = divmod(rem_10, 5)
    
    count = count_10 + count_5 + rem_5
    return count


ans = get_change(9)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))