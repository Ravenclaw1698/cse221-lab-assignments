import sys

def solve():
    sys.setrecursionlimit(2005)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    inorder = input_data[1:n+1]
    postorder = input_data[n+1:2*n+1]
    
    inorder_map = {val: i for i, val in enumerate(inorder)}
    preorder = []
    
    def build(in_left, in_right, post_left, post_right):
        if in_left > in_right:
            return
            
        root_val = postorder[post_right]
        preorder.append(root_val)
        
        mid = inorder_map[root_val]
        left_size = mid - in_left
        
        build(in_left, mid - 1, post_left, post_left + left_size - 1)
        build(mid + 1, in_right, post_left + left_size, post_right - 1)
        
    build(0, n - 1, 0, n - 1)
    sys.stdout.write(" ".join(preorder) + "\n")

if __name__ == '__main__':
    solve()