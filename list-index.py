# streaming = ['netflix', 'hulu', 'disney+', 'appletv+']

# index = streaming.index('gooog')
# print('The index of disney+ is:', index)
# # ValueError


mistake_list = []
add_more = ''
quit = False

mistakes_done = False

while quit == False:
    try:
        add_more = input('\nWould you like to add a mistake type? Y/N ').lower().strip()
        if add_more[0] == 'y':
            while add_more[0] == 'y':
                new_mistake = input('---\nEnter the name of your mistake type: ')
                mistake_list.append(new_mistake)
                while True:
                    try:
                        add_more = input('---\nWould you like to continue? Y/N ').lower().strip()
                        if add_more[0] == 'y':
                            break
                        elif add_more[0] == 'n':
                            quit = True
                            mistakes_done = True
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
        elif add_more[0] == 'n':
            quit = True
            mistakes_done = False
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

print('\nThe mistakes list is: ')
for c, i in enumerate(mistake_list):
    print(f'Mistake {c}: {i}')
print('---\n')


    
    
    