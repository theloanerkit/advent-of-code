def read(year, day, fmt):
    f = open(f"{year}/{day}.txt","r")
    if fmt == "str":
        data = f.read()
    elif fmt == "list":
        data = f.readlines()
    f.close()
    return data