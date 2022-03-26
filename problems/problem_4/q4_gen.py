from random import randint as rng

T = 10

with open("input_4_2.txt", "w+") as fs:
    fs.write(str(T) + "\n")
    for i in range(T):
        fs.write("{} {} {}\n{} {}\n{} {} {}\n".format(
            rng(-100, 100), 
            rng(-100, 100), 
            rng(-100, 100), 
            rng(-100, 100), 
            rng(-100, 100), 
            rng(-100, 100), 
            rng(-100, 100), 
            rng(-100, 100), 
        ))
