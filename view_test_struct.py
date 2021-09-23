# for c, i in enumerate(test_index):
#     print(f'Test structure: {i["name"]}\nTest location: {c+1}\n-')
# test_choice = int(input('Please enter the location of your test'))-1

# view = input('To see the test structure, press S.\nTo see your test results, press R')
# if view == 's':
#     print(test_raw[test_choice])
# else:
#     print(test_db[test_choice])
# print(test_db)

long = {'long': {'AAA': [0, 10, ''], 'BBB': {'aaa': [0, 10, ''], 'bbb': {'last': [0, 10, '']}}}}
short = {'short': {'AAA': [0, 10, '']}}
dct = {'mini':[0, 10, '']}

dictlist = [{'long': {'AAA': [0, 10, ''], 'BBB': {'aaa': [0, 10, ''], 'bbb': {'last': [0, 10, '']}}}}, {'short': {'AAA': [0, 10, '']}}, {'mini':[0, 10, '']}]



for title, v in dct.items():
    print(f'\nTest Name: {title}\n----------------') 
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

