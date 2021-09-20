# Project Plan

## Ultimate goal

The ultimate goal for this, is to create a web app with a database that allows user to log in, create and customize a simple account.

Within the account they will be able to:

* Change profile photo, email & password
* Add and update a number of different assignments and tests
* View a homepage that has visualizations of current scores
* View visualizations specific assignments/ test series

This will be a responsive web app in Flask or Django.

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

## Project Phases

### Project Timeline

| Phase | Name | Duration | When |
| ----- | ---- | -------- | --- |
| 1 | Project Submission | 3-4 Days | 20-24 Sept 21 |
| 2 | Database Integration | 3-4 Days | 12-15 Oct 21 |
| 3 | Simple Web App | 1-2 Weeks | 15-22 Nov 21 |
| 4 | Portfolio Ready - Visualizations | 2-4 Weeks | 22 Nov-13 Dec 21 |
| 5 | Finishing Touches- Launch | 1 Week | 13-20 Dec 21 |
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