import error_messages


# ANALYZE TEST SCORES
def analyze(test_db, test_index):
    
    num_tests = 0
    total_score = 0
    avg_score = 0

    max_score = 0
    top_score = 0
    top_name = ''
    low_score = 1000000000
    low_name = ''
    mistake_list = []

    if test_db == []: # If no scores in test database
        error_messages.no_scores()
    else: # List available tests to choose from
        
        print('\nHere are your test names and locations:\n-> Enter "q" to return to main menu\n---\n')
        for c, i in enumerate(test_index):
            print(f'Test structure: {i["name"]} || Test location: {c+1}') # Display locations from 1
        test_choice = get_test_choice(test_db, test_index)
        if test_choice < 0:
            return
        
        num_tests = len(test_db[test_choice]) # Number of tests at chosen index
        max_score = test_index[test_choice]['maxscore']
        tests = test_db[test_choice] # All tests at chosen location

        tmp_mlist = test_index[test_choice]['mistakes']
        for mistake in tmp_mlist: # Convert string of mistakes into a list of dictionaries
            mistake_list.append({'name':mistake.strip(), 'count':0})
        
        total_score, top_name, top_score, low_name, low_score, mistake_list = sum_scores_and_mistakes(tests, mistake_list)
        
        avg_score = float(total_score) / num_tests
        name = test_index[test_choice]['name']
        # The index of the test +1 converted to a string
        top_name = str(int(top_name) + 1)
        low_name = str(int(low_name) + 1)
        
        print_main_analysis(name, num_tests, max_score, avg_score, top_name, top_score, low_name, low_score)

        tally = sorted(mistake_list, key=lambda k: k['count']) # Sort mistakes is ascending order
        print_mistakes_tally(tmp_mlist, tally)
        wait_for_user()


def get_test_choice(test_db, test_index):
    test_choice = -1
    while True:
        try:
            # Take user choice for test location
            test_choice = int(input('---\n\nPlease enter the location of your tests: '))-1
            if test_choice > len(test_index) or test_choice < 0:
                error_messages.invalid_sel(len(test_index))
                continue
            elif test_db[test_choice] == []:
                error_messages.no_scores2()
                continue
            else: # If choice meets all criteria
                return test_choice 
        except:
            error_messages.letter_error()
            to_menu = -1
            return to_menu 


def sum_scores_and_mistakes(tests, mistake_list):
    overall_score = 0
    top_score = 0 # Top score achieved
    top_name = '' # Top score's test name
    low_score = 1000000000 # Lowest score achieved
    low_name = '' # Low score's test name
    
    for c, test in enumerate(tests):
        score = 0 # Score/ test
        for section1_name, section1_values in test.items():
            if isinstance(section1_values, dict) != True: # If list of scores and mistakes 
                test = section1_values
                if isinstance(test, list) == True: 
                    score += section1_values[0] # Add to test's score
                    for type in mistake_list:
                        if type['name'] in section1_values[2]:
                            type['count'] += 1 # Count mistakes
                        else:
                            pass
                else: # If no more sections or score lists
                    print()
                    pass
            
            else: # If there are more sections, continue count
                for section2_name, section2_values in test[section1_name].items():
                    if isinstance(test[section1_name][section2_name], dict) != True:
                        test = section2_values
                        if isinstance(test, list) == True:
                            score += section2_values[0]
                            for type in mistake_list:
                                if type['name'] in section2_values[2]:
                                    type['count'] += 1
                                else:
                                    pass
                        else:
                            pass 
                    
                    else:
                        for section3_name, section3_values in test[section1_name][section2_name].items():
                            if isinstance(test[section1_name][section2_name][section3_name], dict) != True:
                                test = section3_values
                                if isinstance(test, list) == True:
                                    score += section3_values[0]
                                    for type in mistake_list:
                                        if type['name'] in section3_values[2]:
                                            type['count'] += 1
                                        else:
                                            pass
                                else:
                                    pass
                            
                            else:
                                for section4_name, section4_values in test[section1_name][section2_name][section3_name].items():
                                    if isinstance(test[section1_name][section2_name][section3_name][section4_name], dict) != True:
                                        score += section4_values[0]
                                        for type in mistake_list:
                                            if type['name'] in section4_values[2]:
                                                type['count'] += 1
                                            else:
                                                pass
                                    
                                    else:
                                        for section5_name, section5_values in test[section1_name][section2_name][section3_name][section4_name].items():
                                            score += section5_values[0]
                                            for type in mistake_list:
                                                if type['name'] in section5_values[2]:
                                                    type['count'] += 1
                                                else:
                                                    pass
        
        if score > top_score: # If test's score > top score
            top_score = score
            top_name = str(c)
        elif score == top_score: # If scores are the same
            top_name += f', {str(c)}'
        if score < low_score: # If test's score < top score
            low_score = score
            low_name = str(c)
        elif score == low_score: # If scores are the same
            low_name += f', {str(c)}'

        overall_score += score

    return overall_score, top_name, top_score, low_name, low_score, mistake_list


def print_main_analysis(name, num_tests, max_score, avg_score, top_name, top_score, low_name, low_score):
    print(f'''
    =====================================
    |          Score Analysis           |
    ------------------------------------|
    | Name of test: ............. {name}
    | Number of tests: .......... {num_tests}
    | Maximum score possible .... {max_score}
    |-----------------------------------
    | Overall score average ..... {avg_score}
    |-----------------------------------
    | Top score on ............ test #{top_name}
    | Overall top score ......... {top_score}
    | Lowest score on ......... test #{low_name}
    | Overall lowest score ...... {low_score}
    |===================================|
    |         Mistakes Rankings         |
    |-----------------------------------|''')


def print_mistakes_tally(tmp_mlist, tally):
    if len(tmp_mlist) >= 6: 
        # Display the top three least and most common mistakes
        print('    | Least common mistakes:')
        for mistake in tally[0:3]: # Ascending order
            print(f"    |\t{mistake['name']}: {mistake['count']} times")
        print('    | Most common mistakes:')
        for mistake in tally[-4::-1]: # Descending order
            print(f"    |\t{mistake['name']}: {mistake['count']} times")
    
    if len(tmp_mlist) < 6 and len(tally) > 3: 
        # Display the top two least and most common mistakes
        print('    | Least common mistakes:')
        for mistake in tally[0:2]:
            print(f"    |\t{mistake['name']}: {mistake['count']} times")
        print('    | Most common mistakes:')
        for mistake in tally[-2::-1]:
            print(f"    |\t{mistake['name']}: {mistake['count']} times")
    
    else: 
        # Print all mistakes from the least to most common
        print('    | From least to most common:')
        for mistake in tally:
            print(f"    |\t{mistake['name']}: {mistake['count']} times")

    print('    =====================================\n')


def wait_for_user():
    while True:
        input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
        break # Hold page until user continues