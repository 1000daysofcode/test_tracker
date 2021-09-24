import copy

test_raw = [{'IELTS': {'Reading': {'Part 1': [0, 7, ''], 'Part 2': [0, 7, ''], 'Part 3': [0, 7, '']}, 'Writing': {'Part 1': [0, 7, ''], 'Part 2': [0, 7, ''], 'Part 3': [0, 7, ''], 'Part 4': [0, 7, '']}}}]
test_db = []
# old_test_db = [[{'long': {'AAA': [0, 10, ''], 'BBB': {'aaa': [0, 10, ''], 'bbb': {'last': [0, 10, '']}}}}, {'short': {'AAA': [0, 10, '']}}, {'mini':[0, 10, '']}]]
test_index = [{'name':'IELTS', 'mistakes': '1, 2, 3'}]

dct = {}

if len(test_raw) < 1:
    print(f'\n========================================================\n| Please add at least one test score in order to view. |\n========================================================')
else:
    print('\nHere are your test names and locations:\n')
    for c, i in enumerate(test_index):
        print(f'Test structure: {i["name"]} || Test location: {c+1}')
    while True:
        try:
            test_choice = int(input('---\n\nPlease enter the location of the test you want to add a score for: '))-1
            if test_choice > len(test_index)-1 or test_choice < 0:
                print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================')
                continue
            else:
                break
        except ValueError:
            print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
            continue
    dct = copy.deepcopy(test_raw[test_choice])
    for title, v in dct.items():
            print(f'Test Name: {title}\n----------------') 
            if isinstance(v, dict) != True:
                test = v
                if isinstance(test, list) == True:
                    while True:
                        try:
                            u_score = int(input(f'What was your score out of {v[1]}? '))
                            if u_score > v[1] or test_choice < 0:
                                print(f'\n==================================\n| Please enter a number from 0 to {v[1]}. |\n==================================')
                                continue
                            else:
                                break
                        except ValueError:
                            print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
                            continue
                    dct[title][0] = u_score
                    if u_score < v[1]:
                        add_m = 'undefined'
                        while True:
                            if add_m == 'n':
                                break
                            u_mistake = input('Please enter mistakes one at a time: ').strip()
                            if u_mistake not in test_index[test_choice]['mistakes']:
                                print('That is not a valid mistake type.')
                                continue
                            elif u_mistake in v[2]:
                                print('You have already entered that mistake.')
                                continue
                            else:
                                while True:
                                    try:
                                        add_m = input('Would you like to add another mistake? Y/N' ).lower().strip()
                                        if add_m[0] == 'y' or add_m[0] == 'n':
                                            break
                                        elif isinstance(add_m, str) == False:
                                            print('\n=================================\n| That is not a valid response. |\n=================================')
                                            continue
                                        else:
                                            print('\n=================================\n| That is not a valid response. |\n=================================')
                                            continue
                                    except IndexError:
                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                        continue
                                if add_m == 'y':
                                    while True:
                                        if dct[title][2] == '':
                                            dct[title][2] = u_mistake
                                            while True:
                                                try:
                                                    add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                    if add_m[0] == 'y' or add_m[0] == 'n':
                                                        break
                                                    elif isinstance(add_m, str) == False:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                        continue
                                                    else:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                        continue
                                                except IndexError:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                                    continue
                                            if add_m[0] == 'y':
                                                continue
                                            else:
                                                break
                                        else:
                                            dct[title][2] = f', {u_mistake}' 
                                            while True:
                                                try:
                                                    add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                    if add_m[0] == 'y' or add_m[0] == 'n':
                                                        break
                                                    elif isinstance(add_m, str) == False:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                        continue
                                                    else:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                        continue
                                                except IndexError:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                                    continue
                                            if add_m[0] == 'y':
                                                continue
                                            else:
                                                break
                                else:
                                    pass
                else:
                    print('ERROR: THIS IS INVALID. CONTACT DEVELOPER.')
                    pass
            else:
                for layer1, v1 in dct[title].items():
                    print(f'{layer1}')
                    if isinstance(dct[title][layer1], dict) != True:
                        test = v1
                        if isinstance(test, list) == True:
                            while True:
                                try:
                                    u_score = int(input(f'What was your score out of {v1[1]}? '))
                                    if u_score > v1[1] or test_choice < 0:
                                        print(f'\n==================================\n| Please enter a number from 0 to {v[1]}. |\n==================================')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
                                    continue
                            dct[title][layer1][0] = u_score
                            if u_score < v1[1]:
                                add_m = 'undefined'
                                while True:
                                    if add_m == 'n':
                                        break
                                    u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                    if u_mistake not in test_index[test_choice]['mistakes']:
                                        print('That is not a valid mistake type.')
                                        continue
                                    elif u_mistake in v1[2]:
                                        print('You have already entered that mistake.')
                                        continue
                                    else:
                                        while True:
                                            try:
                                                add_m = input('Would you like to add a mistake? Y/N').lower().strip()
                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                    break
                                                elif isinstance(add_m, str) == False:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                                    continue
                                                else:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                                    continue
                                            except IndexError:
                                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                                continue
                                        if add_m == 'y':
                                            while True:
                                                if dct[title][layer1][2] == '':
                                                    dct[title][layer1][2] = u_mistake
                                                    while True:
                                                        try:
                                                            add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                            if add_m[0] == 'y' or add_m[0] == 'n':
                                                                break
                                                            elif isinstance(add_m, str) == False:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                continue
                                                            else:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                continue
                                                        except IndexError:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================')
                                                            continue
                                                    if add_m[0] == 'y':
                                                        continue
                                                    else:
                                                        break
                                                else:
                                                    dct[title][layer1][2] = f', {u_mistake}'
                                                    while True:
                                                        try:
                                                            add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                            if add_m[0] == 'y' or add_m[0] == 'n':
                                                                break
                                                            elif isinstance(add_m, str) == False:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                continue
                                                            else:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                continue
                                                        except IndexError:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================')
                                                            continue
                                                    if add_m[0] == 'y':
                                                        continue
                                                    else:
                                                        break
                                        else:
                                            pass
                        else:
                            print(f'{layer1}') 
                    else:
                        for layer2, v2 in dct[title][layer1].items():
                            print(f'{layer2} : ')
                            if isinstance(dct[title][layer1][layer2], dict) != True:
                                test = v2
                                if isinstance(test, list) == True:
                                    while True:
                                        try:
                                            u_score = int(input(f'What was your score out of {v2[1]}? '))
                                            if u_score > v2[1] or test_choice < 0:
                                                print(f'\n==================================\n| Please enter a number from 0 to {v[1]}. |\n==================================')
                                                continue
                                            else:
                                                break
                                        except ValueError:
                                            print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
                                            continue
                                    dct[title][layer1][layer2][0] = u_score
                                    if u_score < v2[1]:
                                        add_m = 'undefined'
                                        while True:
                                            if add_m == 'n':
                                                break
                                            u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                            if u_mistake not in test_index[test_choice]['mistakes']:
                                                print('That is not a valid mistake type.')
                                                continue
                                            elif u_mistake in v2[2]:
                                                print('You have already entered that mistake.')
                                                continue
                                            else:
                                                while True:
                                                    try:
                                                        add_m = input('Would you like to add a mistake? Y/N').lower().strip()
                                                        if add_m[0] == 'y' or add_m[0] == 'n':
                                                            break
                                                        elif isinstance(add_m, str) == False:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================')
                                                            continue
                                                        else:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================')
                                                            continue
                                                    except IndexError:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                        continue
                                                if add_m == 'y':
                                                    while True:
                                                        if dct[title][layer1][layer2][2] == '':
                                                            dct[title][layer1][layer2][2] = u_mistake
                                                            while True:
                                                                try:
                                                                    add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                                    if add_m[0] == 'y' or add_m[0] == 'n':
                                                                        break
                                                                    elif isinstance(add_m, str) == False:
                                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                        continue
                                                                    else:
                                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                        continue
                                                                except IndexError:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                    continue
                                                            if add_m[0] == 'y':
                                                                continue
                                                            else:
                                                                break
                                                        else:
                                                            dct[title][layer1][layer2][2] = f', {u_mistake}'
                                                            while True:
                                                                try:
                                                                    add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                                    if add_m[0] == 'y' or add_m[0] == 'n':
                                                                        break
                                                                    elif isinstance(add_m, str) == False:
                                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                        continue
                                                                    else:
                                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                        continue
                                                                except IndexError:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                    continue
                                                            if add_m[0] == 'y':
                                                                continue
                                                            else:
                                                                break
                                                else:
                                                    pass
                                else:
                                    print(layer2 + " : " + str(dct[title][layer1][layer2]))
                            else:
                                for layer3, v3 in dct[title][layer1][layer2].items():
                                    while True:
                                        try:
                                            u_score = int(input(f'What was your score out of {v3[1]}? '))
                                            if u_score > v3[1] or test_choice < 0:
                                                print(f'\n==================================\n| Please enter a number from 0 to {v[1]}. |\n==================================')
                                                continue
                                            else:
                                                break
                                        except ValueError:
                                            print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
                                            continue
                                    dct[title][layer1][layer2][layer3][0] = u_score
                                    if u_score < v3[1]:
                                        add_m = 'undefined'
                                        while True:
                                            if add_m == 'n':
                                                break
                                            u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                            if u_mistake not in test_index[test_choice]['mistakes']:
                                                print('That is not a valid mistake type.')
                                                continue
                                            elif u_mistake in v3[2]:
                                                print('You have already entered that mistake.')
                                                continue
                                            else:
                                                while True:
                                                    try:
                                                        add_m = input('Would you like to add a mistake? Y/N').lower().strip()
                                                        if add_m[0] == 'y' or add_m[0] == 'n':
                                                            break
                                                        elif isinstance(add_m, str) == False:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================')
                                                            continue
                                                        else:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================')
                                                            continue
                                                    except IndexError:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                        continue
                                                if add_m == 'y':
                                                    while True:
                                                        if dct[title][layer1][layer2][layer3][2] == '':
                                                            dct[title][layer1][layer2][layer3][2] = u_mistake
                                                            while True:
                                                                try:
                                                                    add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                                    if add_m[0] == 'y' or add_m[0] == 'n':
                                                                        break
                                                                    elif isinstance(add_m, str) == False:
                                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                        continue
                                                                    else:
                                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                        continue
                                                                except IndexError:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                    continue
                                                            if add_m[0] == 'y':
                                                                continue
                                                            else:
                                                                break
                                                        else:
                                                            dct[title][layer1][layer2][layer3][2] = f', {u_mistake}'
                                                            while True:
                                                                try:
                                                                    add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                                    if add_m[0] == 'y' or add_m[0] == 'n':
                                                                        break
                                                                    elif isinstance(add_m, str) == False:
                                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                        continue
                                                                    else:
                                                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                        continue
                                                                except IndexError:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                                                    continue
                                                            if add_m[0] == 'y':
                                                                continue
                                                            else:
                                                                break
                                                else:
                                                    pass
                    print('----------------') 
            print('\n\n================')


