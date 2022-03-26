import random as rng

with open("input_2_2.txt", "w+") as fs:
    for i in range(200):
        N = rng.randint(3, 7)
        fs.write(str(N)+"\n")
        for i in range(N):
            point = (
                rng.randint(-50, 50),
                rng.randint(-50, 50),
                rng.randint(-50, 50)
            )
            fs.write(str(point) + "\n")
