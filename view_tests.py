def view(dct):
    for section1_name, section1_values in dct.items():
        print(f'-> {section1_name}\n----------------') 
        if isinstance(section1_values, dict) != True: # not divided into more sections
            next_section = section1_values
            if isinstance(next_section, list) == True: # if it is a list of scores, print score
                print(f'\tScore: {section1_values[0]} out of: {section1_values[1]} || Mistakes: {section1_values[2]}')
            else:
                print()
                pass
        
        else: # If the value of the subsection is a dictionary, print remainder of test
            for section2_name, section2_values in dct[section1_name].items():
                print(f'{section2_name}')
                if isinstance(dct[section1_name][section2_name], dict) != True:
                    next_section = section2_values
                    if isinstance(next_section, list) == True:
                        print(f'\tScore: {section2_values[0]} out of: {section2_values[1]} || Mistakes: {section2_values[2]}')
                    else:
                        print(f'{section2_name}') 
                
                else:
                    for section3_name, section3_values in dct[section1_name][section2_name].items():
                        print(f'{section3_name} : ') 
                        if isinstance(dct[section1_name][section2_name][section3_name], dict) != True:
                            next_section = section3_values
                            if isinstance(next_section, list) == True:
                                print(f'\tScore: {section3_values[0]} out of: {section3_values[1]} || Mistakes: {section3_values[2]}')
                            else:
                                print(section3_name + " : " + str(dct[section1_name][section2_name][section3_name]))
                        
                        else:
                            for section4_name, section4_values in dct[section1_name][section2_name][section3_name].items():
                                print(f'\t{section4_name} ',end='')
                                if isinstance(dct[section1_name][section2_name][section3_name][section4_name], dict) != True:
                                    next_section = section4_values
                                    if isinstance(next_section, list) == True: 
                                        print(f'|| Score: {section4_values[0]} out of: {section4_values[1]} || Mistakes: {section4_values[2]}')
                                    else:
                                        print(f'\t{section4_name} ',end='')
                                
                                else: # Print all scores in final layer
                                    for section5_name, section5_values in dct[section1_name][section2_name][section3_name][section4_name].items():
                                        print(f'\n\t{section5_name} || Score: {section5_values[0]} out of: {section5_values[1]} || Mistakes: {section5_values[2]}')
                
                print('----------------') # Print in between major sections of the test