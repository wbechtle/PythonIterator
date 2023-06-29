#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 4/11/2023
#Project: Fibonacci Sequence Class.
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Create a class that generates the Fibonacci sequence of numbers (0, 1, 1, 2, 3, 5, 8....) 
#such that each number is the sum of the preceding two numbers. Your class should not print 
#out any values, but should implement the iterator functions __iter__(),  __next__() and 
#StopIteration exception. (Your class needs to generate the values, not have them literally 
#stored.)"
#--------------------------------------------------------------------------------------------
class Fibonacci_Sequence:

    def __init__(self, sequence_limit):

        self.sequence_limit = sequence_limit
        self.iterations = 0

    def __iter__(self):

        self.number_one = 0
        self.number_two = 1
        self.number_to_return = 0

        return self

    def __next__(self):

        self.iterations += 1

        if self.iterations <= self.sequence_limit:

            self.number_to_return = self.number_one
            self.number_one, self.number_two = self.number_two, self.number_one + self.number_two

            return self.number_to_return

        else:

            raise StopIteration
