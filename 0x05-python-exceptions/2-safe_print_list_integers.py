#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    if my_list is None:
        my_list = []

        count = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print(f"{my_list[i]}", end="")
                count += 1

                print()  # Add a new line after printing integers
                return count
