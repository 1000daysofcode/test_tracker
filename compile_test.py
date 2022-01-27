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
    
    test = {testname:['tbd', sect_part_score, 'none :)']}
    test_max_score = sect_part_score
    
    return testname, test, test_max_score, num_of_levels # Return results for main function


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
                
                if second_sect['parent'] == first_sect['name']: # If the subsection has the right parent folder
                    dict2.update({second_sect['name']:second_sect['score']})
                else:
                    continue
            
            test_dict.update({first_sect['name']:dict2}) # Update main dict after subsections added to second dict
        
        else: # If no sections, add section and score set to main dict
            test_dict.update({first_sect['name']:first_sect['score']})

    test = {testname:test_dict}
    
    return testname, test, test_max_score, num_of_levels


def max_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, subsection2_dicts, subsection3_dicts, test_dict):
    for first_sect in subsection1_dicts:
        
        if 'score' not in first_sect.keys(): # If the section includes more sections
            dict2 = {}
            for second_sect in subsection2_dicts:
                
                if 'score' not in second_sect.keys(): # If the section includes more sections
                    if second_sect['parent'] == first_sect['name']: # If the subsection has the right parent folder
                        dict3 = {}
                        for third_sect in subsection3_dicts:
                            
                            if third_sect['parent'] == second_sect['name']: # If the subsection has the right parent folder
                                dict3.update({third_sect['name']:third_sect['score']})
                            else:
                                continue
                        
                        dict2.update({second_sect['name']:dict3}) # Update second dict after subsections added to third dict
                    else:
                        continue
                
                elif second_sect['parent'] == first_sect['name']: # If no sections, add section and score set to second dict
                    dict2.update({second_sect['name']:second_sect['score']})
                else:
                    continue
            
            test_dict.update({first_sect['name']:dict2}) # Update main dict after subsections added to second dict
        
        else: # If no sections, add section and score set to main dict
            test_dict.update({first_sect['name']:first_sect['score']})

    test = {testname:test_dict}
    return testname, test, test_max_score, num_of_levels


def compile_test_scores(scores_dct, subsection1, subsection2, subsection3, subsection4):
    for first_sect in subsection1:
        if 'score' not in first_sect.keys(): # If the section includes more sections
            dict2 = {}
            for second_sect in subsection2:
                
                if 'score' not in second_sect.keys(): # If the section includes more sections
                    if second_sect['parent'] == first_sect['name']: # If the subsection has the right parent folder
                        dict3 = {}
                        for third_sect in subsection3: 

                            if 'score' not in third_sect.keys(): # If the section includes more sections
                                if third_sect['parent'] == second_sect['name']: # If the subsection has the right parent folder
                                    dict4 = {}
                                    for fourth_sect in subsection4:
                                        
                                        if fourth_sect['gparent'] == third_sect['parent'] == second_sect['name']: # If the subsection has the right parent folder
                                            dict4.update({fourth_sect['name']:fourth_sect['score']})
                                        else:
                                            pass
                                   
                                    dict3.update({third_sect['name']:dict4}) # Update third dict after subsections added to fourth dict
                                else:    
                                    continue
                            
                            elif third_sect['parent'] == second_sect['name']:  # If no sections, add section and score set to third dict
                                dict3.update({third_sect['name']:third_sect['score']})
                        
                        dict2.update({second_sect['name']:dict3}) # Update second dict after subsections added to third dict
                    else:
                        continue
                
                elif second_sect['parent'] == first_sect['name']: # If no sections, add section and score set to second dict
                    dict2.update({second_sect['name']:second_sect['score']})
                else:
                    continue
            
            scores_dct.update({first_sect['name']:dict2}) # Update main dict after subsections added to second dict
        
        else: # If no sections, add section and score set to main dict
            scores_dct.update({first_sect['name']:first_sect['score']})
    
    return scores_dct