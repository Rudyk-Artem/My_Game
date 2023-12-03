from random import randrange
from tkinter import *
g=randrange(1,3)
r=randrange(1,7)
p1=[0]*9
p2=[0]*9
pn=[2,1,0,5,4,3,8,7,6]
rf=['','①','②','③','④','⑤','⑥']
def caunt():
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
    l1['text']=str(c1)
    l2['text']=str(c2)
    if(c1>c2):
        l0['text']='Виграв перший гравець'
        l3['fg']='#fdd017'
        l4['fg']='#fdd017'
        l5['fg']='#fdd017'
        l6['fg']='#fdd017'
        l7['fg']='#fdd017'
        l8['fg']='#fdd017'
        l9['fg']='#fdd017'
        l10['fg']='#fdd017'
        l11['fg']='#fdd017'
    elif(c1<c2):
        l0['text']='Виграв другий гравець'
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
        l0['text']='Перемогла дружба'
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
    c.bind('<Button-1>',caunt)
def fil():
    c=True
    cc=True
    for i in range(9):
        if(p1[i]==0):
            c=False
            break
    for i in range(9):
        if(p2[i]==0):
            cc=False
            break
    if(c or cc):
        caunt()
    return
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
def inf(event):
    global g
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
        for i in range(3):
            for j in range(3):
                if(10+j*80<x and x<80+j*80 and 10+i*80<y and y<80+i*80):
                    if(p1[i*3+j]==0):
                        if(r==p2[pn[i*3+j]]):
                            p2[pn[i*3+j]]=0
                        vis(i*3+j)
                        g=2
                        ran()
    elif(g==2):
        for i in range(3):
            for j in range(3):
                if(271+j*80<x and x<341+j*80 and 10+i*80<y and y<80+i*80):
                    if(p2[i*3+j]==0):
                        if(r==p1[pn[i*3+j]]):
                            p1[pn[i*3+j]]=0
                        vis(i*3+j)
                        g=1
                        ran()
    fil()

My_window=Tk()
My_window.title("+&×")
My_window.geometry("531x285")
My_window["bg"]="#88ddff" 
c=Canvas(My_window,width=505,height=244,bd=1,highlightcolor='#984332',bg='#4499ee')
c.place(x=10,y=25)
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
l0=Label(My_window,text='',fg="#000000",bg="#88ddff",justify=CENTER,font=15)
l0.pack(fill=X)
l1=Label(My_window,text='',fg="#000000",bg="#88ddff",font=15)
l1.place(x=128,y=0)
l2=Label(My_window,text='',fg="#000000",bg="#88ddff",font=15)
l2.place(x=388,y=0)
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
c.bind('<Button-1>',inf)
if(g==1):
    l1['text']=str(r)
else:
    l2['text']=str(r)
My_window.mainloop()