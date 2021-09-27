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

tests = test_db[test_choice]
print(f'Below are all test results for test {test_index[test_choice-1]}:\n\n================')
for c, dct in enumerate(tests):
    print(f'Test #{c+1}\n----------------')
    for title, v in dct.items():
        print(f'-> {title}\n----------------') 
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