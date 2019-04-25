# create an array
animals = []

def create_new():
    print('\n')
    new_animal = input('Animal Name: ')
    animals.append(new_animal)
    print(new_animal, ' Saved')
    input('Press enter to continue')

def print_list(array):
    print('\n')
    for single_animal in array:
        print(single_animal)
    input('Press enter to continue')

def count_animal():
    print('\n')
    print('their are: ', len(animals), ' in the array')
    input('Press enter to continue')

def sort_animal():
    alpha_list = sorted(animals)
    print_list(alpha_list)

def menu():
    print('\n')
    print('***** Welcome to the menu **********')
    print('_' * 20)
    print('1 - Add new animal')
    print('2 - List animals')
    print('3 - Count the Animals')
    print('4 - sort in alphabetical order')
    print('x - Close the program')
    print('\n')
    option = input('Please select an option: ')
    return option

selection = ''
print('You selected ', selection)

while selection != 'x' or 'X':
    selection = menu()

    if selection == '1':
        print('\n')
        print('user wants to add a new animal')
        create_new()
    elif selection == '2':
        print('\n')
        print('User wants to list the animals')
        print_list(animals)
    elif selection == '3':
        print('\n')
        print('User wants to count the animals')
        count_animal()
    elif selection == '4':
        print('\n')
        print('User wants to print the animals in alphabetical order')
        sort_animal()
    else:
        print('moving on')
        
print('Goodbye')