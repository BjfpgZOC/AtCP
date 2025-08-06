n = int(input())
a = list(map(int, input().split()))

store = {}
count = 0

for j, a_j in enumerate(a):
    count += store.get(j - a_j, 0)
    store[j + a_j] = store.get(j + a_j, 0) + 1

print(count)