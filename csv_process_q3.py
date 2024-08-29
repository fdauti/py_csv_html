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
Browse for CSV files, chose columns from selected CSV to be displayed in HTML format
'''
print("Content-type: text/html \n\n")

import os
import webbrowser
import pandas
import cgi

formData = cgi.FieldStorage()

#catch the file uploaded by user and the cloumns selected
File = formData.getvalue("filename")
col_list = formData.getlist("column")

#process the list of columns with pandas and covert to hmtl
csvdata = pandas.read_csv(File, usecols=col_list)
htmldata = csvdata.to_html()

#use the os.path library and abspath method to generate html file,  
#to be diplayed and combine its full path in a url
path = os.path.abspath('csv_display.html')
url = 'file://' + path

#open html file for writing, display in browser with open() method of webbrowser library
f = open(path, 'w')
f.write(htmldata)
f.close()
webbrowser.open(url)
