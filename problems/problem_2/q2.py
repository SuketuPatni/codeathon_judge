import itertools

ORIGIN = (0,0,0)

def find_distance(tuple1, tuple2):
    return (
        (tuple1[0] - tuple2[0]) ** 2 +\
        (tuple1[1] - tuple2[1]) ** 2 +\
        (tuple1[2] - tuple2[2]) ** 2
    ) ** 0.5

for _ in range(int(input())):
    N = int(input())
    point_list = [] # 3-length tuples list
    for _ in range(N):
        point_list.append(eval(input()))
    
    distance_list = []
    for i in itertools.permutations(point_list):
        distance = find_distance(ORIGIN, i[0]) + find_distance(ORIGIN, i[-1])
        for j in range(len(i) - 1):
            distance += find_distance(i[j], i[j + 1])
        distance_list.append(distance)

    print("{:.3f}".format(min(distance_list)))
