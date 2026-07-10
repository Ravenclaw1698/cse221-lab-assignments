import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    T = int(input_data[0])
    out = []
    idx = 1
    
    for _ in range(T):
        a = int(input_data[idx])
        n = int(input_data[idx+1])
        m = int(input_data[idx+2])
        idx += 3
        
        a %= m
        if a == 0:
            out.append("0")
            continue
        if a == 1:
            out.append(str(n % m))
            continue
            
        base_X = a
        base_Y = a
        res_X = 1
        res_Y = 0
        
        while n > 0:
            if n & 1:
                res_Y = (res_X * base_Y + res_Y) % m
                res_X = (res_X * base_X) % m
            base_Y = (base_X * base_Y + base_Y) % m
            base_X = (base_X * base_X) % m
            n >>= 1
            
        out.append(str(res_Y))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()