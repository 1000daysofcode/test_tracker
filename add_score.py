import copy
import error_messages
from compile_test import compile_test_scores as make_test

# ADD A scores_dct SCORED TEST
def add_scores(test_raw, test_index):
    if len(test_raw) < 1:
        error_messages.no_struct()
    else:
        
        test_copy = {}
        scores_dct = {}
        subsection1 = []
        subsection2 = []
        subsection3 = [] 
        subsection4 = []
        
        print('\nHere are your test names and locations:\n')
        for c, i in enumerate(test_index):
            print(f'Test structure: {i["name"]} || Test location: {c+1}') # Index +1 is displayed
        
        test_choice = get_test_choice(len(test_index))
        test_copy = copy.deepcopy(test_raw[test_choice])
        
        for section1_name, section1_values in test_copy.items():
            print(f'\nTest Name: {section1_name}\n----------------') 
            if isinstance(section1_values, dict) != True:
                test = section1_values
                
                if isinstance(test, list) == True: # If list of scores, get user input
                    actual_score = get_actual_score(section1_values[1], test_choice)
                    # If score less than max, require at least one mistake
                    if actual_score < section1_values[1] and len(test_index[test_choice]['mistakes']) > 0:
                        add_more = 'undefined'
                        tmp_mistake_list = []
                        
                        while True and len(tmp_mistake_list) != len(test_index[test_choice]['mistakes']):
                            mistake_name = input('Please enter mistakes one at a time: ').strip()
                            if not valid_mistake_choice(mistake_name, tmp_mistake_list, test_index[test_choice]['mistakes']):
                                continue
                            
                            else: # If conditions are met, append mistake
                                tmp_mistake_list.append(mistake_name)
                                if test_copy[section1_name][2] == 'none :)': # If no mistakes have yet been entered
                                    add_more = add_more_mistakes(len(tmp_mistake_list), len(test_index[test_choice]['mistakes']))
                                    if add_more[0] == 'y': # Add more mistake types
                                        continue 
                                    else: # Append this section's name and score info
                                        subsection1.append({'name':section1_name, 'score':[actual_score, test_copy[section1_name][1], ', '.join(tmp_mistake_list)]})
                                        break
                                
                                else: # If a mistake has been entered
                                    add_more = add_more_mistakes(len(tmp_mistake_list), len(test_index[test_choice]['mistakes']))
                                    if add_more[0] == 'y':
                                        continue
                                    else:
                                        subsection1.append({'name':section1_name, 'score':[actual_score, test_copy[section1_name][1], ', '.join(tmp_mistake_list)]})
                                        break
                        
                        else: # If there are no remaining mistakes
                            subsection1.append({'name':section1_name, 'score':[actual_score, test_copy[section1_name][1], ', '.join(tmp_mistake_list)]})
                            print("---\nNo remaining mistake types.\n")
                    elif actual_score == section1_values[1]: # If perfect score, skip mistakes
                        subsection1.append({'name':section1_name, 'score':[actual_score, test_copy[section1_name][1], test_copy[section1_name][2]]})
                else: ### Diagnose this condition when refactoring- MAY BE UNNEEDED
                    error_messages.UNDEFINED_ERROR()
                    pass
            
            else: # Iterate through next section if it goes deeper
                subsection1.append({'name':section1_name})
                for section2_name, section2_values in test_copy[section1_name].items():
                    print(f'\n{section2_name}')
                    if isinstance(test_copy[section1_name][section2_name], dict) != True:
                        test = section2_values
                        
                        if isinstance(test, list) == True:
                            actual_score = get_actual_score(section2_values[1], test_choice)
                            if actual_score < section2_values[1] and len(test_index[test_choice]['mistakes']) > 0:
                                add_more = 'undefined'

                                tmp_mistake_list = []
                                while True and len(tmp_mistake_list) != len(test_index[test_choice]['mistakes']):
                                    mistake_name = input('Please enter the mistakes one at a time: ').strip()
                                    if not valid_mistake_choice(mistake_name, tmp_mistake_list, test_index[test_choice]['mistakes']):
                                        continue
                                    
                                    else: # If conditions are met
                                        tmp_mistake_list.append(mistake_name)
                                        if test_copy[section1_name][section2_name][2] == 'none :)':
                                            add_more = add_more_mistakes(len(tmp_mistake_list), len(test_index[test_choice]['mistakes']))
                                            if add_more[0] == 'y':
                                                continue
                                            else:
                                                subsection2.append({'parent':section1_name, 'name':section2_name, 'score':[actual_score, test_copy[section1_name][section2_name][1], ', '.join(tmp_mistake_list)]})
                                                break
                                        
                                        else: # If a mistake has been entered
                                            add_more = add_more_mistakes(len(tmp_mistake_list), len(test_index[test_choice]['mistakes']))
                                            if add_more[0] == 'y':
                                                continue
                                            else:
                                                subsection2.append({'parent':section1_name, 'name':section2_name, 'score':[actual_score, test_copy[section1_name][section2_name][1], ', '.join(tmp_mistake_list)]})
                                                break
                                
                                else: # If there are no remaining mistakes
                                    subsection2.append({'parent':section1_name, 'name':section2_name, 'score':[actual_score, test_copy[section1_name][section2_name][1], ', '.join(tmp_mistake_list)]})
                                    print("---\nNo remaining mistake types.\n")
                            elif actual_score == section2_values[1]: # If perfect score, skip mistakes
                                subsection2.append({'parent':section1_name, 'name':section2_name, 'score':[actual_score, test_copy[section1_name][section2_name][1], test_copy[section1_name][section2_name][2]]})
                        else: # If not a dictionary or list, print subsection --> CONSIDER DELETING (THIS MAY BE AN ARTIFACT)
                            print(f'\n{section2_name}') 
                    
                    else: # Iterate through next section if it goes deeper
                        subsection2.append({'parent':section1_name,'name':section2_name})
                        for section3_name, section3_values in test_copy[section1_name][section2_name].items():
                            print(f'\n{section3_name} : ')
                            if isinstance(test_copy[section1_name][section2_name][section3_name], dict) != True:
                                test = section3_values
                                
                                if isinstance(test, list) == True:
                                    actual_score = get_actual_score(section3_values[1], test_choice)
                                    if actual_score < section3_values[1] and len(test_index[test_choice]['mistakes']) > 0:
                                        add_more = 'undefined'
                                        
                                        tmp_mistake_list = []
                                        while True and len(tmp_mistake_list) != len(test_index[test_choice]['mistakes']):
                                            mistake_name = input('Please enter the mistakes one at a time: ').strip()
                                            if not valid_mistake_choice(mistake_name, tmp_mistake_list, test_index[test_choice]['mistakes']):
                                                continue

                                            else: # If conditions are met
                                                tmp_mistake_list.append(mistake_name)
                                                # If no mistakes have yet been entered
                                                if test_copy[section1_name][section2_name][section3_name][2] == 'none :)':
                                                    add_more = add_more_mistakes(len(tmp_mistake_list), len(test_index[test_choice]['mistakes']))
                                                    if add_more[0] == 'y':
                                                        continue
                                                    else:
                                                        subsection3.append({'parent':section2_name, 'name':section3_name, 'score':[actual_score, test_copy[section1_name][section2_name][section3_name][1], ', '.join(tmp_mistake_list)]})
                                                        break
                                                
                                                else: # If a mistake has been entered
                                                    add_more = add_more_mistakes(len(tmp_mistake_list), len(test_index[test_choice]['mistakes']))
                                                    if add_more[0] == 'y':
                                                        continue
                                                    else:
                                                        subsection3.append({'parent':section2_name, 'name':section3_name, 'score':[actual_score, test_copy[section1_name][section2_name][section3_name][1], ', '.join(tmp_mistake_list)]})
                                                        break
                                        
                                        else: # If there are no remaining mistakes
                                            subsection3.append({'parent':section2_name, 'name':section3_name, 'score':[actual_score, test_copy[section1_name][section2_name][section3_name][1], ', '.join(tmp_mistake_list)]})
                                            print("---\nNo remaining mistake types.\n")
                                    elif actual_score == section3_values[1]: # If there is a perfect score
                                        subsection3.append({'parent':section2_name, 'name':section3_name, 'score':[actual_score, test_copy[section1_name][section2_name][section3_name][1], test_copy[section1_name][section2_name][section3_name][2]]})
                                else: # If not a dictionary or list, print subsection --> CONSIDER DELETING (THIS MAY BE AN ARTIFACT)
                                    print('\n' + section3_name + " : " + str(test_copy[section1_name][section2_name][section3_name]))
                            
                            else: # Iterate through next section if it goes deeper (final layer)
                                subsection3.append({'parent':section2_name,'name':section3_name})
                                
                                # As there can be no more lists deeper than this, 
                                # we will not check for dictionaries now (we already have above for this section) 
                                
                                for section4_name, section4_values in test_copy[section1_name][section2_name][section3_name].items():
                                    print(f'{section4_name} : ')
                                    
                                    actual_score = get_actual_score(section4_values[1], test_choice)
                                    if actual_score < section4_values[1] and len(test_index[test_choice]['mistakes']) > 0:
                                        add_more = 'undefined'
                                        
                                        tmp_mistake_list = []
                                        while True and len(tmp_mistake_list) != len(test_index[test_choice]['mistakes']):
                                            mistake_name = input('Please enter the mistakes one at a time: ').strip()
                                            if not valid_mistake_choice(mistake_name, tmp_mistake_list, test_index[test_choice]['mistakes']):
                                                continue

                                            else: # If conditions are met
                                                tmp_mistake_list.append(mistake_name)
                                                if test_copy[section1_name][section2_name][section3_name][section4_name][2] == 'none :)':
                                                    add_more = add_more_mistakes(len(tmp_mistake_list), len(test_index[test_choice]['mistakes']))
                                                    if add_more[0] == 'y':
                                                        continue
                                                    else:
                                                        subsection4.append({'gparent':section2_name, 'parent':section3_name, 'name':section4_name, 'score':[actual_score, test_copy[section1_name][section2_name][section3_name][section4_name][1], ', '.join(tmp_mistake_list)]})
                                                        break
                                                
                                                else: # If a mistake has been entered
                                                    add_more = add_more_mistakes(len(tmp_mistake_list), len(test_index[test_choice]['mistakes']))
                                                    if add_more[0] == 'y':
                                                        continue
                                                    else:
                                                        subsection4.append({'gparent':section2_name, 'parent':section3_name, 'name':section4_name, 'score':[actual_score, test_copy[section1_name][section2_name][section3_name][section4_name][1], ', '.join(tmp_mistake_list)]})
                                                        break
                                        
                                        else: # If there are no remaining mistakes
                                            subsection4.append({'gparent':section2_name, 'parent':section3_name, 'name':section4_name, 'score':[actual_score, test_copy[section1_name][section2_name][section3_name][section4_name][1], ', '.join(tmp_mistake_list)]})
                                            print("---\nNo remaining mistake types.\n")
                                    elif actual_score == section4_values[1]: # If there is a perfect score
                                        subsection4.append({'gparent':section2_name, 'parent':section3_name, 'name':section4_name, 'score':[actual_score, test_copy[section1_name][section2_name][section3_name][section4_name][1], test_copy[section1_name][section2_name][section3_name][section4_name][2]]})
                    
                    
                    print('----------------') # Divide each main section with a line
                print('\n\n================') # Print after input is fully completed
                
                ## print(f'\n{subsection1}\n\n{subsection2}\n\n{subsection3}\n\n{subsection4}') ## This is for error checking
            
            new_scores_dct = make_test(scores_dct, subsection1, subsection2, subsection3, subsection4)
            scores_dct = new_scores_dct
            
            # Create the test dictionary with the test name as the main key, then return the name of the test, the dictionary, it's maximum and how many layers deep the test is
            test_copy = {test_index[test_choice]['name']:scores_dct}
            print('\nScores successfully added. Returning to menu.')
            return test_choice, test_copy 

