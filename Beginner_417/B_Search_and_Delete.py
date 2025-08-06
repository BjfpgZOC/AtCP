n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

i = 0
while i < len(b) and a and b[i] <= a[-1]:
    if b[i] in a:
        a.remove(b[i])
    i += 1

print(" ".join(map(str, a)))
