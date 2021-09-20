# Greet user
print('Welcome to Test Tracker Version 0!')

# Ask for name (add to variable)
name = input('\n\nPlease enter your name: ')

# Ask for class name, then
cName = input('\n\nPlease enter the name of the class: ')

# Initialize test max score variable
maxScore = 0
numLevels = 0
subSize = []

# AssembleTest
def org_test():       
    levelCheck = True
    # Check number of subfolders needed by asking:
        # "Is this divided into parts?" 
        # Y = name part, specify number of parts, 
        # N = Begin to get max scores for all sections
    while levelCheck == True:
        moreLevels = input('Is this divided into parts? y/n')
        if moreLevels == 'y'.lower():
            if numLevels > 3:
                print("You've reached the maximum number of subsections")
                levelCheck = False
            else:
                get_subSize = input('How many parts?')
                for count, i in enumerate(range(get_subSize)):
                    subName = input('Please enter the section name: ')
                    subSize.append([count,subName])
                numLevels += 1
                continue
        elif moreLevels == 'n'.lower():
            levelCheck = False
        else:
            continue

org_test()

for i in range(numLevels):

    



# Print table organized and ask user to confirm

    # Here is your test organization:
    
    # Test Name: 'IELTS'
    # =============================
    # | Test 1 | Reading | Part 1 |
    # | Test 1 | Reading | Part 2 |
    # | Test 1 | Reading | Part 3 |
    # | Test 1 | Reading | Part 4 |
    # | Test 1 | Writing | Part 1 |
    # | Test 1 | Writing | Part 2 |
    # | Test 1 | Writing | Part 3 |
    # =============================
    # + 3 more tests like 'Test 1'

    # Is this correct? Y/ N

# Once complete, request user to input information

# Once data completed, allow user 4 options:
    # View score trends -> Type 'S'
    # View entire test --> Type 'T'
    # Update test score -> Type 'U'
    # Add another test --> Type 'A'

# Type 'QUIT NOW' at any time to quit program. Confirmation y/n

dct = {'ielts':{'test 1':{'reading':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a'],'part 4':[0, 'n/a']},'writing':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a']}},'test 2':{'reading':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a'],'part 4':[0, 'n/a']},'writing':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a']}},'test 3':{'reading':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a'],'part 4':[0, 'n/a']},'writing':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a']}},'test 4':{'reading':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a'],'part 4':[0, 'n/a']},'writing':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a']}}},'toefl':'nada'}

print(dct['ielts']['test 3']['writing']['part 3'][1])
print(dct['toefl'])




        