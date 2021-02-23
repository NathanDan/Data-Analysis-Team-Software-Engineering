#TEAM SOFTWARE ENGINEERING GROUP 2 - DATA ANALYSIS
#NATHAN JONES, ELA SALAH, RYAN MUSIWA, SAMUAL BAILEY, SAM DAVEY & BEN MOSS
#DEVELOPED AND CODED BY NATHAN JONES
#FEB/MAR/APR/MAY 2021

#COVID-19 AND POLUTION LEVELS TRACKER
#VERSION 1.1.2

import tkinter as tk                                             #IMPORTING THE TKINTER MODULE TO BE USED IN THE PROGRAM
import sys                                                       #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON
import os.path                                                   #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS
import os                                                        #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC.
import matplotlib.pyplot as plt                                  #IMPORTING MATPLOTLIB SO THAT GRAPHS CAN BE CREATED AND PRODUCED IN THE PROGRAM
import pandas as pd                                              #ALLOWS FOR CERTIAN MATHMATICAL FUNCTIONS AND READING OF CSV DATA TO TAKE PLACE

from tkinter import messagebox, Label, Button, FALSE, Tk, Entry  #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  #ALLOWING FOR THE MATPLOTLIB GRAPHS TO BE INSERTED INTO THE TKINTER GUI'S

