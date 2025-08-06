n = int(input())
it, ix, iy = 0, 0, 0
possible = True

for _ in range(n):
    t, x, y = map(int, input().split())
    dur = t - it
    x_time = abs(x - ix)
    y_time = abs(y - iy)
    rem_time = dur - x_time - y_time

    if rem_time >= 0 and rem_time % 2 == 0:
        it, ix, iy = t, x, y
    else:
        possible = False
        break

print(["No", "Yes"][possible])