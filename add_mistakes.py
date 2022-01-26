import error_messages


# MAKE A MISTAKE LIST FOR INDEX
def make_mlist():
    
    mistake_list = [] # A list of mistake types
    add_more = 'y' # request one mistake type minimum
    quit = False # If 'quit' is true, stop adding mistake types
    
    while quit == False:
        if add_more[0] == 'y':
            while add_more[0] == 'y':
                new_mistake = input('---\nPlease enter one type of mistake: ')
                mistake_list.append(new_mistake)
                if add_more_mistake_types():
                    continue
                quit = True
                break
    print('\nThe mistakes list is: ')
    for c, i in enumerate(mistake_list):
        print(f'Mistake {c+1}: {i}')
    print('---\n')
    
    while True: # Hold page until user continues
        input('\nPress enter to continue. \n\n----------------\n')
        break
    return mistake_list 


def add_more_mistake_types():
    proceed = True

    while True:
        try:
            add_more = input('---\nWould you like to add more mistakes? Y/N ').lower().strip()
            if add_more[0] == 'y':
                break # Continue through another iteration of main function loop
            elif add_more[0] == 'n':
                proceed = False
                break # 'quit = true' to end main loop, then break from this loop
            elif isinstance(add_more, str) == False:
                error_messages.invalid()
                continue
            else:
                error_messages.invalid()
                continue
        except IndexError:
            error_messages.invalid()
            continue

    return proceed