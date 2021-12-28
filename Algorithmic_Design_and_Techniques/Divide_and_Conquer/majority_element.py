# python3
import sys


def is_majority(x, arr):
    mid = len(arr)//2
    if len(arr) <= 3:
        count = 0
        for i in range(len(arr)):
            if arr[i] == x:
                count += 1
        if count > 1:
            return True
        else:
            return False
        
    left = is_majority(x, arr[:mid])
    right = is_majority(x, arr[mid:])
    return  (left and right)
    

def get_majority_element(a, n):
    #for x in a:
    #    if is_majority(x, a):
    #        return 1
    d = dict()
    
    for ele in a:
        if ele not in d:
            d[ele] = 1
        else:
            d[ele] += 1
    
    for ele in d.keys():
        if d[ele] > n/2:
            return 1
    
    return 0

#arr = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
#arr = [2, 3, 9, 2, 2]
#n = len(arr) 
#ans = get_majority_element(arr, n)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #print(a)
    ans =  get_majority_element(a, n) 
    print(ans)
    