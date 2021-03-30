def x_or(x,y):
    if x==1 and y!=1:
        return 1
    if x!=1 and y==1:
        return 1
    else:
        return 0
a = list(map(int,input().split()))
print(x_or(a[0],a[1]))
