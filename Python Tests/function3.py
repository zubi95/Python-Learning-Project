#Creating function to get initial of a name
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initial are: ' + first_name_initial + last_name_initial)

# Ask for someones name and return the initials

# first_name = input('Enter your first name: ')
# first_name_initial = first_name[0:1]

# last_name = input('Enter your last name: ')
# last_name_initial = last_name[0:1]

# print('Your initial are: ' + first_name_initial + last_name_initial)