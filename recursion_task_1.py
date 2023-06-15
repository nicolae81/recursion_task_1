"""
######################
### TASK ###
Create Palindrome Recursive Function
Create Control Digits Recursive Function
Write A Program To Find Numbers From A List(Recursive Function)
Create A Program To Find Numbers From A List Using Method Binary Search(Recursive&Iterative)
The List Must Be from 0 to 7000(order list) and find number 3479 or 3268.
######################

"""

def palindrome_recursiv(word):

    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome_recursiv(word[1:-1])

def control_digit_recursiv(number):
    final_digit = find_number_recursiv(number)
    if final_digit >= 10:
        return control_digit_recursiv(final_digit)
    return final_digit


def find_number_recursiv(another_number):
        str_number = str(another_number)
        total_sum = 0
        for digit in str_number:
            total_sum += int(digit)
        return total_sum


def binary_search_recursiv(lista_x, left, right, number_x):
    if left > right:
        return "I didn't find it!"
    middle = (left + right) // 2
    if lista_x[middle] == number_x:
        return middle
    if lista_x[middle] > number_x:
        return binary_search_recursiv(lista_x, left, middle - 1, number_x)
    else:
        return binary_search_recursiv(lista_x, middle + 1, right, number_x)


def binary_search_iterativ(lista_x, number_x):
    left = 0
    right = len(lista_x) - 1

    while left <= right:
        middle = (left + right) // 2

        if lista_x[middle] == number_x:
            return middle
        elif lista_x[middle] < number_x:
            left = middle + 1
        else:
            right = middle - 1

    return "I didn't find it!"


def main():

    print("|-----------------------------------------------|")
    print("|                 Main Function                 |")
    print("|-----------------------------------------------|")

    ##########################################################
    ### Palindrome ###
    print("\n\n|-----------------------------------------------|")
    print("|                    Task 1                     |")
    words_list = ['solo', '1234321', 'ana', 'civic', 'python3', 'rokor', 'maxim', 'minim', 'software', 'radar']
    
    for word in words_list:
        if palindrome_recursiv(word):
            print(f" The Word '{word}' is a palindrome.")
        else:
            print(f" The Word '{word}' is not a palindrome.")
    print("|-----------------------------------------------|")
    ##########################################################


    ##########################################################
    ### Control digit ###
    print("\n\n|-----------------------------------------------|")
    print("|                    Task 2                     |")
    numbers_list = [12345, 52314, 12453, 41352, 85432845921]
    
    for number in numbers_list:
        print(f"Control digit for {number} is {control_digit_recursiv(number)}")
    print("|-----------------------------------------------|")
    ##########################################################


    ##########################################################
    ### Search Number ###
    print("\n\n|-----------------------------------------------|")
    print("|                    Task 3                     |")
    ################
    ### create a list from 0 to 7000 ###
    my_list = list(range(0, 7001, 2))
    ################
    print(f"The index was found at: {binary_search_recursiv(my_list, 0, 7000, 3479)}")
    print("|-----------------------------------------------|")
    ##########################################################


    ##########################################################
    ### Binary search ###
    print("\n\n|-----------------------------------------------|")
    print("|                     TASK 4                    |")

    ################
    ### iterativ ###
    number_x = 3268

    result = binary_search_iterativ(my_list, number_x)
    if isinstance(result, int):
        print(f"The number {number_x} was found at index {result}.")
    else:
        print(f"The number {number_x} was not found.")
    print(f"Itaerative found= {binary_search_iterativ(my_list, number_x)}")

    ################


    ################
    ### recursiv ###

    print(f"Recursive found= {binary_search_recursiv(my_list, 0, 7000, 3479)}")
    ################

    print("|-----------------------------------------------|")
    ##########################################################


if __name__ == '__main__':
    main()