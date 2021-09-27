import copy

# test_raw = [{'IELTS': {'Reading': {'Part 1': [0, 7, 'none :)'], 'Part 2': [0, 7, 'none :)'], 'Part 3': [0, 7, 'none :)']}, 'Writing': {'Part 1': [0, 7, 'none :)'], 'Part 2': [0, 7, 'none :)'], 'Part 3': [0, 7, 'none :)'], 'Part 4': [0, 7, 'none :)']}}}]
test_raw = [{'Test': {'Read': {'111': {'222': [7, 7, 'none :)']}}, 'Write': {'111': {'222': [7, 7, 'none :)']}}}}]
test_db = [[]]
# old_test_db = [[{'long': {'AAA': [0, 10, ''], 'BBB': {'aaa': [0, 10, ''], 'bbb': {'last': [0, 10, '']}}}}, {'short': {'AAA': [0, 10, '']}}, {'mini':[0, 10, '']}]]
test_index = [{'name':'IELTS', 'mistakes': ['1', '2', '3']}]
# test_raw = [{'Part 1':[0, 7, 'none :)']}]
# test_index = [{'name': 'Test', 'mistakes': ['1', '2', '3']}]

def add_scores(test_raw, test_index):
    if len(test_raw) < 1:
        print(f'\n========================================================\n| Please add at least one test score in order to view. |\n========================================================')
    else:
        subfold1 = []
        subfold2 = []
        subfold3 = []
        subfold4 = []
        new_dct = {}
        dct = {}
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
                    # dct[title][0] = u_score
                    if u_score < v[1] and len(test_index[test_choice]['mistakes']) > 0:
                        add_m = 'undefined'
                        tmp_m_lst = []
                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                            u_mistake = input('Please enter mistakes one at a time: ').strip()
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
                                if dct[title][2] == 'none :)':
                                    # dct[title][2] = u_mistake
                                    while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                        try:
                                            add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                            if add_m[0] == 'y' or add_m[0] == 'n':
                                                break
                                            elif isinstance(add_m, str) == False:
                                                print('\n=====================s============\n| That is not a valid response. |\n=================================\n')
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
                                        subfold1.append({'name':title, 'score':[u_score, dct[title][1], tmp_m_lst]})
                                        break
                                else:
                                    # dct[title][2] += f', {u_mistake}' 
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
                                        subfold1.append({'name':title, 'score':[u_score, dct[title][1], tmp_m_lst]})
                                        break
                        else:
                            subfold1.append({'name':title, 'score':[u_score, dct[title][1], tmp_m_lst]})
                            print("---\nNo remaining mistake types.\n")
                    elif u_score == v[1]:
                        subfold1.append({'name':title, 'score':[u_score, dct[title][1], dct[title][2]]})
                else:
                    print('\n==============================================\n| ERROR: THIS IS INVALID. CONTACT DEVELOPER. |\n==============================================\n')
                    pass
            else:
                subfold1.append({'name':title})
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
                            # dct[title][layer1][0] = u_score
                            if u_score < v1[1] and len(test_index[test_choice]['mistakes']) > 0:
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
                                        if dct[title][layer1][2] == 'none :)':
                                            # dct[title][layer1][2] = u_mistake
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
                                                subfold2.append({'parent':title, 'name':layer1, 'score':[u_score, dct[title][layer1][1], tmp_m_lst]})
                                                break
                                        else:
                                            # dct[title][layer1][2] += f', {u_mistake}'
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
                                                subfold2.append({'parent':title, 'name':layer1, 'score':[u_score, dct[title][layer1][1], tmp_m_lst]})
                                                break
                                else:
                                    subfold2.append({'parent':title, 'name':layer1, 'score':[u_score, dct[title][layer1][1], tmp_m_lst]})
                                    print("---\nNo remaining mistake types.\n")
                            elif u_score == v1[1]:
                                subfold2.append({'parent':title, 'name':layer1, 'score':[u_score, dct[title][layer1][1], dct[title][layer1][2]]})
                        else:
                            print(f'\n{layer1}') 
                    else:
                        subfold2.append({'parent':title,'name':layer1})
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
                                    # dct[title][layer1][layer2][0] = u_score
                                    if u_score < v2[1] and len(test_index[test_choice]['mistakes']) > 0:
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
                                                    # dct[title][layer1][layer2][2] = u_mistake
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
                                                        subfold3.append({'parent':layer1, 'name':layer2, 'score':[u_score, dct[title][layer1][layer2][1], tmp_m_lst]})
                                                        break
                                                else:
                                                    # dct[title][layer1][layer2][2] += f', {u_mistake}'
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
                                                        subfold3.append({'parent':layer1, 'name':layer2, 'score':[u_score, dct[title][layer1][layer2][1], tmp_m_lst]})
                                                        break
                                        else:
                                            subfold3.append({'parent':layer1, 'name':layer2, 'score':[u_score, dct[title][layer1][layer2][1], tmp_m_lst]})
                                            print("---\nNo remaining mistake types.\n")
                                    elif u_score == v2[1]:
                                        subfold3.append({'parent':layer1, 'name':layer2, 'score':[u_score, dct[title][layer1][layer2][1], dct[title][layer1][layer2][2]]})
                                else:
                                    print('\n' + layer2 + " : " + str(dct[title][layer1][layer2]))
                            else:
                                subfold3.append({'parent':layer1,'name':layer2})
                                for layer3, v3 in dct[title][layer1][layer2].items():
                                    print(f'{layer3} : ')
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
                                    # print(f'{dct[title][layer1][layer2][layer3]}, {layer1}, {layer2}, {layer3}')
                                    # print(dct[title][layer1][layer2][layer3][0])
                                    # dct[title][layer1][layer2][layer3][0] = u_score
                                    # if dct[title][layer1][layer2][layer3][0] != 'tbd':
                                    #     continue
                                    # print()
                                    # print(f'score: {u_score}')
                                    # print(f'{dct[title][layer1][layer2][layer3]}, {layer1}, {layer2}, {layer3}')
                                    if u_score < v3[1] and len(test_index[test_choice]['mistakes']) > 0:
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
                                                    # dct[title][layer1][layer2][layer3][2] = u_mistake
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
                                                        subfold4.append({'gparent':layer1, 'parent':layer2, 'name':layer3, 'score':[u_score, dct[title][layer1][layer2][layer3][1], tmp_m_lst]})
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
                                                        subfold4.append({'gparent':layer1, 'parent':layer2, 'name':layer3, 'score':[u_score, dct[title][layer1][layer2][layer3][1], tmp_m_lst]})
                                                        break
                                        else:
                                            subfold4.append({'gparent':layer1, 'parent':layer2, 'name':layer3, 'score':[u_score, dct[title][layer1][layer2][layer3][1], tmp_m_lst]})
                                            print("---\nNo remaining mistake types.\n")
                                    elif u_score == v3[1]:
                                        subfold4.append({'gparent':layer1, 'parent':layer2, 'name':layer3, 'score':[u_score, dct[title][layer1][layer2][layer3][1], dct[title][layer1][layer2][layer3][2]]})
                    print('----------------') 
                print('\n\n================')
                print(f'\n{subfold1}\n\n{subfold2}\n\n{subfold3}\n\n{subfold4}')
            for prim_f in subfold1:
                if 'score' not in prim_f.keys():
                    dict2 = {}
                    for sec_f in subfold2:
                        if 'score' not in sec_f.keys():
                            if sec_f['parent'] == prim_f['name']:
                                dict3 = {}
                                for ter_f in subfold3:
                                    if 'score' not in ter_f.keys():
                                        if ter_f['parent'] == sec_f['name']:
                                            dict4 = {}
                                            for quad_f in subfold4:
                                                if quad_f['gparent'] == ter_f['parent'] == sec_f['name']:
                                                    dict4.update({quad_f['name']:quad_f['score']})
                                                else:
                                                    pass
                                            dict3.update({ter_f['name']:dict4})
                                        else:    
                                            continue
                                    elif ter_f['parent'] == sec_f['name']:
                                        dict3.update({ter_f['name']:ter_f['score']})
                                dict2.update({sec_f['name']:dict3})
                            else:
                                continue
                        elif sec_f['parent'] == prim_f['name']:
                            dict2.update({sec_f['name']:sec_f['score']})
                        else:
                            continue
                    new_dct.update({prim_f['name']:dict2})
                else:
                    new_dct.update({prim_f['name']:prim_f['score']})
            dct = {test_index[test_choice]['name']:new_dct}
            return test_choice, dct  

    

test_choice, new_dct = add_scores(test_raw, test_index)

test_db[test_choice].append(new_dct)
while True:
    input('Scores successfully added.\n\nPress enter to continue.\n----------------\n')
    break
print(test_db)