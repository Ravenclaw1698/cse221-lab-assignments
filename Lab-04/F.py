import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    x = int(data[1])
    y = int(data[2])

    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1),  (1, 0),  (1, 1)]

    moves = []
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            moves.append((nx, ny))

    moves.sort()

    out = [str(len(moves))]
    for a, b in moves:
        out.append(f"{a} {b}")

    print('\n'.join(out))

if __name__ == "__main__":
    main()