def get_test_choice(num):
    while True:
        try:
            test_choice = int(input('---\n\nPlease enter the location of the test you want to add a score for: '))-1
            if test_choice > num-1 or test_choice < 0:
                error_messages.invalid_sel(num)
                continue
            else:
                break
        except ValueError:
            error_messages.only_digits()
            continue
    
    return test_choice


def get_actual_score(num, test_choice):
    while True:
        try:
            # Get the score from the user from 0 to the maximum score
            actual_score = int(input(f'\nWhat was your score out of {num}? '))
            if actual_score > num or test_choice < 0:
                error_messages.invalid_sel(num)
                continue
            else:
                break
        except ValueError:
            error_messages.only_digits()
            continue
    
    return actual_score

def add_more_mistakes(tmp_mistake_list_len, mistake_list_len):                              
    
    while True and tmp_mistake_list_len != mistake_list_len: # As long as list not full
        try: # If user wants to add more mistakes
            add_more = input('Would you like to add another mistake? Y/N ').lower().strip()
            if add_more[0] == 'y' or add_more[0] == 'n': 
                return add_more # Only accept 'y' or 'n' as input
            elif isinstance(add_more, str) == False:
                error_messages.invalid()
                continue
            else:
                error_messages.invalid()
                continue
        except IndexError:
            error_messages.invalid()
            continue

def valid_mistake_choice(mistake_name, tmp_mistake_list, mistake_list):
    if mistake_name not in mistake_list:
        error_messages.invalid_mis()
        return False
    # Reject mistake if mistake is already entered mistake has nothing entered
    elif mistake_name in tmp_mistake_list and mistake_name != '':
        error_messages.redundant_mis()
        return False
    # Reject mistake if mistake has nothing entered or entered the default
    elif mistake_name == 'none :)' or mistake_name == '':
        error_messages.no_mis()
        return False
    
    return True