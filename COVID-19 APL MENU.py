#TEAM SOFTWARE ENGINEERING GROUP 2 - DATA ANALYSIS
#NATHAN JONES, ELA SALAH, RYAN MUSIWA, SAMUAL BAILEY, SAM DAVEY & BEN MOSS
#FEB/MAR/APR/MAY 2021

#COVID-19 AND POLUTION LEVELS TRACKER MENU

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry    #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from tkinter import *                                              #ALLOWING FOR ALL OF TKINTER'S MODULES TO BE IMPORTED 

import sys         #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON
import os.path     #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS
import os          #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC.
import time as t

MENU = Tk()                                                                                                             #CREATING THE WINDOW THAT WILL BE DISPLAYED TO THE USER

s1 = Label(MENU, text=" ", bg="gray84")                                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
s1.pack()                                                                                                               #DISPLAYING THE SPCAE LABEL

l1 = Label(MENU, text="COVID-19 & Air Pollution Levels", font='Helvetica 12 bold', bg="gray84")                         #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
l1.pack()                                                                                                               #DISPLAYING THE LABEL

s2 = Label(MENU, text=" ", bg="gray84")                                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
s2.pack()                                                                                                               #DISPLAYING THE SPCAE LABEL

l2 = Label(MENU, text="Please Select One Of The Following Cities To View Their Data", font='Helvetica 10', bg="gray84") #CREATING A LABEL THAT WILL DISPLAY WHAT TO DO
l2.pack()                                                                                                               #DISPLAYING THE LABEL TO THE USER

s3 = Label(MENU, text=" ", bg="gray84")                                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
s3.pack()                                                                                                               #DISPLAYING THE SPCAE LABEL

def London():
    LONDON = Tk.Lon()

    s1 = Label(LONDON, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL

    l1 = Label(LONDON, text="COVID-19 & Air Pollution Levels - London", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
    l1.pack()                                                                                                  #DISPLAYING THE LABEL

    s2 = Label(LONDON, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL

    LONDON.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
    LONDON.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
    LONDON.title("COVID-19 APL - London")            #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
    LONDON.geometry("800x600")                       #GENERATING THE SIZE OF THE WINDOW 
    LONDON.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR
    

def Madrid():
    MADRID = Tk()

    s1 = Label(MADRID, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL

    l1 = Label(MADRID, text="COVID-19 & Air Pollution Levels - Madrid", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
    l1.pack()                                                                                                  #DISPLAYING THE LABEL

    s2 = Label(MADRID, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL

    MADRID.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
    MADRID.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
    MADRID.title("COVID-19 APL - Madrid")            #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
    MADRID.geometry("800x600")                       #GENERATING THE SIZE OF THE WINDOW 
    MADRID.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

def Milan():
    MILAN = Tk()

    s1 = Label(MILAN, text=" ", bg="gray84")                                                                   #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL

    l1 = Label(MILAN, text="COVID-19 & Air Pollution Levels - Milan", font='Helvetica 12 bold', bg="gray84")   #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
    l1.pack()                                                                                                  #DISPLAYING THE LABEL

    s2 = Label(MILAN, text=" ", bg="gray84")                                                                   #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL

    MILAN.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
    MILAN.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
    MILAN.title("COVID-19 APL - Milan")             #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
    MILAN.geometry("800x600")                       #GENERATING THE SIZE OF THE WINDOW 
    MILAN.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

def Berlin():
    BERLIN = Tk()

    s1 = Label(BERLIN, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                     #DISPLAYING THE SPCAE LABEL

    l1 = Label(BERLIN, text="COVID-19 & Air Pollution Levels - Berlin", font='Helvetica 12 bold', bg="gray84")    #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
    l1.pack()                                                                                                     #DISPLAYING THE LABEL

    s2 = Label(BERLIN, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                     #DISPLAYING THE SPCAE LABEL

    BERLIN.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
    BERLIN.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
    BERLIN.title("COVID-19 APL - Berlin")            #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
    BERLIN.geometry("800x600")                       #GENERATING THE SIZE OF THE WINDOW 
    BERLIN.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

def Barcelona():
    BARCELONA = Tk()

    s1 = Label(BARCELONA, text=" ", bg="gray84")                                                                    #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                       #DISPLAYING THE SPCAE LABEL

    l1 = Label(BARCELONA, text="COVID-19 & Air Pollution Levels - Barelona", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
    l1.pack()                                                                                                       #DISPLAYING THE LABEL

    s2 = Label(BARCELONA, text=" ", bg="gray84")                                                                    #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                       #DISPLAYING THE SPCAE LABEL

    BARCELONA.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
    BARCELONA.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
    BARCELONA.title("COVID-19 APL - Barelona")          #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
    BARCELONA.geometry("800x600")                       #GENERATING THE SIZE OF THE WINDOW 
    BARCELONA.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

def Amsterdam():
    AMSTERDAM = Tk()

    s1 = Label(AMSTERDAM, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                        #DISPLAYING THE SPCAE LABEL

    l1 = Label(AMSTERDAM, text="COVID-19 & Air Pollution Levels - Amsterdam", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
    l1.pack()                                                                                                        #DISPLAYING THE LABEL

    s2 = Label(AMSTERDAM, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                        #DISPLAYING THE SPCAE LABEL

    AMSTERDAM.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
    AMSTERDAM.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
    AMSTERDAM.title("COVID-19 APL - Amsterdam")         #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
    AMSTERDAM.geometry("800x600")                       #GENERATING THE SIZE OF THE WINDOW 
    AMSTERDAM.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 
    

b1 = Button(MENU, text="     London - Air Pollution Data   ", command=London)        #CREATING A BUTTON THAT WILL TAKE THE USER TO THE LONDON DATA
b1.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER

b2 = Button(MENU, text="     Madrid - Air Pollution Data    ", command=Madrid)       #CREATING A BUTTON THAT WILL TAKE THE USER TO THE MADRID DATA
b2.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER  

b3 = Button(MENU, text="       Milan - Air Pollution Data     ", command=Milan)      #CREATING A BUTTON THAT WILL TAKE THE USER TO THE MILAN DATA
b3.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER

b4 = Button(MENU, text="       Berlin - Air Pollution Data     ", command=Berlin)    #CREATING A BUTTON THAT WILL TAKE THE USER TO THE BERLIN DATA
b4.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER

b5 = Button(MENU, text="  Barcelona - Air Pollution Data   ", command=Barcelona)         #CREATING A BUTTON THAT WILL TAKE THE USER TO THE AMSTERDAM DATA
b5.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER 

b6 = Button(MENU, text=" Amsterdam - Air Pollution Data", command=Amsterdam)         #CREATING A BUTTON THAT WILL TAKE THE USER TO THE AMSTERDAM DATA
b6.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER 

MENU.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
MENU.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
MENU.title("COVID-19 APL - Menu")              #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
MENU.geometry("400x300")                       #GENERATING THE SIZE OF THE WINDOW 
MENU.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

