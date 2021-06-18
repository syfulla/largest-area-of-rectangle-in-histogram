def algo_histogram(ls:list[int]):
    n=len(ls)
    ma=0
    for i in range(n):
        for j in range(i,n):
            h=min(ls[i:j+1])
            w=j-i+1
            ma=max(ma,h*w)
    return ma
ls=[int(x) for x in input().split()]
print(algo_histogram(ls))
