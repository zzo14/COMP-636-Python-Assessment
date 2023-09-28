try:
    import brmm_data
except ModuleNotFoundError:
    print("Error: The required 'brmm_data.py' file is missing or not found.")
    print("Please make sure 'brmm_data.py' is in the same folder as this script.")
    exit(1)

#import brmm_data    # brmm_data.py MUST be in the SAME FOLDER as this file!
                    # brmm_data.py contains the data lists
import datetime     # We are not using date times for this assessment, but it is
                    # available in the column_output() fn, so do not delete this line

# Data variables
col_drivers = brmm_data.col_drivers
db_drivers = brmm_data.db_drivers
col_runs = brmm_data.col_runs
db_runs = brmm_data.db_runs


def column_output(db_data, cols, format_str):
    # db_data is a list of tuples.
    # cols is a dictionary with column name as the key and data type as the item.
    # format_str uses the following format, with one set of curly braces {} for each column:
    #   eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
    #   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    #   The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
    #       format_str = "{: <5}  {: ^10}  {: >15}"
    #   Make sure the column is wider than the heading text and the widest entry in that column,
    #       otherwise the columns won't align correctly.
    # You can also pad with something other than a space and put characters between the columns, 
    # eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
    #       format_str = "{:.<5} | {:.^10} | {:.>15}"
    print(format_str.format(*cols))
    for row in db_data:
        row_list = list(row)
        for index, item in enumerate(row_list):
            if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""       # Replaces them with an empty string
            elif isinstance(item, datetime.date):    # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_drivers():
    # List the ID, first name, last name, and age of all drivers

    # Create a dictionary of heading names and types to match the column output
    col_driver_list = {'Driver ID': int, 'First Name': str, 'Surname': str, 'Age': int}
    # Convert the dictionary data into a list that displays the required data fields
    display_list = []
    for driver in db_drivers.keys():
        display_list.append((driver,
                             db_drivers[driver][0],
                             db_drivers[driver][1],
                             db_drivers[driver][3]))
    format_columns = "{: >9} | {: <12} {: <12} | {: ^5}"
    print("\nDRIVER LIST\n")    # display a heading for the output
    column_output(display_list, col_driver_list, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output


#2. Junior driver list    
def list_juniors_by_age():
    # Print a list of the junior drivers, sorted by Age.
    # Use col_juniors as the column headings.
    # Amend your code to display the caregiver's full name instead of the caregiver's ID
    col_juniors = {'Driver ID': int, 'Driver Name': str, 'Age': str, 'Caregiver Name': str}
    
    #2. Junior driver list: List the junior drivers, in order of increasing age. Combine their full names (first name and surname) in one column.
    # For juniors aged 12-16, display their caregiver full name.

    # Convert the dictionary data into a list that displays the required data fields
    display_list = []
    for driver in db_drivers.keys():
        if db_drivers[driver][2] == 'J':
            caregiver_name = ""
            if 12 <= db_drivers[driver][3] <= 16 and db_drivers[driver][4] in db_drivers:
                caregiver_name = f"{db_drivers[db_drivers[driver][4]][0]} {db_drivers[db_drivers[driver][4]][1]}"
            display_list.append((driver,
                                f"{db_drivers[driver][0]} {db_drivers[driver][1]}",
                                db_drivers[driver][3],
                                caregiver_name))
            
    sorted_display_list = sorted(display_list, key=lambda age: age[2]) #sort display list by age
    format_columns = "{: >9} | {: <15} | {: <5} | {: ^5}"
    print("\nJUNIORS DRIVER LIST\n")    # display a heading for the output
    column_output(sorted_display_list, col_juniors, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output


#3. List results of runs
def calculate_run_time(Id):
    #calculate total time for any runs
    run_data = db_runs[Id]
    time, cones_hit, wd = run_data[2], run_data[3], run_data[4]

    if time is None:
        return None
    return time + float(cones_hit or 0) * 5 + wd * 10 # calculate total run time with cones hits and wd

def list_runs():
    # Print a list of runs, including the Run Totals.
    # Display in Course order A B C and within that by time (fastest A first, to slowest C last).

    #3. List results of runs: List the run results. For each run, include the time, 
    # cones hit and WD status, and then the calculated Run Total time. 
    # Ensure your list shows all Course A runs first, then B then C, ordered from best to worst Run Total for each course.

    # Convert the dictionary data into a list that displays the required data fields
    display_list = []
    for run_id in db_runs.keys():
        driver_name = f"{db_runs[run_id][1]} - {db_drivers[db_runs[run_id][1]][0]} {db_drivers[db_runs[run_id][1]][1]}"
        display_list.append((run_id,
                             db_runs[run_id][0],
                             driver_name,
                             db_runs[run_id][2] if isinstance(db_runs[run_id][2], (int, float)) else None,  # check if the time data is a valid number
                             db_runs[run_id][3],
                             'YES' if db_runs[run_id][4] == 1 else 'NO',
                             calculate_run_time(run_id)))
    sorted_display_list = sorted(display_list, key=lambda x: (x[1], x[6] == None, x[6])) #sort display list by Course then run total
    format_columns = "{: >8} | {: ^6} | {: <22} | {: ^7} | {: ^5} | {: ^3} | {: ^5}"
    print("\nRUNS LIST")    # display a heading for the output
    # column_output(sorted_display_list, col_runs, format_columns)   # An example of how to call column_output function
    
    # Print Course A runs first
    for course in ['A', 'B', 'C']:
        course_runs = [run for run in sorted_display_list if run[1] == course]
        print(f"\nCourse {course} runs:")
        column_output(course_runs, col_runs, format_columns)

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output


#4. Enter or update run data
def get_numeric_input(prompt, is_integer=False):
    # vaildation
    # Get numeric input from the user with validation and support for keeping existing values.
    # Args:
    #     prompt (str): The input prompt to display.
    #     is_integer (bool, optional): Set to True if expecting integer input, False for float input (time data).

    while True:
        value = input(prompt)
        if value == '':
            return 0 if is_integer else value
        try:
            if is_integer:
                value = int(value)
                if value < 0:
                    print("\nERROR: Cones hits cannot be negative, please enter a valid non-negative integer.")
                else:
                    return value
            else:
                value = round(float(value), 2)
                if value < 0:
                    print("\nERROR: Time cannot be negative, please enter a valid Time data.")
                else:
                    return value
        except ValueError:
            if is_integer:
                print("\nERROR: Invalid input, please enter a valid non-negative integer.")
            else:
                print("\nERROR: Invalid input, please enter a valid Time data.")

def edit_run_results():
    # Display list of runs. Make use of your existing function.
    # Then allow the user to enter a run ID (limited to existing runs), and to update the run data.
    # Add validation so times are in a sensible range, and WD is restricted to 1 or 0.
    list_runs()
    while True:
        run_id = input("\nPlease enter the Run ID you want to update (or 'X' to return to the menu): ")

        if run_id.upper() == 'X':
            print("\nRturning to the Menu...... ")
            break
        
        try:
            run_id = int(run_id)
        except ValueError:
            print(f"\nError: Invalid input for Run ID '{run_id}'. Please enter a valid integer.")
            continue

        if run_id in db_runs:
            print(f"\nUpdating Run ID {run_id}...")

            time_flag = True
            time_enter = get_numeric_input("\nPlease enter the time (or Press Enter to keep existing time): ")  #Enter the time
            if not time_enter:
                if db_runs[run_id][2] == None:
                    time_flag = False
                    print(f"\nRun ID {run_id} doesn't have Time data. No updates were made.")
                else:
                    print("\nTime has kept existing data.")
            else:
                print("\nTime record entered.")
            
            if time_flag:  #no time data, so no cones and wd
                cones_hits = get_numeric_input("\nPlease enter the number of cones hits (or Press Enter for 0): ", is_integer=True)  #Enter the number of cones hits
                print("\nCones Hits reocrd entered.")
                wd_enter = input("\nEnter 'WD/wd' for wrong direction (or press Enter for 0): ") # WD entering
                wd_enter = 1 if wd_enter.upper() == 'WD' else 0
                print("\nWrong Direction record entered.")

                #updating 
                if time_enter != "":
                    db_runs[run_id] = (db_runs[run_id][0], db_runs[run_id][1], time_enter, cones_hits, wd_enter)
                else:
                    if db_runs[run_id][2] is not None:
                        db_runs[run_id] = (db_runs[run_id][0], db_runs[run_id][1], db_runs[run_id][2], cones_hits, wd_enter)
                print(f"\nRun ID {run_id} has been updated successfully.")
                
                input("\nPress Enter to check updated run list.")
                # Display updated list of runs.
                print("\nUpdated Run list: ")
                list_runs()
        
            another_update = input("\nPress Enter for another run updating (or 'X' to return to the menu): ")
            if another_update.upper() == 'X':
                print("\nRturning to the Menu...... ")
                break
        else:
            print(f"\nERROR: Run ID '{run_id}' doesn't exist.")
            continue


#5. Display overall results
def calculate_total_time():
    # Calculate total run time and add them into a dict by driver id
    total_time = {} 
    for run_id, run_data in db_runs.items():
        individual_run_times = calculate_run_time(run_id)
        if run_data[2] != None:
            if run_data[1] not in total_time:
                total_time[run_data[1]] = [individual_run_times]
            else:
                total_time[run_data[1]].append(individual_run_times)
    for d_id, run_time in total_time.items():
        if len(run_time) > 1:
            total_time[d_id] = round(sum(sorted(run_time)[:2]), 2)
        else:
            total_time[d_id] = 'HAG'
    return total_time

def display_final_results():
    # Calculate and display the overall results.
    # Use col_final_results as the column headings. NOTE :
    #   'Driver' is driver ID
    #   'Driver Name' is both names together, e.g., 'Hank Barnard'
    #    Add '(J)' after the name for juniors, e.g., 'Edward Cooper (J)'
    # Order results from best to worst
    # Display any "HAG" results at the bottom
    col_final_results = {'Driver': int, 'Driver Name': str, 'Result': str}

    total_time = calculate_total_time()
    display_list = []
    for driver in db_drivers.keys():
        driver_name = f"{db_drivers[driver][0]} {db_drivers[driver][1]}(J)" if db_drivers[driver][2] == 'J' else f"{db_drivers[driver][0]} {db_drivers[driver][1]}"
        display_list.append((driver,
                             driver_name,
                             total_time.get(driver, 'HAG')))#have no recorded show as "HAG"
    sorted_display_list = sorted(display_list, key=lambda x: (x[2] == 'HAG', x[2]))
    format_columns = "{: >6} | {: <18} | {: ^8}" 
    print("\nOVERALL RESULTS LIST\n")    # display a heading for the output
    column_output(sorted_display_list, col_final_results, format_columns)   # An example of how to call column_output function
    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output


#6. Cone graph
def display_cone_graph():
    # List any drivers who hit cones, along with their total numbers of cones as a repeating symbol or character.
    # Do not list any drivers who did not hit any cones.

    col_cone_graph = {'Driver': str, 'Cones Hits': str}
    cones_data = {}
    display_list = []
    #arrange cone hit data by driver id
    for runs in db_runs.keys():
        cone_hit = db_runs[runs][3]
        if cone_hit != None and cone_hit > 0:
            driver_id = db_runs[runs][1]
            cones_data[driver_id] = cone_hit if driver_id not in cones_data else cones_data[driver_id] + cone_hit
    for id in cones_data:
        driver_name = f"{id} - {db_drivers[id][0]} {db_drivers[id][1]}"
        display_list.append((driver_name,
                             " Δ" * cones_data[id]))
        
    format_columns = "{: <20} | {: >2}" 
    print("\nCONE HITS GRAPH\n")    # display a heading for the output
    column_output(display_list, col_cone_graph, format_columns)   # An example of how to call column_output function
    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output


# function to display the menu
def disp_menu():
    print("==== WELCOME TO BRMM Fun-khana Event ===")
    print(" 1 - List Drivers")
    print(" 2 - List Juniors (by age) including caregivers")
    print(" 3 - List Run Results")
    print(" 4 - Add Run Data")
    print(" 5 - Display Overall Results")
    print(" 6 - Display cones hit graph")
    print(" X - Exit (stops the program)")


# ------------ This is the main program ------------------------

try: 
    # Display menu for the first time, and ask for response
    disp_menu()
    response = input("Please enter menu choice: ") 

    # Don't change the menu numbering or function names in this menu
    # Repeat this loop until the user enters an "X"
    while response.upper() != "X": #1: Modify the code so that the user can enter an X or x to exit the program
        if response == "1":
            list_drivers()
        elif response == "2":
            list_juniors_by_age()
        elif response == "3":
            list_runs()
        elif response == "4":
            edit_run_results()
        elif response == "5":
            display_final_results()
        elif response == "6":
            display_cone_graph()
        else:
            print("\nERROR: Invalid response, please try again (enter 1-6 or X)")

        print("")
        disp_menu()
        response = input("Please select menu choice: ")
except KeyboardInterrupt: # provide a graceful exit if users use a keyboard interrupt (Ctrl+C) to stop the program
    print("\n\nProgram terminated by user.")

print("\n=== Thank you for supporting BRMM, see you at the next event! ===\n")
