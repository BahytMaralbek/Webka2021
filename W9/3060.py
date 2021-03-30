n = int(input())
if n==0:
    print("YES")
    exit()
k = 2
while k != n:
    if k > n:
        print("NO")
        break
    k = k * 2
else:
    print("YES")