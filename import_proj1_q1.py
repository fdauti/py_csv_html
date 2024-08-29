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
'''
import proj1_q1

print("\nThis program will compare two csv files, " 
        "for similar and diffrent values in the first column.")
print("If the files are not in the program directory, "
        "enter the full path to the files!\n")
        
file1 = input("Enter first file name: ")
file2 = input("Enter second file name : ")

proj1_q1.compare(file1,file2) 
