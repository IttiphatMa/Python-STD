from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import datetime 

GUI = Tk()
GUI.title('โปรแกรมบันทึกระยะทาง')
GUI.geometry('400x300')
now = datetime.datetime.now()

L1 = Label(GUI,text='กรอกข้อมูลระยะทาง',font=('Anakotmai',20))
L1.place(x=90,y=30)
#L2 = Label(GUI,text='วันที่',font=('Anakotmai',15))
#L2.place(x=50,y=85)
L3 = Label(GUI,text='ต้นทาง',font=('Anakotmai',15))
L3.place(x=50,y=125)
L4 = Label(GUI,text='ปลายทาง',font=('Anakotmai',15))
L4.place(x=50,y=165)
L5 = Label(GUI,text='กม.',font=('Anakotmai',15))
L5.place(x=300,y=125)
L6 = Label(GUI,text='กม.',font=('Anakotmai',15))
L6.place(x=300,y=165)



##################การคำนวณ
def Button1():
    text =  'ผลรวมระยะทาง'
    value1 = input2.get()
    t = int(value1)
    value2 = input3.get()
    e = int(value2)
    value3 = t+e
    
    messagebox.showinfo(text,f'  {value3} กม.')
    
    
    
############################
FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=160,y=250)
B1 = ttk.Button(FB1,text='บันทึกข้อมูล',command=Button1)
B1.pack(ipadx=5,ipady=5)

#input1= Entry(GUI,bg='white')
#input1.place(x=160,y=90)
input2 = Entry(GUI,bg='white')
input2.place(x=160,y=130)
input3 = Entry(GUI,bg='white')
input3.place(x=160,y=170)




GUI.mainloop()
