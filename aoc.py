def read(year, day, fmt):
    """reads input file

    Args:
        year (str): advent of code year
        day (str): day of advent of code
        fmt (str): either "str" or "list", formats the data

    Returns:
        (str) or (list): returns the data in the format specified
    """
    f = open(f"{year}/{day}.txt","r")
    if fmt == "str":
        data = f.read()
    elif fmt == "list":
        data = f.readlines()
    f.close()
    if fmt == "list":
        for i in range(len(data)):
            data[i] = data[i].replace("\n","")
    return data

def get_smallest(arr, n=1):
    small = []
    for i in range(n):
        small.append(min(arr))
        arr.remove(min(arr))
    return small

def str_to_list(string, sep, elem_type="str"):
    arr = string.split(sep)
    if elem_type == "int":
        for i in range(len(arr)):
            arr[i] = int(arr[i])
    return arr