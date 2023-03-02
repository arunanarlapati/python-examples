# Youtube Link: https://www.youtube.com/watch?v=PgLjwl6Br0k

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd

# initalise the tkinter GUI
root = tk.Tk()

root.geometry("500x500") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0) # makes the root window fixed in size.
root.configure(bg='pink')
root.title("STAR AUTOMOBILES")
# Frame for TreeView
frame1 = tk.LabelFrame(root, text=" Results")
frame1.place(height=400, width=500)
frame1.configure(bg='pink')
# Frame for open file dialog
choose_frame = tk.LabelFrame(root, text="Choose")
choose_frame.place(height=90, width=500, rely=0.8, relx=0)
choose_frame.configure(bg='pink')
# Buttons
button1 = tk.Button(choose_frame, text="Show all", command=lambda: show_all())
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(choose_frame, text="toyota only", command=lambda: Load_toyota())
button2.place(rely=0.65, relx=0.30)



## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).
treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


def show_all():
    
     df = pd.read_csv("C:\\Users\\aruta\\Downloads\\Automobile_data.csv")
     clear_data()
     tv1["column"] = list(df.columns)
     tv1["show"] = "headings"
     for column in tv1["columns"]:
         tv1.heading(column, text=column, anchor='center') # let the column heading = column name
     df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
     
     for row in df_rows:
         tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
     return None


def Load_toyota():
    df1 = pd.read_csv("C:\\Users\\aruta\\Downloads\\Automobile_data.csv")
    car_Manufacturers = df1.groupby('company')
    toyotaDf = car_Manufacturers.get_group('toyota')
    toyotaDf  
      
    clear_data()
    tv1["column"] = list(toyotaDf.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column, anchor='center') # let the column heading = column name

    toyotaDf_rows = toyotaDf.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in toyotaDf_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


root.mainloop()