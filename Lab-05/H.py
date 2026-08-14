import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    r = int(data[idx]); idx += 1
    h = int(data[idx]); idx += 1

    grid = []
    for i in range(r):
        grid.append(data[idx].decode()); idx += 1

    visited = [[False] * h for _ in range(r)]
    best = 0

    for i in range(r):
        for j in range(h):
            if grid[i][j] != '#' and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                count = 0
                while q:
                    x, y = q.popleft()
                    if grid[x][y] == 'D':
                        count += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < r and 0 <= ny < h and not visited[nx][ny] and grid[nx][ny] != '#':
                            visited[nx][ny] = True
                            q.append((nx, ny))
                best = max(best, count)

    print(best)

main()