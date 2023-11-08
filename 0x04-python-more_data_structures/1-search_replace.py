#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if search in my_list:
        return [replace if num == search else num for num in my_list]
    else:
        print(f"{search} not found in the list.")
        return my_list
