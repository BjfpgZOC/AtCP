s = input()
t = []

prev_char = "#"

for char in s:
    if char == "#":
        t.append(char)
    else:
        if prev_char == "#":
            t.append("o")
        else:
            t.append(char)
    
    prev_char = char

print("".join(t))