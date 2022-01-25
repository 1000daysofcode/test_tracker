def view(tests):
    # Enumerate list in order to print where tests are in the 
    for c, dct in enumerate(tests):
        print(f'Test #{c+1}\n----------------')
        # For first level of sections -> CHANGE this name later
        for title, v in dct.items():
            # Print the name of the section
            print(f'-> {title}\n----------------') 
            # If the value is a not a dictionary of other subsections
            if isinstance(v, dict) != True:
                test = v
                # Check to make sure that it is a list, then print out the score
                if isinstance(test, list) == True:
                    print(f'\tScore: {v[0]} out of: {v[1]} || Mistakes: {v[2]}')
                else:
                    print()
                    pass
            # If the value of the first section is a dictionary of subsections, iterate through
            else:
                for layer1, v1 in dct[title].items():
                    # Print the name of the section
                    # print(f'{layer1}')
                    # If the value is a not a dictionary of other subsections
                    if isinstance(dct[title][layer1], dict) != True:
                        test = v1
                        # Check to make sure that it is a list, then print out the score
                        if isinstance(test, list) == True:
                            print(f'\tScore: {v1[0]} out of: {v1[1]} || Mistakes: {v1[2]}')
                        else:
                            # If not, print the name for reference
                            print(f'{layer1}') 
                    # If the value of the second section is a dictionary of subsections, iterate through
                    else:
                        for layer2, v2 in dct[title][layer1].items():
                            # Print the name of the section
                            print(f'{layer2} : ')
                            # If the value is a not a dictionary of other subsections
                            if isinstance(dct[title][layer1][layer2], dict) != True:
                                test = v2
                                # Check to make sure that it is a list, then print out the score
                                if isinstance(test, list) == True:
                                    print(f'\tScore: {v2[0]} out of: {v2[1]} || Mistakes: {v2[2]}')
                                else:
                                    # If not, print the name for reference
                                    print(layer2 + " : " + str(dct[title][layer1][layer2]))
                            # If the value of the third section is a dictionary of subsections, iterate through
                            else:
                                for layer3, v3 in dct[title][layer1][layer2].items():
                                    # Print the name of the section
                                    print(f'\t{layer3} ',end='')
                                    # If the value is a not a dictionary of other subsections
                                    if isinstance(dct[title][layer1][layer2][layer3], dict) != True:
                                        test = v3
                                        # Check to make sure that it is a list, then print out the score
                                        if isinstance(test, list) == True:
                                            print(f'|| Score: {v3[0]} out of: {v3[1]} || Mistakes: {v3[2]}')
                                        else:
                                            # If not, print the name for reference
                                            print(f'\t{layer3} ',end='')
                                    # The last layer should only contain a list, so iterate through and print all scores
                                    else:
                                        for layer4, v4 in dct[title][layer1][layer2][layer3].items():
                                            print(f'\n\t{layer4} || Score: {v4[0]} out of: {v4[1]} || Mistakes: {v4[2]}')
                    # Print in between major parts of the test
                    print('----------------') 
        # Print this line in between tests. Stop between each test and wait for user to press enter to proceed.
        print('\n\n================')  
        while True:
            input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
            break