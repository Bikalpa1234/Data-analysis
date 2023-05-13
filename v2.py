import pandas as pd 
import tkinter as tk
from tkinter import filedialog

data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/Research/Data/Authors.csv')

list1=pd.DataFrame(columns=['Author','Number'])

a=0
for i in range(len(data)):
    a=0
    for j in range(len(data)):
        if str(data.Aaaa[j]) in str(data.Aaaa[i]):
            a=a+1
        
    list1=list1.append({'Author':str(data.Aaaa[i]),'Number':a},ignore_index=True)

df =list1


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def exportCSV ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)

saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()

