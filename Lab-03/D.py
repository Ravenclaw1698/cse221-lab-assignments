import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    T = int(input_data[0])
    idx = 1
    
    MOD = 1000000007
    out = []
    
    for _ in range(T):
        a11 = int(input_data[idx])
        a12 = int(input_data[idx+1])
        a21 = int(input_data[idx+2])
        a22 = int(input_data[idx+3])
        X = int(input_data[idx+4])
        idx += 5
        
        r11, r12, r21, r22 = 1, 0, 0, 1
        
        while X > 0:
            if X & 1:
                n_r11 = (r11 * a11 + r12 * a21) % MOD
                n_r12 = (r11 * a12 + r12 * a22) % MOD
                n_r21 = (r21 * a11 + r22 * a21) % MOD
                n_r22 = (r21 * a12 + r22 * a22) % MOD
                r11, r12, r21, r22 = n_r11, n_r12, n_r21, n_r22
            
            n_a11 = (a11 * a11 + a12 * a21) % MOD
            n_a12 = (a11 * a12 + a12 * a22) % MOD
            n_a21 = (a21 * a11 + a22 * a21) % MOD
            n_a22 = (a21 * a12 + a22 * a22) % MOD
            a11, a12, a21, a22 = n_a11, n_a12, n_a21, n_a22
            
            X >>= 1
            
        out.append(f"{r11} {r12}\n{r21} {r22}")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()