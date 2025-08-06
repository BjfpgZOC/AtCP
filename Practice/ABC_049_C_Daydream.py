s = input()
i = len(s)
possible = True

while i:
    if s[i-7 : i] == "dreamer":
        i -= 7
    elif s[i-6 : i] == "eraser":
        i -= 6
    elif s[i-5 : i] == "dream":
        i -= 5
    elif s[i-5 : i] == "erase":
        i -= 5
    else:
        possible = False
        break

print(["NO", "YES"][possible])