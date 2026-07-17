import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    u = [int(data[idx + i]) for i in range(m)]
    idx += m
    v = [int(data[idx + i]) for i in range(m)]
    idx += m
    w = [int(data[idx + i]) for i in range(m)]
    idx += m

    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[u[i]].append((v[i], w[i]))

    out_lines = []
    for node in range(1, n + 1):
        edges_str = ' '.join(f'({t},{wt})' for t, wt in adj[node])
        if edges_str:
            out_lines.append(f'{node}: {edges_str}')
        else:
            out_lines.append(f'{node}:')

    print('\n'.join(out_lines))

if __name__ == "__main__":
    main()