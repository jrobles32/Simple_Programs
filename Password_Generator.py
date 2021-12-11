import random
import string
import re


def input_validation(prompt):
    while True:
        user_num = input(f'{prompt}')
        list_num = re.split(',\s*|\s', user_num)

        three_values = []
        for character in list_num:
            if character.isdigit():
                user_int = int(character)
                three_values.append(user_int)
            else:
                continue

        if len(three_values) == 3:
            upper, lower, digits = three_values[0], three_values[1], three_values[2]
        else:
            print('Not a valid input. Please provide three integers.')
            continue

        return upper, lower, digits


def continue_generating():
    while True:
        user_input = input('\nDo you want to generate more passwords? (yes/no) ')
        if user_input.lower() == ('yes' or 'y'):
            print()
            return True
        elif user_input.lower() == ('no' or 'n'):
            print('Quitting program.')
            return False
        else:
            print('You did not provide a valid input. Try Again.')
            continue


def multiples():
    while True:
        user_input = input('How many passwords do you want to print? ')
        print()
        if user_input.isdigit():
            num_print = int(user_input)
            return num_print
        else:
            print('You did not provide a valid input. Try Again.')
            continue


def generate_password(uppercase, lowercase, digits, special=False):
    upper_let = random.sample(list(string.ascii_uppercase), k=uppercase)
    lower_lets = random.sample(list(string.ascii_lowercase), k=lowercase)
    num_choice = ''.join(random.choices(list(string.digits), k=digits))
    special_choice = random.choice(list('$!*.%'))

    first_control = upper_let[0] if uppercase > 0 else ''
    if first_control != '':
        middle_control = 0 if (uppercase - 1) + lowercase <= 0 else (uppercase - 1) + lowercase
    else:
        middle_control = lowercase
    middle_values = ''.join(random.sample(upper_let[1:] + lower_lets, k=middle_control))

    if special:
        password = first_control + middle_values + num_choice + special_choice
    else:
        password = first_control + middle_values + num_choice
    return password


def main():
    while True:
        upper, lower, digits = \
        input_validation('Input desired format of password: [uppercase, lowercase, digits] ')

        num_to_generate = multiples()
        for quantity in range(num_to_generate):
            password = generate_password(uppercase=upper, lowercase=lower, digits=digits)
            print('Generated password: ' + password)

        if continue_generating():
            pass
        else:
            break


if __name__ == '__main__':
    main()
