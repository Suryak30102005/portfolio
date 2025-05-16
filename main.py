def arm(n):
    s = str(n)
    p = len(s)
    s1 = 0
    for i in s:
        s1 += int(i) ** p
    return s1 == n

a = int(input())
b = int(input())
a1 = []
for j in range(a, b + 1):
    if arm(j):
        a1.append(j)
print(a1)