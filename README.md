# Invoice
In a field of freelancing especially freelance writers who gets paid for the words they write, it is unavoidable that they haven't had to deal with making invoices for the articles they wrote and its respective word count, only to be sent to their client who in turn pays them for their hard-work. This application aims to automate the tedious process of editing and inserting each column of the invoice. With the help of Invoice you can  make you invoices in just one click!  
For this application to work you need to save all your articles in the same folder or direcctory. 
You only have to run the app.py file and the application window will pop open asking you for path of the directory, path of the directory you want to save the invoice on, name of the excel file, title which is set to False by default and dummy which is also set to False by default.
The first 3 parameters is pretty self explanatory but the last two might be a little confusing.

Title (bool, def: False):
  In microsoft office word you can actually assign a title to the file you are working with. If you want to know more you can search it out. Invoice extracts the title information from each file and makes a list out of it. It is set to False by default which means you won't be getting this value until you change  the setting to True.

Dummy(bool, def: False):
  Every freelance writer (that I've known) is given specific limits to the words they have to write in an article by their client. It can be 200, 500 or may 1000 or even more. But while actually writing the article there will always be some up and down regarding the specified wordcount. Invoice tries to guess the specified wordcount from the actual word count of the article. Note that the actual word count will always be recorded  in the final excel file but assumed or predicted specified  word count is optional.

The result will be an excel file having the following header:
a. File name(docx)
b. Title (if set to True)
c. Created (date the file was created)
d. Modified (date if the file was modified at any given time)
e. Word count (actual word count of the file .docx)
f. Dummy word count
 
 
 
 