def MenuMain():
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
        MENU.destroy()                                                                                             #CLOSING THE MENU AFTER THE WINDOW HAS BEEN LAUNCHED
        LONDON = Tk()                                                                                              #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

        s1 = Label(LONDON, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s1.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL
        Back = Button(LONDON, text="Main Menu", command=MenuMain)                                                  #CREATING A BUTTON THAT WILL TAKE THE USER TO THE LONDON DATA
        Back.pack()                                                                                                #DISPLAYING THE BUTTON TO THE USER
        s2 = Label(LONDON, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s2.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL
        l1 = Label(LONDON, text="COVID-19 & Air Pollution Levels - London", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
        l1.pack()                                                                                                  #DISPLAYING THE LABEL
        s3 = Label(LONDON, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
        s3.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL

        LONDON.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
        LONDON.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
        LONDON.title("COVID-19 APL - London")            #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
        LONDON.geometry("1600x600")                      #GENERATING THE SIZE OF THE WINDOW 
        LONDON.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, LONDON)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - London',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, LONDON)                                            #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                   #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                             #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - London',ax=ax) #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 


        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, LONDON)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - London',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH

    def Madrid():
        MENU.destroy()                                                                                             #CLOSING THE MENU AFTER THE WINDOW HAS BEEN LAUNCHED
        MADRID = Tk()                                                                                              #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

        s1 = Label(MADRID, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s1.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL
        Back = Button(MADRID, text="Main Menu", command=MenuMain)                                                  #CREATING A BUTTON THAT WILL TAKE THE USER TO THE LONDON DATA
        Back.pack()                                                                                                #DISPLAYING THE BUTTON TO THE USER
        s2 = Label(MADRID, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s2.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL
        l1 = Label(MADRID, text="COVID-19 & Air Pollution Levels - Madrid", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
        l1.pack()                                                                                                  #DISPLAYING THE LABEL
        s3 = Label(MADRID, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
        s3.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL

        MADRID.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
        MADRID.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
        MADRID.title("COVID-19 APL - Madrid")            #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
        MADRID.geometry("1600x600")                      #GENERATING THE SIZE OF THE WINDOW 
        MADRID.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MADRID)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Madrid',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MADRID)                                            #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                   #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                             #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Madrid',ax=ax) #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 


        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        df20 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MADRID)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Madrid',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        
    def Milan():
        MENU.destroy()                                                                                           #CLOSING THE MENU AFTER THE WINDOW HAS BEEN LAUNCHED
        MILAN = Tk()                                                                                             #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

        s1 = Label(MILAN, text=" ", bg="gray84")                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s1.pack()                                                                                                #DISPLAYING THE SPCAE LABEL
        Back = Button(MILAN, text="Main Menu", command=MenuMain)                                                 #CREATING A BUTTON THAT WILL TAKE THE USER TO THE LONDON DATA
        Back.pack()                                                                                              #DISPLAYING THE BUTTON TO THE USER
        s2 = Label(MILAN, text=" ", bg="gray84")                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s2.pack()                                                                                                #DISPLAYING THE SPCAE LABEL
        l1 = Label(MILAN, text="COVID-19 & Air Pollution Levels - Milan", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
        l1.pack()                                                                                                #DISPLAYING THE LABEL
        s3 = Label(MILAN, text=" ", bg="gray84")                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
        s3.pack()                                                                                                #DISPLAYING THE SPCAE LABEL

        MILAN.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
        MILAN.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
        MILAN.title("COVID-19 APL - Milan")             #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
        MILAN.geometry("1600x600")                      #GENERATING THE SIZE OF THE WINDOW 
        MILAN.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                               #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                             #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MILAN)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                   #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                   #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Milan',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                               #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                             #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MILAN)                                            #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                   #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                            #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Milan',ax=ax) #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 


        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                               #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        df20 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                             #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MILAN)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                   #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                   #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Milan',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        
    def Berlin():
        MENU.destroy()                                                                                             #CLOSING THE MENU AFTER THE WINDOW HAS BEEN LAUNCHED
        BERLIN = Tk()                                                                                              #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

        s1 = Label(BERLIN, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s1.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL
        Back = Button(BERLIN, text="Main Menu", command=MenuMain)                                                  #CREATING A BUTTON THAT WILL TAKE THE USER TO THE LONDON DATA
        Back.pack()                                                                                                #DISPLAYING THE BUTTON TO THE USER
        s2 = Label(BERLIN, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s2.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL
        l1 = Label(BERLIN, text="COVID-19 & Air Pollution Levels - Berlin", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
        l1.pack()                                                                                                  #DISPLAYING THE LABEL
        s3 = Label(BERLIN, text=" ", bg="gray84")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
        s3.pack()                                                                                                  #DISPLAYING THE SPCAE LABEL


        BERLIN.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
        BERLIN.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
        BERLIN.title("COVID-19 APL - Berlin")            #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
        BERLIN.geometry("1600x600")                      #GENERATING THE SIZE OF THE WINDOW 
        BERLIN.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BERLIN)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Berlin',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BERLIN)                                            #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                   #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                             #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Berlin',ax=ax) #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 


        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        df20 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BERLIN)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Berlin',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH

    def Barcelona():
        MENU.destroy()                                                                                                   #CLOSING THE MENU AFTER THE WINDOW HAS BEEN LAUNCHED
        BARCELONA = Tk()                                                                                                 #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

        s1 = Label(BARCELONA, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s1.pack()                                                                                                        #DISPLAYING THE SPCAE LABEL
        Back = Button(BARCELONA, text="Main Menu", command=MenuMain)                                                     #CREATING A BUTTON THAT WILL TAKE THE USER TO THE LONDON DATA
        Back.pack()                                                                                                      #DISPLAYING THE BUTTON TO THE USER
        s2 = Label(BARCELONA, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s2.pack()                                                                                                        #DISPLAYING THE SPCAE LABEL
        l1 = Label(BARCELONA, text="COVID-19 & Air Pollution Levels - Barcelona", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
        l1.pack()                                                                                                        #DISPLAYING THE LABEL
        s3 = Label(BARCELONA, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
        s3.pack()                                                                                                        #DISPLAYING THE SPCAE LABEL

        BARCELONA.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
        BARCELONA.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
        BARCELONA.title("COVID-19 APL - Barcelona")         #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
        BARCELONA.geometry("1600x600")                      #GENERATING THE SIZE OF THE WINDOW 
        BARCELONA.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BARCELONA)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Barcelona',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")   #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")   #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BARCELONA)                                            #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                      #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Barcelona',ax=ax) #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 


        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        df20 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BARCELONA)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Barcelona',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH

    def Amsterdam():
        MENU.destroy()                                                                                                   #CLOSING THE MENU AFTER THE WINDOW HAS BEEN LAUNCHED
        AMSTERDAM = Tk()                                                                                                 #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

        s1 = Label(AMSTERDAM, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s1.pack()                                                                                                        #DISPLAYING THE SPCAE LABEL
        Back = Button(AMSTERDAM, text="Main Menu", command=MenuMain)                                                     #CREATING A BUTTON THAT WILL TAKE THE USER TO THE LONDON DATA
        Back.pack()                                                                                                      #DISPLAYING THE BUTTON TO THE USER
        s2 = Label(AMSTERDAM, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
        s2.pack()                                                                                                        #DISPLAYING THE SPCAE LABEL
        l1 = Label(AMSTERDAM, text="COVID-19 & Air Pollution Levels - Amsterdam", font='Helvetica 12 bold', bg="gray84") #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
        l1.pack()                                                                                                        #DISPLAYING THE LABEL
        s3 = Label(AMSTERDAM, text=" ", bg="gray84")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
        s3.pack()                                                                                                        #DISPLAYING THE SPCAE LABEL

        AMSTERDAM.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
        AMSTERDAM.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
        AMSTERDAM.title("COVID-19 APL - Amsterdam")         #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
        AMSTERDAM.geometry("1600x600")                      #GENERATING THE SIZE OF THE WINDOW 
        AMSTERDAM.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, AMSTERDAM)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Amsterdam',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")   #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")   #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, AMSTERDAM)                                            #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                      #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Amsterdam',ax=ax) #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 


        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        df20 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, AMSTERDAM)                                             #DISPLAYING THE GRAPH IN THE TKINTER WINDOW FOR THE CITY
        Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Amsterdam',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        

    b1 = Button(MENU, text="     London - Air Pollution Data   ", command=London)        #CREATING A BUTTON THAT WILL TAKE THE USER TO THE LONDON DATA
    b1.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER

    b2 = Button(MENU, text="     Madrid - Air Pollution Data    ", command=Madrid)       #CREATING A BUTTON THAT WILL TAKE THE USER TO THE MADRID DATA
    b2.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER  

    b3 = Button(MENU, text="       Milan - Air Pollution Data     ", command=Milan)      #CREATING A BUTTON THAT WILL TAKE THE USER TO THE MILAN DATA
    b3.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER

    b4 = Button(MENU, text="       Berlin - Air Pollution Data     ", command=Berlin)    #CREATING A BUTTON THAT WILL TAKE THE USER TO THE BERLIN DATA
    b4.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER

    b5 = Button(MENU, text="  Barcelona - Air Pollution Data   ", command=Barcelona)     #CREATING A BUTTON THAT WILL TAKE THE USER TO THE AMSTERDAM DATA
    b5.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER 

    b6 = Button(MENU, text=" Amsterdam - Air Pollution Data", command=Amsterdam)         #CREATING A BUTTON THAT WILL TAKE THE USER TO THE AMSTERDAM DATA
    b6.pack()                                                                            #DISPLAYING THE BUTTON TO THE USER 

    MENU.resizable(0,0)                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
    MENU.resizable(width=FALSE, height=FALSE)      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
    MENU.title("COVID-19 APL - Menu")              #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
    MENU.geometry("400x300")                       #GENERATING THE SIZE OF THE WINDOW 
    MENU.configure(background='gray84')            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

MenuMain()
