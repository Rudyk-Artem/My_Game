from keyboard import press_and_release
from random import randrange 
from os import startfile
from time import sleep
from tkinter import *
My_window=Tk()
My_window.title("Math Challenge")
geom=[531,285]
My_window.geometry(f"{geom[0]}x{geom[1]}+{My_window.winfo_screenwidth()//2-geom[0]//2}+{My_window.winfo_screenheight()//2-(geom[1]+30)//2}")
My_window.resizable(width=False,height=False)
My_window["bg"]="#88ddff"
with open('db.txt','r') as file:
    info=file.readlines()
for i in range(len(info)):
    if(info[i]=="Position:\n"):
        if(info[i+1]=="t\n"):
            if(My_window.winfo_screenwidth()>=1920 and My_window.winfo_screenheight()>=1080):
                indentsBetweenWindows="NewWindow:\n"
            else:
                indentsBetweenWindows="NewWindowCompact:\n"
            for i in range(len(info)):
                if(info[i]==indentsBetweenWindows):
                    My_window.geometry("+%d+%d" % (int(info[i+int(info[i+1])*2+2]),int(info[i+int(info[i+1])*2+3])))
                    info[i+1]=f"{(int(info[i+1])+1)%9}\n"
            infostr=""
            for i in range(len(info)):
                infostr=infostr+info[i]
            with open('db.txt','w') as file:
                file.write(infostr)

for i in range(len(info)):
    if(info[i]=="Language:\n"):
        translation=info[i+1][:-1]
with open(f'translator/{translation}.txt','r') as file:
    translation=file.readlines()
tif=0
til=0
finishD=False
for i in range(len(translation)):
    if(translation[i]=="|Math Challenge:\n"):
        tif=i
for i in range(len(translation)-tif-1):
    if(translation[i+tif][0]=="|"):
        til=i
