try: 
    import sys
    filename = sys.argv[1]

    err_string = "incorrect/invalid information formatting"

    with open(filename, "r") as fs:
        info = fs.read().split("\n")[:2]
        try:
            adm, ques = [i.split("#")[1] for i in info]
            adm, ques = [i.strip() for i in (adm, ques)]
            
            # what 0 regex knowledge does to a mf:-
            correct_format = adm.isdigit()\
                and ques[0].upper() == "Q"\
                and ques[1] in ["1","2","3","4"]\
                and all([i.startswith("#") for i in info])
            if correct_format:
                print(f"{ques}_{adm}")
            else:
                print(err_string)
        except:
            print(err_string)
except:
    print("an error occurred in get_info.py")