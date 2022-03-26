try:
    
    import sys
    filename = sys.argv[1]

    with open(filename, "r+") as fs:
        contents = fs.read()
        indented = "\n\t".join(contents.split("\n"))
        main_str = f"try: \n\t{indented}\nexcept: \n\tprint('an error occured in {filename}')"
        fs.seek(0)
        fs.truncate()
        fs.write(main_str)

except:
    print("an error occurred")