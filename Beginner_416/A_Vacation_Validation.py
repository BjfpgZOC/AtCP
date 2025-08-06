n, l, r = map(int, input().split())
s = input()

possible = True

for i in range(l - 1, r):
    if s[i] != "o":
        possible = False
        break

print(["No", "Yes"][possible])
