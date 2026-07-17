import sys
import math

def main():
    # Read all input from standard input
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1

    # Precompute the coprime graph
    # graph[i] will store the sorted list of neighbors for node i
    graph = [[] for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and math.gcd(i, j) == 1:
                graph[i].append(j)

    # Process each query
    results = []
    for _ in range(Q):
        X = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1
        
        # Check if there are at least K neighbors
        if K <= len(graph[X]):
            # K is 1-indexed, so we access K - 1
            results.append(str(graph[X][K - 1]))
        else:
            results.append("-1")

    # Fast output
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()