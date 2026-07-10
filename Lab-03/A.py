import sys

def merge(a, b):
    res = []
    i = 0
    j = 0
    inv = 0
    la = len(a)
    lb = len(b)
    
    while i < la and j < lb:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            inv += la - i
            j += 1
            
    res.extend(a[i:])
    res.extend(b[j:])
    return res, inv

def merge_divide(arr):
    if len(arr) <= 1:
        return arr, 0
        
    mid = len(arr) // 2
    a1, inv1 = merge_divide(arr[:mid])
    a2, inv2 = merge_divide(arr[mid:])
    
    merged, inv3 = merge(a1, a2)
    
    return merged, inv1 + inv2 + inv3

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    
    ordered_arr, total_inv = merge_divide(arr)
    
    sys.stdout.write(str(total_inv) + "\n")
    sys.stdout.write(" ".join(str(x) for x in ordered_arr) + "\n")

if __name__ == '__main__':
    solve()