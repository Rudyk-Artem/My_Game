from keyboard import press_and_release
from os import startfile
from time import sleep
from tkinter import *
My_window=Tk()
My_window.title("Math Challenge Rules")
My_window.geometry(f"800x630")
My_window.resizable(width=False,height=False)
My_window["bg"]="#4499ee"
l1=Label(My_window,justify=LEFT,bg="#4499ee",text="Правила:",fg="#000000",font=("Areal",13))
l1.place(x=10,y=52)
l2=Label(My_window,text="Мова",fg="#000000",bg="#4499ee",font=("Areal",14))
l2.place(x=600,y=190)
l3=Label(My_window,text="©",fg="#000000",bg="#4499ee",font=("Areal",11))
l3.place(x=780,y=600,anchor=NE)
c1=Canvas(My_window,width=533,height=317,bd=1,highlightcolor='#994433',bg='#4499ff')
c2=Canvas(My_window,width=64,height=64,bd=1,highlightcolor='#994433',bg='#4499ff')
lbl1=["Українська","English","москальська"]
lb1=Listbox(My_window,font=("Areal",14),height=len(lbl1),width=15,selectmode=SINGLE)
for i in lbl1:
    lb1.insert(END,i)
lb1.place(x=600,y=220)
c1.place(x=40,y=160)
c2.place(x=370,y=10)
img=[]
for i in lbl1:
    img=img+[(str(i),PhotoImage(file=f'translator/{i}.png'))]
def BackMenu(e=0):
    with open('db.txt','r') as file:
        info=file.readlines()
    for i in range(len(info)):
        if(info[i]=="Language:\n"):
            try:
                info[i+1]=f"{lb1.get(lb1.curselection())}\n"
            except BaseException:
                print("Не вибрана мова")
    infostr=""
    for i in range(len(info)):
        infostr=infostr+info[i]
    with open('db.txt','w') as file:
        file.write(infostr)
    My_window.destroy()
def Reboot(e=0):
    if(e==1):
        with open('db.txt','r') as file:
            info=file.readlines()
        for i in range(len(info)):
            if(info[i]=="Language:\n"):
                try:
                    info[i+1]=f"{lb1.get(lb1.curselection())}\n"
                except BaseException:
                    print("Не вибрана мова")
        infostr=""
        for i in range(len(info)):
            infostr=infostr+info[i]
        with open('db.txt','w') as file:
            file.write(infostr)
    with open('db.txt','r') as file:
        info=file.readlines()
    for i in range(len(info)):
        if(info[i]=="Language:\n"):
            translation=info[i+1][:-1]
    c1.delete("all")
    for i in range(len(img)):
        if(img[i][0]==translation):
            c1.create_image(3,3,anchor='nw',image=img[i][1])
    with open(f'translator/{translation}.txt','r') as file:
        translation=file.readlines()
    tif=0
    til=0
    for i in range(len(translation)):
        if(translation[i]=="|Math Challenge Rules:\n"):
            tif=i
    for i in range(len(translation)-tif-1):
        if(translation[i+tif][0]=="|"):
            til=i
    translationtext=[translation[tif-1],"",""]
    for i in range(til-2):
        translationtext[1]=translationtext[1]+translation[tif+i+1]
    translationtext[2]=translation[-3]
    l2['text']=translationtext[0]
    l1['text']=translationtext[1]
    l3['text']=translationtext[2]
Reboot()
bimg1=PhotoImage(file="image/dback.png")
bimg2=PhotoImage(file="image/reboot.png")
img3=PhotoImage(file="image/logotype.png")
Button(My_window,text="Назад",bg="#4499ee",font=("Arial",13),image=bimg1,command=BackMenu).place(x=1,y=1)
Button(My_window,text="Заново",bg="#4499ee",font=("Arial",13),image=bimg2,command=lambda:Reboot(1)).place(x=774,y=1)
c2.create_image(3,3,anchor='nw',image=img3)
My_window.mainloop()