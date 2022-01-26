import error_messages
from simple_test import build_simple_dict as build_simple_dict
from complex_test import build_custom_dict as build_custom_dict


def make_test_shell():
    choice = 'undefined'
    while choice != False and choice[0] != 'c' and choice[0] != 's':
        if choice == 'undefined':
            choice = get_input()
            if choice[0] == 's': # Simple test
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2: # Names should be from 3-20 characters
                        error_messages.name_length()
                        continue
                    else:
                        return build_simple_dict(testname)
            
            else: # Custom test
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2: # Names should be from 3-20 characters
                        error_messages.name_length()
                        continue
                    else:
                        return build_custom_dict(testname)


def get_input():
    while True:
        try: # Choose simple or custom test build
            choice = take_choice()
            # Only accept input if that is a choice for simple or complex test structures
            if choice[0] == 's' or choice[0] == 'c':
                break
            elif isinstance(choice, str) == False:
                error_messages.invalid()
                continue
            else:
                error_messages.invalid()
                continue
        except IndexError:
            error_messages.invalid()
            continue
    return choice


def take_choice():
    return (input('''\n-----------------\n\nWould you like to make a simple test or a custom test?

============================
| Simple Test:             |
----------------------------===============================
| Each part in a simple test has the same number of parts.|
| These are faster to set up and perfect for small or     |
| simply organized tests.                                 |
|                          --> Type S for a 'simple test' |
===========================================================

============================
| Custom Test:             |
----------------------------================================
| Every part in a custom test is customized by the user.   | 
| Each part can be arranged in different ways. This takes  |
| more time, but is good if your test is large or arranged |
| in a more complex way.                                   |
|                           --> Type C for a 'custom test' |
============================================================

Please choose S/C: ''')).lower().strip()