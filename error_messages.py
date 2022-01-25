# Global error types
def invalid():
    print('\n=================================\n| That is not a valid response. |\n=================================')

def invalid_sel(num):
    print(f'\n==================================\n| Please enter a number up to {num}. |\n==================================')

def letter_error():
    print(f'\n===============================================\n| Letter entered. Now returning to main menu. |\n===============================================')

def no_scores():
    print(f'\n========================================================\n| Please add at least one test score in order to view. |\n========================================================')

def no_scores2():
    print(f'\n===================================================\n| There are not yet any scores for this test type |\n===================================================')

def no_struct():
    print(f'\n============================================================\n| Please add at least one test structure in order to view. |\n============================================================')

# Errors in test analysis
def no_scores3():
    print(f'\n===================================================\n| There are not yet any scores for this test type |\n===================================================')

# Errors in structure builders
def above_1():
    print('\n==================================\n| Please enter a number above 1. |\n==================================')

def name_length():
    print('\n==================================================\n| Please enter a name from 3-20 characters long. |\n==================================================\n')

def num_range():
    print('\n===================================\n| Please enter a number from 1-10. |\n====================================')

def only_digits():
    print('\n=============================\n| Please enter only digits. |\n=============================')

# Errors in score adder
def invalid_mis():
    print('\n=====================================\n| That is not a valid mistake type. |\n=====================================\n')

def no_mis():
    print('\n===========================\n| Please enter a mistake. |\n===========================\n')

def redundant_mis():
    print('\n==========================================\n| You have already entered that mistake. |\n==========================================\n')

def UNDEFINED_ERROR():
    print('\n==============================================\n| ERROR: THIS IS INVALID. CONTACT DEVELOPER. |\n==============================================\n')