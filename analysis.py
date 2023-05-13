import pandas as pd 
import tkinter as tk
from tkinter import filedialog

data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/c2.csv')

first=pd.DataFrame(columns=['Aaaa'])

#print(data.head())



#print(a)

#b=str(a).split(',')
#print(b[0]) 
#print(len(b))

print(len(data))
print(str(data.Author[2]).split(','))



for m in range(len(data)):
    name= data.Author[m]
    sp=str(name).split(',')
    for p in range(len(sp)):
       first=first.append({'Aaaa':sp[p]},ignore_index=True)



df =first


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





    




