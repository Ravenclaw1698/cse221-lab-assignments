import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    positions = []
    pos_set = set()
    for _ in range(k):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        positions.append((x, y))
        pos_set.add((x, y))

    offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
               (2, 1), (2, -1), (-2, 1), (-2, -1)]

    for x, y in positions:
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if (nx, ny) in pos_set:
                print("YES")
                return

    print("NO")

if __name__ == "__main__":
    main()