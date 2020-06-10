from tkinter import *
from tkinter.ttk import *
from invoice import Invoice
from main import Program


def button_handle():
    truth_table = {
        '1' : True,
        '0' : False,
        }
    
    path_get = ent_path.get()
    file_path_get = ent_path_frm.get()
    filename_get = ent_filesave.get()
    title_bool_get = truth_table[str(v_title.get())]
    dummy_bool_get = truth_table[str(v_dummy.get())]
    
    #call script
    script = Program(path_get, file_path_get, filename_get, title_bool_get, dummy_bool_get)

    #Run the script
    script.run()


#application layout
window = Tk()
window.title('Invoice File Saver')

window.rowconfigure([i for i in range(10)], weight=1, minsize=30)
window.columnconfigure([i for i in range(8)], weight=1, minsize=50)



lbl_path = Label(window, text='Path of the working directory')
lbl_path.grid(row=1, column=0, columnspan=2,  sticky='ew', padx=5, pady=5)

ent_path = Entry(window)
ent_path.grid(row=1, column=2, columnspan=5, sticky='ew')

lbl_path_frm = Label(window, text='Path to save the invoice')
lbl_path_frm.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

ent_path_frm = Entry(window)
ent_path_frm.grid(row=2, column=2, columnspan=5, sticky='ew')

lbl_filesave = Label(window, text='File Name:')
lbl_filesave.grid(row=3, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

ent_filesave = Entry(window)
ent_filesave.grid(row=3, column=2, columnspan=5, sticky='ew', padx=5, pady=5)

lbl_radio_title = Label(window, text='Title')
lbl_radio_title.grid(row=4, column=0, columnspan=5, sticky='ew', padx=5, pady=5)


#radio button widget for title_
v_title = StringVar(window)
r_true = Radiobutton(window, text='True', value=True, variable=v_title)
r_true.grid(row=4, column=2)

r_false = Radiobutton(window, text='False', value=False, variable=v_title)
r_false.grid(row=4, column=3)


lbl_radio_dum = Label(window, text='Dummy word count')
lbl_radio_dum.grid(row=5, column=0, columnspan=5, sticky='ew', padx=5, pady=5)

#radio button widget for dummy word count
v_dummy = StringVar(window)
r_true = Radiobutton(window, text='True', value=True, variable=v_dummy)
r_true.grid(row=5, column=2)

r_false = Radiobutton(window, text='False', value=False, variable=v_dummy)
r_false.grid(row=5, column=3)

fr_save = Frame(window)

#button to save invoice
btn_save = Button(fr_save, text='Save Invoice', command=button_handle)
btn_save.grid()
btn_save.bind('<Button-2>', button_handle)

fr_save.grid(row=7, column=6)

window.mainloop()
