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
    """gets the smallest n elements in a list

    Args:
        arr (list): list to search
        n (int, optional): number of elements to look for. Defaults to 1.

    Returns:
        (list): list containing the smallest n elements of the list
    """
    small = []
    for i in range(n):
        small.append(min(arr))
        arr.remove(min(arr))
    return small

def str_to_list(string, sep, elem_type="str"):
    """converts a string to a list

    Args:
        string (str): string to be converted to a list
        sep (str): separator to split the string at
        elem_type (str, optional): type of the elements in the resulting list. Defaults to "str".

    Returns:
        (list): list of elements from the original string
    """
    arr = string.split(sep)
    if elem_type == "int":
        for i in range(len(arr)):
            arr[i] = int(arr[i])
    return arr