# COMP-636-Python-Assessment

## Introduction
The Bankside-Rakaia Motorkhana Mavens (BRMM) car club has asked for a system to help manage its August ‘Have-a-go Fun Motorkhana’ event. You are provided with an outline of the code for the system to complete.
Motorkhana is a type of motorsport where the aim is to drive around a course made of cones as fast as possible without hitting any cones or going the wrong way.

## Requirements
The system needs to keep a record of drivers, their run results for each course, and the overall results for the day, as well as recording juniors and their nominated parents or caregivers, if appropriate.
- Drivers are stored as a dictionary of key: value pairs. Each key is the driver ID. Each value part contains a tuple (First Name, Surname, Category, Age, Caregiver). Category is ‘J’ for any junior drivers. Drivers who are not juniors do not have an age record. Caregiver is the
driver ID of an adult driver in the list (for drivers aged 12-16).
- Runs are stored as a dictionary of key: value pairs. Each key is a run ID. Each value part contains a tuple (Course, Driver, Time, Cones, WD). Driver is a driver ID. Time is recorded to the nearest 0.01 of a second. Cones contain the number of cones hit, if any. WD (wrong
direction) is either 1 (went the wrong direction around one or more cones) or 0 (no wrong direction).
- Missing data values are recorded as None.
- One function (list_drivers) for menu option 1 has already been provided for you. This lists all of the drivers and displays Driver ID, First Name, Last Name and Age.
- You must use the provided column_output function for all on-screen displays of data (except for the graph of cones hit). You will need to convert your dictionary data into the correct format for this function (the list_drivers function gives an example of how to do this). Do not
modify this function.
- Validate all user input appropriately. If data of the wrong type is entered by the user, this should be captured without causing the program to crash or any other type of error. Also, ensure that only valid values that make sense can be entered.

## Tasks
Add the following features to the system: (Marks shown are an indication and may change a little.)
1. Menu enhancement: Modify the code so that the user can enter an upper- or lower-case X (i.e., X or x) to exit the program.
2. Junior driver list: List the junior drivers, in order of increasing age. Combine their full names (first name and surname) in one column (e.g., ‘Kiri Smith’, not ‘Kiri’ ‘Smith’). For juniors aged 12-16, display their caregiver’s full name, not the caregiver’s driver ID.
3. List results of runs: List the run results. For each run, include the time, cones hit and WD status, and then the calculated Run Total time. Ensure your list shows all Course A runs first, then B then C, ordered from best to worst Run Total for each course.
4. Enter or update run data: First display the run results (from Task 3 above), then allow the user to add or update the times, cones hit and WD, for the existing runs. Ask the user for the ID of the run you want to update and check that the run ID exists. The user can enter the number of cones hit, but 0 is entered automatically if no value is entered. Ensure the time and number of cones are in a sensible range. The user types in ‘wd’ to enter the wrong direction (in upper or lower case), otherwise no value for WD should default to 0. After updating a run, a user has the option to update another run or return to the menu.
5. Display overall results: Calculate and display the overall results for the August ‘Have a Go’. For each driver show the sum of their best two runs. Show results from best to worst, with any "HAG" results at the bottom of the list. Show each driver’s full name in one column and show ‘(J)’ after the name of junior drivers (e.g., ‘Edward Cooper (J)’).
6. Cone graph: Display a graph of the number of cones hit by each driver. Exclude drivers who did not hit any cones. Choose any symbol or character (e.g., Δ, C, ) to represent each cone hit, with a space between each symbol or character.
