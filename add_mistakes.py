# MAKE A MISTAKE LIST FOR INDEX
def make_mlist():
    # Initialize variables
    mistake_list = [] # A list of mistake types
    add_more = 'y' # Set to 'yes' to always request one mistake type minimum
    quit = False # If 'quit' is true, we will stop creating mistake types
    mistakes_done = False ### CONSIDER DELETING- ARTIFACT FROM PREVIOUS VERSION
    
    while quit == False:
        # If user chooses to add more mistakes, proceed
        if add_more[0] == 'y':
            while add_more[0] == 'y':
                new_mistake = input('---\nPlease enter one type of mistake: ')
                mistake_list.append(new_mistake)
                while True:
                    # Only accept 'y' or 'n' as input
                    try:
                        add_more = input('---\nWould you like to add more mistakes? Y/N ').lower().strip()
                        # If user chooses to proceed, break from loop and continue through an iteration of main function loop
                        if add_more[0] == 'y':
                            break
                        # If user is done adding mistakes, set 'quit' to true to end main loop, then break from this loop
                        elif add_more[0] == 'n':
                            quit = True
                            mistakes_done = True ### CONSIDER DELETING- ARTIFACT FROM PREVIOUS VERSION
                            break
                        elif isinstance(add_more, str) == False:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                        else:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                    except IndexError:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
    # Print all mistakes for user's information
    print('\nThe mistakes list is: ')
    for c, i in enumerate(mistake_list):
        print(f'Mistake {c+1}: {i}')
    print('---\n')
    # Hold page until user continues
    while True:
        input('\nPress enter to continue. \n\n----------------\n')
        break
    return mistake_list 