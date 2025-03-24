import sys

n = int(sys.stdin.readline())

for _ in range(n):
    dress = {}
    c = int(sys.stdin.readline())
    for _ in range(c):
        i, k = sys.stdin.readline().split()
        if k in dress:
            dress[k].append(i)
        else:
            dress[k] = [i]

    if len(dress.keys()) == 1:
            print(c)
    else:
        count = 1
        for key in dress:
            count *= (len(dress[key]) + 1)
        print(count - 1)