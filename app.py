import copy # Import to deep copy test structures and make new dictionaries without affecting originals

def main():
    choice = 'undefined'
    print('''-----------------



  ______          __     ______                __            
 /_  __/__  _____/ /_   /_  __/________ ______/ /_____  _____
  / / / _ \/ ___/ __/    / / / ___/ __ `/ ___/ //_/ _ \/ ___/
 / / /  __(__  ) /_     / / / /  / /_/ / /__/ ,< /  __/ /    
/_/  \___/____/\__/    /_/ /_/   \__,_/\___/_/|_|\___/_/ 
                                            ____
     _   _____  __________(_)___  ____     / __ \                
    | | / / _ \/ ___/ ___/ / __ \/ __ \   / / / /                
    | |/ /  __/ /  (__  ) / /_/ / / / /  / /_/ /                 
    |___/\___/_/  /____/_/\____/_/ /_/   \____/                  
                                                     
''')

    # Ask for name (add to variable)
    name = input('\n\nWelcome to Test Tracker! Please enter your name: ')
    # Greet user
    print(f'\nWelcome, {name}!\n\nPlease create at least one test structure to continue.')

    # Initialize data structures
    test_raw = [] # Test structures
    test_db = [] # Test scores
    test_index = [] # Test name, location in raw/db and mistake lists

    # Main loop runs until users quit by pressing 'q'
    while choice != False and choice[0] != 'q':
        if choice == 'undefined':
            while True:
                try:
                    choice = (input('''
    ===============================================
    |                  Main Menu                  |
    -----------------------------------------------
    | View your scores ................ press 'V' |
    | View a score analysis ........... press 'A' |
    | Add a new score ................. press 'N' |
    | Create another test structure ... press 'S' |
    | Exit the program ................ press 'Q' |
    ===============================================

Enter an option: ''')).lower().strip()
                    # Only accept the options in the menu
                    if choice[0] == 'v' or choice[0] == 'a' or choice[0] == 'n' or choice[0] == 's' or choice[0] == 'q':
                        break
                    # If input is not a string, reject input
                    elif isinstance(choice, str) == False:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                   # If the first letter is anything else aside from one of the letters, reject input
                    else:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                except IndexError:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            # VIEW TESTS
            if choice[0] == 'v':
                # Reject this choice if there are no test structures
                if len(test_raw) < 1 or len(test_index) < 1:
                    print(f'\n========================================================\n| Please add at least one test score in order to view. |\n========================================================')
                    choice = 'undefined'
                    continue
                else:
                    print('\nHere are your test names and locations:\n')
                    # Display the name and locaton of each test structure in the index. Index +1 is displayed to be user-friendly
                    for c, i in enumerate(test_index):
                        print(f'Test structure: {i["name"]} || Test location: {c+1}')
                    while True:
                        try:
                            # User chooses test to view
                            test_choice = int(input('---\n\nPlease enter the location of your tests:\n-> Enter "q" to return to main menu\n---\n'))-1
                            # User must choose from index 0 to the last number in the list
                            if test_choice > len(test_index) or test_choice < 0:
                                print(f'\n==================================\n| Please enter a number up to {len(test_index)+1}. |\n==================================')
                                continue
                            # Reject input if there is no score yet added for this test
                            elif test_db[test_choice] == []:
                                print(f'\n===================================================\n| There are not yet any scores for this test type |\n===================================================')
                                continue
                            else:
                                # Accept input and break if all conditions are met
                                break
                        except:
                            # If input throws an error, remind user only to enter numbers, return to main menu in case input was 'q'
                            print(f'\n===============================================\n| Letter entered. Now returning to main menu. |\n===============================================')
                            break
                    #Choose all tests in database at the location the user chose
                    try:
                        tests = test_db[test_choice]
                        print(f'\nBelow are all test results for test "{test_index[test_choice-1]["name"]}:"\n================\n')
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
                    except IndexError:
                        print('\n-> Returning to main menu')
                        choice = 'undefined'
                        continue
                    # Reset choice to undefined and continue through the main loop
                    choice = 'undefined'
                    continue
            # ANALYZE TEST RESULTS
            elif choice[0] == 'a':
                # Reject this choice if there are no test scores 
                if len(test_db) < 1 or len(test_index) < 1:
                    print(f'\n========================================================\n| Please add at least one test score in order to view. |\n========================================================')
                    choice = 'undefined'
                    continue
                else:
                    # Call analyze function with database and test index as parameters
                    analyze(test_db, test_index)
                    # After function completes, reset choice to undefined and continue through the main loop
                    choice = 'undefined'
                    continue
            # ADD NEW TEST SCORES
            elif choice[0] == 'n':
                # Reject this choice if there are no test structures
                if len(test_raw) < 1 or len(test_index) < 1:
                    print(f'\n============================================================\n| Please add at least one test structure in order to view. |\n============================================================')
                    choice = 'undefined'
                    continue
                else:
                    # Call function to add new scores, pass the raw tests and test index as parameters
                    index, scores = add_scores(test_raw, test_index)
                    # Append new test to the to database at the correct index
                    test_db[index].append(scores)
                    # print(test_db) ### CONSIDER DELETING THIS PRINT STATEMENT
                    # After function completes, reset choice to undefined and continue through the main loop
                    choice = 'undefined'
                    continue
            # ADD NEW TEST STRUCTURE
            elif choice[0] == 's':
                # Call function to make new test structure
                # 'testname't is the test's name, 'dct' is the structure, 'total' is the total possible score and 'levels' is the how many layers are in the score up to 4
                testname, dct, total, levels = make_test_shell()
                # Add a new space into the database to store all scores of this test type
                test_db.append([])
                # Add test structure to the list of test structures
                test_raw.append(dct)
                # Add spot on test index with information for analysis
                test_index.append({'name':testname, 'maxscore':total, 'mistakes':make_mlist()})
                # Print completed structure so user understands results
                print(f'\nTest "{testname}" created. Please see below:\n')
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
                            print(f'{layer1}')
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
                # Let user view test print out before returning to main menu
                while True:
                    input('\nPress enter to continue.\n----------------\n')
                    break
                choice = 'undefined'
                continue
            # When user closes app with 'q', close app.
            else:
                print('''
Thank you for using Test Tracker version 0!

   ______                ____               __
  / ____/___  ____  ____/ / /_  __  _____  / /
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ / 
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/  
\____/\____/\____/\__,_/_.___/\__, /\___(_)   
                             /____/          
                             
''')
                choice = False

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
                                # If no mistakes habe yet been entered
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

