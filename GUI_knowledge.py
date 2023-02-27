from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from tkinter import simpledialog


GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')#กำหนดความกว้างของโปรแกรม



#B1 = ttk.Button(GUI,text='เลือกวันที่')
#B1.pack(ipadx=20,ipady=20)#pack ตั้งค่าปุ่มให้อยู่ตรงกลาง


def Button2():
    text = 'บันทึกแล้ว'
    messagebox.showinfo('ระยะทาง',text)

FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=200,y=260)
B2 = ttk.Button(FB1,text='บันทึกข้อมูล',command=Button2)
B2.pack(ipadx=10,ipady=20)





GUI.mainloop()
