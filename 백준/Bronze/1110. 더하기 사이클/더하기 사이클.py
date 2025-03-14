n = int(input())
cycle = 0

left = n // 10
right = n % 10
new = right * 10 + ((left + right) % 10)
cycle += 1

while n != new:
    left = new // 10
    right = new % 10
    new = right * 10 + ((left + right) % 10)
    cycle += 1

print(cycle)