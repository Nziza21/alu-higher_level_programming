#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line."""
    for i in my_list:
        if type(i) != int:
            raise TypeError("All elements must be integers")
        print("{:d}".format(i))



