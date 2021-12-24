# python3


n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

a_s = sorted(a)

result = a_s[-1] * a_s[-2]

print(result)