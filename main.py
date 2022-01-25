import analyze_score as analyze
import add_score as add_scores
import create_structure as make_test_shell
import add_mistakes as make_mlist

# Start main function
def main_app():
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

# Call the main function
main_app()