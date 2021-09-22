# Import functions
from choose_test import make_test_shell as make_test

# Greet user
print('-----------------\n\nWelcome to Test Tracker Version 0!')

# Ask for name (add to variable)
name = input('\n\nPlease enter your name: ')
print(f'\nWelcome, {name}!')

# Initialize test max score variable
maxScore = 0
numLevels = 0
test_raw = [{'IELTS': {'Test 1': {'Reading': {'Part 1': [0, ''], 'Part 2': [0, ''], 'Part 3': [0, ''], 'Part 4': [0, '']}, 'Writing': {'Part 1': [0, ''], 'Part 2': [0, ''], 'Part 3': [0, '']}}}}]
test_db = [{}]
test_index = [{'name':'IELTS','location':0}]
            
dict, levels = make_test()
print('\nTest created. Please see below:')
print(f'\n-----------------\n\nNumber of levels: {levels}\n\nDictionary:\n\n{dict}\n')

for i in test_index:
    print(f'Test structure: {i["name"]}\nTest location: {i["location"]+1}\n-')
test_choice = int(input('Please enter the location of your test'))-1

view = input('To see the test structure, press S.\nTo see your test results, press R')
if view == 's':
    print(test_raw[test_choice])
else:
    print(test_db[test_choice])
print(test_db)

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

# dct = {'ielts':{'test 1':{'reading':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a'],'part 4':[0, 'n/a']},'writing':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a']}},'test 2':{'reading':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a'],'part 4':[0, 'n/a']},'writing':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a']}},'test 3':{'reading':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a'],'part 4':[0, 'n/a']},'writing':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a']}},'test 4':{'reading':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a'],'part 4':[0, 'n/a']},'writing':{'part 1':[0, 'n/a'],'part 2':[0, 'n/a'],'part 3':[0, 'n/a']}}},'toefl'}

# print(dct['ielts']['test 3']['writing']['part 3'][1])
# print(dct['toefl'])

