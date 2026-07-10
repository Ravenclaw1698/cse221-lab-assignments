import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = input_data[1:]
    
    stack = [(0, n - 1)]
    res = []
    
    while stack:
        left, right = stack.pop()
        if left > right:
            continue
        
        mid = (left + right) // 2
        res.append(a[mid])
        
        stack.append((mid + 1, right))
        stack.append((left, mid - 1))
        
    sys.stdout.write(" ".join(res) + "\n")

if __name__ == '__main__':
    solve()