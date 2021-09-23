# Import functions
from typing import Dict
from choose_test import make_test_shell as make_test
from view_test import print_dict as view_dict

# Greet user
print('-----------------\n\nWelcome to Test Tracker version 0!')

# Ask for name (add to variable)
name = input('\n\nPlease enter your name: ')
print(f'\nWelcome, {name}!\n\nPlease create at least one test structure to continue.')

# Initialize test max score variable
maxScore = 0
numLevels = 0
test_raw = []
test_db = []
test_index = [{'name':'IELTS'}]
            
testname, dict_s, levels = make_test()
test_raw.append(dict_s)
test_index.append({'name':testname})

print('\nTest created. Please see below:')
view_dict(dict_s)

choice = 'undefined'
while choice != False and choice[0] != 'q':
    if choice == 'undefined':
        while True:
            try:
                choice = (input('''
===============================================
|                  Main Menu                  |
-----------------------------------------------
| View your scores ................ press 'V' |
| View a score analysis ........... press 'A' |
| Add a new score ................. press 'N' |
| Create another test structure ... press 'S' |
| Exit the program ................ press 'Q' |
===============================================

Enter an option: ''')).lower().strip()
                if choice[0] == 'v' or choice[0] == 'a' or choice[0] == 'n' or choice[0] == 's' or choice[0] == 'q':
                    break
                elif isinstance(choice, str) == False:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
                else:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            except IndexError:
                print('\n=================================\n| That is not a valid response. |\n=================================')
                continue
        if choice[0] == 'v':
            print('\nYou chose to view your scores.')
            choice = 'undefined'
            continue
        elif choice[0] == 'a':
            print('\nYou chose to view a score analysis')
            choice = 'undefined'
            continue
        elif choice[0] == 'n':
            print('\nYou chose to add a new score')
            choice = 'undefined'
            continue
        elif choice[0] == 's':
            print('\nYou chose to create a new test structure')
            choice = 'undefined'
            continue
        else:
            print('\nThank you for using Test Tracker version 0! Goodbye')
            choice = False

for i in test_index:
    print(f'Test structure: {i["name"]}\nTest location: {i["location"]+1}\n-')
test_choice = int(input('Please enter the location of your test'))-1

view = input('To see the test structure, press S.\nTo see your test results, press R')
if view == 's':
    print(test_raw[test_choice])
else:
    print(test_db[test_choice])
print(test_db)

# Type 'QUIT NOW' at any time to quit program. Confirmation y/n

