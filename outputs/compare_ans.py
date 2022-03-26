try:
    import sys

    filename = sys.argv[1] # Q5_2000000_3_out.txt
    ques_no = int(filename[1])

    # compare outputs
    with open(f"../model_outputs/output_{ques_no}.txt", "r") as model_o_temp:
        model = model_o_temp.read().strip().split("\n")

    with open(filename, "r") as o_temp:
        output = o_temp.read().strip().split("\n")

    def compare(list1, list2):    
        if list1 == list2:
            print("All tests passed successfully.")
        elif len(list1) != len(list2):
            print("Not all test cases covered")
        else:
            for i in range(0, len(list1), 1):
                if list1[i] != list2[i]:
                    check = False
                    print(f"Difference in output and expected output in test case {i+1}.")
                    print(f"Output: {list1[i]}\nExpected output: {list2[i]}")


    compare(model, output)
except:
    print("an error occurred")