# Choose between simple and custom test types
def make_test_shell():
    choice = 'undefined'
    while choice != False and choice[0] != 'c' and choice[0] != 's':
        if choice == 'undefined':
            while True:
                try: # Choose simple or custom test build
                    choice = (input('''\n-----------------\n\nWould you like to make a simple test or a custom test?

============================
| Simple Test:             |
----------------------------===============================
| Each part in a simple test has the same number of parts.|
| These are faster to set up and perfect for small or     |
| simply organized tests.                                 |
|                          --> Type S for a 'simple test' |
===========================================================

============================
| Custom Test:             |
----------------------------================================
| Every part in a custom test is customized by the user.   | 
| Each part can be arranged in different ways. This takes  |
| more time, but is good if your test is large or arranged |
| in a more complex way.                                   |
|                           --> Type C for a 'custom test' |
============================================================

Please choose S/C: ''')).lower().strip()
                    # Only accept input if that is a choice for simple or complex test structures
                    if choice[0] == 's' or choice[0] == 'c':
                        break
                    elif isinstance(choice, str) == False:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                    else:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                except IndexError:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            # If user chooses a simple test, take a name for the test, then create a simple test with the name as the parameter
            if choice[0] == 's':
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2: # Names should be from 3-20 characters in length for readability
                        print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                        continue
                    else:
                        return build_simple_dict(testname)
            # If user chooses a custom test, take a name for the test, then create a custom test with the name as the parameter
            else:
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2: # Names should be from 3-20 characters in length for readability
                        print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                        continue
                    else:
                        return build_custom_dict(testname)

