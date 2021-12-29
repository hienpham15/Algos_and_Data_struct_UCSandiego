# python3

import sys


def binary_search(a, x, case):
    left, right = 0, len(a)-1
    # write your code here
    while left <= right:
        mid = (right + left)//2
        if x > a[mid]:
            left = mid + 1
        elif x < a[mid]:
            right = mid - 1
        else:
            while True:
                if mid + 1 < len(a) and a[mid+1] == a[mid]:
                    mid += 1
                else:
                    return mid
    
    if case == 'start':
        return right
    elif case == 'end':
        return left


def look_up(array, lut):
    result = []
    
    for element in array:
        result.append(lut[element])
    return result
        

def fast_count_segments(starts, ends, points):
    cnt = {}
    segments_num = 0

    listpoints = [(x, 'l') for x in starts]
    listpoints += [(x, 'p') for x in points]
    listpoints += [(x, 'r') for x in ends]

    listpoints.sort()

    for p in listpoints:
        if p[1] == 'l':
            segments_num += 1
        elif p[1] == 'r':
            segments_num -= 1
        else:
            cnt[p[0]] = segments_num

    return [cnt[x] for x in points]

#starts = [0, -3, 7]
#ends = [5, 2, 10]
#points = [6, 1]
#ans = fast_count_segments(starts, ends, points)


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')