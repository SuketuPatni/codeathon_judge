def if_square_root(n):
    result = 0
    if n < 0:
        result = (False, -1)
    elif n == 0:
        result = (True, 0)
    else:
        i = int(n ** 0.5) - 1
        while True:
            if i * i == n:
                result = (True, i)
                break
            if i * i > n:
                result = (False, -1)
                break
            i += 1

    return result

def mode(l):
    max_freq = 1
    for i in l:
        _ = l.count(i)
        if _ > max_freq:
            max_freq = _
    return max_freq

for i in range(int(input())):
    first_row = [int(i) for i in input().split()]
    second_row = [int(i) for i in input().split()]
    third_row = [int(i) for i in input().split()]
    possibles = []

    # AP
    if not (first_row[0] + third_row[2]) % 2:
        possibles.append((first_row[0] + third_row[2])//2)

    if not (first_row[1] + third_row[1]) % 2:
        possibles.append((first_row[1] + third_row[1])//2)

    if not (first_row[2] + third_row[0]) % 2:
        possibles.append((first_row[2] + third_row[0])//2)

    if not (second_row[0] + second_row[1]) % 2:
        possibles.append((second_row[0] + second_row[1])//2)

    # GP
    temp1 = if_square_root((first_row[0] * third_row[2]))
    temp2 = if_square_root((first_row[1] * third_row[1]))
    temp3 = if_square_root((first_row[2] * third_row[0]))
    temp4 = if_square_root((second_row[0] * second_row[1]))

    if temp1[0]:
        possibles.append(temp1[1])
    if temp2[0]:
        possibles.append(temp2[1])
    if temp3[0]:
        possibles.append(temp3[1])
    if temp4[0]:
        possibles.append(temp4[1])

    print(mode(possibles))

    

    

    
    
    
