n, total = map(int, input().split())
a, b, c = -1, -1, -1

for i in range(0, n + 1):
    for j in range(n + 1 - i):
        k = n - i - j
        if (((i * 10000) + (j * 5000) + (k * 1000)) == total) and k >= 0:
            a, b, c = i, j, k

print(str(a) + " " + str(b) + " " + str(c))
