import bisect

n, q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
flavours = A[:]

for i in range(1, n):
    A[i] += A[i - 1]

max_flav = flavours[-1]

for _ in range(q):
    b = int(input())
    if b == 1:
        print(1)
        continue
    if b > max_flav:
        print(-1)
        continue
    
    t = b - 1
    k = bisect.bisect_right(flavours, t)
    s_l = A[k-1] if k else 0
    s_r = (n - k) * t

    print(s_l + s_r + 1)