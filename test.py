from invoice import Invoice


'''
test file to check the working of invoice module
you can uncomment the variables below and store your local  file_path, path, filename, title_bool value and dummy_bool value

path as the name suggests is the path of the directory where all your docx file is stored or  saved
file_path is the path to the directory where you want to save your invoice excel file
filename is the name that you want to give to your excel file
title_bool is a boolean value that is set to False by default. This if changed to True will give you the title column of the table
dummy_bool is a boolean  value set to False by default that gives you round off value for your assumed word count
'''
##path = 'D:/python/alexda_project/docx'
##file_path = 'D:/python/alexda_project/docx/invoice'
##filename = 'demo2'
##title_bool = False
##dummy_bool = False

files_name, files_path = Invoice.get_files(path)
print('files:')
for i in range(len(files_name)):
    print(files_name[i])
print('\n\nfiles path: ')
for i in range(len(files_name)):
    print(files_path[i])

print('\n\nWordcounts:')
wordcount = Invoice.all_file_wordcount(files_path)
for i in range(len(wordcount)):
    print(wordcount[i])

print('\n\ndummy wordcounts:')
dummy = Invoice.dummy_wordcount(wordcount)
for i in range(len(dummy)):
    print(dummy[i])

c, m, t = Invoice.getProperties(files_path)
print('\n\nCreated:')
for i  in range(len(c)):
    print(c[i])
print('\n\nModified')
for i in range(len(m)):
    print(m[i])
print('\n\nTitles:')
for i in range(len(t)):
    print(t[i])

properties = Invoice.proper_properties(files_name, t, c, m, wordcount, dummy, title_bool, dummy_bool)
print('\n\nValues without t and d')
for i in range(len(properties)):
    print(properties[i])

properties_t = Invoice.proper_properties(files_name, t, c, m, wordcount, dummy, title_bool, dummy_bool)
print('\n\nproper_properties with t')
for i in range(len(properties_t)):
    print(properties_t[i])

properties_d = Invoice.proper_properties(files_name, t, c, m, wordcount, dummy, title_bool, dummy_bool)
print('\n\nvalues with d')
for i in range(len(properties_d)):
    print(properties_d[i])

properties_td = Invoice.proper_properties(files_name, t, c, m, wordcount, dummy, title_bool, dummy_bool)
print('\n\nvalues with t and d')
for i in range(len(properties_td)):
    print(properties_td[i])


data = Invoice.dictionary(properties, title_bool, dummy_bool)
print('\n\ndata:')
for k, y in data.items():
    print(k, ':', y)

data_t = Invoice.dictionary(properties_t, title_bool, dummy_bool)
print('\n\ndata_t:')
for k, y in data_t.items():
    print(k, ':', y)

data_d = Invoice.dictionary(properties_d, title_bool, dummy_bool)
print('\n\ndata_d:')
for k, y in data_d.items():
    print(k, ':', y)

data_td = Invoice.dictionary(properties_td, title_bool, dummy_bool)
print('\n\ndata_td:')
for k, y in data_td.items():
    print(k, ':', y)

table = Invoice.table(data)
print(table)

table_t = Invoice.table(data_t)
print(table_t)

table_td = Invoice.table(data_td)
print(table_td)

table_d = Invoice.table(data_d)
print(table_d)



