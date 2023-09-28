# COMP-636-Python-Assessment

## Introduction
The Bankside-Rakaia Motorkhana Mavens (BRMM) car club has asked for a system to help manage its August ‘Have-a-go Fun Motorkhana’ event. You are provided with an outline of the code for the system to complete.
Motorkhana is a type of motorsport where the aim is to drive around a course made of cones as fast as possible without hitting any cones or going the wrong way.

## Requirements
The system needs to keep a record of drivers, their run results for each course, and the overall results for the day, as well as recording juniors and their nominated parents or caregivers, if appropriate.
- Drivers are stored as a dictionary of key: value pairs. Each key is the driver ID. Each value part contains a tuple (First Name, Surname, Category, Age, Caregiver). Category is ‘J’ for any junior drivers. Drivers who are not juniors do not have an age recorded. Caregiver is the
driver ID of an adult driver in the list (for drivers aged 12-16).
- Runs are stored as a dictionary of key:value pairs. Each key is a run ID. Each value part contains a tuple (Course, Driver, Time, Cones, WD). Driver is a driver ID. Time is recorded to the nearest 0.01 of a second. Cones contains the number of cones hit, if any. WD (wrong
direction) is either 1 (went the wrong direction around one or more cones) or 0 (no wrong direction).
- Missing data values are recorded as None.
- One function (list_drivers) for menu option 1 has already been provided for you. This lists all of the drivers and displays Driver ID, First Name, Last Name and Age.
- You must use the provided column_output function for all on-screen display of data (except for the graph of cones hit). You will need to convert your dictionary data into the correct format for this function (the list_drivers function gives an example of how to do this). Do not
modify this function.
- Validate all user input appropriately. If data of the wrong type is entered by the user, this should be captured without causing the program to crash or any other type of error. Also ensure that only valid values that make sense can be entered.
