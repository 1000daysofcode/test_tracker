import copy

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
                            test_choice = int(input('---\n\nPlease enter the location of your tests: '))-1
                            # User must choose from index 0 to the last number in the list
                            if test_choice > len(test_index) or test_choice < 0:
                                print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================')
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
                            print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
                            return
                    #Choose all tests in database at the location the user chose
                    tests = test_db[test_choice]
                    print(f'Below are all test results for test {test_index[test_choice-1]}:\n\n================')
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
                        # Print this line in between tests. Stop between each test and wait for user to press enter to proceed.
                        print('\n\n================')  
                        while True:
                            input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
                            break     
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
                print(f'\nTest "{testname}" created. Please see below:')
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
                    input('Press enter to continue. \n\n----------------\n')
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

    if test_db == []:
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
                elif test_db[test_choice] == []:
                    print(f'\n===================================================\n| There are not yet any scores for this test type |\n===================================================')
                    continue
                else:
                    break
            except:
                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
                return
        num_tests = len(test_db[test_choice])
        max_s = test_index[test_choice]['maxscore']
        tests = test_db[test_choice]

        tmp_mlist = test_index[test_choice]['mistakes']
        for each in tmp_mlist:
            m_list.append({'name':each.strip(), 'count':0})
        for c, dct in enumerate(tests):
            for title, v in dct.items():
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
                        if isinstance(dct[title][layer1], dict) != True:
                            test = v1
                            if isinstance(test, list) == True:
                                score += v1[0]
                                for type in m_list:
                                    if type['name'] in v1[2]:
                                        type['count'] += 1
                                    else:
                                        pass
                            else:
                                pass 
                        else:
                            for layer2, v2 in dct[title][layer1].items():
                                if isinstance(dct[title][layer1][layer2], dict) != True:
                                    test = v2
                                    if isinstance(test, list) == True:
                                        score += v2[0]
                                        for type in m_list:
                                            if type['name'] in v2[2]:
                                                type['count'] += 1
                                            else:
                                                pass
                                    else:
                                        pass
                                else:
                                    for layer3, v3 in dct[title][layer1][layer2].items():
                                        if isinstance(dct[title][layer1][layer2][layer3], dict) != True:
                                            score += v3[0]
                                            for type in m_list:
                                                if type['name'] in v3[2]:
                                                    type['count'] += 1
                                                else:
                                                    pass
                                        else:
                                            for layer4, v4 in dct[title][layer1][layer2][layer3].items():
                                                score += v4[0]
                                                for type in m_list:
                                                    if type['name'] in v4[2]:
                                                        type['count'] += 1
                                                    else:
                                                        pass
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

        total_s += score
        a_score = float(total_s) / num_tests
        name = test_index[test_choice]['name']
        top_n = str(int(top_n) + 1)
        low_n = str(int(low_n) + 1)

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



