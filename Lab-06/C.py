import sys
from collections import deque
from array import array

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    x1 = int(data[1]); y1 = int(data[2]); x2 = int(data[3]); y2 = int(data[4])

    if x1 == x2 and y1 == y2:
        sys.stdout.write("0\n")
        return

    pad = 2
    W = n + 2 * pad
    total = W * W
    dist = array('i', [-2]) * total

    for px in range(pad, pad + n):
        base = px * W
        for py in range(pad, pad + n):
            dist[base + py] = -1

    offsets = [dx * W + dy for dx, dy in ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))]

    start = (x1 - 1 + pad) * W + (y1 - 1 + pad)
    target = (x2 - 1 + pad) * W + (y2 - 1 + pad)

    dist[start] = 0
    q = deque([start])
    while q:
        ci = q.popleft()
        cd = dist[ci]
        if ci == target:
            sys.stdout.write(str(cd) + "\n")
            return
        for off in offsets:
            ni = ci + off
            if dist[ni] == -1:
                dist[ni] = cd + 1
                q.append(ni)

    sys.stdout.write("-1\n")

main()