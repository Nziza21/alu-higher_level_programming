#!/usr/bin/python3
"""Module that defines MyList class"""

class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
