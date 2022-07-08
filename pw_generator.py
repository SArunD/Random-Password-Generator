# Here, we import the Random and String Modules
import random
import string

# Here, we define the global variables that store numbers, letters, and other characters
NUMBERS = list(string.digits)
ALPHABET = list(string.ascii_letters)
PUNCTUATION = list(string.punctuation[0] + string.punctuation[2:6] + string.punctuation[20:22])


# This function gets user-input for # of passwords and generates that many passwords
def get_input():
    # This array stores all of our passwords
    passwords = []
    # This variable stores user-input for # of passwords
    num_of_passwords = int(input('How Many Passwords To Generate? '))
    # This variable stores user-input for password length
    password_length = int(input('What Should Password Length Be? '))
    # This loop will run until we generate all our passwords
    for i in range(num_of_passwords):
        # At each iteration, add a new password to our array
        passwords.append(generate_password(password_length))
    # After all passwords are generated, print them out
    print_passwords(passwords)

    # Ask the user if they want to generate more passwords
    again = input('Generate More Passwords? (Y or N) ')
    # If the user enters Y, then call get_input() to restart the process
    if again == 'Y':
        print()
        get_input()
    # If the user enter N, then END
    else:
        print('\nThank You For Using Our Program! Goodbye!')


# This function generates and returns a unique password
def generate_password(password_length):
    # Here, we specifically want to use the global variables
    global NUMBERS, ALPHABET, PUNCTUATION

    # Initially, our password variable is empty
    password = ''
    # This loop will repeat until our password's length is equal to password_length parameter
    for i in range(password_length):
        # This array stores random characters from each of the global variables
        options = [random.choice(ALPHABET), random.choice(NUMBERS), random.choice(PUNCTUATION)]
        # At each iteration, chose a random item from options
        password += random.choice(options)
        # Then, shuffle the elements of options to decrease password repetition
        random.shuffle(options)
    # Lastly, return the password
    return password


# This function takes in an array and prints all elements within that array
def print_passwords(passwords):
    # This loop will run until we print all element of passwords
    for i in range(len(passwords)):
        print('{}.\t{}'.format(i+1, passwords[i]))


# Here, we start our password generator program
get_input()