# if len(test_db) < 1:
#     print(f'\n====================================================\n| Please submit a new test score in order to view. |\n====================================================')
# else:
#     print('\nHere are your test names and locations:\n')
#     for c, i in enumerate(test_index):
#         print(f'Test structure: {i["name"]} || Test location: {c+1}')
#     while True:
#         try:
#             test_choice = int(input('---\n\nPlease enter the location of your tests: '))-1
#             if test_choice > len(test_index) or test_choice < 0:
#                 print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================')
#                 continue
#             else:
#                 break
#         except ValueError:
#             print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
#             continue
#     tests = test_db[test_choice]
#     print(f'Below are all test results for test {test_index[test_choice-1]}:\n\n================')
#     for c, dct in enumerate(tests):
#     for title, v in dct.items():
#             print(f'{c+1}) Test Name: {title}\n----------------') 
#             if isinstance(v, dict) != True:
#                 test = v
#                 if isinstance(test, list) == True:
#                     print(f'\tScore: {v[0]} out of: {v[1]} || Mistakes: {v[2]}')
#                 else:
#                     print()
#                     pass
#             else:
#                 for layer1, v1 in dct[title].items():
#                     print(f'{layer1}')
#                     if isinstance(dct[title][layer1], dict) != True:
#                         test = v1
#                         if isinstance(test, list) == True:
#                             print(f'\tScore: {v1[0]} out of: {v1[1]} || Mistakes: {v1[2]}')
#                         else:
#                             print(f'{layer1}') 
#                     else:
#                         for layer2, v2 in dct[title][layer1].items():
#                             print(f'{layer2} : ')
#                             if isinstance(dct[title][layer1][layer2], dict) != True:
#                                 test = v2
#                                 if isinstance(test, list) == True:
#                                     print(f'\tScore: {v2[0]} out of: {v2[1]} || Mistakes: {v2[2]}')
#                                 else:
#                                     print(layer2 + " : " + str(dct[title][layer1][layer2]))
#                             else:
#                                 for layer3, v3 in dct[title][layer1][layer2].items():
#                                     print(f'\t{layer3} || Score: {v3[0]} out of: {v3[1]} || Mistakes: {v3[2]}')
#                     print('----------------') 
#             print('\n\n================')  
#     while True:
#         input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
#         break       

