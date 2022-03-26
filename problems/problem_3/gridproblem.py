n=int(input())
h=eval(input())
ans=0
for x in range(1,n+1):
    for y in range(1,n+1):
        for s in range(1,n+1):
            if x+s-1<=n and y+s-1<=n:
                for p in h:
                    if x<=p[0]<=x+s-1 and y<=p[1]<=y+s-1:
                        break
                else:
                    ans+=1
print(ans)