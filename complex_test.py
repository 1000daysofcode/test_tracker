import compile_test
import error_messages


# BUILD A COMPLEX TEST (More detailed input)
def build_custom_dict(testname):
    
    test_dict = {}
    num_of_levels = 0
    sect_part_score = 0
    test_max_score = 0
    num_times_to_proceed = 0
    make_more_levels = 'undefined'
    
    # sectCount1 = 0 # The number of parts a section is divided into
    # sectCount2 = 0 # The number of parts a section is divided into
    
    subsection1_dicts = []
    subsection2_dicts = []
    subsection3_dicts = []

    while make_more_levels != False and make_more_levels[0] != 'n':
        if make_more_levels == 'undefined':
            
            make_more_levels = decide_to_divide() # Choose whether to divide section
            
            if make_more_levels[0] == 'y': # If the user chose to divide the section
                num_of_levels += 1 # The test is divided at least one time
                
                sect_count = get_sect_count(testname)
                
                print(f'\nPlease enter the name(s) for the section(s)\n-----------------')
                for i in range(sect_count):
                    section_name1 = get_section_name(i+1)
                    
                    times_to_proceed, total_section_score, subsection_dicts = create_subsection(subsection1_dicts, section_name1, testname)
                    
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
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        for j in range(i['count']): 
                            section_name2 = get_section_name(j+1)
                            
                            times_to_proceed, total_section_score, subsection_dicts = create_subsection(subsection2_dicts, section_name2, i["name"])
                    
                            num_times_to_proceed += times_to_proceed
                            test_max_score += total_section_score
                            subsection2_dicts = subsection_dicts
            
            else: # Return a two-layer test
                return compile_test.two_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, test_dict)
            
            if num_times_to_proceed > 0:
                num_times_to_proceed = 0
                num_of_levels += 1 # The test is divided a third time
                
                for i in subsection2_dicts:
                    if 'score' in i.keys(): # Skip all sections that contain scores, since they are not divided
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        for j in range(i['count']):
                            section_name3 = get_section_name(j+1)
                            
                            sect_part_score = get_sect_part_score(section_name3) # Get the maximum score deepest section
                            test_max_score += sect_part_score

                            subsection3_dicts.append({'parent':i['name'], 'name':section_name3, 'score':['tbd', sect_part_score, 'none :)']})
                
                return compile_test.max_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, subsection2_dicts, subsection3_dicts, test_dict)
            
            else: # return a three-layer test
                
                return compile_test.three_layer_test(testname, test_max_score, num_of_levels, subsection1_dicts, subsection2_dicts, test_dict)


# MAKE SUBSECTIONS
def create_subsection(subsection_dicts, section_name, parent_name):
    times_to_proceed = 0
    total_section_score = 0

    while True:
        try:
            make_more_levels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()

            if make_more_levels[0] == 'y': # If user decides to divide
                times_to_proceed += 1
                sect_count = get_sect_count(section_name) # Number of times to divide sections (up to 10)
                
                subsection_dicts.append({'parent':parent_name, 'name':section_name, 'count':sect_count})
                break
            
            elif make_more_levels[0] == 'n': # If user decides not to divide
                sect_part_score = get_sect_part_score(section_name)
                total_section_score += sect_part_score # Add score to the total maximum score for the test

                subsection_dicts.append({'parent':parent_name,'name':section_name, 'score':['tbd', sect_part_score, 'none :)']})
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


def get_sect_count(name):
    while True:
        try:
            sect_count = int(input(f'Please enter the number of sections in "{name}": '))
            print('-')
            if sect_count > 10 or sect_count < 1:
                error_messages.num_range()
                continue
            else:
                break
        except ValueError:
            error_messages.num_range()
            continue
    return sect_count


def get_section_name(num):
    while True:
        name = input(f'Please enter a section name for section {num}: ')
        if len(name) > 20 or len(name) <= 2:
            error_messages.name_length()
            continue
        else:
            break
    return name


def get_sect_part_score(name):
    while True:
        try:
            sect_part_score = int(input(f'What is the maximum score for {name}? '))
            if sect_part_score < 1:
                error_messages.above_1()
                continue
            else:
                break
        except ValueError:
            error_messages.only_digits()
    return sect_part_score