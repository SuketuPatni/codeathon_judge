def gp(x,y,z):
    return x/y==y/z

def ap(x,y,z):
    return x-y==y-z

def matrix(m,n):
    m[1].insert(1,n)
    ans=0
    for i in m:
        ans+=gp(i[0],i[1],i[2])+ap(i[0],i[1],i[2])
    for i in range(3):
        ans+=ap(m[0][i],m[1][i],m[2][i])+gp(m[0][i],m[1][i],m[2][i])
    ans+=ap(m[0][0],m[1][1],m[2][2])+gp(m[0][0],m[1][1],m[2][2])+ap(m[2][0],m[1][1],m[0][2])+gp(m[2][0],m[1][1],m[0][2])
    m[1].pop(1)
    return ans
Matrix=[[[1,2,3],[4,6],[7,8,9]],[[1,1,1],[1,1],[1,1,1]]] 
d={}
for i in range(1,10):
    d[i]=0
    for j in Matrix:
        d[i]+=matrix(j,i)
a=0
an=0
print(d)
for i,j in d.items():
    if j>a:
        a=j
        an=i
print(an)

