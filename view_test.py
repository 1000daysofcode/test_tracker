from choose_test import make_test_shell as make_test

test_raw = [{'IELTS': {'Test 1': {'Reading': {'Part 1': [0, ''], 'Part 2': [0, ''], 'Part 3': [0, ''], 'Part 4': [0, '']}, 'Writing': {'Part 1': [0, ''], 'Part 2': [0, ''], 'Part 3': [0, '']}}}}]
test_db = [{}]
test_index = [{'name':'IELTS','location':0}]
            
dict, levels = make_test()
print('\nTest created. Please see below:')
print('\n-----------------\n\nNumber of levels: 2\n\nDictionary:\n{things:stuff}\n')

for i in test_index:
    print(f'Test structure: {i["name"]}\nTest location: {i["location"]+1}\n-')
test_choice = int(input('Please enter the location of your test'))-1

view = input('To see the test structure, press S.\nTo see your test results, press R')
if view == 's':
    print(test_raw[test_choice])
else:
    print(test_db[test_choice])
print(test_db)

def print_dict(dct):
    for title, v in dct.items():
        print(f'\nTest Name: {title}\n----------------')
        for layer1, v1 in dct[title].items():
            print(f'{layer1}')
            if isinstance(dct[title][layer1], dict) != True:
                test = v1
                if isinstance(test, list) == True:
                    print(f'\tScore: {v1[0]} || Mistakes: {v1[1]}')
                else:
                    print(str(dct[title][layer1])) 
            else:
                for layer2, v2 in dct[title][layer1].items():
                    print(f'{layer2} : ')
                    if isinstance(dct[title][layer1][layer2], dict) != True:
                        test = v2
                        if isinstance(test, list) == True:
                            print(f'\tScore: {v2[0]} || Mistakes: {v2[1]}')
                        else:
                            print(layer2 + " : " + str(dct[title][layer1][layer2]))
                    else:
                        for layer3, v3 in dct[title][layer1][layer2].items():
                            print(f'\t{layer3} || Score: {v3[0]} || Mistakes: {v3[1]}')
            print('----------------\n')