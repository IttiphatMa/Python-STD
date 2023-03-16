from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from tkinter import simpledialog

###############CSV##########################

import csv

def writecsv(datalist):
    with open('std4.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist)# datalist = ['pen','pencil','eraser']


def readcsv():
    with open('std4.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data

##################END CSV####################################

GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกระยะการเดินทาง') #ชื่อโปรแกรม 
GUI.geometry('350x300')#ขนาดโปรแกรม

LF1 = ttk.LabelFrame(GUI,text='กรุณากรอกระยะทาง')
LF1.pack(ipadx=100,ipady=100)

L1=Label(GUI,text='ขาไป(กม.)',font=('Angsana New',13),fg='Blue')
L1.place(x=120,y=20)

L2=Label(GUI,text='ขากลับ(กม.)',font=('Angsana New',13),fg='Blue')
L2.place(x=120,y=80)

###############SECTION RIGHT#######################


a = StringVar()#ตัวแปรพิเศษใช้ในGUI
in1 =ttk.Entry(LF1,textvariable=a)
in1.place(x=30,y=40)

b = StringVar()#ตัวแปรพิเศษใช้ในGUI
in2 =ttk.Entry(LF1,textvariable=b)
in2.place(x=30,y=100)
#################################################


from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d')
    a = in1.get()#ดึงข้อมูลจากinput1
    b = in2.get()#ดึงข้อมูลจากinput2
    text = [t,a,b] #[เวลา,รับข้อมูลจากinput1,รับข้อมูลจากinput2]
    writecsv(text) #บันทึกลง CSV
    a.set("") #เครียร์ช่องรับข้อมูล a
    b.set("") #เครียร์ช่องรับข้อมูล b
    
B1 = ttk.Button(GUI, text='บันทึก',command=SaveData)
B1.pack(ipadx=20,ipady=10)

#################################################


GUI.mainloop()
