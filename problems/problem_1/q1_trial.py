for i in range(int(input())):
    info = input().split("\t")
    m, rc, hc, rp, hp = [int(i) for i in info]

    if hc == 0:
        c = 0
        p = m // rp
    elif hp == 0:
        c = m // rc
        p = 0
    else:
        c = int((hc * (rp + m * hp) - hp * rc)/(2 * hc * hp * rc)) + 1
        p = int((m - c * rc)/rp)
        
    cp = (c, p)
    h = ((1 + c * hc)*(1 + p * hp)) ** 0.5
    print(cp, h, sep="\t")