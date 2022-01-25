# ANALYZE TEST SCORES
def analyze(test_db, test_index):
    # Initialize all variables
    score = 0 # Total score per test
    num_tests = 0 # Number of tests of a chosen type
    total_s = 0 # Combined score of all tests
    avg = 0 # Average score per test
    max_s = 0 # Highest score possible
    top_s = 0 # Top score achieved
    top_n = '' # Top score's test name
    low_s = 1000000000 # Lowest score achieved
    low_n = '' # Low score's test name
    m_list = [] # List of mistake types for chosen test type

    # If no scores in test database for this score, return to loop
    if test_db == []:
        print(f'\n====================================================\n| Please submit a new test score in order to view. |\n====================================================')
    # Else list out available tests to choose from
    else:
        print('\nHere are your test names and locations:\n-> Enter "q" to return to main menu\n---\n')
        # Display tests in index for user to choose from (locations are from 1 for better user experience)
        for c, i in enumerate(test_index):
            print(f'Test structure: {i["name"]} || Test location: {c+1}')
        while True:
            try:
                # Take user choice for test location
                test_choice = int(input('---\n\nPlease enter the location of your tests: '))-1
                # Do not accept choice if choice is out of the range of tests available
                if test_choice > len(test_index) or test_choice < 0:
                    print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================')
                    continue
                # Do not accept choice if there are no scores in the database for that test type
                elif test_db[test_choice] == []:
                    print(f'\n===================================================\n| There are not yet any scores for this test type |\n===================================================')
                    continue
                # Accept the choice if it meets all criteria
                else:
                    break
            except:
                # If the user did not enter a number, break from function to return to main menu
                print(f'\n===============================================\n| Letter entered. Now returning to main menu. |\n===============================================')
                return
        
        num_tests = len(test_db[test_choice]) # Number of tests is the length of the list inside the database list at the chosen index location
        max_s = test_index[test_choice]['maxscore'] # Maximum score is the maximum score value added from when the structure was created and added to the index
        tests = test_db[test_choice] # The list of tests is all tests in the list inside the database list at the chosen index location

        tmp_mlist = test_index[test_choice]['mistakes'] # "Tmp_mlist" is simplified variable mistake types available for this test 
        # Convert string of mistakes into a list of dictionaries that counts mistakes overall
        for each in tmp_mlist:
            m_list.append({'name':each.strip(), 'count':0})
        # For each test
        for c, dct in enumerate(tests):
            # For first sections in the test
            for title, v in dct.items():
                if isinstance(v, dict) != True:
                    test = v
                    # If this is a list of scores and mistakes, add to test's score and count mistakes
                    if isinstance(test, list) == True:
                        score += v[0]
                        for type in m_list:
                            if type['name'] in v[2]:
                                type['count'] += 1
                            else:
                                pass
                    # If this is not a dictionary of more sections or a list of scores, do nothing
                    else:
                        print()
                        pass
                # If this is a a dictionary of more sections, iterate through the second layer of sections
                else:
                    for layer1, v1 in dct[title].items():
                        if isinstance(dct[title][layer1], dict) != True:
                            test = v1
                            # If this is a list of scores and mistakes, add to test's score and count mistakes
                            if isinstance(test, list) == True:
                                score += v1[0]
                                for type in m_list:
                                    if type['name'] in v1[2]:
                                        type['count'] += 1
                                    else:
                                        pass
                            # If this is not a dictionary of more sections or a list of scores, do nothing
                            else:
                                pass 
                        # If this is a a dictionary of more sections, iterate through the third layer of sections
                        else:
                            for layer2, v2 in dct[title][layer1].items():
                                if isinstance(dct[title][layer1][layer2], dict) != True:
                                    test = v2
                                    # If this is a list of scores and mistakes, add to test's score and count mistakes
                                    if isinstance(test, list) == True:
                                        score += v2[0]
                                        for type in m_list:
                                            if type['name'] in v2[2]:
                                                type['count'] += 1
                                            else:
                                                pass
                                    # If this is not a dictionary of more sections or a list of scores, do nothing
                                    else:
                                        pass
                                # If this is a a dictionary of more sections, iterate through the third layer of sections
                                else:
                                    for layer3, v3 in dct[title][layer1][layer2].items():
                                        # If this is a list of scores and mistakes, add to test's score and count mistakes
                                        if isinstance(dct[title][layer1][layer2][layer3], dict) != True:
                                            score += v3[0]
                                            for type in m_list:
                                                if type['name'] in v3[2]:
                                                    type['count'] += 1
                                                else:
                                                    pass
                                        # If this is a a dictionary of more sections, iterate through the final fourth layer of sections
                                        else:
                                            for layer4, v4 in dct[title][layer1][layer2][layer3].items():
                                                # Add to test's score and count mistakes
                                                score += v4[0]
                                                for type in m_list:
                                                    if type['name'] in v4[2]:
                                                        type['count'] += 1
                                                    else:
                                                        pass
            # If test's score is larger than the top score, update the top score and top score's name
            if score > top_s:
                top_s = score
                top_n = str(c)
            # If scores are the same, at the score to the name
            elif score == top_s:
                top_n += f', {str(c)}'
            # If test's score is less than the top score, update the lowest score and lowest score's name
            if score < low_s:
                low_s = score
                low_n = str(c)
            # If scores are the same, at the score to the name
            elif score == low_s:
                low_n += f', {str(c)}' 
        # Add the tests score to overall score
        total_s += score
        # The average test score is the overall score divided by the number of tests
        a_score = float(total_s) / num_tests
        # The name of this type of test
        name = test_index[test_choice]['name']
        # The index of the test +1 converted to a string for readability
        top_n = str(int(top_n) + 1)
        low_n = str(int(low_n) + 1)
        # Print main analysis
        print(f'''
    =====================================
    |          Score Analysis           |
    ------------------------------------|
    | Name of test: ............. {name}
    | Number of tests: .......... {num_tests}
    | Maximum score possible .... {max_s}
    |-----------------------------------
    | Overall score average ..... {a_score}
    |-----------------------------------
    | Top score on ............ test #{top_n}
    | Overall top score ......... {top_s}
    | Lowest score on ......... test #{low_n}
    | Overall lowest score ...... {low_s}
    |===================================|
    |         Mistakes Rankings         |
    |-----------------------------------|''')

        # Sort mistakes is ascending order
        tally = sorted(m_list, key=lambda k: k['count'])
        # If 6 or more mistake types, display the top three least and most common mistakes
        if len(tmp_mlist) >= 6:
            print('    | Least common mistakes:')
            for mst in tally[0:3]: # Ascending order
                print(f"\t| {mst['name']}: {mst['count']} times")
            print('    | Most common mistakes:')
            for mst in tally[-3::-1]: # Descending order
                print(f"\t| {mst['name']}: {mst['count']} times")
        # If 4 or 5 mistake types, display the top two least and most common mistakes
        if len(tmp_mlist) < 6 and len(tally) > 3:
            print('    | Least common mistakes:')
            for mst in tally[0:2]: # Ascending order
                print(f"    | {mst['name']}: {mst['count']} times")
            print('    | Most common mistakes:')
            for mst in tally[-2::-1]: # Descending order
                print(f"    | {mst['name']}: {mst['count']} times")
        # If three or less mistake types, print all mistakes from the least to most common
        else:
            print('    | From least to most common:        |')
            for mst in tally:
                print(f"    | {mst['name']}: {mst['count']} times")

        print('    =====================================\n')
        # Hold page until user continues
        while True:
            input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
            break   