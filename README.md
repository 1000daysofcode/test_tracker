# Version 0 ReadMe

## Features

The initial version includes four key features:

1) Create custom test structures
2) Add grades for each user-created test
3) View all grades for each test type
4) View an analysis of each test type's results

---

## User Guide

## Starting the program

Upon starting the program, enter your name so the program knows what to call you. From there you can choose from one of the main features. Press the corresponding key and enter to choose the correct option.

## Creating test structures

In order to create structures, first choose whether to make a 'simplified' test structure or a 'custom' test structure. Then create the given structure **What's the difference between test structures?**

### -> Custom test structure

Customization is maximized, allowing for virtually any test structure. This requires more input from the user. In other words, the user must specify for each and every section:

* Whether there are additional sections
* How many sections there are (if any)
* The specific maximum score for each

This is best for tests with more complex structures that have different grades for different parts.

### -> Simplified test structures

User input is minimized and decisions about test structure are generalized. If you choose a number of parts for a section to be divided into, this will apply to all sections in this level. If you choose a maximum score, this score will be applied to *all* sections in this level. 

Less input is therefore required from the user, but there is much less customization available. This is best for simple tests that don't have complex structure.

## Finishing the structure

Once the main structure is created, you must enter a minimum of one (but an unlimited maximum) mistake types to analyze. This can be anything (e.g. 'grammar' on a writing test).

Once the user has finished adding mistake types, everything is added to the program's memory and the user is returned to the main menu.

## Adding a new score

Once at least one test structure has been added, the user can add new scores for any test structure. To do so, select this option, then select which structure to add a score for.

The user will be asked for each section's score. If the score is perfect, the program will prompt for the next score. However, if the score is under the maximum score the program will prompt for at least one mistake type to be entered.

Upon successful score entry, the user will be informed that score submission was successful then returned to the main menu.

## Viewing test scores

Once at least one test score has been added, users can view all test scores entered for each particular test type. Simply choose the view option, where all available test types are displayed. Then enter the number of the test to access scores for and, if there are tests are available, the scores for each test will be printed one-at-a-time in an easy-to-read manner.

## Viewing score analyses

Once at least one test score has been added, users can view a simple analysis each particular test type's scores. The process of accessing these analyses is the same as for viewing test scores.

Choose the analyze option, where all available test types are displayed. Then enter the number of the test to access scores for and, if there are tests are available, an analysis will be printed including:

* The highest scored test & corresponding test number
* The lowest scored test & corresponding test number
* The overall average score (the average across all tests of the chosen type)
* The least and most common mistakes made across all tests

## Closing the program

The program can be closed from the main menu at any time by entering the appropriate option.

---

## Functions at a glance

This program is broken into a number of functions, with everything happening within the main loop (main). Once the program is started, it requests a name, then greets the user and opens the main menu. If the user chooses 'q', the program will quit. Otherwise there is a series of if statements that will accept one of the following options:

| Key | Purpose |
| --- | ------- |
| 'v' | view the test scores |
| 'a' | analyze test scores |
| 'n' | add a new test score |
| 's' | add a new test structure |

Until the user enters at least one structure, if conditions prevent the user from accessing any options aside from 's' or 'q'. Once a structure has been added, the user can access the 'n' option, but if conditions prevent access to both the 'v' and 'a' options. Once at least one structure and one score have been added, the user can select all options.

## Structure functions

Creating a structure references four unique functions:

### Choose a structure (make_test_shell)

This function displays information on both the simplified test structure and custom test structure and will only accept input for one of these two options (through error checking try/except statements and if conditions). Based on the user's choice, the function will call either test structure, which are separate functions.

After the test structure returns the pertinent results based on user input, this function returns to the main menu where it was originally called. Once it returns to the menu, it will call a function to gather mistake types for this structure.

### Creating a list of mistake types (make_mlist)

This simple function requires a minimum of one mistake type to add to a list, appends the mistake to the list, then asks the user whether they'd like to add another type. If the user inputs that they want to continue, the program will start another iteration through the the loop and do this again. If not, it will print the list of mistakes for the user and then return this to the main function.

*Finally,* the main function will take all returned information to:

* Add the structure to the list of raw test structures
* Add the name, maximum score possible and mistake types to the test index
* Add a new empty list to the database so that new scores can be stored appropriately.

Once this is done, the entire test will be printed so the user can note the layout. The screen is held by a simple while loop, which the user can exit by pressing enter (then returning to the main menu).

### Simple Test (build_simple_dict)

