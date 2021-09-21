def builddict(testname):
    moreLevels = 'undefined'    
    maxScore = 0
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
                dict = {testname:[0,'mistakes']}
                return dict, numLevels

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
                    dict1.update({layer1[1]:[0, '']})
                return dict1, numLevels
            
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
                    dict3.update({layer3[1]:[0, '']})
                for layer2 in subfold2:
                    dict2.update({layer2[1]:dict3})
                for layer1 in subfold1:
                    dict1.update({layer1[1]:dict2})
                return dict1, numLevels
            else:
                for layer2 in subfold2:
                    dict2.update({layer2[1]:[0, '']})
                for layer1 in subfold1:
                    dict1.update({layer1[1]:dict2})
                return dict1, numLevels
        elif moreLevels[0] == 'n':
            dict = {testname:[0,'mistakes']}
            return dict, numLevels
        else:
            continue

dict, levels = builddict('IELTS')
print(f'\n-----------------\n\nNumber of levels: {levels}\n\nDictionary:\n\n{dict}\n')