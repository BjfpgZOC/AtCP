n, a, b = map(int, input().split())
total = 0

for i in range(1, n+1):
    s = str(i)
    intsum = 0
    for j in s:
        intsum += int(j)

    if intsum >= a and intsum <= b:
        total += i

print(total)
    