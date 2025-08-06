s = input()
t = set(input())
val = True

for i in range(len(s)):
    if i == 0:
        continue
    if s[i].isupper():
        if s[i - 1] not in t:
            val = False
            break

print(["No", "Yes"][val])