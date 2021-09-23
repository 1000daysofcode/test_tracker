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
            continue #enclose in loop to force at least 1 y/n answer

name, dict, total, levels = build_custom_dict('IELTS')
print(f'\n-----------------\n\nNumber of levels: {levels}\n{name} (Maximum possible: {total}):\n\n{dict}\n')