import error_messages
from view_tests import view
from add_score import add_scores
from analyze_score import analyze
from add_mistakes import make_mlist
from create_structure import make_test_shell


# Start main function
def main_loop():
    choice = 'undefined'
    display_welcome()

    name = input('\n\nWelcome to Test Tracker! Please enter your name: ')
    print(f'\nWelcome, {name}!\n\nPlease create at least one test structure to continue.')

    test_raw = [] # Test structures
    test_db = [] # Test scores
    test_index = [] # Test name, location in raw/db and mistake lists

    while choice != False and choice[0] != 'q': # Quit by pressing 'q'
        if choice == 'undefined':
            choice = make_choice()
            
            # VIEW TESTS
            if choice[0] == 'v':
                if len(test_raw) < 1 or len(test_index) < 1:
                    error_messages.no_scores() # if there are no test structures
                    choice = 'undefined'
                    continue
                
                else:
                    test_choice = get_test_choice(test_index, test_db)
                    try:
                        tests = test_db[test_choice]
                        print(f'\nBelow are all test results for test "{test_index[test_choice-1]["name"]}:"\n================\n')
                        
                        for c, dct in enumerate(tests):
                            print(f'Test #{c+1}\n----------------')
                            view(dct)
                            print('\n\n================') # Print between tests
                            wait_for_user()
                    except IndexError:
                        print('\n-> Returning to main menu')
                        choice = 'undefined'
                        continue
                    choice = 'undefined'
                    continue
            
            # ANALYZE TEST RESULTS
            elif choice[0] == 'a':
                if len(test_db) < 1 or len(test_index) < 1: # If there are no test scores 
                    error_messages.no_scores()
                    choice = 'undefined'
                    continue
                else:
                    analyze(test_db, test_index)
                    choice = 'undefined'
                    continue
            
            # ADD NEW TEST SCORES
            elif choice[0] == 'n':
                if len(test_raw) < 1 or len(test_index) < 1: # If there are no test structures
                    error_messages.no_struct()
                    choice = 'undefined'
                    continue
                else:
                    index, scores = add_scores(test_raw, test_index)
                    test_db[index].append(scores)
                    choice = 'undefined'
                    continue
            
            # ADD NEW TEST STRUCTURE
            elif choice[0] == 's':
                # 'dct' is the structure, 'total' is the total possible score and 'levels' is the how many layers
                testname, dct, total, levels = make_test_shell()

                test_db.append([]) # Add a new space into the database
                test_raw.append(dct) # Add test structure to the list
                test_index.append({'name':testname, 'maxscore':total, 'mistakes':make_mlist()}) # Add spot on test index 
            
                print(f'\nTest "{testname}" created. Please see below:\n') # Print completed structure
                view(dct)
                while True:
                    input('\nPress enter to continue.\n----------------\n')
                    break
                choice = 'undefined'
                continue
            
            else: # Close app if 'q'
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


def make_choice():
    while True:
        try:
            choice = menu_selection()
            if valid_choice(choice):
                return choice
            elif isinstance(choice, str) == False:
                error_messages.invalid()
                continue
            else:
                error_messages.invalid()
                continue
        except IndexError:
            error_messages.invalid()
            continue


def valid_choice(choice):
    return choice[0] == 'v' or choice[0] == 'a' or choice[0] == 'n' or choice[0] == 's' or choice[0] == 'q'


def get_test_choice(test_index, test_db):
    test_choice = -1
    
    print('\nHere are your test names and locations:\n')
    for c, i in enumerate(test_index):
        print(f'Test structure: {i["name"]} || Test location: {c+1}') # Index +1 is displayed
    
    while True:
        try:
            test_choice = int(input('---\n\nPlease enter the location of your tests:\n-> Enter "q" to return to main menu\n---\n'))-1
            if test_choice > len(test_index) or test_choice < 0:
                error_messages.invalid_sel(len(test_index)+1)
                continue
            elif test_db[test_choice] == []:
                error_messages.no_scores2() # if no score yet added for this test
                continue
            else:
                break # if all conditions are met
        except:
            error_messages.letter_error() # only enter numbers
            break

    return test_choice


def wait_for_user():
    while True: 
            input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
            break # Stop between each test and wait for user


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