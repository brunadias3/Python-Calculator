# Welcome Function

def welcome():
    print('\nWelcome to calculator program!')

# Calculator


def calculator():
    operation = input('''
    Type the operation:
    + for addition
    - for subtraction
    * for multiplication
    / for division\n
    ''')

    lista = {'-','+','/','*'}

    if not operation in lista:
        print('\nInvalid Play')
        again()
    
    else:
        n1 = int(input('\nfirst number: '))
        n2 = int(input('second number: '))

        # operations
        if operation == '+':
            result = n1 + n2
            print('{} + {} = {}'.format(n1, n2, result))
            again()

        elif operation == '-':
            result = n1 - n2
            print('{} - {} = {}'.format(n1, n2, result))
            again()

        elif operation == '*':
            result = n1 * n2
            print('{} * {} = {}'.format(n1, n2, result))
            again()

        elif operation == '/':
            result = n1/n2
            print('{} / {} = {}'.format(n1, n2, result))
            again()

# Again Function
def again():
    question = input('''
    Do you want do more operations?
    Y for yes
    N for no\n
    ''')

    if question == 'Y' or question == 'y':
        calculator()

    elif question == 'N' or question == 'n':
        print('see you')

    else:
        print('Invalid caractere')
        exit()


welcome()
calculator()
