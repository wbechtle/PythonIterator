#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 4/11/2023
#Project: Test Fibonacci Sequence Class.
#--------------------------------------------------------------------------------------------
#PROGRAMMING TASK
#-----------------
#"Write a test program to test your class by outputting the first 10 values of the Fibonacci 
#sequence. Then reset and output the first 20 values."
#--------------------------------------------------------------------------------------------
from fibonacci_sequence import Fibonacci_Sequence
from itertools import tee

#Constants...
SEQUENCE_ONE_LENGTH = 10
SEQUENCE_TWO_LENGTH = 20

#This function is used to display the results to the screen.
def display_iterator_elements(iterator):
    
    #Create counter to insert commas as needed.
    number_index = 0

    #Use itertools tee method to create two copies of the iterator.
    copy_one, copy_two = tee(iterator, 2)

    #Iterator length.
    iterator_length = len(list(copy_one))

    #Iterate through and display each element inside the iterator.
    for number in copy_two:

        #Selection statement is logic for printing commas.
        if number_index != iterator_length - 1:
            print(number, end = ', ')
            number_index += 1
        else:
            print(number)
            number_index = 0

#Main function is used to hold the logic used to complete the programming task.
def main():

    #Create sequence list to hold values to loop through.
    sequence_length_list = [SEQUENCE_ONE_LENGTH, SEQUENCE_TWO_LENGTH]

    #Display explanation.
    print('\nDisplay the first 10 of fibonacci sequence, then display the first 20.\n')

    #for loop used to create needed amount of sequences and make code D.R.Y.
    for sequence_length in sequence_length_list:

        #Instantiate a fibonacci_iterator object with associated value.
        fibonacci_iterator = Fibonacci_Sequence(sequence_length)

        #Display the elements of the iterator.
        display_iterator_elements(fibonacci_iterator)

        #New line to make things pretty.
        print()

#Run the main function if loaded as main.
if __name__ == '__main__':
    main()