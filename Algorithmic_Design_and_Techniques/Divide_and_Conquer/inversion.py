# python3
import sys

def merge(first, second):
    n = len(first)
    m = len(second)
    inv_count = 0
    res = []
    
    i, j = 0, 0
    while i < n and j < m:
        if first[i] <= second[j]:
            res.append(first[i])
            i += 1
        else:
            res.append(second[j])
            j += 1
            inv_count += len(first[i:])
    
    if i == n:
        res += second[j:]
    else:
        res += first[i:]
        
    return res, inv_count
            
    
    
def get_number_of_inversions(array, begin, end):
    if len(array[begin:end]) <= 1:
        return array[begin:end], 0
    
    middle = (begin + end)//2
    
    first_half, first_count = get_number_of_inversions(array, begin, middle)
    second_half, second_count = get_number_of_inversions(array, middle, end)
    
    result, inv_count = merge(first_half, second_half)
    total_inv = first_count + second_count + inv_count
    return result, total_inv

#array = [2, 3, 9, 2, 8, 10]
#ans = get_number_of_inversions(array, 0, len(array))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, 0, len(a))[1])
