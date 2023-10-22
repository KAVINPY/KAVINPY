from tkinter import*
root=Tk()
l=[]
num1=0
k=0
h=0
e=Entry(root,width=50)
e.grid(row=0,column=4,columnspan=3)
def func(nums):
    global k
    k=k+1
    e.insert(k,nums)
    global num1
    num1=int(e.get())
def add():
    global h
    if h==1:
        n=e.get()
        for i in range(len(n)):
            e.delete(0)
        global l
        l=[]
    l.append(num1)
    for i in range(len(str(num1))):
        e.delete(0)
def result():
    global num1
    num1=int(e.get())
    l.append(num1)
    for i in range(len(str(num1))):
        e.delete(0)
    sums=0
    for i in range(len(l)):
        sums=sums+l[i]
    e.insert(0,sums)
    global h
    h=h+1
def clear():
    n=e.get()
    for i in range(len(n)):
        e.delete(0)
mylabel1=Button(text="1",command=lambda:func("1"))
mylabel2=Button(text="2",command=lambda:func("2"))
mylabel3=Button(text="3",command=lambda:func("3"))
mylabel4=Button(text="4",command=lambda:func("4"))
mylabel5=Button(text="5",command=lambda:func("5"))
mylabel6=Button(text="6",command=lambda:func("6"))
mylabel7=Button(text="7",command=lambda:func("7"))
mylabel8=Button(text="8",command=lambda:func("8"))
mylabel9=Button(text="9",command=lambda:func("9"))
mylabel0=Button(text="0",command=lambda:func("0"))
mylabeladd=Button(text="+",command=add)
mylabelclear=Button(text="clear",command=clear)
mylabeleq=Button(text="=",command=result)


mylabel1.grid(row=1,column=0)
mylabel2.grid(row=1,column=1)
mylabel3.grid(row=1,column=2)
mylabel4.grid(row=2,column=0)
mylabel5.grid(row=2,column=1)
mylabel6.grid(row=2,column=2)
mylabel7.grid(row=6,column=0)
mylabel8.grid(row=6,column=1)
mylabel9.grid(row=6,column=2)
mylabeladd.grid(row=7,column=0)
mylabel0.grid(row=7,column=1)
mylabelclear.grid(row=8,column=0,columnspan=3)
mylabeleq.grid(row=7,column=2)
