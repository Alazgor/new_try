# Debugging exercises
# The following is a list of buggy python code snippets.Try debugging them using Pycharm
# ('s IDE debugger (click to make breakpoints, traverse the code using buttons or keyboard shortcuts (F7 for Step Into, '
#  'F8 for Step Over in Pycharm) and become a detective to solve the mystery of the bug). Describe what is wrong and why '
#  'in a comment and fix the code.)
#
#



# # This code should return a list of small elements(less than threshold) from the given list
#
#
# def filter_low(lst, threshold=5):
#     for element in lst:
#         low = []
#         if element < threshold:
#             low.append(element)
#     return low
#
#
# my_list = [5, 2, 12, 7, 3, 8]
# result = filter_low(my_list)
# print(result)
# # The following code should remove even numbers from a list
#
#
# def remove_even_numbers(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             numbers.remove(num)
#     return numbers
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = remove_even_numbers(numbers)
# print(result)
# # The following code is supposed to print the original and squared list of numbers
#
#
# def square_elements(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** 2
#     return numbers
#
#
# numbers = [1, 2, 3, 4]
# result = square_elements(numbers)
# print(numbers)
# print(result)
# # The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.We sleep
# # in if it is not a weekday or we 're on vacation. Return True if we sleep in. Exercise from here.
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True
#
#
# def sleep_in(weekday, vacation):
#     if vacation is True:
#         return True
#     elif weekday != True or vacation != True:
#         return True
#     else
#         return False
#
#
# result = sleep_in(False, False)
# print(result)







