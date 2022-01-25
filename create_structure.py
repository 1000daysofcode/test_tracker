import error_messages
from simple_test import build_simple_dict as build_simple_dict
from complex_test import build_custom_dict as build_custom_dict

# Choose between simple and custom test types
def make_test_shell():
    choice = 'undefined'
    while choice != False and choice[0] != 'c' and choice[0] != 's':
        if choice == 'undefined':
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
            
            # If user chooses a simple test, take a name for the test, then create a simple test with the name as the parameter
            if choice[0] == 's':
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2: # Names should be from 3-20 characters in length for readability
                        error_messages.name_length()
                        continue
                    else:
                        return build_simple_dict(testname)
            
            # If user chooses a custom test, take a name for the test, then create a custom test with the name as the parameter
            else:
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2: # Names should be from 3-20 characters in length for readability
                        error_messages.name_length()
                        continue
                    else:
                        return build_custom_dict(testname)

def print_preview(dct):
    for title, v in dct.items():
                    # Print the name of the section
                    print(f'-> {title}\n----------------') 
                    # If the value is a not a dictionary of other subsections
                    if isinstance(v, dict) != True:
                        test = v
                        # Check to make sure that it is a list, then print out the score
                        if isinstance(test, list) == True:
                            print(f'\tScore: {v[0]} out of: {v[1]} || Mistakes: {v[2]}')
                        else:
                            print()
                            pass
                    # If the value of the first section is a dictionary of subsections, iterate through
                    else:
                        for layer1, v1 in dct[title].items():
                            # Print the name of the section
                            print(f'{layer1}')
                            # If the value is a not a dictionary of other subsections
                            if isinstance(dct[title][layer1], dict) != True:
                                test = v1
                                # Check to make sure that it is a list, then print out the score
                                if isinstance(test, list) == True:
                                    print(f'\tScore: {v1[0]} out of: {v1[1]} || Mistakes: {v1[2]}')
                                else:
                                    # If not, print the name for reference
                                    print(f'{layer1}') 
                            # If the value of the second section is a dictionary of subsections, iterate through
                            else:
                                for layer2, v2 in dct[title][layer1].items():
                                    # Print the name of the section
                                    print(f'{layer2} : ')
                                    # If the value is a not a dictionary of other subsections
                                    if isinstance(dct[title][layer1][layer2], dict) != True:
                                        test = v2
                                        # Check to make sure that it is a list, then print out the score
                                        if isinstance(test, list) == True:
                                            print(f'\tScore: {v2[0]} out of: {v2[1]} || Mistakes: {v2[2]}')
                                        else:
                                            # If not, print the name for reference
                                            print(layer2 + " : " + str(dct[title][layer1][layer2]))
                                    # If the value of the third section is a dictionary of subsections, iterate through
                                    else:
                                        for layer3, v3 in dct[title][layer1][layer2].items():
                                            # Print the name of the section
                                            print(f'\t{layer3} ',end='')
                                            # If the value is a not a dictionary of other subsections
                                            if isinstance(dct[title][layer1][layer2][layer3], dict) != True:
                                                test = v3
                                                # Check to make sure that it is a list, then print out the score
                                                if isinstance(test, list) == True:
                                                    print(f'|| Score: {v3[0]} out of: {v3[1]} || Mistakes: {v3[2]}')
                                                else:
                                                    # If not, print the name for reference
                                                    print(f'\t{layer3} ',end='')
                                            # The last layer should only contain a list, so iterate through and print all scores
                                            else:
                                                for layer4, v4 in dct[title][layer1][layer2][layer3].items():
                                                    print(f'\n\t{layer4} || Score: {v4[0]} out of: {v4[1]} || Mistakes: {v4[2]}')
                            # Print in between major parts of the test
                            print('----------------')
                # Let user view test print out before returning to main menu

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