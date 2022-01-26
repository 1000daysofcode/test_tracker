import error_messages

def single_part_test(testname, test_max_score, num_of_levels):
    while True:
        try:
            sect_part_score = int(input(f'What is the maximum score for {testname}? '))
            if sect_part_score < 1:
                error_messages.above_1()
                continue
            else:
                break
        except ValueError:
            error_messages.only_digits()
    
    # Create a test and return results for main function
    test = {testname:['tbd', sect_part_score, 'none :)']}
    test_max_score = sect_part_score
    
    return testname, test, test_max_score, num_of_levels


def two_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, test_dict):
    for layer in subsection1_dicts:
        test_dict.update({layer['name']:layer['score']})
    
    test = {testname:test_dict}
    
    return testname, test, test_max_score, num_of_levels


def three_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, subsection2_dicts, test_dict):
    for first_sect in subsection1_dicts:
        
        if 'score' not in first_sect.keys(): # If the section includes more sections
            dict2 = {}
            for second_sect in subsection2_dicts:
                
                # If the subsection has the right parent folder, update a second dictionary of sections
                if second_sect['parent'] == first_sect['name']: 
                    dict2.update({second_sect['name']:second_sect['score']})
                else:
                    continue
            
            # Once all relevant sections are added to the the second dictionary, update the main dictionary
            test_dict.update({first_sect['name']:dict2})
        
        # If the section has no sections, add that section and its score set to the main dictionary
        else:
            test_dict.update({first_sect['name']:first_sect['score']})

    test = {testname:test_dict}
    
    return testname, test, test_max_score, num_of_levels


def max_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, subsection2_dicts, subsection3_dicts, test_dict):
    for first_sect in subsection1_dicts:
        
        if 'score' not in first_sect.keys(): # If the section includes more sections
            dict2 = {}
            for second_sect in subsection2_dicts:
                
                if 'score' not in second_sect.keys(): # If the section includes more sections
                    if second_sect['parent'] == first_sect['name']:
                        dict3 = {}
                        for third_sect in subsection3_dicts:
                            
                            # If the subsection has the right parent folder, update a third dictionary of sections
                            if third_sect['parent'] == second_sect['name']:
                                dict3.update({third_sect['name']:third_sect['score']})
                            else:
                                continue
                        
                        # Once all relevant sections are added to the the third dictionary, update the second dictionary
                        dict2.update({second_sect['name']:dict3})
                    else:
                        continue
                
                # If no sections, add that section and its score set to the second dictionary
                elif second_sect['parent'] == first_sect['name']:
                    dict2.update({second_sect['name']:second_sect['score']})
                else:
                    continue
            # Once all relevant sections are added to the the second dictionary, update the main dictionary
            test_dict.update({first_sect['name']:dict2})
        
        # If the section has no sections, add that section and its score set to the second dictionary
        else:
            test_dict.update({first_sect['name']:first_sect['score']})

    test = {testname:test_dict}
    return testname, test, test_max_score, num_of_levels