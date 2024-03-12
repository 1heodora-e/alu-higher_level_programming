#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''Square represents an instance of a square shape'''

    def __init__(self, size=0):
        '''Initializes a new square object

           Args:
                size (int): The size of the square.
        '''
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
           Computes the area of the square based on the size.

           Returns:
               The value of the area (int).
        '''
        return self.__size ** 2
