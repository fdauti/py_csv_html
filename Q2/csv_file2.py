#!C:\Users\fotip\AppData\Local\Microsoft\WindowsApps\python3.9.exe
'''/**************************************************************************************
* SRT211 – Project1
* I declare that this assignment is my own work in accordance with Seneca Academic Policy.
* No part of this assignment has been copied manually or electronically from any other
* source (including web sites) or distributed to other students.
*
* Name: Fatjon Dauti
*
*****************************************************************************************/
Convert CSV file to HTML format and display on browser
'''
print("Content-type: text/html \n\n")

import os
import webbrowser
import pandas

#use pandas rach_csv function to display file2.csv 
#when the users clicks on the file from the webpage
csvdata = pandas.read_csv("file2.csv")
htmldata = csvdata.to_html()

#use the os.path library and abspath method to generate html file,  
#to be diplayed and combine its full path in a url
path = os.path.abspath('csv_file2.html')
url = 'file://' + path

#open html file for writing, display in browser with open() method of webbrowser library
f = open(path, 'w')
f.write(htmldata)
f.close()
webbrowser.open(url)
