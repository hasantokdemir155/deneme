from tkinter import *
from tkinter import ttk


liste=[["124","ali"],["126","can"],["131","mert"]]

pnx=Tk()
pnx.geometry("400x400")
lstx=ttk.Treeview(pnx)

lstx["columns"]= ("ogrno","ogradı")

lstx.column("#0",width = 5)

lstx.column("ogrno",width=50)
lstx.column("ogradı",width=100)

lstx.heading("ogrno",text="Öğrencino")
lstx.heading("ogradı",text="Öğrenciadı")

for i in liste:
    
    a=i[0]
    b=i[1]
    lstx.insert('',"end",text="",values=(a,b))
        #print(a,b)


lstx.pack()
pnx.mainloop()
