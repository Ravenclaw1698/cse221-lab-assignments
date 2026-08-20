import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    words = [w.decode() for w in data[1:1+n]]

    letters = set()
    for w in words:
        letters.update(w)

    adj = {c: set() for c in letters}
    indeg = {c: 0 for c in letters}

    valid = True
    for i in range(n - 1):
        w1 = words[i]
        w2 = words[i + 1]
        min_len = min(len(w1), len(w2))
        found = False
        for j in range(min_len):
            if w1[j] != w2[j]:
                a, b = w1[j], w2[j]
                if b not in adj[a]:
                    adj[a].add(b)
                    indeg[b] += 1
                found = True
                break
        if not found:
            if len(w1) > len(w2):
                valid = False
                break

    if not valid:
        print(-1)
        return

    heap = [c for c in letters if indeg[c] == 0]
    heapq.heapify(heap)
    order = []
    while heap:
        c = heapq.heappop(heap)
        order.append(c)
        for nxt in adj[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                heapq.heappush(heap, nxt)

    if len(order) != len(letters):
        print(-1)
    else:
        print(''.join(order))

main()