import random
import string
import re


def input_validation(prompt):
    """
    validates user input to ensure three different digits are present. Repeats until proper input is provided.

    :param prompt: prompt that will be displayed to user to obtain input.
    :type prompt: str
    :return: three different values.
    :rtype: int
    """
    while True:
        user_num = input(f'{prompt}')

        # Splits user input into a list based on a common or empty space.
        list_num = re.split(',\s*|\s', user_num)

        # Attempting to convert found characters to integers and placing them into list.
        three_values = []
        for character in list_num:
            if character.isdigit():
                user_int = int(character)
                three_values.append(user_int)
            else:
                continue

        # Determines if three digits are found and creates and error to retry.
        if len(three_values) == 3:
            upper, lower, digits = three_values[0], three_values[1], three_values[2]
        else:
            print('Not a valid input. Please provide three integers.')
            continue

        return upper, lower, digits


def continue_generating():
    """
    Obtains user input to determine if user wants to generate more passwords. Repeats until proper input is provided.

    :return: True if user wants to continue generating passwords, False otherwise.
    :rtype: bool
    """
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
    """
    Obtains a user input to determine how many passwords should be printed out at once.

    :return: Number of passwords to be printed out.
    :rtype: int
    """
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
    """
    Creates a random password based on user defined characteristics.

    :param uppercase: how many uppercase characters user wants.
    :type uppercase: int
    :param lowercase: how many lowercase characters user wants.
    :type lowercase: int
    :param digits: how many digit characters user wants.
    :type digits: int
    :param special: True if user wants special characters. Default is false.
    :type special: bool
    :return: A random password.
    :rtype: str
    """
    # Creating random sample of characters
    upper_let = random.sample(list(string.ascii_uppercase), k=uppercase)
    lower_lets = random.sample(list(string.ascii_lowercase), k=lowercase)
    num_choice = ''.join(random.choices(list(string.digits), k=digits))
    special_choice = random.choice(list('$!*.%'))

    # Ensures first character is capital if user wants capital letters. [personal preference]
    first_control = upper_let[0] if uppercase > 0 else ''

    # Controlling sequence of letters to ensure capital and lower case are mixed.
    if first_control != '':
        middle_control = 0 if (uppercase - 1) + lowercase <= 0 else (uppercase - 1) + lowercase
    else:
        middle_control = lowercase
    middle_values = ''.join(random.sample(upper_let[1:] + lower_lets, k=middle_control))

    # Adds special character if user desires it.
    if special:
        password = first_control + middle_values + num_choice + special_choice
    else:
        password = first_control + middle_values + num_choice

    return password


def main():
    """
    Creates the password generator.

    :return: none
    """
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
