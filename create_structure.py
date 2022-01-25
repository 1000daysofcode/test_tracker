import simple_test as build_simple_dict
import complex_test as build_custom_dict

# Choose between simple and custom test types
def make_test_shell():
    choice = 'undefined'
    while choice != False and choice[0] != 'c' and choice[0] != 's':
        if choice == 'undefined':
            while True:
                try: # Choose simple or custom test build
                    choice = (input('''\n-----------------\n\nWould you like to make a simple test or a custom test?

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
                    # Only accept input if that is a choice for simple or complex test structures
                    if choice[0] == 's' or choice[0] == 'c':
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
            # If user chooses a simple test, take a name for the test, then create a simple test with the name as the parameter
            if choice[0] == 's':
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2: # Names should be from 3-20 characters in length for readability
                        print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                        continue
                    else:
                        return build_simple_dict(testname)
            # If user chooses a custom test, take a name for the test, then create a custom test with the name as the parameter
            else:
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2: # Names should be from 3-20 characters in length for readability
                        print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                        continue
                    else:
                        return build_custom_dict(testname)