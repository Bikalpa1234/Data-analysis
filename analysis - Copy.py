import pandas as pd 
import tkinter as tk
from tkinter import filedialog

data= pd.read_csv('C:/Users/DELL/OneDrive/Desktop/Book1.csv')

first=pd.DataFrame()

#print(data.head())



#print(a)

#b=str(a).split(',')
#print(b[0]) 
#print(len(b))

print(len(data))
print(data.loc[[2]])

substring='Institute of Engineering'

for m in range(len(data)):
    name= data.Affiliations[m]
    sp=str(name)
    if sp.find(substring)==-1:
        print(m)
        first= data.drop(m)
        
    


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





    