The functions for both the simple and custom test are quite similar, so the function will be explained in detail in this section and the differences present in the custom test function will be explained in the following section.

This function is, at its core, a series of nested for loops and if conditions:

1) **Choosing whether to break the test into sections:** First, it checks whether the user would like to break the test into sections. If not, it prompts for the maximum score of the test and creates a simple dictionary that houses the test name (key), then a value of a placeholder actual score, maximum score and a placeholder mistake list. The function returns this as part of the output.

2) **Choosing whether to break sections into subsections:** The user is again prompted to input whether they'd like to break these sections into more parts. If not, the program iterates through the list of dictionaries (adding names and score-related information as above for each subsection) and updates a blank dictionary, which is then stored as the value of the test dictionary. If the user opts not to break the section into more subsections, they are prompted to name them and choose a maximum score that applies to all sections that are not further divided.

3) **Choosing whether to divide the subsections further:** The user is prompted to decide whether each section will be further divided. If none are divided further, the program iterates through all subsections and creates a dictionary (further explanation to follow). If the user chooses to divide a subsection further, they are prompted to choose how many sections there are for each section and name each of these sections. Again, the user is prompted to decide whether to divide the subsections further. If they decide not to, the user chooses a score that applies to all subsections in this subsection. If they decide to divide, the program allows for a fourth and final layer of parts.

4) **Adding the final layer of subsections:** If the user opts to continue dividing into sections, they are not permitted to further divide these sections. The program will prompt for the name and maximum score of each subsection for the section, then once done append this to the list of dictionaries as noted above. If the user does not opt to do so, the program iterates through all subsections and creates a dictionary (further explanation below).

> *A few notes on how the information is stored:*

>Each layer of the dictionary is stored in a list of dictionaries with either a name and count of subsections or, if there are no subsections, a name, parent key name and score list.

5) **Iterating through the lists to create the structure:** Either at the end of the final loop or at the end of the third/ fourth bullet point above, the function will iterate through all lists. Put simply: if there is a score in this section's value, update it to the dictionary. If not, go one level deeper and check to see whether that has a score (and the parent key matches). Do this through all three lists of dictionaries until no items remain.

6) **What the function returns:** The function will return to the main function the name of the test, the maximum score possible, the number of levels of subdivision and, of course, the test dictionary.

### Custom Test (build_custom_dict): the differences

The main difference between the simple test function and the custom test function is that the custom test function does not apply subdivisions or maximum scores to all tests in a section. Instead, it prompts the user for whether they would like to divide for each section and subsection, as well as the maximum score for each.

Other than this, the way the function loops through the inputs and the if conditions used function in much the same way. The final dictionary is also created with the same loop.

## The new score function (add_scores)

The function that add scores iterates through the test in a similar way to the below view and analyze functions. As such, it lists the name and location of each test structure the user has entered and prompts the user to enter a choice for which to add a score. Error checking try/except statements and if conditions prevent a choice outside the range of test structures available.

Once a choice has been made, this function makes of deep copy of the test structure, then iterates through each layer of the dictionary:

* If the (sub)section is further divided, the name is printed so that the user understands where in the test they are.
* If there is a score, the program gets input for the score.
* If that score is under the maximum score, the function prompts for a minimum of one mistake type, then requests additional mistake types.
  * The user can choose not to add more mistakes or
  * Can continue adding mistakes until there are none remaining. In which case, the function proceeds to the next question
* If this was a perfect score, the program will request input for the next question.

Like the test structure functions, section information is stored in lists of dictionaries. In this function, there is a slight difference: there are four lists instead of three.

1) First group of sections
2) First group of subsections
3) Second group of subsections
4) Any final (nondivisible) parts

Mistakes are stored in temporary lists in the same way that the make_mlist function stores them. Though once the user selects not to continue adding mistakes (or if there are no mistake types left), this list is then added to the score value as a joined string.

Once the function has iterated through all sections and subsections, a for loop constructs the dictionary in the same way the test structure functions do. The only difference is the additional list of dictionaries.

The function then returns the completed dictionary of scores and the index to which it needs to be appended. The main program will then append it to the appropriate index within the test score database.

## The score view function

This part of the program first lists the name and location of each test structure the user has entered and prompts the user to enter a choice to view. Error checking try/except statements and if conditions prevent a choice with no scores or outside the range.

Once the user has made a valid choice, the program loops through the list of dictionaries, printing the index number of each, then printing as follows (in nested for loops):

