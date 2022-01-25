import error_messages

# BUILD A COMPLEX TEST (More detailed input)
def build_custom_dict(testname):
    
    # Initialize variables
    moreLevels = 'undefined' # User chooses whether they will divide sections into more parts ('y' or 'n')
    proceed_num = 0 # Add to this variable if user chooses to divide a section into more parts
    maxScore = 0 # The maximum score for a particular part of a test
    totalMax = 0 # The overall maximum score for a test type
    numLevels = 0 # The number of levels deep a test is divided 
    sectCount1 = 0 # The number of parts a section is divided into
    sectCount2 = 0 # The number of parts a section is divided int
    subfold1 = [] # A list of dictionaries for the first layer of sections in the test
    subfold2 = [] # A list of dictionaries for the second layer of sections in the test
    subfold3 = [] # A list of dictionaries for the third layer of sections in the test
    dict1 = {} # A dictionary that will hold all dictionaries

    while moreLevels != False and moreLevels[0] != 'n':
        if moreLevels == 'undefined':
            
            # Require user to choose whether they will divide the section into more parts
            while True:
                try:
                    moreLevels = (input('\n-----------------\n\nIs this divided into parts? Y/N ')).lower().strip()
                    if moreLevels[0] == 'y' or moreLevels[0] == 'n':
                        break
                    elif isinstance(moreLevels, str) == False:
                        error_messages.invalid()
                        continue
                    else:
                        error_messages.invalid()
                        continue
                except IndexError:
                    error_messages.invalid()
                    continue
            
            # If the user choose to divide the section into more parts, proceed
            if moreLevels[0] == 'y':
                numLevels += 1 # The test is divided at least one time
                while True:
                    # User decides how many times to divide the test (from 1-10 times)
                    try:
                        get_subSize1 = int(input('\nHow many identical parts? '))
                        if get_subSize1 > 10 or get_subSize1 < 1:
                            error_messages.num_range()
                            continue
                        else:
                            break
                    except ValueError:
                        error_messages.num_range()
                        continue
                print(f'\nPlease enter the name(s) for the section(s)\n-----------------')
                
                # For EACH section, ask user to first enter name of the section
                for i in range(get_subSize1):
                    while True:
                        subName1 = input(f'Please enter a section name for section {i+1}: ')
                        if len(subName1) > 20 or len(subName1) <= 2:
                            error_messages.name_length()
                            continue
                        else:
                            break
                    
                    # Next, as user to decide whether they will divide this single section into more parts
                    while True:
                        try:
                            moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                            # If user decides to divide into more parts, proceed
                            if moreLevels[0] == 'y':
                                proceed_num += 1 # Add to the number -> this means will we create another level of sections within the previous section
                                while True:
                                    # User decides how many times to divide this single section (from 1-10 times)
                                    try:
                                        sectCount1 = int(input(f'Please enter the number of sections in "{subName1}": '))
                                        print('-')
                                        if sectCount1 > 10 or sectCount1 < 1:
                                            error_messages.num_range()
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        error_messages.num_range()
                                        continue
                                # Add this section to the list of dictionaries, with the number of times it is divided as 'count'
                                subfold1.append({'name':subName1, 'count':sectCount1})
                                break
                            
                            # If user decides not to divide into more parts, proceed
                            elif moreLevels[0] == 'n':
                                # Get the maximum score for this single section
                                while True:
                                    try:
                                        maxScore = int(input(f'What is the maximum score for {subName1}? '))
                                        totalMax += maxScore # Add score to the total maximum score for the test
                                        if maxScore < 1:
                                            error_messages.above_1()
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        error_messages.only_digits()
                                
                                # Add this section to the list of dictionaries with the name of the section 
                                # and the score list ("actual score, maximum score, mistakes")
                                subfold1.append({'name':subName1, 'score':['tbd', maxScore, 'none :)']})
                                break
                            # Only accept numbers
                            elif isinstance(moreLevels, str) == False:
                                error_messages.invalid()
                                continue
                            else:
                                error_messages.invalid()
                                continue
                        except IndexError:
                            error_messages.invalid()
                            continue
           
            # If user does not want to divide the test into parts at all, make a very simple test structure 
            else:
                while True:
                    try:
                        maxScore = int(input(f'What is the maximum score for {testname}? ')) # Take the maximum score for this part
                        totalMax += maxScore
                        if maxScore < 1:
                            error_messages.above_1()
                            continue
                        else:
                            break
                    except ValueError:
                        error_messages.only_digits()
                
                # Create a test, add score to the test's maximum score and return the name of the test, 
                # the dictionary, it's maximum and how many layers deep the test is
                test = {testname:['tbd', maxScore, 'none :)']}
                totalMax += maxScore
                return testname, test, totalMax, numLevels
           
            # If a section was divided at least once more, proceed to second layer of sections
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1 # The test is divided a second time
                # Iterate through all first sections
                for i in subfold1:
                    if 'score' in i.keys(): # Skip all sections that contain scores, since they are not divided
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        # Based on how many parts the user chose to divide into, get a name for each part
                        for j in range(i['count']): 
                            while True:
                                subName2 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName2) > 20 or len(subName2) <= 2:
                                    error_messages.name_length()
                                    continue
                                else:
                                    break
                            
                            # Add a list of dictionaries for this single section's sections, with the number of times it is divided as 'count'
                            while True:
                                # Require user to choose whether they will divide the section into more parts
                                try:
                                    moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                                    if moreLevels[0] == 'y':
                                        # Add to the number -> this means will we create another level of sections within the current section
                                        proceed_num += 1 
                                        while True:
                                            # User decides how many times to divide these sections (from 1-10 times)
                                            try:
                                                sectCount2 = int(input(f'Please enter the number of sections in "{subName2}": '))
                                                print('-')
                                                if sectCount2 > 10 or sectCount2 < 1:
                                                    error_messages.num_range()
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                error_messages.num_range()
                                                continue
                                        
                                        # Add this section to the list of dictionaries, with its name, its parent section's name 
                                        # and the number of times it is divided as 'count'
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'count':sectCount2}) 
                                        break
                                    
                                    # If user decides not to divide this section into more parts, proceed
                                    elif moreLevels[0] == 'n':
                                        # Get the maximum score for this specific section
                                        while True:
                                            try:
                                                maxScore = int(input(f'What is the maximum score for {subName2}? '))
                                                totalMax += maxScore # Add score to the total maximum score for the test
                                                if maxScore < 1:
                                                    error_messages.above_1()
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                error_messages.only_digits()
                                        
                                        # Add this section to the list of dictionaries with the name of the section 
                                        # and the score list ("actual score, maximum score, mistakes")
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'score':['tbd', maxScore, 'none :)']}) 
                                        break
                                    # Only accept numbers
                                    elif isinstance(moreLevels, str) == False:
                                        error_messages.invalid()
                                        continue
                                    else:
                                        error_messages.invalid()
                                        continue
                                except IndexError:
                                    error_messages.invalid()
                                    continue
            
            # If the user chose not to divide ANY section, append all sections to the main dictionary 
            # and return the name of the test, the dictionary, it's maximum score and how many layers deep the test is
            else:
                for layer in subfold1:
                    dict1.update({layer['name']:layer['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            
            # If a section was divided at least once more, proceed to third layer of sections
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1 # The test is divided a third time
                
                # Iterate through all second sections
                for i in subfold2:
                    if 'score' in i.keys(): # Skip all sections that contain scores, since they are not divided
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        # Based on how many parts the user chose to divide into, get a name for each part
                        for j in range(i['count']):
                            while True:
                                subName3 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName3) > 20 or len(subName3) <= 2:
                                    error_messages.name_length()
                                    continue
                                else:
                                    break
                            
                            # Add a list of dictionaries for this single section's sections, with the number of times it is divided as 'count'
                            while True:
                                # Get the maximum score for this final (deepest) specific section
                                try:
                                    maxScore = int(input(f'What is the maximum score for {subName3}? '))
                                    totalMax += maxScore
                                    if maxScore < 1:
                                        error_messages.above_1()
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    error_messages.only_digits()
                            # Add this section to the list of dictionaries with the name of the section 
                            # and the score list ("actual score, maximum score, mistakes")
                            subfold3.append({'parent':i['name'], 'name':subName3, 'score':['tbd', maxScore, 'none :)']})
                
                # After all final sections have been added to the last list of dictionaries, 
                # iterate through ALL sections, starting with the list of main sections
                for prim_f in subfold1:
                    # If the section includes more dictionaries of other sections, proceed
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        # Iterate through all subsections of this section
                        for sec_f in subfold2:
                            # If the section includes more dictionaries of other sections, proceed
                            if 'score' not in sec_f.keys():
                                # If the subsection has the right parent folder, update the second dictionary of sections
                                if sec_f['parent'] == prim_f['name']:
                                    # Iterate through all subsections of this section
                                    dict3 = {}
                                    for ter_f in subfold3:
                                        # If the subsection has the right parent folder, update the third dictionary of sections
                                        if ter_f['parent'] == sec_f['name']:
                                            dict3.update({ter_f['name']:ter_f['score']})
                                        else:
                                            continue
                                    # Once all relevant sections are added to the the third dictionary, update the second dictionary
                                    dict2.update({sec_f['name']:dict3})
                                else:
                                    continue
                            # If the section has no sections, add that section and its score set to the second dictionary
                            elif sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        
                        # Once all relevant sections are added to the the second dictionary, update the main dictionary
                        dict1.update({prim_f['name']:dict2})
                    # If the section has no sections, add that section and its score set to the second dictionary
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                
                # Create the test dictionary with the test name as the main key, then return the name of the test, 
                # the dictionary, it's maximum and how many layers deep the test is
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            
            # If the user chose not to divide ANY section, proceed
            else:
                # Iterate through all sections in the list of main sections
                for prim_f in subfold1:
                    # If the section includes more dictionaries of other sections, proceed
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        # Iterate through all subsections of this section
                        for sec_f in subfold2:
                            # If the subsection has the right parent folder, update a second dictionary of sections
                            if sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        # Once all relevant sections are added to the the second dictionary, update the main dictionary
                        dict1.update({prim_f['name']:dict2})
                    # If the section has no sections, add that section and its score set to the main dictionary
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                
                # Create the test dictionary with the test name as the main key, then return the name of the test, 
                # the dictionary, it's maximum and how many layers deep the test is
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
        
        # If the user chose not to divide test into ANY parts ### CONSIDER DELETION; MAY BE UNNEEDED
        elif moreLevels == 'n':
            while True:
                try:
                    maxScore = int(input(f'What is the maximum score for {testname}? ')) # Take the maximum score for this part
                    totalMax += maxScore # Add the score to the total maximum score for the test
                    if maxScore < 1:
                        error_messages.above_1()
                        continue
                    else:
                        break
                except ValueError:
                    error_messages.only_digits()
            
            # Create a test, add score to the test's maximum score and return the name of the test, 
            # the dictionary, it's maximum and how many layers deep the test is
            dict = {testname:['tbd', maxScore, 'none :)']}
            test = {testname:dict}
            return testname, test, totalMax, numLevels
        else:
            continue