def code(m,c,ca,p,pa):
    d={}
    for i in range(int(m/c)+1):
        j=int((m-(i*c))/p)
        d[(i,j)]=((ca*i+1)*(pa*j+1))**0.5
    h=0
    a=0
    for i,j in d.items():
        if j>h:
            a=i
            h=j     
    return a, h
for i in range(int(input())):
    info = input().split("\t")
    m, c, ca, p, pa = [int(i) for i in info]
    i,j=code(m,c,ca,p,pa)
    print(i, round(j, 3), sep="\t")