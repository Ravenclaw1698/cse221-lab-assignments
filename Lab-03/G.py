import sys

def solve():
    sys.setrecursionlimit(2005)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    inorder = input_data[1:n+1]
    preorder = input_data[n+1:2*n+1]
    
    inorder_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0
    postorder = []
    
    def build(in_left, in_right):
        nonlocal pre_idx
        if in_left > in_right:
            return
            
        root_val = preorder[pre_idx]
        pre_idx += 1
        mid = inorder_map[root_val]
        
        build(in_left, mid - 1)
        build(mid + 1, in_right)
        postorder.append(root_val)
        
    build(0, n - 1)
    print(" ".join(postorder))

if __name__ == '__main__':
    solve()