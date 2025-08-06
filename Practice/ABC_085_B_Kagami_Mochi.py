n = int(input())

mochi = set()

for i in range(n):
    d = int(input())
    if d not in mochi:
        mochi.add(d)

print(len(mochi))