from keyboard import press_and_release
from os import startfile
from time import sleep
from tkinter import *
with open('db.txt','r') as file:
    info=file.readlines()
for i in range(len(info)):
    if(info[i]=="NewWindow:\n"):
        info[i+1]="0\n"
    if(info[i]=="NewWindowCompact:\n"):
        info[i+1]="0\n"
    if(info[i]=="Position:\n"):
        info[i+1]="t\n"
infostr=""
for i in range(len(info)):
    infostr=infostr+info[i]
with open('db.txt','w') as file:
    file.write(infostr)
try:
    for i in range(9):
        startfile("Math Challenge.exe")
        sleep(0.05)
except FileNotFoundError:
    print("У вас немає елементу програми який ви намагаєтесь відкрити")
sleep(0.5)
with open('db.txt','r') as file:
    info=file.readlines()
for i in range(len(info)):
    if(info[i]=="Position:\n"):
        info[i+1]="f\n"
infostr=""
for i in range(len(info)):
    infostr=infostr+info[i]
with open('db.txt','w') as file:
    file.write(infostr)