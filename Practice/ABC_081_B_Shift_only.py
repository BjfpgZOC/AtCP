n = int(input())
nums = list(map(int, input().split()))
count = 0

while all(num % 2 == 0 for num in nums):
    count += 1
    nums = [num // 2 for num in nums]

print(count)