import copy

def main():
    choice = 'undefined'
    # Greet user
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

    # Ask for name (add to variable)
    name = input('\n\nWelcome to Test Tracker! Please enter your name: ')
    print(f'\nWelcome, {name}!\n\nPlease create at least one test structure to continue.')

    # Initialize data structures
    test_raw = []
    test_db = []
    test_index = []

    while choice != False and choice[0] != 'q':
        if choice == 'undefined':
            while True:
                try:
                    choice = (input('''
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
                    if choice[0] == 'v' or choice[0] == 'a' or choice[0] == 'n' or choice[0] == 's' or choice[0] == 'q':
                        break
                    elif isinstance(choice, str) == False:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                    else:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                except IndexError:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            if choice[0] == 'v':
                if len(test_db) < 1:
                    print(f'\n====================================================\n| Please submit a new test score in order to view. |\n====================================================')
                else:
                    print('\nHere are your test names and locations:\n')
                    for c, i in enumerate(test_index):
                        print(f'Test structure: {i["name"]} || Test location: {c+1}')
                    while True:
                        try:
                            test_choice = int(input('---\n\nPlease enter the location of your tests: '))-1
                            if test_choice > len(test_index) or test_choice < 0:
                                print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================')
                                continue
                            else:
                                break
                        except:
                            print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================')
                            continue
                    tests = test_db[test_choice]
                    print(f'Below are all test results for test {test_index[test_choice-1]}:\n\n================')
                    for c, dct in enumerate(tests):
                        for title, v in dct.items():
                                print(f'{c+1}) Test Name: {title}\n----------------') 
                                if isinstance(v, dict) != True:
                                    test = v
                                    if isinstance(test, list) == True:
                                        print(f'\tScore: {v[0]} out of: {v[1]} || Mistakes: {v[2]}')
                                    else:
                                        print()
                                        pass
                                else:
                                    for layer1, v1 in dct[title].items():
                                        print(f'{layer1}')
                                        if isinstance(dct[title][layer1], dict) != True:
                                            test = v1
                                            if isinstance(test, list) == True:
                                                print(f'\tScore: {v1[0]} out of: {v1[1]} || Mistakes: {v1[2]}')
                                            else:
                                                print(f'{layer1}') 
                                        else:
                                            for layer2, v2 in dct[title][layer1].items():
                                                print(f'{layer2} : ')
                                                if isinstance(dct[title][layer1][layer2], dict) != True:
                                                    test = v2
                                                    if isinstance(test, list) == True:
                                                        print(f'\tScore: {v2[0]} out of: {v2[1]} || Mistakes: {v2[2]}')
                                                    else:
                                                        print(layer2 + " : " + str(dct[title][layer1][layer2]))
                                                else:
                                                    for layer3, v3 in dct[title][layer1][layer2].items():
                                                        print(f'\t{layer3} || Score: {v3[0]} out of: {v3[1]} || Mistakes: {v3[2]}')
                                        print('----------------') 
                                print('\n\n================')  
                        while True:
                            input('\nYour tests are above.\n\nPress enter to continue. \n\n----------------\n')
                            break     
                choice = 'undefined'
                continue
            elif choice[0] == 'a':
                print('\nYou chose to view a score analysis.\n')
                choice = 'undefined'
                continue
            elif choice[0] == 'n':
                print('\nYou chose to add a new score.\n')
                if len(test_raw) < 1:
                    print(f'\n========================================================\n| Please add at least one test score in order to view. |\n========================================================')
                    choice = 'undefined'
                    continue
                else:
                    index, scores = add_scores(test_raw, test_db, test_index)
                    test_db[index].append(scores)
                    print(test_db)
                    choice = 'undefined'
                    continue
            elif choice[0] == 's':
                print('\nYou chose to create a new test structure.\n')
                testname, dct, total, levels = make_test_shell()
                test_db.append([])
                test_raw.append(dct)
                test_index.append({'name':testname, 'maxscore':total, 'mistakes':make_mlist()})
                print(f'\nTest "{testname}" created. Please see below:')
                for title, v in dct.items():
                    print(f'\n{title}\n---') 
                    if isinstance(v, dict) != True:
                        test = v
                        if isinstance(test, list) == True:
                            print(f'\tScore: {v[0]} out of: {v[1]} || Mistakes: {v[2]}')
                        else:
                            print('ERROR. PLEASE CONTACT DESIGNER')
                            pass
                    else:
                        for layer1, v1 in dct[title].items():
                            print(f'{layer1}')
                            if isinstance(dct[title][layer1], dict) != True:
                                test = v1
                                if isinstance(test, list) == True:
                                    print(f'\tScore: {v1[0]} out of: {v1[1]} || Mistakes: {v1[2]}')
                                else:
                                    print(f'{layer1}') 
                            else:
                                for layer2, v2 in dct[title][layer1].items():
                                    print(f'{layer2} : ')
                                    if isinstance(dct[title][layer1][layer2], dict) != True:
                                        test = v2
                                        if isinstance(test, list) == True:
                                            print(f'\tScore: {v2[0]} out of: {v2[1]} || Mistakes: {v2[2]}')
                                        else:
                                            print(layer2 + " : " + str(dct[title][layer1][layer2]))
                                    else:
                                        for layer3, v3 in dct[title][layer1][layer2].items():
                                            print(f'\t{layer3} || Score: {v3[0]} out of: {v3[1]} || Mistakes: {v3[2]}')
                            print('----------------')
                while True:
                    input('Press enter to continue. \n\n----------------\n')
                    break
                # print(type(dict_s))
                choice = 'undefined'
                continue
            else:
                print('''
Thank you for using Test Tracker version 0!

   ______                ____               __
  / ____/___  ____  ____/ / /_  __  _____  / /
 / / __/ __ \/ __ \/ __  / __ \/ / / / _ \/ / 
/ /_/ / /_/ / /_/ / /_/ / /_/ / /_/ /  __/_/  
\____/\____/\____/\__,_/_.___/\__, /\___(_)   
                             /____/          
                             
''')
                choice = False

    # for i in test_index:
    #     print(f'Test structure: {i["name"]}\nTest location: {i["location"]+1}\n-')
    # test_choice = int(input('Please enter the location of your test'))-1

    # view = input('To see the test structure, press S.\nTo see your test results, press R')
    # if view == 's':
    #     print(test_raw[test_choice])
    # else:
    #     print(test_db[test_choice])
    # print(test_db)

    # # Type 'QUIT NOW' at any time to quit program. Confirmation y/n

def build_simple_dict(testname):
    moreLevels = 'undefined'    
    maxScore = 0
    totalMax = 0
    numLevels = 0
    subfold1 = []
    subfold2 = []
    subfold3 = []
    dict1 = {}
    dict2 = {}
    dict3 = {}
    while moreLevels != False and moreLevels[0] != 'n':
        if moreLevels == 'undefined':
            while True:
                try:
                    moreLevels = (input('\n-----------------\nIs this divided into parts? Y/N ')).lower().strip()
                    if moreLevels[0] == 'y' or moreLevels[0] == 'n':
                        break
                    elif isinstance(moreLevels, str) == False:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                    else:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                except IndexError:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            if moreLevels[0] == 'y':
                numLevels += 1
                while True:
                    try:
                        get_subSize1 = int(input('\nHow many identical parts? '))
                        print('\n')
                        if get_subSize1 > 10 or get_subSize1 < 1:
                            print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                        continue
                if get_subSize1 > 1:
                    print(f'\nPlease enter the names for all {get_subSize1} parts:\n-----------------')
                else: 
                    print(f'\nPlease enter the name:\n-----------------')
                for i in range(get_subSize1):
                    while True:
                        subName1 = input(f'Please enter a section name for section {i+1}: ')
                        if len(subName1) > 20 or len(subName1) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            break
                    subfold1.append([i+1, subName1])
                while True:
                    try:
                        moreLevels = (input('\n-----------------\nDo you need to divide into more sections [Ask #2]? Y/N ')).lower().strip()
                        if moreLevels[0] == 'y' or moreLevels[0] == 'n':
                            break
                        elif isinstance(moreLevels, str) == False:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                        else:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                    except IndexError:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
            else:
                while True:
                        try:
                            maxScore = int(input(f'What is the maximum score for {testname}? '))
                            totalMax += maxScore
                            if maxScore < 1:
                                print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                continue
                            else:
                                break
                        except ValueError:
                            print('\n=============================\n| Please enter only digits. |\n=============================')
                dict = {testname:[0, maxScore, 'mistakes']}
                return testname, dict, totalMax, numLevels

            # If yes, continue building subfolders, if no process dict
            if moreLevels[0] == 'y':
                numLevels += 1
                while True:
                    try:
                        get_subSize2 = int(input('\nHow many identical parts is this broken into? '))
                        if get_subSize2 > 10 or get_subSize2 < 1:
                            print('\n====================================\n| Please enter a number from 1-10. |\n====================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n====================================\n| Please enter a number from 1-10. |\n====================================')
                        continue
                if get_subSize2 > 1:
                    print(f'\nPlease enter the names for all {get_subSize2} parts:\n-----------------')
                else: 
                    print(f'\nPlease enter the name:\n-----------------')
                for i in range(get_subSize2):
                    while True:
                        subName2 = input(f'Please enter a section name for section {i+1}: ')
                        if len(subName2) > 20 or len(subName2) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            break
                    subfold2.append([i+1, subName2])
                while True:
                    try: 
                        moreLevels = (input('\n-----------------\nDo you need to divide into more sections [Ask #3]? Y/N ')).lower().strip()
                        if moreLevels[0] == 'y' or moreLevels[0] == 'n':
                            break
                        elif isinstance(moreLevels, str) == False:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                        else:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
                    except IndexError:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
            else:
                for layer1 in subfold1:
                    while True:
                        try:
                            maxScore = int(input(f'What is the maximum score for {layer1[1]}? '))
                            totalMax += maxScore
                            if maxScore < 1:
                                print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                continue
                            else:
                                break
                        except ValueError:
                            print('\n=============================\n| Please enter only digits. |\n=============================')
                    dict1.update({layer1[1]:[0, maxScore, 'none :)']})
                return testname, dict1, totalMax, numLevels
            
            if moreLevels[0] == 'y':
                numLevels += 1
                while True:
                    try:
                        get_subSize3 = int(input('\nHow many identical parts? '))
                        if get_subSize3 > 10 or get_subSize3 < 1:
                            print('\n====================================\n| Please enter a number from 1-10. |\n====================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n====================================\n| Please enter a number from 1-10. |\n====================================')
                if get_subSize3 > 1:
                    print(f'\nPlease enter the names for all {get_subSize3} parts:\n-----------------')
                else: 
                    print(f'\nPlease enter the name:\n-----------------')
                for i in range(get_subSize3):
                    while True:
                        subName3 = input(f'Please enter a section name for section {i+1}: ')
                        if len(subName3) > 20 or len(subName3) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            break
                    subfold3.append([i+1, subName3])
                for layer3 in subfold3:
                    while True:
                        try:
                            maxScore = int(input(f'What is the maximum score for {layer3[1]}? '))
                            totalMax += maxScore
                            if maxScore < 1:
                                print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                continue
                            else:
                                break
                        except ValueError:
                            print('\n=============================\n| Please enter only digits. |\n=============================')
                    dict3.update({layer3[1]:[0, maxScore, 'none :)']})
                for layer2 in subfold2:
                    dict2.update({layer2[1]:dict3})
                for layer1 in subfold1:
                    dict1.update({layer1[1]:dict2})
                return testname, dict1, totalMax, numLevels
            else:
                for layer2 in subfold2:
                    while True:
                        try:
                            maxScore = int(input(f'What is the maximum score for {layer2[1]}? '))
                            totalMax += maxScore
                            if maxScore < 1:
                                print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                continue
                            else:
                                break
                        except ValueError:
                            print('\n=============================\n| Please enter only digits. |\n=============================')
                    dict2.update({layer2[1]:[0, maxScore, 'none :)']})
                for layer1 in subfold1:
                    dict1.update({layer1[1]:dict2})
                return testname, dict1, totalMax, numLevels
        elif moreLevels[0] == 'n':
            dict = {testname:[0,'none :)']}
            return testname, dict, totalMax, numLevels
        else:
            continue

def build_custom_dict(testname):
    moreLevels = 'undefined'
    proceed_num = 0
    maxScore = 0
    totalMax = 0
    numLevels = 0
    sectCount1 = 0
    sectCount2 = 0
    subfold1 = []
    subfold2 = []
    subfold3 = []
    dict1 = {}

    while moreLevels != False and moreLevels[0] != 'n':
        if moreLevels == 'undefined':
            while True:
                try:
                    moreLevels = (input('\n-----------------\n\nIs this divided into parts? Y/N ')).lower().strip()
                    if moreLevels[0] == 'y' or moreLevels[0] == 'n':
                        break
                    elif isinstance(moreLevels, str) == False:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                    else:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                except IndexError:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            if moreLevels[0] == 'y':
                numLevels += 1
                while True:
                    try:
                        get_subSize1 = int(input('\nHow many identical parts? '))
                        if get_subSize1 > 10 or get_subSize1 < 1:
                            print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                        continue
                print(f'\nPlease enter the name(s) for the section(s)\n-----------------')
                for i in range(get_subSize1):
                    while True:
                        subName1 = input(f'Please enter a section name for section {i+1}: ')
                        if len(subName1) > 20 or len(subName1) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            break
                    while True:
                        try:
                            moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                            if moreLevels[0] == 'y':
                                proceed_num += 1
                                while True:
                                    try:
                                        sectCount1 = int(input(f'Please enter the number of sections in "{subName1}": '))
                                        print('-')
                                        if sectCount1 > 10 or sectCount1 < 1:
                                            print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                        continue
                                subfold1.append({'name':subName1, 'count':sectCount1})
                                break
                            elif moreLevels[0] == 'n':
                                while True:
                                    try:
                                        maxScore = int(input(f'What is the maximum score for {subName1}? '))
                                        totalMax += maxScore
                                        if maxScore < 1:
                                            print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print('\n=============================\n| Please enter only digits. |\n=============================')
                                subfold1.append({'name':subName1, 'score':[0, maxScore, 'none :)']})
                                break
                            elif isinstance(moreLevels, str) == False:
                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                continue
                            else:
                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                continue
                        except IndexError:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
            else:
                while True:
                    try:
                        maxScore = int(input(f'What is the maximum score for {testname}? '))
                        totalMax += maxScore
                        if maxScore < 1:
                            print('\n==================================\n| Please enter a number above 1. |\n==================================')
                            continue
                        else:
                            break
                    except ValueError:
                        print('\n=============================\n| Please enter only digits. |\n=============================')
                test = {testname:[0, maxScore, 'Mistakes']}
                return testname, test, totalMax, numLevels

            # If yes, continue building subfolders, if no process dict
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1
                # get_subSize2 = int(input('How many identical parts? '))
                for i in subfold1:
                    if 'score' in i.keys():
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        for j in range(i['count']):
                            while True:
                                subName2 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName2) > 20 or len(subName2) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    break
                            while True:
                                try:
                                    moreLevels = (input('Do you need to divide into more sections? Y/N ')).lower().strip()
                                    if moreLevels[0] == 'y':
                                        proceed_num += 1
                                        while True:
                                            try:
                                                sectCount2 = int(input(f'Please enter the number of sections in "{subName2}": '))
                                                print('-')
                                                if sectCount2 > 10 or sectCount2 < 1:
                                                    print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                                continue
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'count':sectCount2}) 
                                        break
                                    elif moreLevels[0] == 'n':
                                        while True:
                                            try:
                                                maxScore = int(input(f'What is the maximum score for {subName2}? '))
                                                totalMax += maxScore
                                                if maxScore < 1:
                                                    print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print('\n=============================\n| Please enter only digits. |\n=============================')
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'score':[0, maxScore, 'none :)']}) 
                                        break
                                    elif isinstance(moreLevels, str) == False:
                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                        continue
                                    else:
                                        print('\n=================================\n| That is not a valid response. |\n=================================')
                                        continue
                                except IndexError:
                                    print('\n=================================\n| That is not a valid response. |\n=================================')
                                    continue
                            # subfold2.append([sectCount2, subName2])           
            else:
                for layer in subfold1:
                    dict1.update({layer['name']:layer['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            
            if proceed_num > 0:
                proceed_num = 0
                numLevels += 1
                # get_subSize3 = int(input('How many identical parts? '))
                for i in subfold2:
                    if 'score' in i.keys():
                        continue
                    else:     
                        print(f'\nPlease enter the names for section "{i["name"]}"\n-----------------')
                        for j in range(i['count']):
                            while True:
                                subName3 = input(f'Please enter the section name for section {j+1}: ')
                                if len(subName3) > 20 or len(subName3) <= 2:
                                    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                    continue
                                else:
                                    break
                            while True:
                                try:
                                    maxScore = int(input(f'What is the maximum score for {subName3}? '))
                                    totalMax += maxScore
                                    if maxScore < 1:
                                        print('\n==================================\n| Please enter a number above 1. |\n==================================')
                                        continue
                                    else:
                                        break
                                except ValueError:
                                    print('\n=============================\n| Please enter only digits. |\n=============================')
                            subfold3.append({'parent':i['name'], 'name':subName3, 'score':[0, maxScore, 'none :)']})
                for prim_f in subfold1:
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        for sec_f in subfold2:
                            if 'score' not in sec_f.keys():
                                if sec_f['parent'] == prim_f['name']:
                                    dict3 = {}
                                    for ter_f in subfold3:
                                        if ter_f['parent'] == sec_f['name']:
                                            dict3.update({ter_f['name']:ter_f['score']})
                                        else:
                                            continue
                                    dict2.update({sec_f['name']:dict3})
                                else:
                                    continue
                            elif sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        dict1.update({prim_f['name']:dict2})
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
            else:
                for prim_f in subfold1:
                    if 'score' not in prim_f.keys():
                        dict2 = {}
                        for sec_f in subfold2:
                            if sec_f['parent'] == prim_f['name']:
                                dict2.update({sec_f['name']:sec_f['score']})
                            else:
                                continue
                        dict1.update({prim_f['name']:dict2})
                    else:
                        dict1.update({prim_f['name']:prim_f['score']})
                test = {testname:dict1}
                return testname, test, totalMax, numLevels
                
                # test = {testname:dict1}
                # return test, numLevels

        elif moreLevels == 'n':
            dict = {testname:[0,'mistakes']}
            test = {testname:dict}
            return testname, test, totalMax, numLevels
        else:
            continue

def make_test_shell():
    choice = 'undefined'
    while choice != False and choice[0] != 'c' and choice[0] != 's':
        if choice == 'undefined':
            while True:
                try:
                    choice = (input('''\n-----------------\n\nWould you like to make a simple test or a custom test?

============================
| Simple Test:             |
----------------------------===============================
| Each part in a simple test has the same number of parts.|
| These are faster to set up and perfect for small or     |
| simply organized tests.                                 |
|                          --> Type S for a 'simple test' |
===========================================================

============================
| Custom Test:             |
----------------------------================================
| Every part in a custom test is customized by the user.   | 
| Each part can be arranged in different ways. This takes  |
| more time, but is good if your test is large or arranged |
| in a more complex way.                                   |
|                           --> Type C for a 'custom test' |
============================================================

Please choose S/C: ''')).lower().strip()
                    if choice[0] == 's' or choice[0] == 'c':
                        break
                    elif isinstance(choice, str) == False:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                    else:
                        print('\n=================================\n| That is not a valid response. |\n=================================')
                        continue
                except IndexError:
                    print('\n=================================\n| That is not a valid response. |\n=================================')
                    continue
            if choice[0] == 's':
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2:
                        print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                        continue
                    else:
                        return build_simple_dict(testname)
            else:
                while True:
                    testname = input('\nEnter a name for this test: ')
                    if len(testname) > 20 or len(testname) <= 2:
                        print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                        continue
                    else:
                        return build_custom_dict(testname)

def print_dict(dct):
    for title, v in dct.items():
        print(f'\nTest Name: {title}\n----------------')
        for layer1, v1 in dct[title].items():
            print(f'{layer1}')
            if isinstance(dct[title][layer1], dict) != True:
                test = v1
                if isinstance(test, list) == True:
                    print(f'\tScore: {v1[0]} out of: {v1[1]} || Mistakes: {v1[2]}')
                else:
                    print(str(dct[title][layer1])) 
            else:
                for layer2, v2 in dct[title][layer1].items():
                    print(f'{layer2} : ')
                    if isinstance(dct[title][layer1][layer2], dict) != True:
                        test = v2
                        if isinstance(test, list) == True:
                            print(f'\tScore: {v2[0]} out of: {v2[1]} || Mistakes: {v2[2]}')
                        else:
                            print(layer2 + " : " + str(dct[title][layer1][layer2]))
                    else:
                        for layer3, v3 in dct[title][layer1][layer2].items():
                            print(f'\t{layer3} || Score: {v3[0]} out of: {v3[1]} || Mistakes: {v3[2]}')
            print('----------------')

def make_mlist():
    mistake_list = []
    add_more = ''
    quit = False

    mistakes_done = False

    while quit == False:
        try:
            add_more = input('\nWould you like to add a mistake type? Y/N ').lower().strip()
            if add_more[0] == 'y':
                while add_more[0] == 'y':
                    new_mistake = input('---\nEnter the name of your mistake type: ')
                    mistake_list.append(new_mistake)
                    while True:
                        try:
                            add_more = input('---\nWould you like to add more mistakes? Y/N ').lower().strip()
                            if add_more[0] == 'y':
                                break
                            elif add_more[0] == 'n':
                                quit = True
                                mistakes_done = True
                                break
                            elif isinstance(add_more, str) == False:
                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                continue
                            else:
                                print('\n=================================\n| That is not a valid response. |\n=================================')
                                continue
                        except IndexError:
                            print('\n=================================\n| That is not a valid response. |\n=================================')
                            continue
            elif add_more[0] == 'n':
                quit = True
                mistakes_done = False
                break
            elif isinstance(add_more, str) == False:
                print('\n=================================\n| That is not a valid response. |\n=================================')
                continue
            else:
                print('\n=================================\n| That is not a valid response. |\n=================================')
                continue
        except IndexError:
            print('\n=================================\n| That is not a valid response. |\n=================================')
            continue
    print('\nThe mistakes list is: ')
    for c, i in enumerate(mistake_list):
        print(f'Mistake {c}: {i}')
    print('---\n')
    while True:
        input('Press enter to continue. \n\n----------------\n')
        break
    return mistake_list

def add_scores(test_raw, test_db, test_index):
    dct = {}
    if len(test_raw) < 1:
        print(f'\n========================================================\n| Please add at least one test score in order to view. |\n========================================================')
    else:
        print('\nHere are your test names and locations:\n')
        for c, i in enumerate(test_index):
            print(f'Test structure: {i["name"]} || Test location: {c+1}')
        while True:
            try:
                test_choice = int(input('---\n\nPlease enter the location of the test you want to add a score for: '))-1
                if test_choice > len(test_index)-1 or test_choice < 0:
                    print(f'\n==================================\n| Please enter a number up to {len(test_index)}. |\n==================================\n')
                    continue
                else:
                    break
            except ValueError:
                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                continue
        dct = copy.deepcopy(test_raw[test_choice])
        for title, v in dct.items():
                print(f'\nTest Name: {title}\n----------------') 
                if isinstance(v, dict) != True:
                    test = v
                    if isinstance(test, list) == True:
                        while True:
                            try:
                                u_score = int(input(f'\nWhat was your score out of {v[1]}? '))
                                if u_score > v[1] or test_choice < 0:
                                    print(f'\n======================================\n| Please enter a number from 0 to {v[1]}. |\n======================================\n')
                                    continue
                                else:
                                    break
                            except ValueError:
                                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                continue
                        dct[title][0] = u_score
                        if u_score < v[1] and len(test_index[test_choice]['mistakes']) > 0:
                            add_m = 'undefined'
                            tmp_m_lst = []
                            while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                u_mistake = input('Please enter mistakes one at a time: ').strip()
                                if u_mistake not in test_index[test_choice]['mistakes']:
                                    print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                    continue
                                elif u_mistake in tmp_m_list and u_mistake != '':
                                    print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                    continue
                                elif u_mistake == '':
                                    print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                    continue
                                else:
                                    tmp_m_lst.append(u_mistake)
                                    if dct[title][2] == 'none :)':
                                        dct[title][2] = u_mistake
                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                            try:
                                                add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                    break
                                                elif isinstance(add_m, str) == False:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                    continue
                                                else:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                    continue
                                            except IndexError:
                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                continue
                                        if add_m[0] == 'y':
                                            continue
                                        else:
                                            break
                                    else:
                                        dct[title][2] += f', {u_mistake}' 
                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                            try:
                                                add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                    break
                                                elif isinstance(add_m, str) == False:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                    continue
                                                else:
                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                    continue
                                            except IndexError:
                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                continue
                                        if add_m[0] == 'y':
                                            continue
                                        else:
                                            break
                            else:
                                print("---\nNo remaining mistake types.\n")
                    else:
                        print('\n==============================================\n| ERROR: THIS IS INVALID. CONTACT DEVELOPER. |\n==============================================\n')
                        pass
                else:
                    for layer1, v1 in dct[title].items():
                        print(f'\n{layer1}')
                        if isinstance(dct[title][layer1], dict) != True:
                            test = v1
                            if isinstance(test, list) == True:
                                while True:
                                    try:
                                        u_score = int(input(f'\nWhat was your score out of {v1[1]}? '))
                                        if u_score > v1[1] or test_choice < 0:
                                            print(f'\n======================================\n| Please enter a number from 0 to {v1[1]}. |\n======================================\n')
                                            continue
                                        else:
                                            break
                                    except ValueError:
                                        print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                        continue
                                dct[title][layer1][0] = u_score
                                if u_score < v1[1] and len(test_index[test_choice]['mistakes']) > 0:
                                    add_m = 'undefined'
                                    tmp_m_lst = []
                                    while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                        u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                        if u_mistake not in test_index[test_choice]['mistakes']:
                                            print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                            continue
                                        elif u_mistake in tmp_m_list and u_mistake != '':
                                            print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                            continue
                                        elif u_mistake == '':
                                            print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                            continue
                                        else:
                                            tmp_m_lst.append(u_mistake)
                                            if dct[title][layer1][2] == 'none :)':
                                                dct[title][layer1][2] = u_mistake
                                                while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                    try:
                                                        add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                        if add_m[0] == 'y' or add_m[0] == 'n':
                                                            break
                                                        elif isinstance(add_m, str) == False:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                            continue
                                                        else:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                            continue
                                                    except IndexError:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                        continue
                                                if add_m[0] == 'y':
                                                    continue
                                                else:
                                                    break
                                            else:
                                                dct[title][layer1][2] += f', {u_mistake}'
                                                while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                    try:
                                                        add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                        if add_m[0] == 'y' or add_m[0] == 'n':
                                                            break
                                                        elif isinstance(add_m, str) == False:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                            continue
                                                        else:
                                                            print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                            continue
                                                    except IndexError:
                                                        print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                        continue
                                                if add_m[0] == 'y':
                                                    continue
                                                else:
                                                    break
                                    else:
                                        print("---\nNo remaining mistake types.\n")
                            else:
                                print(f'\n{layer1}') 
                        else:
                            for layer2, v2 in dct[title][layer1].items():
                                print(f'\n{layer2} : ')
                                if isinstance(dct[title][layer1][layer2], dict) != True:
                                    test = v2
                                    if isinstance(test, list) == True:
                                        while True:
                                            try:
                                                u_score = int(input(f'\nWhat was your score out of {v2[1]}? '))
                                                if u_score > v2[1] or u_score < 0:
                                                    print(f'\n======================================\n| Please enter a number from 0 to {v2[1]}. |\n======================================\n')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                                continue
                                        dct[title][layer1][layer2][0] = u_score
                                        if u_score < v2[1] and len(test_index[test_choice]['mistakes']) > 0:
                                            add_m = 'undefined'
                                            tmp_m_lst = []
                                            while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                                if u_mistake not in test_index[test_choice]['mistakes']:
                                                    print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                                    continue
                                                elif u_mistake in tmp_m_lst and u_mistake != '':
                                                    print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                                    continue
                                                elif u_mistake == '':
                                                    print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                                    continue
                                                else:
                                                    tmp_m_lst.append(u_mistake)
                                                    if dct[title][layer1][layer2][2] == 'none :)':
                                                        dct[title][layer1][layer2][2] = u_mistake
                                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                            try:
                                                                add_m = input('Would you like to add another mistake? Y/N ').lower().strip()
                                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                                    break
                                                                elif isinstance(add_m, str) == False:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                                else:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                            except IndexError:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                continue
                                                        if add_m[0] == 'y':
                                                            continue
                                                        else:
                                                            break
                                                    else:
                                                        dct[title][layer1][layer2][2] += f', {u_mistake}'
                                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                            try:
                                                                add_m = input('Would you like to add another mistake? Y/N ').lower().strip()
                                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                                    break
                                                                elif isinstance(add_m, str) == False:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                                else:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                            except IndexError:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                continue
                                                        if add_m[0] == 'y':
                                                            continue
                                                        else:
                                                            break
                                            else:
                                                print("---\nNo remaining mistake types.\n")
                                    else:
                                        print('\n' + layer2 + " : " + str(dct[title][layer1][layer2]))
                                else:
                                    for layer3, v3 in dct[title][layer1][layer2].items():
                                        while True:
                                            try:
                                                u_score = int(input(f'\nWhat was your score out of {v3[1]}? '))
                                                if u_score > v3[1] or test_choice < 0:
                                                    print(f'\n======================================\n| Please enter a number from 0 to {v3[1]}. |\n======================================\n')
                                                    continue
                                                else:
                                                    break
                                            except ValueError:
                                                print(f'\n=====================================\n| Please enter a number digit only. |\n=====================================\n')
                                                continue
                                        dct[title][layer1][layer2][layer3][0] = u_score
                                        if u_score < v3[1] and len(test_index[test_choice]['mistakes']) > 0:
                                            add_m = 'undefined'
                                            tmp_m_lst = []
                                            while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                u_mistake = input('Please enter the mistakes one at a time: ').strip()
                                                if u_mistake not in test_index[test_choice]['mistakes']:
                                                    print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')
                                                    continue
                                                elif u_mistake in tmp_m_lst and u_mistake != '':
                                                    print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')
                                                    continue
                                                elif u_mistake == '':
                                                    print('\n===========================\n| Please enter a mistake. |\n===========================\n')
                                                    continue
                                                else:
                                                    tmp_m_lst.append(u_mistake)
                                                    if dct[title][layer1][layer2][layer3][2] == 'none :)':
                                                        dct[title][layer1][layer2][layer3][2] = u_mistake
                                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                            try:
                                                                add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                                    break
                                                                elif isinstance(add_m, str) == False:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                                else:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                            except IndexError:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                continue
                                                        if add_m[0] == 'y':
                                                            continue
                                                        else:
                                                            break
                                                    else:
                                                        dct[title][layer1][layer2][layer3][2] += f', {u_mistake}'
                                                        while True and len(tmp_m_lst) != len(test_index[test_choice]['mistakes']):
                                                            try:
                                                                add_m = input('Would you like to add another mistake? Y/N').lower().strip()
                                                                if add_m[0] == 'y' or add_m[0] == 'n':
                                                                    break
                                                                elif isinstance(add_m, str) == False:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                                else:
                                                                    print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                    continue
                                                            except IndexError:
                                                                print('\n=================================\n| That is not a valid response. |\n=================================\n')
                                                                continue
                                                        if add_m[0] == 'y':
                                                            continue
                                                        else:
                                                            break
                                            else:
                                                print("---\nNo remaining mistake types.\n")
                        print('----------------') 
                print('\n\n================')
    return test_choice, dct
    
main()