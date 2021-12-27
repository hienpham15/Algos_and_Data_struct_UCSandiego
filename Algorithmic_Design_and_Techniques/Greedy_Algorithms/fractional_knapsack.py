# python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    
    lut = dict()
    for i in range(len(values)):
        lut[values[i]/weights[i]] = weights[i]

    val_per_weight = dict(reversed(sorted(lut.items())))
    vpw_list = list(val_per_weight.keys())
    i = 0
    
    while capacity > 0 and i < len(vpw_list):
        weight = val_per_weight[vpw_list[i]]
        
        if weight > capacity:
            value += vpw_list[i]*capacity
            capacity = 0
        else:
            value += vpw_list[i] * weight
            capacity -= weight
            i += 1

    return value


#capacity = 50
#weights = [40, 50, 30]
#values = [60, 100, 120]
#ans = get_optimal_value(capacity, weights, values)



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))