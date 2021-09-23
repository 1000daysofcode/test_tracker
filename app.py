def main():
    choice = 'undefined'
    # Greet user
    print('-----------------\n\nWelcome to Test Tracker version 0!')

    # Ask for name (add to variable)
    name = input('\n\nPlease enter your name: ')
    print(f'\nWelcome, {name}!\n\nPlease create at least one test structure to continue.')

    # Initialize data structures
    test_raw = []
    test_db = []
    test_index = [{'name':'IELTS'}]

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
                print('\nYou chose to view your scores.\n')
                choice = 'undefined'
                continue
            elif choice[0] == 'a':
                print('\nYou chose to view a score analysis.\n')
                choice = 'undefined'
                continue
            elif choice[0] == 'n':
                print('\nYou chose to add a new score.\n')
                choice = 'undefined'
                continue
            elif choice[0] == 's':
                print('\nYou chose to create a new test structure.\n')
                testname, dct, total, levels = make_test_shell()
                test_raw.append(dct)
                test_index.append({'name':testname, 'maxscore':total})
                print(f'\nTest "{testname}" created. Please see below:\n\nTest name: {testname}')
                for title, v in dct.items():
                    print(f'\nTest Name: {title}\n----------------') 
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
                # print(type(dict_s))
                choice = 'undefined'
                continue
            else:
                print('\nThank you for using Test Tracker version 0! Goodbye\n')
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
                    dict1.update({layer1[1]:[0, maxScore, '']})
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
                    dict3.update({layer3[1]:[0, maxScore, '']})
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
                    dict2.update({layer2[1]:[0, maxScore, '']})
                for layer1 in subfold1:
                    dict1.update({layer1[1]:dict2})
                return testname, dict1, totalMax, numLevels
        elif moreLevels[0] == 'n':
            dict = {testname:[0,'mistakes']}
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
                                subfold1.append({'name':subName1, 'score':[0, maxScore, '']})
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
                                        subfold2.append({'parent':i['name'], 'name':subName2, 'score':[0, maxScore, '']}) 
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
                            subfold3.append({'parent':i['name'], 'name':subName3, 'score':[0, maxScore, '']})
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

main()