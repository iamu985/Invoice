from invoice import Invoice


'''
=================================
Main Running Script of The application
=================================

Returns a table of all data and exports it to an excel file

'''

class Program():

    def __init__(self, path, file_path, filename, title_bool, dummy_bool):
        self.path = path
        self.file_path = file_path
        self.filename = filename
        self.title_bool = title_bool
        self.dummy_bool = dummy_bool

    def run(self):
        #getting a list of documents file name and its respective paths
        documents, documents_path = Invoice.get_files(self.path)
        print('Fetched files')

        #getting a list of word counts of the document
        wordcount = Invoice.all_file_wordcount(documents_path)
        print('Fetched word counts')

        #list of rounded off word counts
        dummy_count = Invoice.dummy_wordcount(wordcount)
        print('Fetched dummy count')

        #list of properties
        property_create, property_modified, property_title = Invoice.getProperties(documents_path)
        print('Fetched properties')
        
        #getting list of values
        property_values = Invoice.proper_properties(documents, property_title, property_create, property_modified, wordcount, dummy_count, self.title_bool, self.dummy_bool)
        print('Fetched proper properties')
        
        #fetch dictionary of data of properties
        data = Invoice.dictionary(property_values, self.title_bool, self.dummy_bool)
        print('Fetched Data')
        
        #drawing table
        table = Invoice.table(data)
        print('Table Drawn')
        

        #exporting the table to an excel file
        Invoice.export(table, self.file_path, self.filename)
        
        print('Invoice Saved')




##    def run(self):
##        print(self.path)
##        print(self.file_path)
##        print(self.filename)
##        print(self.title_bool)
##        print(self.dummy_bool)
##        documents, documents_path = Invoice.get_files(self.path)
##
##        print(documents)
##        print(documents_path)
##
##        wordcount = Invoice.all_file_wordcount(documents_path)
##        print(wordcount)
##
##        dummy_count = Invoice.actual_wordcount(wordcount)
##        print(dummy_count)
##
##        property_create, property_modified, property_title = Invoice.getProperties(documents_path)
##        print(property_create)
##
##        property_values = Invoice.proper_properties(documents, property_title, property_create, property_modified, wordcount, dummy_count, self.title_bool, self.dummy_bool)
##        print(property_values)
'''If you want to test the script go ahead and uncomment this block'''
##path = 'D:/python/alexda_project/docx'
##file_path = 'D:/python/alexda_project/docx/invoice'
##filename = 'demo_with_title'
##title_bool = True
##dummy_bool = True
##
##script = Program(path, file_path, filename, title_bool, dummy_bool)
##script.run()













