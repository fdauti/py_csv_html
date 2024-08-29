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
   Develop a Python program which compares 2 csv files and:
   -displays students (student ID) who exists in both courses
   -displays students (student ID) who dosn't exists in both courses
'''
def compare(file1="file1.csv", file2="file2.csv"):
    '''
    Open 2 csv files for reading, by default will use file1 and file2,
    read the content as a list, create 2 new lists by appending the first 
    item of each row (corresponding to the Student ID) starting from 2nd row
    Convert the lists to sets and apply sets methods.
    '''
    try:
        f1 = open(file1, 'r') 
        f2 = open(file2, 'r')
        r1 = f1.readlines()
        r2 = f2.readlines()
        
        list1 = []
        for item in r1[1:]:
            list1.append(item.split(',')[0])
        list2 = []
        for item in r2[1:]:
            list2.append(item.split(',')[0])

        s1 = set(list1)
        s2 = set(list2)
        print("\nStudents who are taking both courses:") #Duplicate items in first column of each file
        dup = s1.intersection(s2) #get duplicate values on both sets
        for item in dup:
            print(item)
        print("\nStudents who aren't taking both courses") #Diffrent items in first column of each file
        diff = s1.symmetric_difference(s2) #get values that both sets do not share
        for item in diff:
            print(item)

    except FileNotFoundError:
        print('\nError. Please make sure both files exist!')
    except:
        print('\nProgram error detected!')

if __name__ == "__main__":
    compare()