translationtext=translation[tif+1:tif+til]
c=Canvas(My_window,width=505,height=244,bd=1,highlightcolor='#994433',bg='#4499ff')
c.create_rectangle(10,10,80,80,fill='#3399ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(90,10,160,80,fill='#2a91ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(170,10,240,80,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(10,90,80,160,fill='#3399ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(90,90,160,160,fill='#2a91ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(170,90,240,160,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(10,170,80,240,fill='#3399ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(90,170,160,240,fill='#2a91ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(170,170,240,240,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(271,10,341,80,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(351,10,421,80,fill='#2a91ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(431,10,501,80,fill='#3399ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(271,90,341,160,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(351,90,421,160,fill='#2a91ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(431,90,501,160,fill='#3399ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(271,170,341,240,fill='#2288ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(351,170,421,240,fill='#2a91ff',outline='#2255ff',width=2,activedash=(9, 9))
c.create_rectangle(431,170,501,240,fill='#3399ff',outline='#2255ff',width=2,activedash=(9, 9))
c.place(x=10,y=25)
l0=Label(My_window,text=' ',fg="#000000",bg="#88ddff",justify=CENTER,font=("Arial",13))
l1=Label(My_window,text='',fg="#000000",bg="#88ddff",justify=CENTER,font=("Arial",13))
l2=Label(My_window,text='',fg="#000000",bg="#88ddff",justify=CENTER,font=("Arial",13))
l1.place(x=115,y=0,width=40)
l2.place(x=376,y=0,width=40)
l3=Label(My_window,text='',fg="#000000",bg="#3399ff",font=("Arial",40))
l4=Label(My_window,text='',fg="#000000",bg="#2a91ff",font=("Arial",40))
l5=Label(My_window,text='',fg="#000000",bg="#2288ff",font=("Arial",40))
l6=Label(My_window,text='',fg="#000000",bg="#3399ff",font=("Arial",40))
l7=Label(My_window,text='',fg="#000000",bg="#2a91ff",font=("Arial",40))
l8=Label(My_window,text='',fg="#000000",bg="#2288ff",font=("Arial",40))
l9=Label(My_window,text='',fg="#000000",bg="#3399ff",font=("Arial",40))
l10=Label(My_window,text='',fg="#000000",bg="#2a91ff",font=("Arial",40))
l11=Label(My_window,text='',fg="#000000",bg="#2288ff",font=("Arial",40))
l12=Label(My_window,text='',fg="#000000",bg="#2288ff",font=("Arial",40))
l13=Label(My_window,text='',fg="#000000",bg="#2a91ff",font=("Arial",40))
l14=Label(My_window,text='',fg="#000000",bg="#3399ff",font=("Arial",40))
l15=Label(My_window,text='',fg="#000000",bg="#2288ff",font=("Arial",40))
l16=Label(My_window,text='',fg="#000000",bg="#2a91ff",font=("Arial",40))
l17=Label(My_window,text='',fg="#000000",bg="#3399ff",font=("Arial",40))
l18=Label(My_window,text='',fg="#000000",bg="#2288ff",font=("Arial",40))
l19=Label(My_window,text='',fg="#000000",bg="#2a91ff",font=("Arial",40))
l20=Label(My_window,text='',fg="#000000",bg="#3399ff",font=("Arial",40))
inp=[2,1,0,5,4,3,8,7,6]
rf=['','①','②','③','④','⑤','⑥']
def NewGame(e=0):
    with open('db.txt','r') as file:
        info=file.readlines()
    for i in range(len(info)):  
        if(info[i]=="Saving:\n"):
            info[i+1]=f"000000000 000000000 {randrange(1,3)} {randrange(1,7)}\n"
        if(info[i]=="Save:\n"):
            info[i+1]="0\n"
    infostr=""
    for i in range(len(info)):
        infostr=infostr+info[i]
    with open('db.txt','w') as file:
        file.write(infostr)
    try:
        startfile("Math Challenge.exe")
    except FileNotFoundError:
        try:
            startfile("Math Challenge.py")
            sleep(1)
            press_and_release('F5')
        except FileNotFoundError:
            print("Щось пішло не так!?")
    My_window.destroy()
def Save(e=0):
    with open('db.txt','r') as file:
        info=file.readlines()
    for i in range(len(info)):
        if(info[i]=="Save:\n"):
            info[i+1]="1\n"
        if(info[i]=="Saving:\n"):
            info[i+1]=f"{p1[0]}{p1[1]}{p1[2]}{p1[3]}{p1[4]}{p1[5]}{p1[6]}{p1[7]}{p1[8]} {p2[0]}{p2[1]}{p2[2]}{p2[3]}{p2[4]}{p2[5]}{p2[6]}{p2[7]}{p2[8]} {g} {r}\n"
    infostr=""
    for i in range(len(info)):
        infostr=infostr+info[i]
    with open('db.txt','w') as file:
        file.write(infostr)
    My_window.destroy()
def caunt(e=0):
    c1=0
    c2=0
    pp1=p1.copy()
    pp2=p2.copy()
    for i in range(3):
        if(pp1[i*3]==pp1[i*3+1]==pp1[i*3+2]!=1):
            c1=c1+pp1[i*3]**3
            pp1[i*3]=0
            pp1[i*3+1]=0
            pp1[i*3+2]=0
    for i in range(3):
        if(pp1[0+i]==pp1[3+i]==pp1[6+i]!=1):
            c1=c1+pp1[i]**3
            pp1[0+i]=0
            pp1[3+i]=0
            pp1[6+i]=0
    for i in range(3):
        if(pp1[i*3]==pp1[i*3+1]!=1):
            c1=c1+pp1[i*3]**2
            pp1[i*3]=0
            pp1[i*3+1]=0
    for i in range(3):
        if(pp1[i*3+1]==pp1[i*3+2]!=1):
            c1=c1+pp1[i*3+1]**2
            pp1[i*3+1]=0
            pp1[i*3+2]=0
    for i in range(3):
        if(pp1[i]==pp1[i+3]!=1):
            c1=c1+pp1[i]**2
            pp1[i]=0
            pp1[i+3]=0
    for i in range(3):
        if(pp1[i+3]==pp1[i+6]!=1):
            c1=c1+pp1[i+3]**2
            pp1[i+3]=0
            pp1[i+6]=0
    for i in range(3):
        if(pp1[i*3]==pp1[i*3+2] and 0==p1[i*3+1]!=1):
            c1=c1+pp1[i*3]**2
            pp1[i*3]=0
            pp1[i*3+2]=0
    for i in range(3):
        if(pp1[0+i]==pp1[6+i] and 0==p1[3+i]!=1):
            c1=c1+pp1[i]**2
            pp1[0+i]=0
            pp1[6+i]=0
    for i in range(9):
        c1=c1+pp1[i]
    for i in range(3):
        if(pp2[i*3]==pp2[i*3+1]==pp2[i*3+2]!=1):
            c2=c2+pp2[i*3]**3
            pp2[i*3]=0
            pp2[i*3+1]=0
            pp2[i*3+2]=0
    for i in range(3):
        if(pp2[0+i]==pp2[3+i]==pp2[6+i]!=1):
            c2=c2+pp2[i]**3
            pp2[0+i]=0
            pp2[3+i]=0
            pp2[6+i]=0
    for i in range(3):
        if(pp2[i*3]==pp2[i*3+1]!=1):
            c2=c2+pp2[i*3]**2
            pp2[i*3]=0
            pp2[i*3+1]=0
    for i in range(3):
        if(pp2[i*3+1]==pp2[i*3+2]!=1):
            c2=c2+pp2[i*3+1]**2
            pp2[i*3+1]=0
            pp2[i*3+2]=0
    for i in range(3):
        if(pp2[i]==pp2[i+3]!=1):
            c2=c2+pp2[i]**2
            pp2[i]=0
            pp2[i+3]=0
    for i in range(3):
        if(pp2[i+3]==pp2[i+6]!=1):
            c2=c2+pp2[i+3]**2
            pp2[i+3]=0
            pp2[i+6]=0
    for i in range(3):
        if(pp2[i*3]==pp2[i*3+2] and 0==p2[i*3+1]!=1):
            c2=c2+pp2[i*3]**2
            pp2[i*3]=0
            pp2[i*3+2]=0
    for i in range(3):
        if(pp2[0+i]==pp2[6+i] and 0==p2[3+i]!=1):
            c2=c2+pp2[i]**2
            pp2[0+i]=0
            pp2[6+i]=0
    for i in range(9):
        c2=c2+pp2[i]
    l0.pack(fill=X)
    l1['text']=str(c1)
    l2['text']=str(c2)
    try:
        a1=int(e1.get())
        a2=int(e2.get())
    except:
        a1,a2=0,0
    if(c1>c2 or (c1==c2 and c1==a1 and c2!=a2)):
        l0['text']=translationtext[0][:-1]
        l3['fg']='#fdd017'
        l4['fg']='#fdd017'
        l5['fg']='#fdd017'
        l6['fg']='#fdd017'
        l7['fg']='#fdd017'
        l8['fg']='#fdd017'
        l9['fg']='#fdd017'
        l10['fg']='#fdd017'
        l11['fg']='#fdd017'
    elif(c1<c2 or (c1==c2 and c2==a2 and c1!=a1)):
        l0['text']=translationtext[1][:-1]
        l12['fg']='#fdd017'
        l13['fg']='#fdd017'
        l14['fg']='#fdd017'
        l15['fg']='#fdd017'
        l16['fg']='#fdd017'
        l17['fg']='#fdd017'
        l18['fg']='#fdd017'
        l19['fg']='#fdd017'
        l20['fg']='#fdd017'
    else:
        l0['text']=translationtext[2][:-1]
        l3['fg']='#ccc'
        l4['fg']='#ccc'
        l5['fg']='#ccc'
        l6['fg']='#ccc'
        l7['fg']='#ccc'
        l8['fg']='#ccc'
        l9['fg']='#ccc'
        l10['fg']='#ccc'
        l11['fg']='#ccc'
        l12['fg']='#ccc'
        l13['fg']='#ccc'
        l14['fg']='#ccc'
        l15['fg']='#ccc'
        l16['fg']='#ccc'
        l17['fg']='#ccc'
        l18['fg']='#ccc'
        l19['fg']='#ccc'
        l20['fg']='#ccc'
    if(c1==a1):
        e1['bg']='#2f2'
    else:
        e1['bg']='#f22'
    if(c2==a2):
        e2['bg']='#2f2'
    else:
        e2['bg']='#f22'
    c.bind('<Button-1>',NewGame)
def postfinish():
    if(e1.get()=='' or e2.get()==''):
        b0['text']=translationtext[4][:-1]
    else:
        b0.destroy()
        caunt()
def finish():
    global finishD,l
    finishD=True
    if(l):
       caunt()
    else:
        e1.place(x=84,y=3)
        e2.place(x=425,y=3)
        b0.place(anchor=CENTER,relx=0.5,y=12)
def fil():
    c1=True
    c2=True
    for i in range(9):
        if(p1[i]==0):
            c1=False
            break
    for i in range(9):
        if(p2[i]==0):
            c2=False
            break
    if(c1 or c2):
        finish()
def ran():
    global r
    r=randrange(1,7)
    if(g==1):
        l1['text']=str(r)
        l2['text']=''
    else:
        l1['text']=''
        l2['text']=str(r)
def vis(n):
    if(g==1):
        p1[n]=r
        f=[lambda: l3.place(x=25,y=37),lambda: l4.place(x=105,y=37),lambda: l5.place(x=185,y=37),lambda: l6.place(x=25,y=117),lambda: l7.place(x=105,y=117),lambda: l8.place(x=185,y=117),lambda: l9.place(x=25,y=197),lambda: l10.place(x=105,y=197),lambda: l11.place(x=185,y=197)]
        f[n]()
    else:
        p2[n]=r
        f=[lambda: l12.place(x=287,y=37),lambda: l13.place(x=367,y=37),lambda: l14.place(x=447,y=37),lambda: l15.place(x=287,y=117),lambda: l16.place(x=367,y=117),lambda: l17.place(x=447,y=117),lambda: l18.place(x=287,y=197),lambda: l19.place(x=367,y=197),lambda: l20.place(x=447,y=197)]
        f[n]()
    l3['text']=str(rf[p1[0]])
    l4['text']=str(rf[p1[1]])
    l5['text']=str(rf[p1[2]])
    l6['text']=str(rf[p1[3]])
    l7['text']=str(rf[p1[4]])
    l8['text']=str(rf[p1[5]])
    l9['text']=str(rf[p1[6]])
    l10['text']=str(rf[p1[7]])
    l11['text']=str(rf[p1[8]])
    l12['text']=str(rf[p2[0]])
    l13['text']=str(rf[p2[1]])
    l14['text']=str(rf[p2[2]])
    l15['text']=str(rf[p2[3]])
    l16['text']=str(rf[p2[4]])
    l17['text']=str(rf[p2[5]])
    l18['text']=str(rf[p2[6]])
    l19['text']=str(rf[p2[7]])
    l20['text']=str(rf[p2[8]])
def player1(x,y):
    global g
    for i in range(3):
        for j in range(3):
            if(10+j*80<x and x<80+j*80 and 10+i*80<y and y<80+i*80):
                if(p1[i*3+j]==0):
                    if(r==p2[inp[i*3+j]]):
                        p2[inp[i*3+j]]=0
                    vis(i*3+j)
                    g=2
                    ran()
def player2(x,y):
    global g
    for i in range(3):
        for j in range(3):
            if(271+j*80<x and x<341+j*80 and 10+i*80<y and y<80+i*80):
                if(p2[i*3+j]==0):
                    if(r==p1[inp[i*3+j]]):
                        p1[inp[i*3+j]]=0
                    vis(i*3+j)
                    g=1
                    ran()
def EventXY(event):
    global g,finishD
    if(finishD):
        return
    for i in range(len(str(event))):
        if(str(event)[i:i+2]=='x='):
            d=str(event)[i+2:-1]
            break
    for i in range(len(d)):
        if(d[i]==' '):
            x=int(d[:i])
    for i in range(len(d)):
        if(d[i]=='='):
            y=int(d[i+1:])
    if(x<255 and g==1):
        player1(x,y)
    elif(g==2):
        player2(x,y)
    fil()
def Load():
    global g,r,p1,p2,l
    g=randrange(1,3)
    r=randrange(1,7)
    p1=[0]*9
    p2=[0]*9
    l=True
    with open('db.txt','r') as file:
        info=file.readlines()
    for i in range(len(info)):
        if(info[i]=="Save:\n"):
            if(info[i+1][0]=='1'):
                for i in range(len(info)):
                    if(info[i]=="Saving:\n"):
                        li=info[i+1][:-1]
                        p1=[int(li[0]),int(li[1]),int(li[2]),int(li[3]),int(li[4]),int(li[5]),int(li[6]),int(li[7]),int(li[8])]
                        p2=[int(li[10]),int(li[11]),int(li[12]),int(li[13]),int(li[14]),int(li[15]),int(li[16]),int(li[17]),int(li[18])]
                        g=1
                        for i in range(9):
                            if(p1[i]!=0):
                                r=p1[i]
                                vis(i)
                        g=2
                        for i in range(9):
                            if(p2[i]!=0):
                                r=p2[i]
                                vis(i)
                        g,r=int(li[20]),int(li[22])
    for i in range(len(info)):
        if(info[i]=="GoesFirst:\n"):
            if(info[i+1]=='f\n'):
                g=1
            if(info[i+1]=='s\n'):
                g=2
        if(info[i]=="Learn:\n"):
            if(info[i+1]=='t\n'):
                l=False
c.bind('<Button-1>',EventXY)
bimg1=PhotoImage(file="image/back.png")
bimg2=PhotoImage(file="image/new game.png")
b0=Button(My_window,text=translationtext[3][:-1],fg="#000000",bg="#88ddff",justify=CENTER,font=("Arial",8),command=postfinish)
b1=Button(My_window,text="Зберегти",bg="#88ddff",font=("Arial",13),image=bimg1,command=Save).place(x=10,y=1)
b2=Button(My_window,text="Знову",bg="#88ddff",font=("Arial",13),image=bimg2,command=NewGame).place(x=496,y=1)
e1=Entry(My_window,width=3)
e2=Entry(My_window,width=3)
Load()
fil()
if(g==1):
    l1['text']=str(r)
else:
    l2['text']=str(r)
My_window.mainloop()