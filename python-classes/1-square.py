#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """Initialize the square with a given size.
        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
