def builddict():
    moreLevels = 'undefined'    
    maxScore = 0
    numLevels = 0
    sectCount1 = 0
    sectCount2 = 0
    sectCount3 = 0
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
                for i in range(get_subSize1):
                    while True:
                        subName1 = input(f'Please enter a section name for section {i+1}: ')
                        print('\n')
                        if len(subName1) > 20 or len(subName1) <= 2:
                            print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                            continue
                        else:
                            break
                    while True:
                        try:
                            sectCount1 = int(input(f'Please enter the number of sections in {subName1}: '))
                            print('\n')
                            if sectCount1 > 10 or sectCount1 < 1:
                                print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                continue
                            else:
                                break
                        except ValueError:
                            print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                            continue
                    subfold1.append([sectCount1, subName1])
                while True:
                    try:
                        moreLevels = (input('-----------------\nDo you need to divide into more sections [Ask #2]? Y/N ')).lower().strip()
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
                dict = {'test_name':[0,'mistakes']}
                return dict, numLevels

            # If yes, continue building subfolders, if no process dict
            if moreLevels[0] == 'y':
                numLevels += 1
                # get_subSize2 = int(input('How many identical parts? '))
                for i in subfold1:
                    print(f'\nPlease enter the names for section {i[1]}')
                    for j in range(i[0]):
                        while True:
                            subName2 = input(f'Please enter the section name for section {j+1}: ')
                            if len(subName2) > 20 or len(subName2) <= 2:
                                print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                continue
                            else:
                                break
                        while True:
                            try:
                                sectCount2 = int(input(f'Please enter the number of sections in {subName2}: '))
                                if sectCount2 > 10 or sectCount2 < 1:
                                    print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                    continue
                                else:
                                    break
                            except ValueError:
                                print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                continue
                        subfold2.append([sectCount2, subName2])           
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
            
            if moreLevels == 'y':
                numLevels += 1
                # get_subSize3 = int(input('How many identical parts? '))
                for i in subfold2:
                    print(f'\nPlease enter the names for section {i[1]}\n-----------------\n')
                    for j in range(i[0]):
                        while True:
                            subName3 = input(f'Please enter the section name for section {j+1}: ')
                            if len(subName3) > 20 or len(subName3) <= 2:
                                print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')
                                continue
                            else:
                                break
                        while True:
                            try:
                                sectCount3 = int(input(f'Please enter the number of sections in {subName3}: '))
                                if sectCount3 > 10 or sectCount3 < 1:
                                    print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                    continue
                                else:
                                    break
                            except ValueError:
                                print('\n===================================\n| Please enter a number from 1-10. |\n====================================')
                                continue
                        subfold3.append([sectCount3, subName3])
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
        elif moreLevels == 'n':
            dict = {'test_name':[0,'mistakes']}
            return dict, numLevels
        else:
            continue #enclose in loop to force at least 1 y/n answer

dict, levels = builddict()
print(f'\n-----------------\n\nNumber of levels: {levels}\n\nDictionary:\n\n{dict}\n')