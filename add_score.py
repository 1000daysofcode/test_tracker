import copy

test_raw = [{'IELTS': {'Reading': {'Part 1': [0, 7, 'none :)'], 'Part 2': [0, 7, 'none :)'], 'Part 3': [0, 7, 'none :)']}, 'Writing': {'Part 1': [0, 7, 'none :)'], 'Part 2': [0, 7, 'none :)'], 'Part 3': [0, 7, 'none :)'], 'Part 4': [0, 7, 'none :)']}}}]
test_db = [[{'IELTS': {'Reading': {'Part 1': [6, 7, '1, 2'], 'Part 2': [7, 7, 'none :)'], 'Part 3': [7, 7, 'none :)']}, 'Writing': {'Part 1': [7, 7, 'none :)'], 'Part 2': [7, 7, 'none :)'], 'Part 3': [3, 7, '3'], 'Part 4': [2, 7, '3, 2, 1']}}}]]
# old_test_db = [[{'long': {'AAA': [0, 10, ''], 'BBB': {'aaa': [0, 10, ''], 'bbb': {'last': [0, 10, '']}}}}, {'short': {'AAA': [0, 10, '']}}, {'mini':[0, 10, '']}]]
test_index = [{'name':'IELTS', 'mistakes': ['1', '2', '3']}]

