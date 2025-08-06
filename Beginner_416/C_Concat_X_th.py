from itertools import product

n, k, x = map(int, input().split())
s = []
all_cs = []

for _ in range(n):
    s.append(input())

for i in product(range(n), repeat = k):
    cs = ""
    for j in i:
        cs += s[j]
    
    all_cs.append(cs)

all_cs.sort()
print(all_cs[x - 1])