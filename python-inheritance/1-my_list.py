#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and adds a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of list that adds a method to print
    the list elements in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
