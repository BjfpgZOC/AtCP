s = str(input())

ind = [i for i, c in enumerate(s) if c == 't']
fr = 0.0
l = len(ind)


for i in range(l):
    for j in range(i + 1, l):
        sub_in_l = ind[j] - ind[i] - 1
        if sub_in_l >= 1:
            fr = max(fr, (j - i - 1)/(sub_in_l))
print(f'{fr:.17f}')