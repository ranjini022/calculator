import math
from tkinter import *

root=Tk()
root.title("Simple Calculator")

e=Entry(root, width=60, borderwidth=7)
e.grid(row=0, column=0, columnspan=5,pady=10)

def click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
def clear():
    e.delete(0,END)
def equal():
    sec_num=e.get()
    e.delete(0,END)
    if fuc=="addition":
        e.insert(0, fnum + int(sec_num))
    if fuc=="subtract":
        e.insert(0, fnum - int(sec_num))
    if fuc== "multi":
        e.insert(0, fnum * int(sec_num))
    if fuc== "divi":
        e.insert(0, fnum / int(sec_num))
    if fuc == "pow":
        e.insert(0, pow(fnum,int(sec_num)))
    if fuc == "sin":
        e.insert(0, math.sin(math.radians(int(sec_num))))
    if fuc == "cos":
        e.insert(0, math.cos(math.radians(int(sec_num))))
    if fuc == "tan":
        e.insert(0, math.tan(math.radians(int(sec_num))))
    if fuc == "percent":
        e.insert(0, fnum/100)
    if fuc == "sqrt":
        e.insert(0, math.sqrt(int(sec_num)))
    if fuc == "fact":
        e.insert(0, math.factorial(sec_num))


def add():
    first_num=e.get()
    global fnum
    global fuc
    fuc="addition"
    fnum=int(first_num)
    e.delete(0,END)
def sub():
    first_num=e.get()
    global fnum
    global fuc
    fuc="subtract"
    fnum=int(first_num)
    e.delete(0,END)
def mul():
    first_num=e.get()
    global fnum
    global fuc
    fuc="multi"
    fnum=int(first_num)
    e.delete(0,END)
def div():
    first_num=e.get()
    global fnum
    global fuc
    fuc="divi"
    fnum=int(first_num)
    e.delete(0,END)
def power():
    first_num=e.get()
    global fnum
    global fuc
    fuc="pow"
    fnum=int(first_num)
    e.delete(0,END)
def percent():
    first_num=e.get()
    global fnum
    fnum=int(first_num)
    e.delete(0,END)
    e.insert(0,fnum/100)
def inverse():
    first_num=e.get()
    global fnum
    fnum=int(first_num)
    e.delete(0,END)
    e.insert(0,pow(fnum,(-1)))
def sin():
    global fuc
    fuc="sin"
    e.delete(0,END)
def cos():
    global fuc
    fuc="cos"
    e.delete(0,END)
def tan():
    global fuc
    fuc="tan"
def log():
    num=e.get()
    e.insert(0, math.log(num,10))
def ln():
    num=e.get()
    e.insert(0, math.log(num,2.71))
def sqrt():
    global fuc
    fuc="sqrt"
    e.delete(0,END)
def fac():
    global fuc
    fuc="fact"
    e.delete(0,END)
button_pi=Button(root,text="pi",padx=30,pady=30,command=lambda : click(1)).grid(row=5,column=4)
button_1=Button(root,text="1",padx=30,pady=30,command=lambda : click(1)).grid(row=1,column=0)
button_2=Button(root,text="2",padx=30,pady=30,command=lambda : click(2)).grid(row=1,column=1)
button_3=Button(root,text="3",padx=30,pady=30,command=lambda : click(3)).grid(row=1,column=2)
button_4=Button(root,text="4",padx=30,pady=30,command=lambda : click(4)).grid(row=2,column=0)
button_5=Button(root,text="5",padx=30,pady=30,command=lambda : click(5)).grid(row=2,column=1)
button_6=Button(root,text="6",padx=30,pady=30,command=lambda : click(6)).grid(row=2,column=2)
button_7=Button(root,text="7",padx=30,pady=30,command=lambda : click(7)).grid(row=3,column=0)
button_8=Button(root,text="8",padx=30,pady=30,command=lambda : click(8)).grid(row=3,column=1)
button_9=Button(root,text="9",padx=30,pady=30,command=lambda : click(9)).grid(row=3,column=2)
button_0=Button(root,text="0",padx=30,pady=30,command=lambda : click(0)).grid(row=4,column=0)
button_clc=Button(root,text="clr",padx=26,pady=30,command=lambda :clear()).grid(row=4,column=0)
button_eq=Button(root,text="=",padx=67,pady=30,command=lambda :equal()).grid(row=4,column=1,columnspan=2)
button_add=Button(root,text="+",padx=30,pady=30,command=lambda :add()).grid(row=1,column=3)
button_sub=Button(root,text="-",padx=30,pady=30,command=lambda :sub()).grid(row=2,column=3)
button_mul=Button(root,text="*",padx=30,pady=30,command=lambda :mul()).grid(row=3,column=3)
button_div=Button(root,text="/",padx=30,pady=30,command=lambda :div()).grid(row=4,column=3)
button_pow=Button(root,text="^",padx=30,pady=30,command=lambda :power()).grid(row=4,column=3)
button_per=Button(root,text="%",padx=29,pady=30,command=lambda :percent()).grid(row=4,column=3)
button_bi=Button(root,text="1/x",padx=26,pady=30,command=lambda :inverse()).grid(row=5,column=3)
button_sin=Button(root,text="sin",padx=25,pady=30,command=lambda :sin()).grid(row=5,column=0)
button_cos=Button(root,text="cos",padx=25,pady=30,command=lambda :cos()).grid(row=5,column=1)
button_tan=Button(root,text="tan",padx=25,pady=30,command=lambda :tan()).grid(row=5,column=2)
button_log=Button(root,text="lg",padx=30,pady=30,command=lambda :log()).grid(row=1,column=4)
button_elog=Button(root,text="ln",padx=30,pady=30,command=lambda :ln()).grid(row=2,column=4)
button_sqrt=Button(root,text="sqrt",padx=25,pady=30,command=lambda :sqrt()).grid(row=3,column=4)
button_fac=Button(root,text="!",padx=34,pady=30,command=lambda :fac()).grid(row=4,column=4)

root.mainloop()


