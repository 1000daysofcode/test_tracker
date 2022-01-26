import compile_test
import error_messages


# BUILD A SIMPLE TEST (Less detailed input)
def build_simple_dict(testname):
    
    test_dict = {} 
    num_of_levels = 0
    sect_part_score = 0 
    test_max_score = 0 
    num_times_to_proceed = 0 
    make_more_levels = 'undefined'

    subsection1_dicts = [] 
    subsection2_dicts = [] 
    subsection3_dicts = []
    
    while make_more_levels != False and make_more_levels[0] != 'n':
        if make_more_levels == 'undefined':
            
            make_more_levels = decide_to_divide() # Choose whether to divide section

            # If the user chose to divide the section into more parts
            if make_more_levels[0] == 'y':
                num_of_levels += 1 # The test is divided at least one time
                
                get_subSize1 = get_sectCount()
                
                print(f'\nPlease enter the name(s) for the section(s)\n-----------------') 
                section_names = [] # List of section_names that all section_names are appended to
                section_names = add_to_section_names(section_names, get_subSize1) # Get a name for each part

                times_to_proceed, total_section_score, subsection_dicts = create_subsection(subsection1_dicts, section_names, testname)

                num_times_to_proceed += times_to_proceed
                test_max_score += total_section_score
                subsection1_dicts = subsection_dicts

            else: # Return a very simple test structure 
                return compile_test.single_part_test(testname, test_max_score, num_of_levels)
            
            if num_times_to_proceed > 0:
                num_times_to_proceed = 0
                num_of_levels += 1 # The test is divided a second time

                for i in subsection1_dicts:
                    if 'score' in i.keys(): # Skip all sections that contain scores, since they are not divided
                        continue
                    else:     
                        print(f'\nPlease enter the section_names for section "{i["name"]}"\n-----------------')
                        section_names = [] # List of section_names that all section_names are appended to
                        section_names = add_to_section_names(section_names, i['count']) # Get a name for each part

                        times_to_proceed, total_section_score, subsection_dicts = create_subsection(subsection2_dicts, section_names, i["name"])

                        num_times_to_proceed += times_to_proceed
                        test_max_score += total_section_score
                        subsection2_dicts = subsection_dicts

            else: # Return a two-layer test
                return compile_test.two_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, test_dict)

            if num_times_to_proceed > 0:
                num_times_to_proceed = 0
                num_of_levels += 1 # The test is divided a third time
                
                for i in subsection2_dicts:
                    if 'score' in i.keys():
                        continue
                    else:     
                        print(f'\nPlease enter the section_names for "{i["parent"]} - {i["name"]}"\n-----------------')
                        section_names = [] # List of section_names that all section_names are appended to
                        section_names = add_to_section_names(section_names, i['count'])
                        
                        sect_part_score = get_sect_part_score() # Get the maximum score
                        
                        for name in section_names: # Append final layer to last dict list
                            subsection3_dicts.append({'parent':i['name'], 'name':name, 'score':['tbd', sect_part_score, 'none :)']})
                            test_max_score += sect_part_score
                
                return compile_test.max_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, subsection2_dicts, subsection3_dicts, test_dict)
            
            else: # return a three-layer test
                return compile_test.three_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, subsection2_dicts, test_dict)

# MAKE SUBSECTIONS
def create_subsection(subsection_dicts, section_names, parent_name):
    times_to_proceed = 0
    total_section_score = 0

    while True:
        try:
            make_more_levels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
            
            if make_more_levels[0] == 'y': # If user decides to divide into more parts
                times_to_proceed += 1 
                section1_count = get_sectCount() # Number of times to divide sections (up to 10)
                
                for name in section_names: # Add a list of dictionaries for each section's sections
                    subsection_dicts.append({'parent':parent_name, 'name':name, 'count':section1_count})
                break
            
            elif make_more_levels[0] == 'n': # If user decides not to divide
                sect_part_score = get_sect_part_score() # Get the maximum score
                
                for name in section_names:
                    subsection_dicts.append({'parent':parent_name, 'name':name, 'score':['tbd', sect_part_score, 'none :)']})
                    total_section_score += sect_part_score
                break
            elif isinstance(make_more_levels, str) == False:
                error_messages.invalid()
                continue
            else:
                error_messages.invalid()
                continue
        except IndexError:
            error_messages.invalid()
            continue

    return times_to_proceed, total_section_score, subsection_dicts


# HELPER FUNCTIONS
def decide_to_divide():
    while True:
        try:
            make_more_levels = (input('\n-----------------\n\nIs this divided into parts? Y/N ')).lower().strip()
            if make_more_levels[0] == 'y' or make_more_levels[0] == 'n':
                return make_more_levels
            
            elif isinstance(make_more_levels, str) == False:
                error_messages.invalid()
                continue
            else:
                error_messages.invalid()
                continue
        except IndexError:
            error_messages.invalid()
            continue


def get_sectCount():
    while True:
        try:
            sectCount = int(input(f'Please enter the number of sections: '))
            print('-')
            if sectCount > 10 or sectCount < 1:
                error_messages.num_range()
                continue
            else:
                return sectCount
        except ValueError:
            error_messages.num_range()
            continue


def add_to_section_names(section_names, num):
    for i in range(num):
        while True:
            name = input(f'Please enter a section name for section {i+1}: ')
            if len(name) > 20 or len(name) <= 2: # Name from 3-20 characters
                error_messages.name_length()
                continue
            else:
                section_names.append(name)
                break
    return section_names


def get_sect_part_score():
    while True:
        try:
            sect_part_score = int(input(f'What is the maximum score for each these sections? '))
            if sect_part_score < 1:
                error_messages.above_1()
                continue
            else:
                return sect_part_score
        except ValueError:
            error_messages.only_digits()