# BUILD A SIMPLE TEST (Less detailed input)
def build_simple_dict(testname):
    moreLevels = 'undefined'
    proceed_num = 0
    maxScore = 0
    totalMax = 0
    numLevels = 0
    sectCount1 = 0
    sectCount2 = 0
    subfold1 = []
    subfold2 = []
    subfold3 = []
    dict1 = {}

    while moreLevels != False and moreLevels[0] != 'n':
        if moreLevels == 'undefined':
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
            if moreLevels[0] == 'y':
                numLevels += 1
                while True:
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
                names = []
                for i in range(get_subSize1):
                    while True:
                        subName1 = input(f'Please enter a section name for section {i+1}: ')
                        if len(subName1) > 20 or len(subName1) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            names.append(subName1)
                            break
                while True:
                    try:
                        moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                        if moreLevels[0] == 'y':
                            proceed_num += 1
                            while True:
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
                            for name in names:
                                subfold1.append({'name':name, 'count':sectCount1})
                            break
                        elif moreLevels[0] == 'n':
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
                            for name in names:
                                subfold1.append({'name':name, 'score':['tbd', maxScore, 'none :)']})
                                totalMax += maxScore
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
            else:
                while True:
                    try:
                        maxScore = int(input(f'What is the maximum score for {testname}? '))
                        if maxScore < 1:
                            print('\n==================================\n| Please enter a number above 1. |\n==================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n=============================\n| Please enter only digits. |\n=============================')
                test = {testname:['tbd', maxScore, 'none :)']}
                totalMax += maxScore
                return testname, test, totalMax, numLevels

            # If yes, continue building subfolders, if no process dict
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1
                for i in subfold1:
                    if 'score' in i.keys():
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        names = []
                        for j in range(i['count']):
                            while True:
                                subName2 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName2) > 20 or len(subName2) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    names.append(subName2)
                                    break
                        while True:
                            try:
                                moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                                if moreLevels[0] == 'y':
                                    proceed_num += 1
                                    while True:
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
                                    for name in names:
                                        subfold2.append({'parent':i['name'], 'name':name, 'count':sectCount2}) 
                                    break
                                elif moreLevels[0] == 'n':
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
                                    for name in names:
                                        subfold2.append({'parent':i['name'], 'name':name, 'score':['tbd', maxScore, 'none :)']}) 
                                        totalMax += maxScore
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
            else:
                for layer in subfold1:
                    dict1.update({layer['name']:layer['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1
                for i in subfold2:
                    if 'score' in i.keys():
                        continue
                    else:     
                        print(f'\nPlease enter the names for "{i["parent"]} - {i["name"]}"\n-----------------')
                        names = []
                        for j in range(i['count']):
                            while True:
                                subName3 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName3) > 20 or len(subName3) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    names.append(subName3)
                                    break
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
                        for name in names:    
                            subfold3.append({'parent':i['name'], 'name':name, 'score':['tbd', maxScore, 'none :)']})
                            totalMax += maxScore
                for prim_f in subfold1:
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        for sec_f in subfold2:
                            if 'score' not in sec_f.keys():
                                if sec_f['parent'] == prim_f['name']:
                                    dict3 = {}
                                    for ter_f in subfold3:
                                        if ter_f['parent'] == sec_f['name']:
                                            dict3.update({ter_f['name']:ter_f['score']})
                                        else:
                                            continue
                                    dict2.update({sec_f['name']:dict3})
                                else:
                                    continue
                            elif sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        dict1.update({prim_f['name']:dict2})
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            else:
                for prim_f in subfold1:
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        for sec_f in subfold2:
                            if sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        dict1.update({prim_f['name']:dict2})
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels

# BUILD A COMPLEX TEST (More detailed input)
def build_custom_dict(testname):
    moreLevels = 'undefined'
    proceed_num = 0
    maxScore = 0
    totalMax = 0
    numLevels = 0
    sectCount1 = 0
    sectCount2 = 0
    subfold1 = []
    subfold2 = []
    subfold3 = []
    dict1 = {}

    while moreLevels != False and moreLevels[0] != 'n':
        if moreLevels == 'undefined':
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
            if moreLevels[0] == 'y':
                numLevels += 1
                while True:
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
                for i in range(get_subSize1):
                    while True:
                        subName1 = input(f'Please enter a section name for section {i+1}: ')
                        if len(subName1) > 20 or len(subName1) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            break
                    while True:
                        try:
                            moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                            if moreLevels[0] == 'y':
                                proceed_num += 1
                                while True:
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
                                subfold1.append({'name':subName1, 'count':sectCount1})
                                break
                            elif moreLevels[0] == 'n':
                                while True:
                                    try:
                                        maxScore = int(input(f'What is the maximum score for {subName1}? '))
                                        totalMax += maxScore
                                        if maxScore < 1:
                                            print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print('\n=============================\n| Please enter only digits. |\n=============================')
                                subfold1.append({'name':subName1, 'score':['tbd', maxScore, 'none :)']})
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
            else:
                while True:
                    try:
                        maxScore = int(input(f'What is the maximum score for {testname}? '))
                        totalMax += maxScore
                        if maxScore < 1:
                            print('\n==================================\n| Please enter a number above 1. |\n==================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n=============================\n| Please enter only digits. |\n=============================')
                test = {testname:['tbd', maxScore, 'none :)']}
                return testname, test, totalMax, numLevels

            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1
                for i in subfold1:
                    if 'score' in i.keys():
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        for j in range(i['count']):
                            while True:
                                subName2 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName2) > 20 or len(subName2) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    break
                            while True:
                                try:
                                    moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                                    if moreLevels[0] == 'y':
                                        proceed_num += 1
                                        while True:
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
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'count':sectCount2}) 
                                        break
                                    elif moreLevels[0] == 'n':
                                        while True:
                                            try:
                                                maxScore = int(input(f'What is the maximum score for {subName2}? '))
                                                totalMax += maxScore
                                                if maxScore < 1:
                                                    print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print('\n=============================\n| Please enter only digits. |\n=============================')
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'score':['tbd', maxScore, 'none :)']}) 
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
            else:
                for layer in subfold1:
                    dict1.update({layer['name']:layer['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1
                for i in subfold2:
                    if 'score' in i.keys():
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        for j in range(i['count']):
                            while True:
                                subName3 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName3) > 20 or len(subName3) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    break
                            while True:
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
                            subfold3.append({'parent':i['name'], 'name':subName3, 'score':['tbd', maxScore, 'none :)']})
                for prim_f in subfold1:
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        for sec_f in subfold2:
                            if 'score' not in sec_f.keys():
                                if sec_f['parent'] == prim_f['name']:
                                    dict3 = {}
                                    for ter_f in subfold3:
                                        if ter_f['parent'] == sec_f['name']:
                                            dict3.update({ter_f['name']:ter_f['score']})
                                        else:
                                            continue
                                    dict2.update({sec_f['name']:dict3})
                                else:
                                    continue
                            elif sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        dict1.update({prim_f['name']:dict2})
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            else:
                for prim_f in subfold1:
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        for sec_f in subfold2:
                            if sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        dict1.update({prim_f['name']:dict2})
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
        elif moreLevels == 'n':
            while True:
                try:
                    maxScore = int(input(f'What is the maximum score for {testname}? '))
                    totalMax += maxScore
                    if maxScore < 1:
                        print('\n==================================\n| Please enter a number above 1. |\n==================================')
                        continue
                    else:
                        break
                except ValueError:
                    print('\n=============================\n| Please enter only digits. |\n=============================')
            dict = {testname:['tbd', maxScore, 'none :)']}
            test = {testname:dict}
            return testname, test, totalMax, numLevels
        else:
            continue

# Choose between simple and custom test types

def make_test_shell():
    choice = 'undefined'
    while choice != False and choice[0] != 'c' and choice[0] != 's':
        if choice == 'undefined':
            while True:
                try:
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
            if choice[0] == 's':
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2:
                        print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                        continue
                    else:
                        return build_simple_dict(testname)
            else:
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2:
                        print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                        continue
                    else:
                        return build_custom_dict(testname)

# MAKE A MISTAKE LIST FOR INDEX
def make_mlist():
    mistake_list = []
    add_more = ''
    quit = False

    mistakes_done = False

    while quit == False:
        try:
            add_more = input('\nWould you like to add a mistake type? Y/N ').lower().strip()
            if add_more[0] == 'y':
                while add_more[0] == 'y':
                    new_mistake = input('---\nEnter the name of your mistake type: ')
                    mistake_list.append(new_mistake)
                    while True:
                        try:
                            add_more = input('---\nWould you like to add more mistakes? Y/N ').lower().strip()
                            if add_more[0] == 'y':
                                break
                            elif add_more[0] == 'n':
                                quit = True
                                mistakes_done = True
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
            elif add_more[0] == 'n':
                quit = True
                mistakes_done = False
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
    print('\nThe mistakes list is: ')
    for c, i in enumerate(mistake_list):
        print(f'Mistake {c+1}: {i}')
    print('---\n')
    while True:
        input('Press enter to continue. \n\n----------------\n')
        break
    return mistake_list

# ADD A NEW SCORED TEST
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
main()