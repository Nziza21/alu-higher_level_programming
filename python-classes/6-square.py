#!/usr/bin/python3
"""Defines a class Square with size, position, area computation,
and printing."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
