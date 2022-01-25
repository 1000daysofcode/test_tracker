import error_messages
from view_tests import view
from add_score import add_scores
from analyze_score import analyze
from add_mistakes import make_mlist
from create_structure import make_test_shell, print_preview


# Start main function
def main_loop():
    choice = 'undefined'
    display_welcome()

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
                    choice = menu_selection()
                    # Only accept the options in the menu
                    if choice[0] == 'v' or choice[0] == 'a' or choice[0] == 'n' or choice[0] == 's' or choice[0] == 'q':
                        break
                    # If input is not a string, reject input
                    elif isinstance(choice, str) == False:
                        error_messages.invalid()
                        continue
                   # If the first letter is anything else aside from one of the letters, reject input
                    else:
                        error_messages.invalid()
                        continue
                except IndexError:
                    error_messages.invalid()
                    continue
            
            # VIEW TESTS
            if choice[0] == 'v':
                # Reject this choice if there are no test structures
                if len(test_raw) < 1 or len(test_index) < 1:
                    error_messages.no_scores()
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
                                error_messages.invalid_sel(len(test_index)+1)
                                continue
                            # Reject input if there is no score yet added for this test
                            elif test_db[test_choice] == []:
                                error_messages.no_scores2()
                                continue
                            else:
                                # Accept input and break if all conditions are met
                                break
                        except:
                            # If input throws an error, remind user only to enter numbers, return to main menu in case input was 'q'
                            error_messages.letter_error()
                            break
                    
                    #Choose all tests in database at the location the user chose
                    try:
                        tests = test_db[test_choice]
                        print(f'\nBelow are all test results for test "{test_index[test_choice-1]["name"]}:"\n================\n')
                        view(tests) 
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
                    error_messages.no_scores()
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
                    error_messages.no_struct()
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
                print_preview(dct)
                while True:
                    input('\nPress enter to continue.\n----------------\n')
                    break
                choice = 'undefined'
                continue
            # When user closes app with 'q', close app.
            else:
                display_goodbye()
                choice = False


def display_welcome():
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


def menu_selection():
    return (input('''
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


def display_goodbye():
    print('''
Thank you for using Test Tracker version 0!

   ______                ____               __
  / ____/___  ____  ____/ / /_  __  _____  / /
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ / 
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/  
\____/\____/\____/\__,_/_.___/\__, /\___(_)   
                             /____/          
                             
''')


# Call the main function
main_loop()