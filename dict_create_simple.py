def builddict():
    moreLevels = 'undefined'    
    maxScore = 0
    numLevels = 0
    subfold1 = []
    subfold2 = []
    subfold3 = []
    dict1 = {}
    dict2 = {}
    dict3 = {}
    while moreLevels != False and moreLevels != 'n':
        if moreLevels == 'y' or moreLevels == 'undefined':
            moreLevels = input('Is this divided into parts? y/n')
            if moreLevels == 'y'.lower():
                numLevels += 1
                get_subSize1 = int(input('How many identical parts? '))
                for i in range(get_subSize1):
                    subName1 = input('Please enter the section name: ')
                    subfold1.append([i+1, subName1])
                moreLevels = input('Do you need to divide into more sections 1? y/n')

            # If yes, continue building subfolders, if no process dict
            if moreLevels == 'y':
                numLevels += 1
                get_subSize2 = int(input('How many identical parts? '))
                for i in range(get_subSize2):
                    subName2 = input('Please enter the section name: ')
                    subfold2.append([i+1, subName2])
                moreLevels = input('Do you need to divide into more sections 2? y/n')
            else:
                for layer1 in subfold1:
                    dict1.update({layer1[1]:[0, '']})
                return dict1
            
            if moreLevels == 'y':
                numLevels += 1
                get_subSize3 = int(input('How many identical parts? '))
                for i in range(get_subSize3):
                    subName3 = input('Please enter the section name: ')
                    subfold3.append([i+1, subName3])
                for layer3 in subfold3:
                    dict3.update({layer3[1]:[0, '']})
                for layer2 in subfold2:
                    dict2.update({layer2[1]:dict3})
                for layer1 in subfold1:
                    dict1.update({layer1[1]:dict2})
                return dict1
            else:
                for layer2 in subfold2:
                    dict2.update({layer2[1]:[0, '']})
                for layer1 in subfold1:
                    dict1.update({layer1[1]:dict2})
                return dict1
        elif moreLevels == 'n'.lower():
            pass
        else:
            continue #enclose in loop to force at least 1 y/n answer

print(builddict())

            #Create subfolders, for each subfolder how many fucking folders do you have and what are their names

            # if numLevels > 3:
            #                 print("You've reached the maximum number of subsections")
            #                 levelCheck = False
            #             else:
            #                 get_subSize = input('How many parts?')
            #                 for count, i in enumerate(range(get_subSize)):
            #                     subName = input('Please enter the section name: ')
            #                     subSize.append([count,subName])
            #                 numLevels += 1
            #                 continue