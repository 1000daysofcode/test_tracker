

# view = input('To see the test structure, press S.\nTo see your test results, press R')
# if view == 's':
#     print(test_raw[test_choice])
# else:
#     print(test_db[test_choice])
# print(test_db)

test_db = [[{'long': {'AAA': [0, 10, ''], 'BBB': {'aaa': [0, 10, ''], 'bbb': {'last': [0, 10, '']}}}}, {'short': {'AAA': [0, 10, '']}}, {'mini':[0, 10, '']}]]
test_index = [{'name':'IELTS', 'mistakes': ''}]

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
        except ValueError:
            print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
            continue
    tests = test_db[test_choice]
    print(f'Below are all test results for test {test_index[test_choice-1]}:\n\n================')
    for c, dct in enumerate(tests):
    for title, v in dct.items():
            print(f'{c+1}) Test Name: {title}\n----------------') 
            if isinstance(v, dict) != True:
                test = v
                if isinstance(test, list) == True:
                    print(f'\tScore: {v[0]} out of: {v[1]} || Mistakes: {v[2]}')
                else:
                    print()
                    pass
            else:
                for layer1, v1 in dct[title].items():
                    print(f'{layer1}')
                    if isinstance(dct[title][layer1], dict) != True:
                        test = v1
                        if isinstance(test, list) == True:
                            print(f'\tScore: {v1[0]} out of: {v1[1]} || Mistakes: {v1[2]}')
                        else:
                            print(f'{layer1}') 
                    else:
                        for layer2, v2 in dct[title][layer1].items():
                            print(f'{layer2} : ')
                            if isinstance(dct[title][layer1][layer2], dict) != True:
                                test = v2
                                if isinstance(test, list) == True:
                                    print(f'\tScore: {v2[0]} out of: {v2[1]} || Mistakes: {v2[2]}')
                                else:
                                    print(layer2 + " : " + str(dct[title][layer1][layer2]))
                            else:
                                for layer3, v3 in dct[title][layer1][layer2].items():
                                    print(f'\t{layer3} || Score: {v3[0]} out of: {v3[1]} || Mistakes: {v3[2]}')
                    print('----------------') 
            print('\n\n================')  
    while True:
        input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
        break       




