n = int(input())
count = 0

for _ in range(n):
    a, b = map(int, input().split())
    count = count + 1 if b > a else count

print(count)