import copy
# ADD A NEW SCORED TEST
def add_scores(test_raw, test_index):
    if len(test_raw) < 1:
        print(f'\n========================================================\n| Please add at least one test score in order to view. |\n========================================================')
    else:
        # Initialize variables
        subfold1 = [] # A list of dictionaries for the first layer of sections in the test
        subfold2 = [] # A list of dictionaries for the second layer of sections in the test
        subfold3 = [] # A list of dictionaries for the third layer of sections in the test
        subfold4 = [] # A list of dictionaries for the final layer of sections- which can only be scores- in the test
        new_dct = {} # A dictionary that will hold all dictionaries
        dct = {} # This will be a deep copy of the index to work off
        print('\nHere are your test names and locations:\n')
        # Display the name and locaton of each test structure in the index. Index +1 is displayed to be user-friendly
        for c, i in enumerate(test_index):
            print(f'Test structure: {i["name"]} || Test location: {c+1}')
        while True:
            try:
                # User chooses test to add
                test_choice = int(input('---\n\nPlease enter the location of the test you want to add a score for: '))-1
                # User must choose from index 0 to the last number in the list
                if test_choice > len(test_index)-1 or test_choice < 0:
                    print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================\n')
                    continue
                else:
                    break
            except ValueError:
                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                continue
        # Create a deep copy of the test structure to iterate through and add scores, mistakes to
        dct = copy.deepcopy(test_raw[test_choice])
        # For first level of sections -> CHANGE this name later
        for title, v in dct.items():
            # Print the name of the section
            print(f'\nTest Name: {title}\n----------------') 
            # If the value is a not a dictionary of other subsections
            if isinstance(v, dict) != True:
                test = v
                # Check to make sure that it is a list, then get user input
                if isinstance(test, list) == True:
                    while True:
                        try:
                            # Get the score from the user from 0 to the maximum score
                            u_score = int(input(f'\nWhat was your score out of {v[1]}? '))
                            if u_score > v[1] or test_choice < 0:
                                print(f'\n======================================\n| Please enter a number from 0 to {v[1]}. |\n======================================\n')
                                continue
                            else:
                                break
                        except ValueError:
                            print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                            continue
                    # If the score is less than the maximum score, require user to input at least one mistake
                    if u_score < v[1] and len(test_index[test_choice]['mistakes']) > 0:
                        add_m = 'undefined'
                        # Create a list of mistakes that the user made on this specific section
                        tmp_m_lst = []
                        # User adds the name of their mistake
                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                            u_mistake = input('Please enter mistakes one at a time: ').strip()
                            # Reject mistake if user did not enter it into mistake types when creating this structure
                            if u_mistake not in test_index[test_choice]['mistakes']:
                                print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                continue
                            # Reject mistake if mistake is already entered mistake has nothing entered
                            elif u_mistake in tmp_m_lst and u_mistake != '':
                                print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                continue
                            # Reject mistake if mistake has nothing entered or entered the default
                            elif u_mistake == 'none :)' or u_mistake == '':
                                print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                continue
                            # If conditions are met, accept mistake and append it to the list of mistakes for this problem
                            else:
                                tmp_m_lst.append(u_mistake)
                                # If no mistakes have yet been entered
                                if dct[title][2] == 'none :)':
                                    while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']): # Until not all mistakes have been entered
                                        # Check if user wants to proceed to add more mistakes
                                        try:
                                            add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                            # Only accept 'y' or 'n' as input
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
                                    # If user wishes to proceed, continue through to add more mistake types for this section
                                    if add_m[0] == 'y':
                                        continue
                                    # If user does not wish to proceed, add this section with its name and score information to the list of dictionaries
                                    else:
                                        subfold1.append({'name':title, 'score':[u_score, dct[title][1], ', '.join(tmp_m_lst)]})
                                        break
                                # If at least one mistake has already been entered
                                else:
                                    while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                        # Check if user wants to proceed to add more mistakes
                                        try:
                                            add_m = input('Would you like to add another mistake? Y/N ').lower().strip()
                                            # Only accept 'y' or 'n' as input
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
                                    # If user wishes to proceed, continue through to add more mistake types for this section
                                    if add_m[0] == 'y':
                                        continue
                                    # If user does not wish to proceed, add this section with its name and score information to the list of dictionaries
                                    else:
                                        subfold1.append({'name':title, 'score':[u_score, dct[title][1], ', '.join(tmp_m_lst)]})
                                        break
                        # If there are no remaining mistakes, add this section with its name and score information to the list of dictionaries 
                        else:
                            subfold1.append({'name':title, 'score':[u_score, dct[title][1], ', '.join(tmp_m_lst)]})
                            print("---\nNo remaining mistake types.\n")
                    # If there is a perfect score, add this section with its name and score information to the list of dictionaries (no need to check for mistake types)
                    elif u_score == v[1]:
                        subfold1.append({'name':title, 'score':[u_score, dct[title][1], dct[title][2]]})
                ### Diagnose this condition when refactoring- MAY BE UNNEEDED
                else:
                    print('\n==============================================\n| ERROR: THIS IS INVALID. CONTACT DEVELOPER. |\n==============================================\n')
                    pass
            # If the value of the first section is a dictionary of subsections, iterate through 
            else:
                # Append the name of the section to the first list of dictionaries
                subfold1.append({'name':title})
                # Iterate through the first second layer of subsections
                for layer1, v1 in dct[title].items():
                    # Print the name of the subsection
                    print(f'\n{layer1}')
                    # Check to make sure that it is a list, then get user input
                    if isinstance(dct[title][layer1], dict) != True:
                        test = v1
                        if isinstance(test, list) == True:
                            while True:
                                try:
                                    # Get the score from the user from 0 to the maximum score
                                    u_score = int(input(f'\nWhat was your score out of {v1[1]}? '))
                                    if u_score > v1[1] or test_choice < 0:
                                        print(f'\n======================================\n| Please enter a number from 0 to {v1[1]}. |\n======================================\n')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                    continue
                            # If the score is less than the maximum score, require user to input at least one mistake
                            if u_score < v1[1] and len(test_index[test_choice]['mistakes']) > 0:
                                add_m = 'undefined'
                                # Create a list of mistakes that the user made on this specific section
                                tmp_m_lst = []
                                # User adds the name of their mistake
                                while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                    u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                    # Reject mistake if user did not enter it into mistake types when creating this structure
                                    if u_mistake not in test_index[test_choice]['mistakes']:
                                        print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                        continue
                                    # Reject mistake if mistake is already entered mistake has nothing entered
                                    elif u_mistake in tmp_m_lst and u_mistake != '':
                                        print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                        continue
                                    # Reject mistake if mistake has nothing entered or entered the default
                                    elif u_mistake == 'none :)' or u_mistake == '':
                                        print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                        continue
                                    # If conditions are met, accept mistake and append it to the list of mistakes for this problem
                                    else:
                                        tmp_m_lst.append(u_mistake)
                                        # If no mistakes have yet been entered
                                        if dct[title][layer1][2] == 'none :)':
                                            while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                # Check if user wants to proceed to add more mistakes
                                                try:
                                                    add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                    # Only accept 'y' or 'n' as input
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
                                            # If user wishes to proceed, continue through to add more mistake types for this section
                                            if add_m[0] == 'y':
                                                continue
                                            # If user does not wish to proceed, add this section with its name and score information to the list of dictionaries
                                            else:
                                                subfold2.append({'parent':title, 'name':layer1, 'score':[u_score, dct[title][layer1][1], ', '.join(tmp_m_lst)]})
                                                break
                                        # If at least one mistake has already been entered
                                        else:
                                            while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                try:
                                                    # Check if user wants to proceed to add more mistakes
                                                    add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                    # Only accept 'y' or 'n' as input
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
                                            # If user wishes to proceed, continue through to add more mistake types for this section
                                            if add_m[0] == 'y':
                                                continue
                                            # If user does not wish to proceed, add this section with its name and score information to the list of dictionaries
                                            else:
                                                subfold2.append({'parent':title, 'name':layer1, 'score':[u_score, dct[title][layer1][1], ', '.join(tmp_m_lst)]})
                                                break
                                # If there are no remaining mistakes, add this section with its name and score information to the list of dictionaries 
                                else:
                                    subfold2.append({'parent':title, 'name':layer1, 'score':[u_score, dct[title][layer1][1], ', '.join(tmp_m_lst)]})
                                    print("---\nNo remaining mistake types.\n")
                            # If there is a perfect score, add this section with its name and score information to the list of dictionaries (no need to check for mistake types)
                            elif u_score == v1[1]:
                                subfold2.append({'parent':title, 'name':layer1, 'score':[u_score, dct[title][layer1][1], dct[title][layer1][2]]})
                        
                        # If this not a dictionary or a list,  print the name of the subsection ### CONSIDER DELETING- THIS MAY BE AN ARTIFACT
                        else:
                            print(f'\n{layer1}') 
                    # If the value of the second section is a dictionary of subsections, iterate through 
                    else:
                        # Append the name of the section to the second list of dictionaries
                        subfold2.append({'parent':title,'name':layer1})
                        # Iterate through the second second layer of subsections
                        for layer2, v2 in dct[title][layer1].items():
                            # Print the name of the subsection
                            print(f'\n{layer2} : ')
                            # Check to make sure that it is a list, then get user input
                            if isinstance(dct[title][layer1][layer2], dict) != True:
                                test = v2
                                if isinstance(test, list) == True:
                                    while True:
                                        # Get the score from the user from 0 to the maximum score
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
                                    # If the score is less than the maximum score, require user to input at least one mistake
                                    if u_score < v2[1] and len(test_index[test_choice]['mistakes']) > 0:
                                        add_m = 'undefined'
                                        # Create a list of mistakes that the user made on this specific section
                                        tmp_m_lst = []
                                        # User adds the name of their mistake
                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                            u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                            # Reject mistake if user did not enter it into mistake types when creating this structure
                                            if u_mistake not in test_index[test_choice]['mistakes']:
                                                print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                                continue
                                            # Reject mistake if mistake is already entered mistake has nothing entered
                                            elif u_mistake in tmp_m_lst and u_mistake != '':
                                                print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                                continue
                                            # Reject mistake if mistake has nothing entered or entered the default
                                            elif u_mistake == 'none :)' or u_mistake == '':
                                                print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                                continue
                                            # If conditions are met, accept mistake and append it to the list of mistakes for this problem
                                            else:
                                                tmp_m_lst.append(u_mistake)
                                                # If no mistakes have yet been entered
                                                if dct[title][layer1][layer2][2] == 'none :)':
                                                    while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                        # Check if user wants to proceed to add more mistakes
                                                        try:
                                                            add_m = input('Would you like to add another mistake? Y/N ').lower().strip()
                                                            # Only accept 'y' or 'n' as input
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
                                                    # If user wishes to proceed, continue through to add more mistake types for this section
                                                    if add_m[0] == 'y':
                                                        continue
                                                    # If user does not wish to proceed, add this section with its name and score information to the list of dictionaries
                                                    else:
                                                        subfold3.append({'parent':layer1, 'name':layer2, 'score':[u_score, dct[title][layer1][layer2][1], ', '.join(tmp_m_lst)]})
                                                        break
                                                # If at least one mistake has already been entered
                                                else:
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
                                                    # If user wishes to proceed, continue through to add more mistake types for this section
                                                    if add_m[0] == 'y':
                                                        continue
                                                    # If user does not wish to proceed, add this section with its name and score information to the list of dictionaries
                                                    else:
                                                        subfold3.append({'parent':layer1, 'name':layer2, 'score':[u_score, dct[title][layer1][layer2][1], ', '.join(tmp_m_lst)]})
                                                        break
                                        # If there are no remaining mistakes, add this section with its name and score information to the list of dictionaries 
                                        else:
                                            subfold3.append({'parent':layer1, 'name':layer2, 'score':[u_score, dct[title][layer1][layer2][1], ', '.join(tmp_m_lst)]})
                                            print("---\nNo remaining mistake types.\n")
                                    # If there is a perfect score, add this section with its name and score information to the list of dictionaries (no need to check for mistake types)
                                    elif u_score == v2[1]:
                                        subfold3.append({'parent':layer1, 'name':layer2, 'score':[u_score, dct[title][layer1][layer2][1], dct[title][layer1][layer2][2]]})
                                # If this not a dictionary or a list,  print the name of the subsection ### CONSIDER DELETING- THIS MAY BE AN ARTIFACT
                                else:
                                    print('\n' + layer2 + " : " + str(dct[title][layer1][layer2]))
                            # If the value of the third section is a dictionary of subsections, iterate through 
                            else:
                                # Append the name of the section to the third list of dictionaries
                                subfold3.append({'parent':layer1,'name':layer2})
                                # Iterate through the third and final layer of subsections to append the fourth layer
                                # As there can be no more lists deeper than this, we will not check for dictionaries now (we already have above for this section) 
                                for layer3, v3 in dct[title][layer1][layer2].items():
                                    # Print the name of the subsection
                                    print(f'{layer3} : ')
                                    while True:
                                        # Get the score from the user from 0 to the maximum score
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
                                    # If the score is less than the maximum score, require user to input at least one mistake
                                    if u_score < v3[1] and len(test_index[test_choice]['mistakes']) > 0:
                                        add_m = 'undefined'
                                        # Create a list of mistakes that the user made on this specific section
                                        tmp_m_lst = []
                                        # User adds the name of their mistake
                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                            u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                            # Reject mistake if user did not enter it into mistake types when creating this structure
                                            if u_mistake not in test_index[test_choice]['mistakes']:
                                                print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                                continue
                                            # Reject mistake if mistake is already entered mistake has nothing entered
                                            elif u_mistake in tmp_m_lst and u_mistake != '':
                                                print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                                continue
                                            # If conditions are met, accept mistake and append it to the list of mistakes for this problem
                                            elif u_mistake == 'none :)' or u_mistake == '':
                                                print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                                continue
                                            # If conditions are met, accept mistake and append it to the list of mistakes for this problem
                                            else:
                                                tmp_m_lst.append(u_mistake)
                                                # If no mistakes have yet been entered
                                                if dct[title][layer1][layer2][layer3][2] == 'none :)':
                                                    while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                        # Check if user wants to proceed to add more mistakes
                                                        try:
                                                            add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                            # Only accept 'y' or 'n' as input
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
                                                    # If user wishes to proceed, continue through to add more mistake types for this section
                                                    if add_m[0] == 'y':
                                                        continue
                                                    # If user does not wish to proceed, add this section with its name and score information to the list of dictionaries
                                                    else:
                                                        subfold4.append({'gparent':layer1, 'parent':layer2, 'name':layer3, 'score':[u_score, dct[title][layer1][layer2][layer3][1], ', '.join(tmp_m_lst)]})
                                                        break
                                                # If at least one mistake has already been entered
                                                else:
                                                    while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                        try:
                                                            # Check if user wants to proceed to add more mistakes
                                                            add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                            # Only accept 'y' or 'n' as input
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
                                                    # If user wishes to proceed, continue through to add more mistake types for this section
                                                    if add_m[0] == 'y':
                                                        continue
                                                    # If user does not wish to proceed, add this section with its name and score information to the list of dictionaries
                                                    else:
                                                        subfold4.append({'gparent':layer1, 'parent':layer2, 'name':layer3, 'score':[u_score, dct[title][layer1][layer2][layer3][1], ', '.join(tmp_m_lst)]})
                                                        break
                                        # If there are no remaining mistakes, add this section with its name and score information to the list of dictionaries 
                                        else:
                                            subfold4.append({'gparent':layer1, 'parent':layer2, 'name':layer3, 'score':[u_score, dct[title][layer1][layer2][layer3][1], ', '.join(tmp_m_lst)]})
                                            print("---\nNo remaining mistake types.\n")
                                    # If there is a perfect score, add this section with its name and score information to the list of dictionaries (no need to check for mistake types)
                                    elif u_score == v3[1]:
                                        subfold4.append({'gparent':layer1, 'parent':layer2, 'name':layer3, 'score':[u_score, dct[title][layer1][layer2][layer3][1], dct[title][layer1][layer2][layer3][2]]})
                    # Divide each main section with a line
                    print('----------------') 
                # Print a thick line once all information has been input
                print('\n\n================')
                ## print(f'\n{subfold1}\n\n{subfold2}\n\n{subfold3}\n\n{subfold4}') ## This is for error checking
            # After all final sections have been added to the last list of dictionaries, iterate through ALL sections, starting with the list of main sections
            for prim_f in subfold1:
                # If the section includes more dictionaries of other sections, proceed
                if 'score' not in prim_f.keys():
                    dict2 = {}
                    # Iterate through all subsections of this section
                    for sec_f in subfold2:
                        # If the section includes more dictionaries of other sections, proceed
                        if 'score' not in sec_f.keys():
                            # If the subsection has the right parent folder, update a second dictionary of sections
                            if sec_f['parent'] == prim_f['name']:
                                dict3 = {}
                                # Iterate through all subsections of this section
                                for ter_f in subfold3:
                                    # If the section includes more dictionaries of other sections, proceed
                                    if 'score' not in ter_f.keys():
                                        # If the subsection has the right parent folder, update a third dictionary of sections
                                        if ter_f['parent'] == sec_f['name']:
                                            dict4 = {}
                                            # Iterate through all subsections of this section
                                            for quad_f in subfold4:
                                                # If the subsection has the right parent and grandparent folder, update a fourth (the deepest) dictionary of sections
                                                if quad_f['gparent'] == ter_f['parent'] == sec_f['name']:
                                                    dict4.update({quad_f['name']:quad_f['score']})
                                                else:
                                                    pass
                                            # Once all relevant sections are added to the the fourth dictionary, update the third dictionary
                                            dict3.update({ter_f['name']:dict4})
                                        else:    
                                            continue
                                    # If the section has no sections, add that section and its score set to the third dictionary
                                    elif ter_f['parent'] == sec_f['name']:
                                        dict3.update({ter_f['name']:ter_f['score']})
                                # Once all relevant sections are added to the the third dictionary, update the second dictionary
                                dict2.update({sec_f['name']:dict3})
                            else:
                                continue
                        # If the section has no sections, add that section and its score set to the second dictionary
                        elif sec_f['parent'] == prim_f['name']:
                            dict2.update({sec_f['name']:sec_f['score']})
                        else:
                            continue
                    # Once all relevant sections are added to the the second dictionary, update the main dictionary
                    new_dct.update({prim_f['name']:dict2})
                # If the section has no sections, add that section and its score set to the second dictionary
                else:
                    new_dct.update({prim_f['name']:prim_f['score']})
            # Create the test dictionary with the test name as the main key, then return the name of the test, the dictionary, it's maximum and how many layers deep the test is
            dct = {test_index[test_choice]['name']:new_dct}
            print('\nScores successfully added. Returning to menu.')
            return test_choice, dct 
