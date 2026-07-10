import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    vals = set(a)
    for x in a:
        vals.add(x * x)
        
    sorted_vals = sorted(list(vals))
    val_to_rank = {val: i + 1 for i, val in enumerate(sorted_vals)}
    
    max_rank = len(sorted_vals)
    bit = [0] * (max_rank + 1)
    
    def add(idx, delta):
        while idx <= max_rank:
            bit[idx] += delta
            idx += idx & (-idx)
            
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s
        
    ans = 0
    for i in range(n):
        target_rank = val_to_rank[a[i] * a[i]]
        ans += i - query(target_rank)
        add(val_to_rank[a[i]], 1)
        
    print(ans)

if __name__ == '__main__':
    solve()