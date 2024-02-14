while True:
    user_number = int(input('Enter a number: '))
    print(user_number ** 2)
    user_answer = input('Do you want to enter another number? Answer Y or N ')
    if user_answer == 'N':
        break