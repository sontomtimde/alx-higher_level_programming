def multiply_list_map(my_list=[], number=0):
    try:
        return list(map(lambda i: i * number, filter(lambda x: isinstance(x, (int, float)), my_list)))
    except TypeError:
        print("Error: Non-numeric elements found in the list.")
        return []