def add_scores():
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
                    print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================\n')
                    continue
                else:
                    break
            except ValueError:
                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                continue
        dct = copy.deepcopy(test_raw[test_choice])
        for title, v in dct.items():
                print(f'\nTest Name: {title}\n----------------') 
                if isinstance(v, dict) != True:
                    test = v
                    if isinstance(test, list) == True:
                        while True:
                            try:
                                u_score = int(input(f'\nWhat was your score out of {v[1]}? '))
                                if u_score > v[1] or test_choice < 0:
                                    print(f'\n======================================\n| Please enter a number from 0 to {v[1]}. |\n======================================\n')
                                    continue
                                else:
                                    break
                            except ValueError:
                                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                continue
                        dct[title][0] = u_score
                        if u_score < v[1] and len(test_index[test_choice]['mistakes']) > 0:
                            add_m = 'undefined'
                            tmp_m_lst = []
                            while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                u_mistake = input('Please enter mistakes one at a time: ').strip()
                                if u_mistake not in test_index[test_choice]['mistakes']:
                                    print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                    continue
                                elif u_mistake in tmp_m_list and u_mistake != '':
                                    print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                    continue
                                elif u_mistake == '':
                                    print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                    continue
                                else:
                                    tmp_m_lst.append(u_mistake)
                                    if dct[title][2] == 'none :)':
                                        dct[title][2] = u_mistake
                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                            try:
                                                add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                    break
                                                elif isinstance(add_m, str) == False:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                    continue
                                                else:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                    continue
                                            except IndexError:
                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                continue
                                        if add_m[0] == 'y':
                                            continue
                                        else:
                                            break
                                    else:
                                        dct[title][2] += f', {u_mistake}' 
                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                            try:
                                                add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                    break
                                                elif isinstance(add_m, str) == False:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                    continue
                                                else:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                    continue
                                            except IndexError:
                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                continue
                                        if add_m[0] == 'y':
                                            continue
                                        else:
                                            break
                            else:
                                print("---\nNo remaining mistake types.\n")
                    else:
                        print('\n==============================================\n| ERROR: THIS IS INVALID. CONTACT DEVELOPER. |\n==============================================\n')
                        pass
                else:
                    for layer1, v1 in dct[title].items():
                        print(f'\n{layer1}')
                        if isinstance(dct[title][layer1], dict) != True:
                            test = v1
                            if isinstance(test, list) == True:
                                while True:
                                    try:
                                        u_score = int(input(f'\nWhat was your score out of {v1[1]}? '))
                                        if u_score > v1[1] or test_choice < 0:
                                            print(f'\n======================================\n| Please enter a number from 0 to {v1[1]}. |\n======================================\n')
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                        continue
                                dct[title][layer1][0] = u_score
                                if u_score < v1[1]:
                                    add_m = 'undefined'
                                    tmp_m_lst = []
                                    while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                        u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                        if u_mistake not in test_index[test_choice]['mistakes']:
                                            print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                            continue
                                        elif u_mistake in tmp_m_list and u_mistake != '':
                                            print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                            continue
                                        elif u_mistake == '':
                                            print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                            continue
                                        else:
                                            tmp_m_lst.append(u_mistake)
                                            if dct[title][layer1][2] == 'none :)':
                                                dct[title][layer1][2] = u_mistake
                                                while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                    try:
                                                        add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                        if add_m[0] == 'y' or add_m[0] == 'n':
                                                            break
                                                        elif isinstance(add_m, str) == False:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                            continue
                                                        else:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                            continue
                                                    except IndexError:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                        continue
                                                if add_m[0] == 'y':
                                                    continue
                                                else:
                                                    break
                                            else:
                                                dct[title][layer1][2] += f', {u_mistake}'
                                                while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                    try:
                                                        add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                        if add_m[0] == 'y' or add_m[0] == 'n':
                                                            break
                                                        elif isinstance(add_m, str) == False:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                            continue
                                                        else:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                            continue
                                                    except IndexError:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                        continue
                                                if add_m[0] == 'y':
                                                    continue
                                                else:
                                                    break
                                    else:
                                        print("---\nNo remaining mistake types.\n")
                            else:
                                print(f'\n{layer1}') 
                        else:
                            for layer2, v2 in dct[title][layer1].items():
                                print(f'\n{layer2} : ')
                                if isinstance(dct[title][layer1][layer2], dict) != True:
                                    test = v2
                                    if isinstance(test, list) == True:
                                        while True:
                                            try:
                                                u_score = int(input(f'\nWhat was your score out of {v2[1]}? '))
                                                if u_score > v2[1] or u_score < 0:
                                                    print(f'\n======================================\n| Please enter a number from 0 to {v2[1]}. |\n======================================\n')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                                continue
                                        dct[title][layer1][layer2][0] = u_score
                                        if u_score < v2[1]:
                                            add_m = 'undefined'
                                            tmp_m_lst = []
                                            while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                                if u_mistake not in test_index[test_choice]['mistakes']:
                                                    print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                                    continue
                                                elif u_mistake in tmp_m_lst and u_mistake != '':
                                                    print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                                    continue
                                                elif u_mistake == '':
                                                    print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                                    continue
                                                else:
                                                    tmp_m_lst.append(u_mistake)
                                                    if dct[title][layer1][layer2][2] == 'none :)':
                                                        dct[title][layer1][layer2][2] = u_mistake
                                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                            try:
                                                                add_m = input('Would you like to add another mistake? Y/N ').lower().strip()
                                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                                    break
                                                                elif isinstance(add_m, str) == False:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                                else:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                            except IndexError:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                continue
                                                        if add_m[0] == 'y':
                                                            continue
                                                        else:
                                                            break
                                                    else:
                                                        dct[title][layer1][layer2][2] += f', {u_mistake}'
                                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                            try:
                                                                add_m = input('Would you like to add another mistake? Y/N ').lower().strip()
                                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                                    break
                                                                elif isinstance(add_m, str) == False:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                                else:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                            except IndexError:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                continue
                                                        if add_m[0] == 'y':
                                                            continue
                                                        else:
                                                            break
                                            else:
                                                print("---\nNo remaining mistake types.\n")
                                    else:
                                        print('\n' + layer2 + " : " + str(dct[title][layer1][layer2]))
                                else:
                                    for layer3, v3 in dct[title][layer1][layer2].items():
                                        while True:
                                            try:
                                                u_score = int(input(f'\nWhat was your score out of {v3[1]}? '))
                                                if u_score > v3[1] or test_choice < 0:
                                                    print(f'\n======================================\n| Please enter a number from 0 to {v3[1]}. |\n======================================\n')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                                continue
                                        dct[title][layer1][layer2][layer3][0] = u_score
                                        if u_score < v3[1]:
                                            add_m = 'undefined'
                                            tmp_m_lst = []
                                            while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                                if u_mistake not in test_index[test_choice]['mistakes']:
                                                    print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                                    continue
                                                elif u_mistake in tmp_m_lst and u_mistake != '':
                                                    print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                                    continue
                                                elif u_mistake == '':
                                                    print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                                    continue
                                                else:
                                                    tmp_m_lst.append(u_mistake)
                                                    if dct[title][layer1][layer2][layer3][2] == 'none :)':
                                                        dct[title][layer1][layer2][layer3][2] = u_mistake
                                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                            try:
                                                                add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                                    break
                                                                elif isinstance(add_m, str) == False:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                                else:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                            except IndexError:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                continue
                                                        if add_m[0] == 'y':
                                                            continue
                                                        else:
                                                            break
                                                    else:
                                                        dct[title][layer1][layer2][layer3][2] += f', {u_mistake}'
                                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                            try:
                                                                add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                                    break
                                                                elif isinstance(add_m, str) == False:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                                else:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                            except IndexError:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                continue
                                                        if add_m[0] == 'y':
                                                            continue
                                                        else:
                                                            break
                                            else:
                                                print("---\nNo remaining mistake types.\n")
                        print('----------------') 
                print('\n\n================')

    test_db[test_choice].append(dct)
    while True:
        input('Scores successfully added.\n\nPress enter to continue.\n----------------\n')
        break
    print(test_db)

add_scores()