# BUILD A SIMPLE TEST (Less detailed input)
def build_simple_dict(testname):
    # Initialize variables
    moreLevels = 'undefined' # User chooses whether they will divide sections into more parts ('y' or 'n')
    proceed_num = 0 # Add to this variable if user chooses to divide a section into more parts
    maxScore = 0 # The maximum score for a particular part of a test
    totalMax = 0 # The overall maximum score for a test type
    numLevels = 0 # The number of levels deep a test is divided 
    sectCount1 = 0 # The number of parts a section is divided into
    sectCount2 = 0 # The number of parts a section is divided int
    subfold1 = [] # A list of dictionaries for the first layer of sections in the test
    subfold2 = [] # A list of dictionaries for the second layer of sections in the test
    subfold3 = [] # A list of dictionaries for the third layer of sections in the test
    dict1 = {} # A dictionary that will hold all dictionaries

    while moreLevels != False and moreLevels[0] != 'n':
        if moreLevels == 'undefined':
            # Require user to choose whether they will divide the section into more parts
            while True:
                try:
                    moreLevels = (input('\n-----------------\n\nIs this divided into parts? Y/N ')).lower().strip()
                    if moreLevels[0] == 'y' or moreLevels[0] == 'n':
                        break
                    elif isinstance(moreLevels, str) == False:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                    else:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                except IndexError:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            # If the user choose to divide the section into more parts, proceed
            if moreLevels[0] == 'y':
                numLevels += 1 # The test is divided at least one time
                while True:
                    # User decides how many times to divide the test (from 1-10 times)
                    try:
                        get_subSize1 = int(input('\nHow many identical parts? '))
                        if get_subSize1 > 10 or get_subSize1 < 1:
                            print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                        continue
                print(f'\nPlease enter the name(s) for the section(s)\n-----------------') 
                names = [] # List of names that all names are appended to
                # Based on how many parts the user chose to divide into, get a name for each part
                for i in range(get_subSize1):
                    while True:
                        subName1 = input(f'Please enter a section name for section {i+1}: ') # Name the section (from 3-20 characters in length)
                        if len(subName1) > 20 or len(subName1) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            names.append(subName1)
                            break
                # Ask whether user wants to divide *all* of these sections into more sections
                while True:
                    try:
                        # Require user to choose whether they will divide the section into more parts
                        moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                        # If user decides to divide into more parts, proceed
                        if moreLevels[0] == 'y':
                            proceed_num += 1 # Add to the number -> this means will we create another level of sections within the previous section
                            while True:
                                # User decides how many times to divide these sections (from 1-10 times)
                                try:
                                    sectCount1 = int(input(f'Please enter the number of sections: '))
                                    print('-')
                                    if sectCount1 > 10 or sectCount1 < 1:
                                        print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                    continue
                            # Add a list of dictionaries for each section's sections, with the number of times it is divided as 'count'
                            for name in names:
                                subfold1.append({'name':name, 'count':sectCount1})
                            break
                        # If user decides not to divide into more parts, proceed
                        elif moreLevels[0] == 'n':
                            # Get the maximum score for each section
                            while True:
                                try:
                                    maxScore = int(input(f'What is the maximum score for each these sections? '))
                                    if maxScore < 1:
                                        print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print('\n=============================\n| Please enter only digits. |\n=============================')
                            # Add a list of dictionaries with the name of the section and the score list ("actual score, maximum score, mistakes")
                            for name in names:
                                subfold1.append({'name':name, 'score':['tbd', maxScore, 'none :)']})
                                totalMax += maxScore
                            break
                        # Only accept numbers
                        elif isinstance(moreLevels, str) == False:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                        else:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                    except IndexError:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
            # If user does not want to divide the test into parts at all, make a very simple test structure 
            else:
                while True:
                    try:
                        maxScore = int(input(f'What is the maximum score for {testname}? ')) # Take the maximum score for this part
                        if maxScore < 1:
                            print('\n==================================\n| Please enter a number above 1. |\n==================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n=============================\n| Please enter only digits. |\n=============================')
                # Create a test, add score to the test's maximum score and return the name of the test, the dictionary, it's maximum and how many layers deep the test is
                test = {testname:['tbd', maxScore, 'none :)']}
                totalMax += maxScore
                return testname, test, totalMax, numLevels
            # If a section was divided at least once more, proceed to second layer of sections
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1 # The test is divided a second time
                # Iterate through all first sections
                for i in subfold1:
                    if 'score' in i.keys(): # Skip all sections that contain scores, since they are not divided
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        names = [] # List of names that all names are appended to
                        # Based on how many parts the user chose to divide into, get a name for each part
                        for j in range(i['count']):
                            while True:
                                subName2 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName2) > 20 or len(subName2) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    names.append(subName2)
                                    break
                        # Add a list of dictionaries for each section's sections, with the number of times it is divided as 'count'
                        while True:
                            # Require user to choose whether they will divide the section into more parts
                            try:
                                moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                                # If user decides to divide into more parts, proceed
                                if moreLevels[0] == 'y':
                                    proceed_num += 1 # Add to the number -> this means will we create another level of sections within the previous section
                                    while True:
                                        # User decides how many times to divide these sections (from 1-10 times)
                                        try:
                                            sectCount2 = int(input(f'Please enter the number of sections: ')) 
                                            print('-')
                                            if sectCount2 > 10 or sectCount2 < 1:
                                                print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                                continue
                                            else:
                                                break
                                        except ValueError:
                                            print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                            continue
                                    # Add a list of dictionaries for each section's sections, with the number of times it is divided as 'count'
                                    for name in names:
                                        subfold2.append({'parent':i['name'], 'name':name, 'count':sectCount2}) 
                                    break
                                # If user decides not to divide into more parts, proceed
                                elif moreLevels[0] == 'n':
                                    # Get the maximum score for each section
                                    while True:
                                        try:
                                            maxScore = int(input(f'What is the maximum score for each these sections? '))
                                            if maxScore < 1:
                                                print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                                continue
                                            else:
                                                break
                                        except ValueError:
                                            print('\n=============================\n| Please enter only digits. |\n=============================')
                                    # Add a list of dictionaries with the name of the section and the score list ("actual score, maximum score, mistakes")
                                    for name in names:
                                        subfold2.append({'parent':i['name'], 'name':name, 'score':['tbd', maxScore, 'none :)']}) 
                                        totalMax += maxScore
                                    break
                                # Only accept numbers
                                elif isinstance(moreLevels, str) == False:
                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                    continue
                                else:
                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                    continue
                            except IndexError:
                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                continue
            # If the user chose not to divide ANY section, append all sections to the main dictionary and return the name of the test, the dictionary, it's maximum and how many layers deep the test is
            else:
                for layer in subfold1:
                    dict1.update({layer['name']:layer['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            # If a section was divided at least once more, proceed to third layer of sections
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1 # The test is divided a third time
                # Iterate through all second sections
                for i in subfold2:
                    if 'score' in i.keys(): # Skip all sections that contain scores, since they are not divided
                        continue
                    else:     
                        print(f'\nPlease enter the names for "{i["parent"]} - {i["name"]}"\n-----------------')
                        names = [] # List of names that all names are appended to
                        # Based on how many parts the user chose to divide into, get a name for each part
                        for j in range(i['count']):
                            while True:
                                subName3 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName3) > 20 or len(subName3) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    names.append(subName3)
                                    break
                        # Get the maximum score for each section
                        while True:
                            try:
                                maxScore = int(input(f'What is the maximum score for sections? '))
                                if maxScore < 1:
                                    print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                    continue
                                else:
                                    break
                            except ValueError:
                                print('\n=============================\n| Please enter only digits. |\n=============================')
                        # Add a list of dictionaries with the name of the section and the score list ("actual score, maximum score, mistakes")
                        for name in names:    
                            subfold3.append({'parent':i['name'], 'name':name, 'score':['tbd', maxScore, 'none :)']})
                            totalMax += maxScore
                # After all final sections have been added to the last list of dictionaries, iterate through ALL sections, starting with the list of main sections
                for prim_f in subfold1:
                    # If the section includes more dictionaries of other sections, proceed
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        # Iterate through all subsections of this section
                        for sec_f in subfold2:
                            # If the section includes more dictionaries of other sections, proceed
                            if 'score' not in sec_f.keys():
                                if sec_f['parent'] == prim_f['name']:
                                    dict3 = {}
                                    # Iterate through all subsections of this section
                                    for ter_f in subfold3:
                                        # If the subsection has the right parent folder, update a third dictionary of sections
                                        if ter_f['parent'] == sec_f['name']:
                                            dict3.update({ter_f['name']:ter_f['score']})
                                        else:
                                            continue
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
                        dict1.update({prim_f['name']:dict2})
                    # If the section has no sections, add that section and its score set to the second dictionary
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                # Create the test dictionary with the test name as the main key, then return the name of the test, the dictionary, it's maximum and how many layers deep the test is
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            # If the user chose not to divide ANY section, proceed
            else:
                # Iterate through all sections in the list of main sections
                for prim_f in subfold1:
                    # If the section includes more dictionaries of other sections, proceed
                    if 'score' not in prim_f.keys(): 
                        dict2 = {}
                        # Iterate through all subsections of this section
                        for sec_f in subfold2:
                            # If the subsection has the right parent folder, update a second dictionary of sections
                            if sec_f['parent'] == prim_f['name']: 
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        # Once all relevant sections are added to the the second dictionary, update the main dictionary
                        dict1.update({prim_f['name']:dict2})
                    # If the section has no sections, add that section and its score set to the main dictionary
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                # Create the test dictionary with the test name as the main key, then return the name of the test, the dictionary, it's maximum and how many layers deep the test is
                test = {testname:dict1}
                return testname, test, totalMax, numLevels

# BUILD A COMPLEX TEST (More detailed input)
def build_custom_dict(testname):
    # Initialize variables
    moreLevels = 'undefined' # User chooses whether they will divide sections into more parts ('y' or 'n')
    proceed_num = 0 # Add to this variable if user chooses to divide a section into more parts
    maxScore = 0 # The maximum score for a particular part of a test
    totalMax = 0 # The overall maximum score for a test type
    numLevels = 0 # The number of levels deep a test is divided 
    sectCount1 = 0 # The number of parts a section is divided into
    sectCount2 = 0 # The number of parts a section is divided int
    subfold1 = [] # A list of dictionaries for the first layer of sections in the test
    subfold2 = [] # A list of dictionaries for the second layer of sections in the test
    subfold3 = [] # A list of dictionaries for the third layer of sections in the test
    dict1 = {} # A dictionary that will hold all dictionaries

    while moreLevels != False and moreLevels[0] != 'n':
        if moreLevels == 'undefined':
            # Require user to choose whether they will divide the section into more parts
            while True:
                try:
                    moreLevels = (input('\n-----------------\n\nIs this divided into parts? Y/N ')).lower().strip()
                    if moreLevels[0] == 'y' or moreLevels[0] == 'n':
                        break
                    elif isinstance(moreLevels, str) == False:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                    else:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                except IndexError:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            # If the user choose to divide the section into more parts, proceed
            if moreLevels[0] == 'y':
                numLevels += 1 # The test is divided at least one time
                while True:
                    # User decides how many times to divide the test (from 1-10 times)
                    try:
                        get_subSize1 = int(input('\nHow many identical parts? '))
                        if get_subSize1 > 10 or get_subSize1 < 1:
                            print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                        continue
                print(f'\nPlease enter the name(s) for the section(s)\n-----------------')
                # For EACH section, ask user to first enter name of the section
                for i in range(get_subSize1):
                    while True:
                        subName1 = input(f'Please enter a section name for section {i+1}: ')
                        if len(subName1) > 20 or len(subName1) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            break
                    # Next, as user to decide whether they will divide this single section into more parts
                    while True:
                        try:
                            moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                            # If user decides to divide into more parts, proceed
                            if moreLevels[0] == 'y':
                                proceed_num += 1 # Add to the number -> this means will we create another level of sections within the previous section
                                while True:
                                    # User decides how many times to divide this single section (from 1-10 times)
                                    try:
                                        sectCount1 = int(input(f'Please enter the number of sections in "{subName1}": '))
                                        print('-')
                                        if sectCount1 > 10 or sectCount1 < 1:
                                            print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                        continue
                                # Add this section to the list of dictionaries, with the number of times it is divided as 'count'
                                subfold1.append({'name':subName1, 'count':sectCount1})
                                break
                            # If user decides not to divide into more parts, proceed
                            elif moreLevels[0] == 'n':
                                # Get the maximum score for this single section
                                while True:
                                    try:
                                        maxScore = int(input(f'What is the maximum score for {subName1}? '))
                                        totalMax += maxScore # Add score to the total maximum score for the test
                                        if maxScore < 1:
                                            print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print('\n=============================\n| Please enter only digits. |\n=============================')
                                # Add this section to the list of dictionaries with the name of the section and the score list ("actual score, maximum score, mistakes")
                                subfold1.append({'name':subName1, 'score':['tbd', maxScore, 'none :)']})
                                break
                            # Only accept numbers
                            elif isinstance(moreLevels, str) == False:
                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                continue
                            else:
                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                continue
                        except IndexError:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
            # If user does not want to divide the test into parts at all, make a very simple test structure 
            else:
                while True:
                    try:
                        maxScore = int(input(f'What is the maximum score for {testname}? ')) # Take the maximum score for this part
                        totalMax += maxScore
                        if maxScore < 1:
                            print('\n==================================\n| Please enter a number above 1. |\n==================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n=============================\n| Please enter only digits. |\n=============================')
                # Create a test, add score to the test's maximum score and return the name of the test, the dictionary, it's maximum and how many layers deep the test is
                test = {testname:['tbd', maxScore, 'none :)']}
                totalMax += maxScore
                return testname, test, totalMax, numLevels
            # If a section was divided at least once more, proceed to second layer of sections
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1 # The test is divided a second time
                # Iterate through all first sections
                for i in subfold1:
                    if 'score' in i.keys(): # Skip all sections that contain scores, since they are not divided
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        # Based on how many parts the user chose to divide into, get a name for each part
                        for j in range(i['count']): 
                            while True:
                                subName2 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName2) > 20 or len(subName2) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    break
                            # Add a list of dictionaries for this single section's sections, with the number of times it is divided as 'count'
                            while True:
                                # Require user to choose whether they will divide the section into more parts
                                try:
                                    moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                                    if moreLevels[0] == 'y':
                                        proceed_num += 1 # Add to the number -> this means will we create another level of sections within the current section
                                        while True:
                                            # User decides how many times to divide these sections (from 1-10 times)
                                            try:
                                                sectCount2 = int(input(f'Please enter the number of sections in "{subName2}": '))
                                                print('-')
                                                if sectCount2 > 10 or sectCount2 < 1:
                                                    print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                                continue
                                        # Add this section to the list of dictionaries, with its name, its parent section's name and the number of times it is divided as 'count'
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'count':sectCount2}) 
                                        break
                                    # If user decides not to divide this section into more parts, proceed
                                    elif moreLevels[0] == 'n':
                                        # Get the maximum score for this specific section
                                        while True:
                                            try:
                                                maxScore = int(input(f'What is the maximum score for {subName2}? '))
                                                totalMax += maxScore # Add score to the total maximum score for the test
                                                if maxScore < 1:
                                                    print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print('\n=============================\n| Please enter only digits. |\n=============================')
                                        # Add this section to the list of dictionaries with the name of the section and the score list ("actual score, maximum score, mistakes")
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'score':['tbd', maxScore, 'none :)']}) 
                                        break
                                    # Only accept numbers
                                    elif isinstance(moreLevels, str) == False:
                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                        continue
                                    else:
                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                        continue
                                except IndexError:
                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                    continue
            # If the user chose not to divide ANY section, append all sections to the main dictionary and return the name of the test, the dictionary, it's maximum score and how many layers deep the test is
            else:
                for layer in subfold1:
                    dict1.update({layer['name']:layer['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            # If a section was divided at least once more, proceed to third layer of sections
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1 # The test is divided a third time
                # Iterate through all second sections
                for i in subfold2:
                    if 'score' in i.keys(): # Skip all sections that contain scores, since they are not divided
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        # Based on how many parts the user chose to divide into, get a name for each part
                        for j in range(i['count']):
                            while True:
                                subName3 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName3) > 20 or len(subName3) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    break
                            # Add a list of dictionaries for this single section's sections, with the number of times it is divided as 'count'
                            while True:
                                # Get the maximum score for this final (deepest) specific section
                                try:
                                    maxScore = int(input(f'What is the maximum score for {subName3}? '))
                                    totalMax += maxScore
                                    if maxScore < 1:
                                        print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print('\n=============================\n| Please enter only digits. |\n=============================')
                            # Add this section to the list of dictionaries with the name of the section and the score list ("actual score, maximum score, mistakes")
                            subfold3.append({'parent':i['name'], 'name':subName3, 'score':['tbd', maxScore, 'none :)']})
                # After all final sections have been added to the last list of dictionaries, iterate through ALL sections, starting with the list of main sections
                for prim_f in subfold1:
                    # If the section includes more dictionaries of other sections, proceed
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        # Iterate through all subsections of this section
                        for sec_f in subfold2:
                            # If the section includes more dictionaries of other sections, proceed
                            if 'score' not in sec_f.keys():
                                # If the subsection has the right parent folder, update the second dictionary of sections
                                if sec_f['parent'] == prim_f['name']:
                                    # Iterate through all subsections of this section
                                    dict3 = {}
                                    for ter_f in subfold3:
                                        # If the subsection has the right parent folder, update the third dictionary of sections
                                        if ter_f['parent'] == sec_f['name']:
                                            dict3.update({ter_f['name']:ter_f['score']})
                                        else:
                                            continue
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
                        dict1.update({prim_f['name']:dict2})
                    # If the section has no sections, add that section and its score set to the second dictionary
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                # Create the test dictionary with the test name as the main key, then return the name of the test, the dictionary, it's maximum and how many layers deep the test is
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            # If the user chose not to divide ANY section, proceed
            else:
                # Iterate through all sections in the list of main sections
                for prim_f in subfold1:
                    # If the section includes more dictionaries of other sections, proceed
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        # Iterate through all subsections of this section
                        for sec_f in subfold2:
                            # If the subsection has the right parent folder, update a second dictionary of sections
                            if sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        # Once all relevant sections are added to the the second dictionary, update the main dictionary
                        dict1.update({prim_f['name']:dict2})
                    # If the section has no sections, add that section and its score set to the main dictionary
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                # Create the test dictionary with the test name as the main key, then return the name of the test, the dictionary, it's maximum and how many layers deep the test is
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
        # If the user chose not to divide test into ANY parts ### CONSIDER DELETION; MAY BE UNNEEDED
        elif moreLevels == 'n':
            while True:
                try:
                    maxScore = int(input(f'What is the maximum score for {testname}? ')) # Take the maximum score for this part
                    totalMax += maxScore # Add the score to the total maximum score for the test
                    if maxScore < 1:
                        print('\n==================================\n| Please enter a number above 1. |\n==================================')
                        continue
                    else:
                        break
                except ValueError:
                    print('\n=============================\n| Please enter only digits. |\n=============================')
            # Create a test, add score to the test's maximum score and return the name of the test, the dictionary, it's maximum and how many layers deep the test is
            dict = {testname:['tbd', maxScore, 'none :)']}
            test = {testname:dict}
            return testname, test, totalMax, numLevels
        else:
            continue

# MAKE A MISTAKE LIST FOR INDEX
def make_mlist():
    # Initialize variables
    mistake_list = [] # A list of mistake types
    add_more = 'y' # Set to 'yes' to always request one mistake type minimum
    quit = False # If 'quit' is true, we will stop creating mistake types
    mistakes_done = False ### CONSIDER DELETING- ARTIFACT FROM PREVIOUS VERSION
    
    while quit == False:
        # If user chooses to add more mistakes, proceed
        if add_more[0] == 'y':
            while add_more[0] == 'y':
                new_mistake = input('---\nPlease enter one type of mistake: ')
                mistake_list.append(new_mistake)
                while True:
                    # Only accept 'y' or 'n' as input
                    try:
                        add_more = input('---\nWould you like to add more mistakes? Y/N ').lower().strip()
                        # If user chooses to proceed, break from loop and continue through an iteration of main function loop
                        if add_more[0] == 'y':
                            break
                        # If user is done adding mistakes, set 'quit' to true to end main loop, then break from this loop
                        elif add_more[0] == 'n':
                            quit = True
                            mistakes_done = True ### CONSIDER DELETING- ARTIFACT FROM PREVIOUS VERSION
                            break
                        elif isinstance(add_more, str) == False:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                        else:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                    except IndexError:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
    # Print all mistakes for user's information
    print('\nThe mistakes list is: ')
    for c, i in enumerate(mistake_list):
        print(f'Mistake {c+1}: {i}')
    print('---\n')
    # Hold page until user continues
    while True:
        input('\nPress enter to continue. \n\n----------------\n')
        break
    return mistake_list 
# Call the main function
main()