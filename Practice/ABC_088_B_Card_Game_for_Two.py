n = int(input())
l = list(map(int, input().split()))
l.sort()

alice, bob = 0, 0

while l:
    alice += l[-1]
    l.pop()
    if l:
        bob += l[-1]
        l.pop()

print(alice - bob)
    
