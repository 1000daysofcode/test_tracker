# for c, tests in selected_type (such as in other view):
#     \
#     \
#     score += actual (index [1])
#     for j in tmp_dict section where it would be updated/printed:
#         if j in dct[etc]'[mistakes']:
#             tmpdcy[j] += 1
#         else:
#             pass
    # if score > top score
    #     top score = score
    #     topnames = tests
    # elif score == top score
    #     topnames += f', {tests}'

    # if score < low score
    #     low score = score
    # elif score == low score
    #     lownames += f', {tests}'

test_db = [[{'long': {'AAA': [8, 10, 'a, b, c'], 'BBB': {'aaa': [0, 10, 'b'], 'bbb': {'last': [5, 10, 'a, b']}}}}, {'short': {'AAA': [4, 10, 'a, b']}}, {'mini':[1, 10, 'a, b, c']}]]
test_index = [{'name':'IELTS', 'maxscore':30, 'mistakes': 'a, b, c'}]


def analyze(test_db, test_index):
    score = 0
    num_tests = 0
    total_s = 0
    avg = 0
    max_s = 0
    top_s = 0
    top_n = ''
    low_s = 1000000000
    low_n = ''
    m_list = []

    if len(test_db) < 1:
        print(f'\n====================================================\n| Please submit a new test score in order to view. |\n====================================================')
    else:
        print('\nHere are your test names and locations:\n')
        for c, i in enumerate(test_index):
            print(f'Test structure: {i["name"]} || Test location: {c+1}')
        while True:
            try:
                test_choice = int(input('---\n\nPlease enter the location of your tests: '))-1
                if test_choice > len(test_index) or test_choice < 0:
                    print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================')
                    continue
                else:
                    break
            except:
                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
                continue
        num_tests = len(test_db[test_choice])
        max_s = test_index[test_choice]['maxscore']
        tests = test_db[test_choice]

        tmp_mlist = test_index[test_choice]['mistakes'].split(',')
        for each in tmp_mlist:
            m_list.append({'name':each.strip(), 'count':0})
        # print(f'Below are all test results for test {test_index[test_choice-1]}:\n\n================')
        for c, dct in enumerate(tests):
            # print(f'Test #{c+1}\n----------------')
            for title, v in dct.items():
                # print(f'-> {title}\n----------------') 
                if isinstance(v, dict) != True:
                    test = v
                    if isinstance(test, list) == True:
                        score += v[0]
                        for type in m_list:
                            if type['name'] in v[2]:
                                type['count'] += 1
                            else:
                                pass
                    else:
                        print()
                        pass
                else:
                    for layer1, v1 in dct[title].items():
                        # print(f'{layer1}')
                        if isinstance(dct[title][layer1], dict) != True:
                            test = v1
                            if isinstance(test, list) == True:
                                score += v1[0]
                                for type in m_list:
                                    if type['name'] in v1[2]:
                                        type['count'] += 1
                                    else:
                                        pass
                                # print(f'\tScore: {v1[0]} out of: {v1[1]} || Mistakes: {v1[2]}')
                            else:
                                # print(f'{layer1}')
                                pass 
                        else:
                            for layer2, v2 in dct[title][layer1].items():
                                # print(f'{layer2} : ')
                                if isinstance(dct[title][layer1][layer2], dict) != True:
                                    test = v2
                                    if isinstance(test, list) == True:
                                        score += v2[0]
                                        for type in m_list:
                                            if type['name'] in v2[2]:
                                                type['count'] += 1
                                            else:
                                                pass
                                        # print(f'\tScore: {v2[0]} out of: {v2[1]} || Mistakes: {v2[2]}')
                                    else:
                                        # print(layer2 + " : " + str(dct[title][layer1][layer2]))
                                        pass
                                else:
                                    for layer3, v3 in dct[title][layer1][layer2].items():
                                        score += v3[0]
                                        for type in m_list:
                                            if type['name'] in v3[2]:
                                                type['count'] += 1
                                            else:
                                                pass
                                        # print(f'\t{layer3} || Score: {v3[0]} out of: {v3[1]} || Mistakes: {v3[2]}')
                        # print('----------------')
            if score > top_s:
                top_s = score
                top_n = str(c)
            elif score == top_s:
                top_n += f', {str(c)}'

            if score < low_s:
                low_s = score
                low_n = str(c)
            elif score == low_s:
                low_n += f', {str(c)}' 
            # print('\n\n================')  

    total_s += score
    a_score = float(total_s) / num_tests
    name = test_index[test_choice]['name']

    print(f'''
        =====================================
        |          Score Analysis           |
        ------------------------------------|
        | Name of test: ............. {name}
        | Number of tests: .......... {num_tests}
        | Maximum score possible .... {max_s}
        |-----------------------------------|
        | Overall score average ..... {a_score}
        |-----------------------------------|
        | Top score on ............ test #{top_n} |
        | Overall top score ......... {top_s}
        | Lowest score on ......... test #{low_n} |
        | Overall lowest score ...... {low_s}
        |===================================|
        |         Mistakes Rankings         |
        |-----------------------------------|''')

    tally = sorted(m_list, key=lambda k: k['count'])

    if len(tally) >= 6:
        print('    | Least common mistakes:')
        for mst in tally[0:3]:
            print(f"\t| {mst['name']}: {mst['count']} times")
        print('    | Most common mistakes:')
        for mst in tally[-3::-1]:
            print(f"\t| {mst['name']}: {mst['count']} times")
    if len(tally) < 6 and len(tally) > 3:
        print('    | Least common mistakes:')
        for mst in tally[0:2]:
            print(f"\t| {mst['name']}: {mst['count']} times")
        print('    | Most common mistakes:')
        for mst in tally[-2::-1]:
            print(f"\t| {mst['name']}: {mst['count']} times")
    else:
        print('    | From least to most common:        |')
        for mst in tally:
            print(f"    | {mst['name']}: {mst['count']} times")

    print('    =====================================\n')

    while True:
        input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
        break   
choice = 'undefined'
# continue