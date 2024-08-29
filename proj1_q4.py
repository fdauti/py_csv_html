#!C:\python\python.exe
'''/**************************************************************************************
* SRT211 – Project1
* I declare that this assignment is my own work in accordance with Seneca Academic Policy.
* No part of this assignment has been copied manually or electronically from any other
* source (including web sites) or distributed to other students.
*
* Name: Fatjon Dauti
*
*****************************************************************************************/
Process a CSV file to display a list of Student ID(s) who missed an activity
selected by the user. Select activities based on partial search phrase entered by user,
and display across the total number of submitted assignments for each user.
'''
import pandas

try:
    file = input("Enter CSV file name: ")
    #Version using files processing (needs header rows in csv file without "," char)
    # f = open(file, 'r') 
    # header = f.readline() #open file and read first the header row
    # f.close()
    # lines = header.split(",") #create a list with the first header row
    
    #Read first row of csv file using pandas and convert it to list
    df_row = pandas.read_csv(file, nrows=1)
    lines = list(df_row)

    print("\nList of activities: ")
    #read list line by line adding a number before each line for easy selection
    #start from second element in the list to avoid "Student ID" column

    lineCounter=1
    for line in lines[1:]: 
        print(str(lineCounter) + ' - ' + line.strip())
        lineCounter += 1

    #sanitize user input, looping to make sure the user enters a number 
        #related to a column present in the csv file
    while True:
        try:
            column = int(input("\nEnter activity number: "))
        except ValueError:
            print("Please enter a number corresponding to your activity")
            continue
        if column <= 0:
            print("Please enter a positive number")
            continue
        elif column > len(lines)-1:
            print("Please enter a valid number corresponding to your activity")
            continue
        else:
            break
    
    #read the csv file as a pandas dataframe and capture the column chosen by user 
    df = pandas.read_csv(file)
    col = df.columns[column]

    print("The following student(s) haven't completed the activity: ")
    #check if there is a null cell in the captured column 
    #display id(s) corresponding to null cells using a list
    
    nul_data = df[col].isnull() 
    id = df[nul_data].iloc[:,0]
    id_list = list(id)
    for i in id_list:
        print(i)

    #bonus for question 4
    actv = input("\nEnter activity to search (case sensitive): ")
    
    #using "lines" list created before, display items (column headers) 
        #related to user input, representing activities
    print("Selected activities")
    for col_name in lines:
        if actv in col_name:
            print("Activity name: ", col_name)
            #count columns with vaules using notnull() method
            data = df[col_name].notnull().sum()
            print("Number of submitted assginments: ", data)

    print("\nNumber of submitted assginments per Sudtent ID:")
    #use pandas to capture columns based on user input and count cells with data
    #convert "Student ID" column and df2 dataframe to lists and display by combing
    #values on each list and adding the total nr. of activities

    df2 = df.filter(regex=actv).count(axis=1)
    id_list = list(df.iloc[:,0])
    df2_list = list(df2)

    print("Student ID \t Nr. of submitted assignemnts")
    col_leng = len(df.filter(regex=actv).columns)
    for i in range(len(id_list)):
        print(str(id_list[i]) + '\t ' + str(df2_list[i]) + "/" + str(col_leng))

except FileNotFoundError:
    print(f'Error. File "{file}" does not exist!')
except KeyboardInterrupt:
    print('\nProgram Interrupted')
except:
    print('\nProgram error detected! Please contact support.')

    #For displaying Student ID(s) who submitted each activity searched by user
    # for item in header_list:
    #     if phrase in item:
    #         print("Selected activities")
    #         print(item)
    #         data = df[item].notnull().sum()
    #         print("Number of submitted assginments: ", data)
    #         columns = df[item].notnull()
    #         print("Student who submitted the assignemnt: ")
    #         ids = df[columns].iloc[:,0]
    #         ids_list = list(ids)
    #         for i in ids_list:
    #             print(i)