* If the (sub)section is further divided, only the name is printed
* If there is a score, the name, actual score, maximum score and list of mistakes is printed

The loop continues through each list item, then prompts the user to click enter in order to proceed to the next test or, if at the end of the tests, to return to the main menu.

## The score analysis function

Like the score view option, this function first lists the name and location of each test structure the user has entered and prompts the user to enter a choice to view. Error checking try/except statements and if conditions prevent a choice with no scores or outside the range.

In much the same way as the view function, this function loops through the list of dictionaries, but instead of printing it collects the following information (in nested for loops):

* If the (sub)section is further divided, search the value for score information
* If there is score information, collect the following information:
  * **Total test score.** This is used to update the top score, lowest score values and total score values.
  * **Top score.** If the test score is larger than current top score, the top score is updated. If they're the same, the name is appended but score unchanged.
  * **Low score.** If the test score is lower than current low score, the low score is updated. If they're the same, the name is appended but score unchanged.
  * **Total score (all tests).** All test scores are added together, which is used to calculate the overall test score average.
  * **Mistake count.** The mistakes are turned into a list of dictionaries that contain the name and count of mistakes for each mistake type. This is used to calculate the least and most common mistakes.

Once the function reaches the end of the final test, in prints:

1) The test name
2) Total number of tests
3) Maximum score possible
4) Average score (this is the total score divided by the length of the the list of tests)
5) The name of the test with the top score followed by the top score
6) The name of the test with the lowest score followed by the lowest score
7) The least and most common mistakes

The program holds this window with a simple while loop until the user presses enter to return to main menu.

---
---

# Project Plan

## Ultimate goal

The ultimate goal for this, is to create a web app with a database that allows user to log in, create and customize a simple account.

Within the account they will be able to:

* Change profile photo, email & password
* Add and update a number of different assignments and tests
* View a homepage that has visualizations of current scores
* View visualizations specific assignments/ test series

This will be a responsive web app in Flask or Django.

---

## Project Function

An app that accepts input from the user about test/quiz scores, with error types as options, and notes trends in the data. This will include:

* Number of mistakes per
  * Test
  * Type
  * Section
* Average test score overall and by:
  * Section
  * Type
  * Test
* Most common errors (top 3)
* Results compared to:
  * Past tests
  * Other times in history

User input will allow them to customize the how data will be categorized:

| Input type | Example |
| ---------- | ------- |
| What they are studying | IELTS |
| Specify subfolders | Book 1, Chapter 1, etc. |
| Specify assignments | Assignment/ Test 1 |
| Specify sections | 'Reading' or 'Task 1' |
| Specify type | Writing task |
| Specify max score | 15 (points) |
| Specify error types | Punctuation error |

Users will then add data to the fields (all fields required)

With enough data, the program will print (on command line for iteration 1) the above information, stylized similar to the below:

| Data Point | Information | Details |
| ----- | ------ | - |
| Tests taken: | ## | |
| Average test score: | ## | |
| Highest test score: | ## | [Test name here] |
| Lowest test score: | ## | [Test name here] |
| Most common mistakes: | [1], [2], [3] | |
| Greatest improvement: | [Mistake] | [Reduction] over [time] |

---
---

## Project Phases

### Project Timeline

| Phase | Name | Duration | When |
| ----- | ---- | -------- | --- |
| 1 | Project Submission | 3-4 Days | 20-24 Sept 21 |
| 2 | Database Integration | 3-4 Days | 12-15 Oct 21 |
| 3 | Simple Web App | 1-2 Weeks | 15-22 Nov 21 |
| 4 | Portfolio Ready - Visualizations | 2-4 Weeks | 22 Nov-13 Dec 21 |
| 5 | Finishing Touches- Launch | 1 Week | 13-20 Dec 21 |

---

#### Iteration 1 (Project Submission)

The first iteration of this program will be the test set-up (categorization), input and tracking function only. The program will not use SQL injection and all data will live within the app to test functionality.

#### Iteration 2 (Database Integration)

The second integration will continue to be a command line tool, but will then store information in an integrated database. This means accounts and information can be stored.

#### Iteration 3 (Simple Web App)

The third iteration will transform into a simple web app that allows account creation and the storing of tests in the SQL database. No visualizations will be present.

#### Iteration 4 (Portfolio Ready)

The fourth iteration of the app will include visualizations for key data points, likely using Python to dynamically create and serve these to Flask and the front end.

#### Iteration 5 (Finishing Touches- Launch)

The fifth iteration will include finishing touches to the program's UI for better flow and a cleaner look.