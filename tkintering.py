import tkinter as tk
from tkinter import filedialog
from changer import PdfMeta,MetaWriter
def open_file_dialog():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
    if filename:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, filename) 
        
def create_entry_pair(window, label_text, row):
    label = tk.Label(window, text=label_text)
    label.grid(column=0, row=row)
    entry = tk.Entry(window, width=50)
    entry.grid(column=1, row=row, pady=5)
    return entry
def choose():
    value = entry_box.get()
    data = PdfMeta(value)
    if data:
        not_found.grid_forget()
        new_window = tk.Toplevel(root)
        new_window.title("MetaData") 
        def change():
            MetaWriter(entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get(),entries[5].get(),entries[6].get(),value)
        fields = [
            "Creator", "Producer", "CreationDate", 
            "ModDate", "KeyWords", "Author", "Title"
        ]
        entries = []
        for i, field in enumerate(fields):
            entry = create_entry_pair(new_window, field, i)
            entry.insert(0,data[i])
            entries.append(entry)
        submit = tk.Button(new_window,text='Submit',command=change)
        submit.grid(row=7,column=0,columnspan=2)
    else:
        not_found.grid(column=0,row=2,columnspan=2)
        
root = tk.Tk()



root.title("File Selection")

entry_box = tk.Entry(root, width=50)
entry_box.grid(column=0, row=0,pady=5)

open_button = tk.Button(root, text="Open File", command=open_file_dialog)
open_button.grid(column=1, row=0,pady=10)

see_metadata_button = tk.Button(root,text="See metadata", command=choose,padx=10,pady=10)
see_metadata_button.grid(column=0,row=1,columnspan=2)
not_found = tk.Label(root,text = "Invalid type")
root.mainloop()
