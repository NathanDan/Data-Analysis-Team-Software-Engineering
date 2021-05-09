#TEAM SOFTWARE ENGINEERING GROUP 2 - DATA ANALYSIS
#NATHAN JONES, ELA SALAH, RYAN MUSIWA, SAMUAL BAILEY, SAM DAVEY & BEN MOSS
#DEVELOPED AND CODED BY NATHAN JONES
#FEB/MAR/APR/MAY 2021

#COVID-19 AND POLUTION LEVELS TRACKER
#VERSION 1.1.9

#MAIN PROGRAM, TABS AND CHARTS CODED BY NATHAN JONES
#WRITTEN STATS CODED BY BEN MOSS
#MAPVIEW CODED BY SAM DAVEY

import tkinter as tk                                             #IMPORTING THE TKINTER MODULE TO BE USED IN THE PROGRAM
import sys                                                       #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON
import os.path                                                   #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS
import os                                                        #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC.
import matplotlib.pyplot as plt                                  #IMPORTING MATPLOTLIB SO THAT GRAPHS CAN BE CREATED AND PRODUCED IN THE PROGRAM
import pandas as pd                                              #ALLOWS FOR CERTIAN MATHMATICAL FUNCTIONS AND READING OF CSV DATA TO TAKE PLACE
  
from tkinter import ttk                                          #IMPORTING THE TKK MODULE THAT ALLOWS FOR TABBED WIDGETS
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry  #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  #ALLOWING FOR THE MATPLOTLIB GRAPHS TO BE INSERTED INTO THE TKINTER GUI'S
from PIL import Image, ImageTk                                   #ALLOWS FOR THE IMPORTS OF IMAGES INTO THE PROGGRAM TO MAKE IT VISUALLY LOOK MORE PROFESSIONAL

def MenuMain():
    MENU = Tk()                                                                                                                    #CREATING THE WINDOW THAT WILL BE DISPLAYED TO THE USER AND HOUSES ALL OF THE DIFFERENT TABS
    MENU.title("COVID-19 Air Polution Levels")                                                                                     #GIVING THE WINDOW A TITLE
    MENU.resizable(width=FALSE, height=FALSE)                                                                                      #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    MENU.geometry("1690x700")                                                                                                      #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE
    tabControl = ttk.Notebook(MENU)                                                                                                #TELLING THE PROGRAM THAT WILL WILL BE A TABBED WIDGET

    style = ttk.Style()                                                                                                             #CREATING A TTK STYLE THAT WILL CHANGE THE COLOUR OF THE WIDGET
    style.configure("W.TFrame", foreground="white", background="white")                                                             #SETTING THE BACKGROUND COLOUR TO BE WHITE, SO THAT THE WIDGET LOOKS SMARTER AND MORE PRESENTABLE
    
    HOMEPAGETAB = ttk.Frame(style="W.TFrame")                                                                                                                     #CREATING THE HOME TAB ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(HOMEPAGETAB, text=" ", bg="white")                                                                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                                                     #DISPLAYING THE SPCAE LABEL                                                                                                
    l1 = Label(HOMEPAGETAB, text="COVID-19 & Air Pollution Levels - Homepage", font='Helvetica 12 bold', bg="white")                                              #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                                                     #DISPLAYING THE LABEL
    s3 = Label(HOMEPAGETAB, text=" ",bg="white")                                                                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                                                     #DISPLAYING THE SPCAE LABEL
    l2 = Label(HOMEPAGETAB, text="Welcome To The Homepage!", font='Helvetica 10 bold', bg="white")                                                                #CREATING A SUB HEADING FOR THE DESCRIPTION 
    l2.pack()                                                                                                                                                     #DISPLAYING THE LABEL
    l3 = Label(HOMEPAGETAB, text=
    """This is a COVID-19 Air Pollution tracking program that looks at the correlation between COVID-19 Lockdowns
    and the overall pollution impact in certain European cities. The program utilses graphs and other visual stats to
    allow for a visual representation of a significant or minimal difference in pollution levels as a result to the on going
    pandemic.""",
    font='Helvetica 10 ', bg="white")                                                                                                                             #CREATING A DESCRIPTION OF THE PROGRAM FOR THE USER TO SEE
    l3.pack()                                                                                                                                                     #DISPLAYING THE LABEL
    l4 = Label(HOMEPAGETAB, text=
    """The data that is being used in this program has been sourced from the World Air Quality Index Project (WAQIP)
    and its Air Quality Historical Data Platform (https://aqicn.org/data-platform) that is a free to use service, that gathers
    Air Quality Data (AQD) from various sources and groups them together to produce a databse that consits of AQD from
    all over the World. As this program is free and for educational purposes we are allowed to use the data-sets from the
    WAQIP as we are not making a profit and are solely using the data to educate and show a trend in the data.""",
    font='Helvetica 10 ', bg="white")                                                                                                                             #CREATING A DESCRIPTION OF THE DATA USED FOR THE USER TO SEE 
    l4.pack()                                                                                                                                                     #DISPLAYING THE LABEL
    
    l5 = Label(HOMEPAGETAB, text="Make sure to keep upto date with the latest updates and features with the website down below!",font='Helvetica 10', bg="white") #CREATING A SUB HEADING FOR THE DESCRIPTION  
    l5.pack()                                                                                                                                                     #DISPLAYING THE LABEL
    s3 = Label(HOMEPAGETAB, text=" ", bg="white")                                                                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                                                     #DISPLAYING THE SPCAE LABEL
    l6 = Label(HOMEPAGETAB, text="The Development Team",font='Helvetica 10 bold',bg="white")                                                                      #CREATING A SUB HEADING FOR THE DESCRIPTION  
    l6.pack()                                                                                                                                                     #DISPLAYING THE LABEL
    l7 = Label(HOMEPAGETAB, text=
    "Nathan Jones, Ben Moss, Samual Bailey, Ryan Musiwa, Sam Davey & Ela Salah", font='Helvetica 10 ', bg="white")                                                #CREATING A LABEL THAT LISTS EVERY ONE WHO IS INVOLVED WITH THE PROGRAM 
    l7.pack()                                                                                                                                                     #DISPLAYING THE LABEL THAT LISTS EVERY ONE WHO IS INVOLVED
    s5 = Label(HOMEPAGETAB, text=" ", bg="white")                                                                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s5.pack()                                                                                                                                                     #DISPLAYING THE SPCAE LABEL
    l8 = Label(HOMEPAGETAB, text="The Coding Team",font='Helvetica 10 bold',bg="white")                                                                           #CREATING A SUB HEADING FOR THE DESCRIPTION  
    l8.pack()                                                                                                                                                     #DISPLAYING THE LABEL
    l9 = Label(HOMEPAGETAB, text=
    "Nathan Jones, Ben Moss & Sam Davey", font='Helvetica 10 ', bg="white")                                                                                       #CREATING A LABEL THAT LISTS EVERY ONE WHO CODED WITH THE PROGRAM 
    l9.pack()                                                                                                                                                     #DISPLAYING THE LABEL THAT LISTS EVERY ONE WHO IS INVOLVED WITH THE PROGRAM 
    s6 = Label(HOMEPAGETAB, text=" ", bg="white")                                                                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s6.pack()                                                                                                                                                     #DISPLAYING THE SPCAE LABEL
    l10 = Label(HOMEPAGETAB, text="Contact Information",font='Helvetica 10 bold', bg="white")                                                                     #CREATING A SUB HEADING FOR THE CONTACT INFORMATION  
    l10.pack()                                                                                                                                                    #DISPLAYING THE LABEL
    l11 = Label(HOMEPAGETAB, text="Website: https://github.com/NathanDan/Data-Analysis-Team-Software-Engineering",font='Helvetica 10', bg="white")                #CREATING A LABEL FOR THE DESCRIPTION OF THE CONTACT INFORMATION 
    l11.pack()                                                                                                                                                    #DISPLAYING THE LABEL
    l12 = Label(HOMEPAGETAB, text="Version 1.1.9",font='Helvetica 9 bold', bg="white")                                                                            #CREATING A LABEL THAT SHOWS WHAT VERSION THE USER IS ON  
    l12.place(x=1600, y=655)                                                                                                                                      #DISPLAYING THE LABEL AT THE BOTTOM OF THE WINDOW


    LONDONTAB = ttk.Frame(style="W.TFrame")                                                                                         #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(LONDONTAB, text=" ",bg="white")                                                                                      #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL                                                                                                
    l1 = Label(LONDONTAB, text="COVID-19 & Air Pollution Levels - London", font='Helvetica 12 bold',bg="white")                     #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                       #DISPLAYING THE LABEL
    s2 = Label(LONDONTAB, text=" ",bg="white")                                                                                      #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL
    
    def LONLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, LONDONTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - London',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, LONDONTAB)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - London',ax=ax)                                             #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('London\\London Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, LONDONTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - London',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def LONAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, LONDONTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - London',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, LONDONTAB)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - London',ax=ax)                                        #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('London\\London Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, LONDONTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - London',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

    def LONSTATS():
        canvas = tk.Canvas(LONDONTAB, width=1690, height=600, bg="white")                                                           #CREATING THE CANVAS FOR THE WRITTEN STATISTICS TO GO
        canvas.place(x=0, y=90)                                                                                                     #DISPLAYING THE CANVAS AND ITS LOCATION IN THE WINDOW

        lS1 = Label(LONDONTAB, text="London 2019 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                        #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS 
        lS1.place(x=145, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(LONDONTAB, text="January = 30",font='Helvetica 9', bg="white")                                                  #CREATING THE JANUARY LABEL
        lS2.place(x=145, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(LONDONTAB, text="February = 28",font='Helvetica 9', bg="white")                                                 #CREATING THE FEBRUARY LABEL
        lS3.place(x=145, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(LONDONTAB, text="March = 25",font='Helvetica 9', bg="white")                                                    #CREATING THE MARCH LABEL
        lS4.place(x=145, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(LONDONTAB, text="April = 43",font='Helvetica 9', bg="white")                                                    #CREATING THE APRIL LABEL
        lS5.place(x=145, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(LONDONTAB, text="May = 29",font='Helvetica 9', bg="white")                                                      #CREATING THE MAY LABEL
        lS6.place(x=145, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(LONDONTAB, text="June = 25",font='Helvetica 9', bg="white")                                                     #CREATING THE JUNE LABEL
        lS7.place(x=145, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(LONDONTAB, text="July = 14",font='Helvetica 9', bg="white")                                                     #CREATING THE JULY LABEL
        lS8.place(x=145, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(LONDONTAB, text="August = 33",font='Helvetica 9', bg="white")                                                   #CREATING THE AUGUST LABLE
        lS9.place(x=145, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(LONDONTAB, text="September = 29",font='Helvetica 9', bg="white")                                               #CREATING THE SEPTEMBER LABEL
        lS10.place(x=145, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(LONDONTAB, text="October = 29",font='Helvetica 9', bg="white")                                                 #CREATING THE OCTOBER LABEL
        lS11.place(x=145, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(LONDONTAB, text="November = 39",font='Helvetica 9', bg="white")                                                #CREATING THE NOVEMBER LABEL
        lS12.place(x=145, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(LONDONTAB, text="December = 34",font='Helvetica 9', bg="white")                                                #CREATING THE DECEMBER LABEL
        lS13.place(x=145, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(LONDONTAB, text="London 2019 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                #CREATING THE HIGHEST MONTHLY AVERAGE LABEL  
        lS14.place(x=145, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(LONDONTAB, text="November = 39",font='Helvetica 9', bg="white")                                                #CREATING THE DATA LABEL
        lS15.place(x=145, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(LONDONTAB, text="London 2019 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                 #CREATING THE LOWEST MONTHLY AVERAGE LABEL  
        lS16.place(x=145, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(LONDONTAB, text="July = 14",font='Helvetica 9', bg="white")                                                    #CREATING THE DATA LABEL
        lS17.place(x=145, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(LONDONTAB, text="London 2019 Yearly Average",font='Helvetica 10 bold', bg="white")                             #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=145, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(LONDONTAB, text="NO2 Yearly Average Was 32.62",font='Helvetica 9', bg="white")                                 #CREATING THE DATA LABEL
        lS19.place(x=145, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(LONDONTAB, text="London NO2 Monthly Changes",font='Helvetica 10 bold', bg="white")                              #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS  
        lS1.place(x=700, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL 

        lS2 = Label(LONDONTAB, text="January = 10.53% DECREASE",font='Helvetica 9', bg="white")                                     #CREATING THE JANUARY LABEL
        lS2.place(x=700, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(LONDONTAB, text="February = 13.33% INCREASE",font='Helvetica 9', bg="white")                                    #CREATING THE FEBRUARY LABEL
        lS3.place(x=700, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(LONDONTAB, text="March On Average Had The Same NO2 Levels",font='Helvetica 9', bg="white")                      #CREATING THE MARCH LABEL
        lS4.place(x=700, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(LONDONTAB, text="April = 77.42% DECREASE",font='Helvetica 9', bg="white")                                       #CREATING THE APRIL LABEL
        lS5.place(x=700, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(LONDONTAB, text="May = 35.90% DECREASE",font='Helvetica 9', bg="white")                                         #CREATING THE MAY LABEL
        lS6.place(x=700, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(LONDONTAB, text="June = 22.22% DECREASE",font='Helvetica 9', bg="white")                                        #CREATING THE JUNE LABEL
        lS7.place(x=700, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(LONDONTAB, text="July = 6.90% INCREASE",font='Helvetica 9', bg="white")                                         #CREATING THE JULY LABEL
        lS8.place(x=700, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(LONDONTAB, text="August = 53.85% DECREASE",font='Helvetica 9', bg="white")                                      #CREATING THE AUGUST LABLEL
        lS9.place(x=700, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(LONDONTAB, text="September = 41.67% DECREASE",font='Helvetica 9', bg="white")                                  #CREATING THE SEPTEMBER LABEL
        lS10.place(x=700, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(LONDONTAB, text="October = 63.64% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE OCTOBER LABEL
        lS11.place(x=700, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(LONDONTAB, text="November = 55.74% DECREASE",font='Helvetica 9', bg="white")                                   #CREATING THE NOVEMBER LABEL
        lS12.place(x=700, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(LONDONTAB, text="December = 47.28% DECREASE",font='Helvetica 9', bg="white")                                   #CREATING THE DECEMBER LABEL
        lS13.place(x=700, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(LONDONTAB, text="London's Largest Monthy Change (DECREASE)",font='Helvetica 10 bold', bg="white")              #CREATING THE HIGHEST MONTHLY CHANGE (DECREASE) LABEL  
        lS14.place(x=700, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(LONDONTAB, text="April = 77.42% DECREASE",font='Helvetica 9', bg="white")                                      #CREATING THE DATA LABEL
        lS15.place(x=700, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(LONDONTAB, text="London's Largest Monthy Change (INCREASE)",font='Helvetica 10 bold', bg="white")              #CREATING THE HIGHEST MONTHLY CHANGE (INCREASE) LABEL  
        lS16.place(x=700, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(LONDONTAB, text="February = 13.33% INCREASE",font='Helvetica 9', bg="white")                                   #CREATING THE DATA LABEL
        lS17.place(x=700, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(LONDONTAB, text="London Yearly Average Change",font='Helvetica 10 bold', bg="white")                           #CREATING THE YEARLY CHANGE LABEL  
        lS18.place(x=700, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(LONDONTAB, text="Yearly Average Change Was A 44.39% DECREASE In NO2 Levels",font='Helvetica 9', bg="white")    #CREATING THE DATA LABEL
        lS19.place(x=700, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(LONDONTAB, text="London 2020 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                        #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS    
        lS1.place(x=1255, y=100)                                                                                                    #DISPLAYING THE HEADING LABEL 

        lS2 = Label(LONDONTAB, text="January = 27",font='Helvetica 9', bg="white")                                                  #CREATING THE JANUARY LABEL
        lS2.place(x=1255, y=120)                                                                                                    #DISPLAYING THE JANUARY LABEL
        lS3 = Label(LONDONTAB, text="February = 32",font='Helvetica 9', bg="white")                                                 #CREATING THE FEBRUARY LABEL
        lS3.place(x=1255, y=140)                                                                                                    #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(LONDONTAB, text="March = 25",font='Helvetica 9', bg="white")                                                    #CREATING THE MARCH LABEL
        lS4.place(x=1255, y=160)                                                                                                    #DISPLAYING THE MARCH LABEL
        lS5 = Label(LONDONTAB, text="April = 19",font='Helvetica 9', bg="white")                                                    #CREATING THE APRIL LABEL
        lS5.place(x=1255, y=180)                                                                                                    #DISPLAYING THE APRIL LABEL
        lS6 = Label(LONDONTAB, text="May = 16",font='Helvetica 9', bg="white")                                                      #CREATING THE MAY LABEL
        lS6.place(x=1255, y=200)                                                                                                    #DISPLAYING THE MAY LABEL
        lS7 = Label(LONDONTAB, text="June = 20",font='Helvetica 9', bg="white")                                                     #CREATING THE JUNE LABEL
        lS7.place(x=1255, y=220)                                                                                                    #DISPLAYING THE JUNE LABEL
        lS8 = Label(LONDONTAB, text="July = 15",font='Helvetica 9', bg="white")                                                     #CREATING THE JULY LABEL
        lS8.place(x=1255, y=240)                                                                                                    #DISPLAYING THE JULY LABEL
        lS9 = Label(LONDONTAB, text="August = 19",font='Helvetica 9', bg="white")                                                   #CREATING THE AUGUST LABLEL
        lS9.place(x=1255, y=260)                                                                                                    #DISPLAYING THE AUGUST LABEL
        lS10 = Label(LONDONTAB, text="September = 19",font='Helvetica 9', bg="white")                                               #CREATING THE SEPTEMBER LABEL
        lS10.place(x=1255, y=280)                                                                                                   #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(LONDONTAB, text="October = 15",font='Helvetica 9', bg="white")                                                 #CREATING THE OCTOBER LABEL
        lS11.place(x=1255, y=300)                                                                                                   #DISLAYING THE OCTOBER LABEL
        lS12 = Label(LONDONTAB, text="November = 22",font='Helvetica 9', bg="white")                                                #CREATING THE NOVEMBER LABEL
        lS12.place(x=1255, y=320)                                                                                                   #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(LONDONTAB, text="December = 21",font='Helvetica 9', bg="white")                                                #CREATING THE DECEMBER LABEL
        lS13.place(x=1255, y=340)                                                                                                   #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(LONDONTAB, text="London 2020 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                #CREATING THE HIGHEST MONTHLY AVERAGE LABEL
        lS14.place(x=1255, y=380)                                                                                                   #DISPLAYING THE LABEL
        lS15 = Label(LONDONTAB, text="February = 32",font='Helvetica 9', bg="white")                                                #CREATING THE DATA LABEL
        lS15.place(x=1255, y=400)                                                                                                   #DISPLAYING THE LABEL
        
        lS16 = Label(LONDONTAB, text="London 2020 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                 #CREATING THE LOWEST MONTHLY AVERAGE LABEL
        lS16.place(x=1255, y=420)                                                                                                   #DISPLAYING THE LABEL
        lS17 = Label(LONDONTAB, text="July = 15 / October = 15",font='Helvetica 9', bg="white")                                     #CREATING THE DATA LABEL
        lS17.place(x=1255, y=440)                                                                                                   #DISPLAYING THE LABEL

        lS18 = Label(LONDONTAB, text="London 2020 Yearly Average",font='Helvetica 10 bold', bg="white")                             #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=1255, y=460)                                                                                                   #DISPLAYING THE LABEL
        lS19 = Label(LONDONTAB, text="NO2 Yearly Average Was 20.77",font='Helvetica 9', bg="white")                                 #CREATING THE DATA LABEL
        lS19.place(x=1255, y=480)                                                                                                   #DISPLAYING THE LABEL
        
    LONLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(LONDONTAB, text="Line Graphs", command=LONLINEGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(LONDONTAB, text="Area Graphs", command=LONAREAGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(LONDONTAB, text="Written Statistics", command=LONSTATS)                                                             #CREATING THE BUTTON THAT DISPLAYS THE WRITTEN STATISTICS FOR THE CITY
    b1.place(x=720, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=795, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=872, y=50)                                                                                                           #DISPLAYING THE YEARLY STATISTICS BUTTON
    
    

    MADRIDTAB = ttk.Frame(style="W.TFrame")                                                                                         #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(MADRIDTAB, text=" ",bg="white")                                                                                      #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                       #DISPLAYING THE SPACE LABEL                                                                                              
    l1 = Label(MADRIDTAB, text="COVID-19 & Air Pollution Levels - Madrid", font='Helvetica 12 bold',bg="white")                     #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                       #DISPLAYING THE LABEL
    s3 = Label(MADRIDTAB, text=" ",bg="white")                                                                                      #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

    def MADLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MADRIDTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Madrid',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MADRIDTAB)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Madrid',ax=ax)                                             #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Madrid\\Madrid Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MADRIDTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Madrid',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def MADAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MADRIDTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Madrid',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MADRIDTAB)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Madrid',ax=ax)                                        #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Madrid\\Madrid Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MADRIDTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Madrid',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

    def MADSTATS():
        canvas = tk.Canvas(MADRIDTAB, width=1690, height=600, bg="white")                                                           #CREATING THE CANVAS FOR THE WRITTEN STATISTICS TO GO
        canvas.place(x=0, y=90)                                                                                                     #DISPLAYING THE CANVAS AND ITS LOCATION IN THE WINDOW

        lS1 = Label(MADRIDTAB, text="Madrid 2019 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                        #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS
        lS1.place(x=145, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(MADRIDTAB, text="January = 34",font='Helvetica 9', bg="white")                                                  #CREATING THE JANUARY LABEL
        lS2.place(x=145, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(MADRIDTAB, text="February = 36",font='Helvetica 9', bg="white")                                                 #CREATING THE FEBRUARY LABEL
        lS3.place(x=145, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(MADRIDTAB, text="March = 26",font='Helvetica 9', bg="white")                                                    #CREATING THE MARCH LABEL
        lS4.place(x=145, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(MADRIDTAB, text="April = 21",font='Helvetica 9', bg="white")                                                    #CREATING THE APRIL LABEL
        lS5.place(x=145, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(MADRIDTAB, text="May = 19",font='Helvetica 9', bg="white")                                                      #CREATING THE MAY LABEL
        lS6.place(x=145, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(MADRIDTAB, text="June = 19",font='Helvetica 9', bg="white")                                                     #CREATING THE JUNE LABEL
        lS7.place(x=145, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(MADRIDTAB, text="July = 15",font='Helvetica 9', bg="white")                                                     #CREATING THE JULY LABEL
        lS8.place(x=145, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(MADRIDTAB, text="August = 17",font='Helvetica 9', bg="white")                                                   #CREATING THE AUGUST LABLE
        lS9.place(x=145, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(MADRIDTAB, text="September = 22",font='Helvetica 9', bg="white")                                               #CREATING THE SEPTEMBER LABEL
        lS10.place(x=145, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(MADRIDTAB, text="October = 26",font='Helvetica 9', bg="white")                                                 #CREATING THE OCTOBER LABEL
        lS11.place(x=145, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(MADRIDTAB, text="November = 18",font='Helvetica 9', bg="white")                                                #CREATING THE NOVEMBER LABEL
        lS12.place(x=145, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(MADRIDTAB, text="December = 24",font='Helvetica 9', bg="white")                                                #CREATING THE DECEMBER LABEL
        lS13.place(x=145, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(MADRIDTAB, text="Madrid 2019 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                #CREATING THE HIGHEST MONTHLY AVERAGE LABEL  
        lS14.place(x=145, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(MADRIDTAB, text="February = 36",font='Helvetica 9', bg="white")                                                #CREATING THE DATA LABEL
        lS15.place(x=145, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(MADRIDTAB, text="Madrid 2019 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                 #CREATING THE LOWEST MONTHLY AVERAGE LABEL  
        lS16.place(x=145, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(MADRIDTAB, text="July = 15",font='Helvetica 9', bg="white")                                                    #CREATING THE DATA LABEL
        lS17.place(x=145, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(MADRIDTAB, text="Madrid 2019 Yearly Average",font='Helvetica 10 bold', bg="white")                             #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=145, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(MADRIDTAB, text="NO2 Yearly Average Was 23.08",font='Helvetica 9', bg="white")                                 #CREATING THE DATA LABEL
        lS19.place(x=145, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(MADRIDTAB, text="Madrid NO2 Monthly Changes",font='Helvetica 10 bold', bg="white")                              #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS  
        lS1.place(x=700, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(MADRIDTAB, text="January = 15.87% DECREASE",font='Helvetica 9', bg="white")                                     #CREATING THE JANUARY LABEL
        lS2.place(x=700, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(MADRIDTAB, text="February = 25% DECREASE",font='Helvetica 9', bg="white")                                       #CREATING THE FEBRUARY LABEL
        lS3.place(x=700, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(MADRIDTAB, text="March = 47.62% DECREASE",font='Helvetica 9', bg="white")                                       #CREATING THE MARCH LABEL
        lS4.place(x=700, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(MADRIDTAB, text="April = 89.66% DECREASE",font='Helvetica 9', bg="white")                                       #CREATING THE APRIL LABEL
        lS5.place(x=700, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(MADRIDTAB, text="May = 71.43% DECREASE",font='Helvetica 9', bg="white")                                         #CREATING THE MAY LABEL
        lS6.place(x=700, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(MADRIDTAB, text="June = 45.16% DECREASE",font='Helvetica 9', bg="white")                                        #CREATING THE JUNE LABEL
        lS7.place(x=700, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(MADRIDTAB, text="July On Average Had The Same NO2 Levels",font='Helvetica 9', bg="white")                       #CREATING THE JULY LABEL
        lS8.place(x=700, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(MADRIDTAB, text="August = 12.5% DECREASE",font='Helvetica 9', bg="white")                                       #CREATING THE AUGUST LABLEL
        lS9.place(x=700, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(MADRIDTAB, text="September = 14.63% DECREASE",font='Helvetica 9', bg="white")                                  #CREATING THE SEPTEMBER LABEL
        lS10.place(x=700, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(MADRIDTAB, text="October = 21.28% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE OCTOBER LABEL
        lS11.place(x=700, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(MADRIDTAB, text="November = 40% INCREASE",font='Helvetica 9', bg="white")                                      #CREATING THE NOVEMBER LABEL
        lS12.place(x=700, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(MADRIDTAB, text="December = 18.18% DECREASE",font='Helvetica 9', bg="white")                                   #CREATING THE DECEMBER LABEL
        lS13.place(x=700, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(MADRIDTAB, text="Madrid's Largest Monthy Change (DECREASE)",font='Helvetica 10 bold', bg="white")              #CREATING THE HIGHEST MONTHLY CHANGE (DECREASE) LABEL  
        lS14.place(x=700, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(MADRIDTAB, text="April = 89.66% DECREASE",font='Helvetica 9', bg="white")                                      #CREATING THE DATA LABEL
        lS15.place(x=700, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(MADRIDTAB, text="Madrid's Largest Monthy Change (INCREASE)",font='Helvetica 10 bold', bg="white")              #CREATING THE HIGHEST MONTHLY CHANGE (INCREASE) LABEL  
        lS16.place(x=700, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(MADRIDTAB, text="November = 40% INCREASE",font='Helvetica 9', bg="white")                                      #CREATING THE DATA LABEL
        lS17.place(x=700, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(MADRIDTAB, text="Madrid Yearly Average Change",font='Helvetica 10 bold', bg="white")                           #CREATING THE YEARLY CHANGE LABEL  
        lS18.place(x=700, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(MADRIDTAB, text="Yearly Average Change Was A 23.37% DECREASE In NO2 Levels",font='Helvetica 9', bg="white")    #CREATING THE DATA LABEL
        lS19.place(x=700, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(MADRIDTAB, text="Madrid 2020 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                        #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS   
        lS1.place(x=1255, y=100)                                                                                                    #DISPLAYING THE HEADING LABEL

        lS2 = Label(MADRIDTAB, text="January = 29",font='Helvetica 9', bg="white")                                                  #CREATING THE JANUARY LABEL
        lS2.place(x=1255, y=120)                                                                                                    #DISPLAYING THE JANUARY LABEL
        lS3 = Label(MADRIDTAB, text="February = 28",font='Helvetica 9', bg="white")                                                 #CREATING THE FEBRUARY LABEL
        lS3.place(x=1255, y=140)                                                                                                    #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(MADRIDTAB, text="March = 16",font='Helvetica 9', bg="white")                                                    #CREATING THE MARCH LABEL
        lS4.place(x=1255, y=160)                                                                                                    #DISPLAYING THE MARCH LABEL
        lS5 = Label(MADRIDTAB, text="April = 8",font='Helvetica 9', bg="white")                                                     #CREATING THE APRIL LABEL
        lS5.place(x=1255, y=180)                                                                                                    #DISPLAYING THE APRIL LABEL
        lS6 = Label(MADRIDTAB, text="May = 9",font='Helvetica 9', bg="white")                                                       #CREATING THE MAY LABEL
        lS6.place(x=1255, y=200)                                                                                                    #DISPLAYING THE MAY LABEL
        lS7 = Label(MADRIDTAB, text="June = 12",font='Helvetica 9', bg="white")                                                     #CREATING THE JUNE LABEL
        lS7.place(x=1255, y=220)                                                                                                    #DISPLAYING THE JUNE LABEL
        lS8 = Label(MADRIDTAB, text="July = 15",font='Helvetica 9', bg="white")                                                     #CREATING THE JULY LABEL
        lS8.place(x=1255, y=240)                                                                                                    #DISPLAYING THE JULY LABEL
        lS9 = Label(MADRIDTAB, text="August = 15",font='Helvetica 9', bg="white")                                                   #CREATING THE AUGUST LABLEL
        lS9.place(x=1255, y=260)                                                                                                    #DISPLAYING THE AUGUST LABEL
        lS10 = Label(MADRIDTAB, text="September = 19",font='Helvetica 9', bg="white")                                               #CREATING THE SEPTEMBER LABEL
        lS10.place(x=1255, y=280)                                                                                                   #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(MADRIDTAB, text="October = 21",font='Helvetica 9', bg="white")                                                 #CREATING THE OCTOBER LABEL
        lS11.place(x=1255, y=300)                                                                                                   #DISLAYING THE OCTOBER LABEL
        lS12 = Label(MADRIDTAB, text="November = 27",font='Helvetica 9', bg="white")                                                #CREATING THE NOVEMBER LABEL
        lS12.place(x=1255, y=320)                                                                                                   #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(MADRIDTAB, text="December = 20",font='Helvetica 9', bg="white")                                                #CREATING THE DECEMBER LABEL
        lS13.place(x=1255, y=340)                                                                                                   #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(MADRIDTAB, text="Madrid 2020 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                #CREATING THE HIGHEST MONTHLY AVERAGE LABEL
        lS14.place(x=1255, y=380)                                                                                                   #DISPLAYING THE LABEL
        lS15 = Label(MADRIDTAB, text="January = 29",font='Helvetica 9', bg="white")                                                 #CREATING THE DATA LABEL
        lS15.place(x=1255, y=400)                                                                                                   #DISPLAYING THE LABEL
        
        lS16 = Label(MADRIDTAB, text="Madrid 2020 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                 #CREATING THE LOWEST MONTHLY AVERAGE LABEL
        lS16.place(x=1255, y=420)                                                                                                   #DISPLAYING THE LABEL
        lS17 = Label(MADRIDTAB, text="April = 8",font='Helvetica 9', bg="white")                                                    #CREATING THE DATA LABEL
        lS17.place(x=1255, y=440)                                                                                                   #DISPLAYING THE LABEL

        lS18 = Label(MADRIDTAB, text="Madrid 2020 Yearly Average",font='Helvetica 10 bold', bg="white")                             #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=1255, y=460)                                                                                                   #DISPLAYING THE LABEL
        lS19 = Label(MADRIDTAB, text="NO2 Yearly Average Was 18.25",font='Helvetica 9', bg="white")                                 #CREATING THE DATA LABEL
        lS19.place(x=1255, y=480)                                                                                                   #DISPLAYING THE LABEL
        
    MADLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(MADRIDTAB, text="Line Graphs", command=MADLINEGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(MADRIDTAB, text="Area Graphs", command=MADAREAGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(MADRIDTAB, text="Written Statistics", command=MADSTATS)                                                             #CREATING THE BUTTON THAT DISPLAYS THE WRITTEN STATISTICS FOR THE CITY
    b1.place(x=720, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=795, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=872, y=50)                                                                                                           #DISPLAYING THE YEARLY STATISTICS BUTTON
    

    
    MILANTAB = ttk.Frame(style="W.TFrame")                                                                                          #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR
    
    s1 = Label(MILANTAB, text=" ",bg="white")                                                                                       #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL                                                                                             
    l1 = Label(MILANTAB, text="COVID-19 & Air Pollution Levels - Milan", font='Helvetica 12 bold',bg="white")                       #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                       #DISPLAYING THE LABEL
    s3 = Label(MILANTAB, text=" ",bg="white")                                                                                       #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

    def MILLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")                                       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MILANTAB)                                                                         #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Milan',ax=ax)                                                        #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")                                      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")                                      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MILANTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Milan',ax=ax)                                              #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Milan\\Milan Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")                                       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MILANTAB)                                                                         #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Milan',ax=ax)                                                        #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def MILAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")                                       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MILANTAB)                                                                         #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Milan',ax=ax)                                                   #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")                                      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")                                      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MILANTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Milan',ax=ax)                                         #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Milan\\Milan Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")                                       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MILANTAB)                                                                         #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Milan',ax=ax)                                                   #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def MILSTATS():
        canvas = tk.Canvas(MILANTAB, width=1690, height=600, bg="white")                                                            #CREATING THE CANVAS FOR THE WRITTEN STATISTICS TO GO
        canvas.place(x=0, y=90)                                                                                                     #DISPLAYING THE CANVAS AND ITS LOCATION IN THE WINDOW

        lS1 = Label(MILANTAB, text="Milan 2019 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                          #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS
        lS1.place(x=145, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(MILANTAB, text="January = 40",font='Helvetica 9', bg="white")                                                   #CREATING THE JANUARY LABEL
        lS2.place(x=145, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(MILANTAB, text="February = 44",font='Helvetica 9', bg="white")                                                  #CREATING THE FEBRUARY LABEL
        lS3.place(x=145, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(MILANTAB, text="March = 34",font='Helvetica 9', bg="white")                                                     #CREATING THE MARCH LABEL
        lS4.place(x=145, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(MILANTAB, text="April = 18",font='Helvetica 9', bg="white")                                                     #CREATING THE APRIL LABEL
        lS5.place(x=145, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(MILANTAB, text="May = 14",font='Helvetica 9', bg="white")                                                       #CREATING THE MAY LABEL
        lS6.place(x=145, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(MILANTAB, text="June = 19",font='Helvetica 9', bg="white")                                                      #CREATING THE JUNE LABEL
        lS7.place(x=145, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(MILANTAB, text="July = 21",font='Helvetica 9', bg="white")                                                      #CREATING THE JULY LABEL
        lS8.place(x=145, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(MILANTAB, text="August = 19",font='Helvetica 9', bg="white")                                                    #CREATING THE AUGUST LABLE
        lS9.place(x=145, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(MILANTAB, text="September = 31",font='Helvetica 9', bg="white")                                                #CREATING THE SEPTEMBER LABEL
        lS10.place(x=145, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(MILANTAB, text="October = 33",font='Helvetica 9', bg="white")                                                  #CREATING THE OCTOBER LABEL
        lS11.place(x=145, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(MILANTAB, text="November = 31",font='Helvetica 9', bg="white")                                                 #CREATING THE NOVEMBER LABEL
        lS12.place(x=145, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(MILANTAB, text="December = 41",font='Helvetica 9', bg="white")                                                 #CREATING THE DECEMBER LABEL
        lS13.place(x=145, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(MILANTAB, text="Milan 2019 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                  #CREATING THE HIGHEST MONTHLY AVERAGE LABEL 
        lS14.place(x=145, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(MILANTAB, text="February = 44",font='Helvetica 9', bg="white")                                                 #CREATING THE DATA LABEL
        lS15.place(x=145, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(MILANTAB, text="Milan 2019 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                   #CREATING THE LOWEST MONTHLY AVERAGE LABEL  
        lS16.place(x=145, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(MILANTAB, text="May = 14",font='Helvetica 9', bg="white")                                                      #CREATING THE DATA LABEL
        lS17.place(x=145, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(MILANTAB, text="Milan 2019 Yearly Average",font='Helvetica 10 bold', bg="white")                               #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=145, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(MILANTAB, text="NO2 Yearly Average Was 28.75",font='Helvetica 9', bg="white")                                  #CREATING THE DATA LABEL
        lS19.place(x=145, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(MILANTAB, text="Milan NO2 Monthly Changes",font='Helvetica 10 bold', bg="white")                                #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS  
        lS1.place(x=700, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(MILANTAB, text="January = 4.88% INCREASE",font='Helvetica 9', bg="white")                                       #CREATING THE JANUARY LABEL
        lS2.place(x=700, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(MILANTAB, text="February = 20% DECREASE",font='Helvetica 9', bg="white")                                        #CREATING THE FEBRUARY LABEL
        lS3.place(x=700, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(MILANTAB, text="March = 22.95% DECREASE",font='Helvetica 9', bg="white")                                        #CREATING THE MARCH LABEL
        lS4.place(x=700, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(MILANTAB, text="April = 20% INCREASE",font='Helvetica 9', bg="white")                                           #CREATING THE APRIL LABEL
        lS5.place(x=700, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(MILANTAB, text="May = 40% INCREASE",font='Helvetica 9', bg="white")                                             #CREATING THE MAY LABEL
        lS6.place(x=700, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(MILANTAB, text="June = 19.05% INCREASE",font='Helvetica 9', bg="white")                                         #CREATING THE JUNE LABEL
        lS7.place(x=700, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(MILANTAB, text="July = 21.28% INCREASE",font='Helvetica 9', bg="white")                                         #CREATING THE JULY LABEL
        lS8.place(x=700, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(MILANTAB, text="August = 19.05% INCREASE",font='Helvetica 9', bg="white")                                       #CREATING THE AUGUST LABLEL
        lS9.place(x=700, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(MILANTAB, text="September = 6.25% INCREASE",font='Helvetica 9', bg="white")                                    #CREATING THE SEPTEMBER LABEL
        lS10.place(x=700, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(MILANTAB, text="October = 16.39% DECREASE",font='Helvetica 9', bg="white")                                     #CREATING THE OCTOBER LABEL
        lS11.place(x=700, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(MILANTAB, text="November = 3.28% DECREASE",font='Helvetica 9', bg="white")                                     #CREATING THE NOVEMBER LABEL
        lS12.place(x=700, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(MILANTAB, text="December = 37.68% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE DECEMBER LABEL
        lS13.place(x=700, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(MILANTAB, text="Milan's Largest Monthy Change (DECREASE)",font='Helvetica 10 bold', bg="white")                #CREATING THE HIGHEST MONTHLY CHANGE (DECREASE) LABEL  
        lS14.place(x=700, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(MILANTAB, text="December = 37.68% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE DATA LABEL
        lS15.place(x=700, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(MILANTAB, text="Milan's Largest Monthy Change (INCREASE)",font='Helvetica 10 bold', bg="white")                #CREATING THE HIGHEST MONTHLY CHANGE (INCREASE) LABEL
        lS16.place(x=700, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(BERLINTAB, text="May = 40% INCREASE",font='Helvetica 9', bg="white")                                           #CREATING THE DATA LABEL       
        lS17.place(x=700, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(MILANTAB, text="Milan Yearly Average Change",font='Helvetica 10 bold', bg="white")                             #CREATING THE YEARLY CHANGE LABEL  
        lS18.place(x=700, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(MILANTAB, text="Yearly Average Change Was A 1.75% DECREASE In NO2 Levels",font='Helvetica 9', bg="white")      #CREATING THE DATA LABEL
        lS19.place(x=700, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(MILANTAB, text="Milan 2020 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                          #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS   
        lS1.place(x=1255, y=100)                                                                                                    #DISPLAYING THE HEADING LABEL

        lS2 = Label(MILANTAB, text="January = 42",font='Helvetica 9', bg="white")                                                   #CREATING THE JANUARY LABEL
        lS2.place(x=1255, y=120)                                                                                                    #DISPLAYING THE JANUARY LABEL
        lS3 = Label(MILANTAB, text="February = 36",font='Helvetica 9', bg="white")                                                  #CREATING THE FEBRUARY LABEL
        lS3.place(x=1255, y=140)                                                                                                    #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(MILANTAB, text="March = 27",font='Helvetica 9', bg="white")                                                     #CREATING THE MARCH LABEL
        lS4.place(x=1255, y=160)                                                                                                    #DISPLAYING THE MARCH LABEL
        lS5 = Label(MILANTAB, text="April = 22",font='Helvetica 9', bg="white")                                                     #CREATING THE APRIL LABEL
        lS5.place(x=1255, y=180)                                                                                                    #DISPLAYING THE APRIL LABEL
        lS6 = Label(MILANTAB, text="May = 21",font='Helvetica 9', bg="white")                                                       #CREATING THE MAY LABEL
        lS6.place(x=1255, y=200)                                                                                                    #DISPLAYING THE MAY LABEL
        lS7 = Label(MILANTAB, text="June = 23",font='Helvetica 9', bg="white")                                                      #CREATING THE JUNE LABEL
        lS7.place(x=1255, y=220)                                                                                                    #DISPLAYING THE JUNE LABEL
        lS8 = Label(MILANTAB, text="July = 26",font='Helvetica 9', bg="white")                                                      #CREATING THE JULY LABEL
        lS8.place(x=1255, y=240)                                                                                                    #DISPLAYING THE JULY LABEL
        lS9 = Label(MILANTAB, text="August = 23",font='Helvetica 9', bg="white")                                                    #CREATING THE AUGUST LABLEL
        lS9.place(x=1255, y=260)                                                                                                    #DISPLAYING THE AUGUST LABEL
        lS10 = Label(MILANTAB, text="September = 33",font='Helvetica 9', bg="white")                                                #CREATING THE SEPTEMBER LABEL
        lS10.place(x=1255, y=280)                                                                                                   #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(MILANTAB, text="October = 28",font='Helvetica 9', bg="white")                                                  #CREATING THE OCTOBER LABEL
        lS11.place(x=1255, y=300)                                                                                                   #DISLAYING THE OCTOBER LABEL
        lS12 = Label(MILANTAB, text="November = 30",font='Helvetica 9', bg="white")                                                 #CREATING THE NOVEMBER LABEL
        lS12.place(x=1255, y=320)                                                                                                   #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(MILANTAB, text="December = 28",font='Helvetica 9', bg="white")                                                 #CREATING THE DECEMBER LABEL
        lS13.place(x=1255, y=340)                                                                                                   #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(MILANTAB, text="Milan 2020 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                  #CREATING THE HIGHEST MONTHLY AVERAGE LABEL
        lS14.place(x=1255, y=380)                                                                                                   #DISPLAYING THE LABEL
        lS15 = Label(MILANTAB, text="January = 42",font='Helvetica 9', bg="white")                                                  #CREATING THE DATA LABEL
        lS15.place(x=1255, y=400)                                                                                                   #DISPLAYING THE LABEL
                
        lS16 = Label(MILANTAB, text="Milan 2020 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                   #CREATING THE LOWEST MONTHLY AVERAGE LABEL
        lS16.place(x=1255, y=420)                                                                                                   #DISPLAYING THE LABEL
        lS17 = Label(MILANTAB, text="May = 21",font='Helvetica 9', bg="white")                                                      #CREATING THE DATA LABEL
        lS17.place(x=1255, y=440)                                                                                                   #DISPLAYING THE LABEL

        lS18 = Label(MILANTAB, text="Milan 2020 Yearly Average",font='Helvetica 10 bold', bg="white")                               #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=1255, y=460)                                                                                                   #DISPLAYING THE LABEL
        lS19 = Label(MILANTAB, text="NO2 Yearly Average Was 28.25",font='Helvetica 9', bg="white")                                  #CREATING THE DATA LABEL
        lS19.place(x=1255, y=480)                                                                                                   #DISPLAYING THE LABEL
        
    MILLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(MILANTAB, text="Line Graphs", command=MILLINEGRAPHS)                                                                #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(MILANTAB, text="Area Graphs", command=MILAREAGRAPHS)                                                                #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(MILANTAB, text="Written Statistics", command=MILSTATS)                                                              #CREATING THE BUTTON THAT DISPLAYS THE WRITTEN STATISTICS FOR THE CITY
    b1.place(x=720, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=795, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=872, y=50)                                                                                                           #DISPLAYING THE YEARLY STATISTICS BUTTON
    


    BERLINTAB = ttk.Frame(style="W.TFrame")                                                                                         #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR
                                                                                                                 
    s1 = Label(BERLINTAB, text=" ", bg="white")                                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL                                                                                                 
    l1 = Label(BERLINTAB, text="COVID-19 & Air Pollution Levels - Berlin", font='Helvetica 12 bold', bg="white")                    #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                       #DISPLAYING THE LABEL
    s3 = Label(BERLINTAB, text=" ", bg="white")                                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

    def BERLINEGRAPHS():
         
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BERLINTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Berlin',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BERLINTAB)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Berlin',ax=ax)                                             #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Berlin\\Berlin Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BERLINTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Berlin',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def BERAREAGRAPHS():
         
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BERLINTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Berlin',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BERLINTAB)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Berlin',ax=ax)                                        #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Berlin\\Berlin Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BERLINTAB)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Berlin',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def BERSTATS():
        canvas = tk.Canvas(BERLINTAB, width=1690, height=600, bg="white")                                                           #CREATING THE CANVAS FOR THE WRITTEN STATISTICS TO GO
        canvas.place(x=0, y=90)                                                                                                     #DISPLAYING THE CANVAS AND ITS LOCATION IN THE WINDOW

        lS1 = Label(BERLINTAB, text="Berlin 2019 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                        #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS 
        lS1.place(x=145, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(BERLINTAB, text="January = 23",font='Helvetica 9', bg="white")                                                  #CREATING THE JANUARY LABEL
        lS2.place(x=145, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(BERLINTAB, text="February = 29",font='Helvetica 9', bg="white")                                                 #CREATING THE FEBRUARY LABEL
        lS3.place(x=145, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(BERLINTAB, text="March = 22",font='Helvetica 9', bg="white")                                                    #CREATING THE MARCH LABEL
        lS4.place(x=145, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(BERLINTAB, text="April = 21",font='Helvetica 9', bg="white")                                                    #CREATING THE APRIL LABEL
        lS5.place(x=145, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(BERLINTAB, text="May = 21",font='Helvetica 9', bg="white")                                                      #CREATING THE MAY LABEL
        lS6.place(x=145, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(BERLINTAB, text="June = 25",font='Helvetica 9', bg="white")                                                     #CREATING THE JUNE LABEL
        lS7.place(x=145, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(BERLINTAB, text="July = 19",font='Helvetica 9', bg="white")                                                     #CREATING THE JULY LABEL
        lS8.place(x=145, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(BERLINTAB, text="August = 25",font='Helvetica 9', bg="white")                                                   #CREATING THE AUGUST LABLEL
        lS9.place(x=145, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(BERLINTAB, text="September = 23",font='Helvetica 9', bg="white")                                               #CREATING THE SEPTEMBER LABEL
        lS10.place(x=145, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(BERLINTAB, text="October = 23",font='Helvetica 9', bg="white")                                                 #CREATING THE OCTOBER LABEL
        lS11.place(x=145, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(BERLINTAB, text="November = 20",font='Helvetica 9', bg="white")                                                #CREATING THE NOVEMBER LABEL
        lS12.place(x=145, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(BERLINTAB, text="December = 22",font='Helvetica 9', bg="white")                                                #CREATING THE DECEMBER LABEL
        lS13.place(x=145, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(BERLINTAB, text="Berlin 2019 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                #CREATING THE HIGHEST MONTHLY AVERAGE LABEL  
        lS14.place(x=145, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(BERLINTAB, text="February = 29",font='Helvetica 9', bg="white")                                                #CREATING THE DATA LABEL
        lS15.place(x=145, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(BERLINTAB, text="Berlin 2019 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                 #CREATING THE LOWEST MONTHLY AVERAGE LABEL  
        lS16.place(x=145, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(BERLINTAB, text="July = 19",font='Helvetica 9', bg="white")                                                    #CREATING THE DATA LABEL
        lS17.place(x=145, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(BERLINTAB, text="Berlin 2019 Yearly Average",font='Helvetica 10 bold', bg="white")                             #CREATING THE YEARLY AVERAGE LABEL 
        lS18.place(x=145, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(BERLINTAB, text="NO2 Yearly Average Was 22.75",font='Helvetica 9', bg="white")                                 #CREATING THE DATA LABEL
        lS19.place(x=145, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(BERLINTAB, text="Berlin NO2 Monthly Changes",font='Helvetica 10 bold', bg="white")                              #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS   
        lS1.place(x=700, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(BERLINTAB, text="January On Average Had The Same NO2 Levels",font='Helvetica 9', bg="white")                    #CREATING THE JANUARY LABEL
        lS2.place(x=700, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(BERLINTAB, text="February = 36.73% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE FEBRUARY LABEL
        lS3.place(x=700, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(BERLINTAB, text="March = 4.65% DECREASE",font='Helvetica 9', bg="white")                                        #CREATING THE MARCH LABEL
        lS4.place(x=700, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(BERLINTAB, text="April = 10% DECREASE",font='Helvetica 9', bg="white")                                          #CREATING THE APRIL LABEL
        lS5.place(x=700, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(BERLINTAB, text="May = 15.38% DECREASE",font='Helvetica 9', bg="white")                                         #CREATING THE MAY LABEL
        lS6.place(x=700, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(BERLINTAB, text="June = 12.77% DECREASE",font='Helvetica 9', bg="white")                                        #CREATING THE JUNE LABEL
        lS7.place(x=700, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(BERLINTAB, text="July = 10% INCREASE",font='Helvetica 9', bg="white")                                           #CREATING THE JULY LABEL
        lS8.place(x=700, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(BERLINTAB, text="August = 17.39% DECREASE",font='Helvetica 9', bg="white")                                      #CREATING THE AUGUST LABLEL
        lS9.place(x=700, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(BERLINTAB, text="September = 4.26% INCREASE",font='Helvetica 9', bg="white")                                   #CREATING THE SEPTEMBER LABEL
        lS10.place(x=700, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(BERLINTAB, text="October = 30% DECREASE",font='Helvetica 9', bg="white")                                       #CREATING THE OCTOBER LABEL
        lS11.place(x=700, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(BERLINTAB, text="November = 10.53% DECREASE",font='Helvetica 9', bg="white")                                   #CREATING THE NOVEMBER LABEL
        lS12.place(x=700, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(BERLINTAB, text="December = 31.58% DECREASE",font='Helvetica 9', bg="white")                                   #CREATING THE DECEMBER LABEL
        lS13.place(x=700, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(BERLINTAB, text="Berlin's Largest Monthy Change (DECREASE)",font='Helvetica 10 bold', bg="white")              #CREATING THE HIGHEST MONTHLY CHANGE (DECREASE) LABEL  
        lS14.place(x=700, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(BERLINTAB, text="February = 36.73% DECREASE",font='Helvetica 9', bg="white")                                   #CREATING THE DATA LABEL
        lS15.place(x=700, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(BERLINTAB, text="Berlin's Largest Monthy Change (INCREASE)",font='Helvetica 10 bold', bg="white")              #CREATING THE HIGHEST MONTHLY CHANGE (INCREASE) LABEL  
        lS16.place(x=700, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(BERLINTAB, text="July = 10% INCREASE",font='Helvetica 9', bg="white")                                          #CREATING THE DATA LABEL   
        lS17.place(x=700, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(BERLINTAB, text="Berlin Yearly Average Change",font='Helvetica 10 bold', bg="white")                           #CREATING THE YEARLY CHANGE LABEL  
        lS18.place(x=700, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(BERLINTAB, text="Yearly Average Change Was A 12.87% DECREASE In NO2 Levels",font='Helvetica 9', bg="white")    #CREATING THE DATA LABEL
        lS19.place(x=700, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(BERLINTAB, text="Berlin 2020 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                        #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS   
        lS1.place(x=1255, y=100)                                                                                                    #DISPLAYING THE HEADING LABEL

        lS2 = Label(BERLINTAB, text="January = 23",font='Helvetica 9', bg="white")                                                  #CREATING THE JANUARY LABEL
        lS2.place(x=1255, y=120)                                                                                                    #DISPLAYING THE JANUARY LABEL
        lS3 = Label(BERLINTAB, text="February = 20",font='Helvetica 9', bg="white")                                                 #CREATING THE FEBRUARY LABEL
        lS3.place(x=1255, y=140)                                                                                                    #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(BERLINTAB, text="March = 21",font='Helvetica 9', bg="white")                                                    #CREATING THE MARCH LABEL
        lS4.place(x=1255, y=160)                                                                                                    #DISPLAYING THE MARCH LABEL
        lS5 = Label(BERLINTAB, text="April = 19",font='Helvetica 9', bg="white")                                                    #CREATING THE APRIL LABEL
        lS5.place(x=1255, y=180)                                                                                                    #DISPLAYING THE APRIL LABEL
        lS6 = Label(BERLINTAB, text="May = 18",font='Helvetica 9', bg="white")                                                      #CREATING THE MAY LABEL
        lS6.place(x=1255, y=200)                                                                                                    #DISPLAYING THE MAY LABEL
        lS7 = Label(BERLINTAB, text="June = 22 - Only 5 Data Points",font='Helvetica 9', bg="white")                                #CREATING THE JUNE LABEL
        lS7.place(x=1255, y=220)                                                                                                    #DISPLAYING THE JUNE LABEL
        lS8 = Label(BERLINTAB, text="July = 21",font='Helvetica 9', bg="white")                                                     #CREATING THE JULY LABEL
        lS8.place(x=1255, y=240)                                                                                                    #DISPLAYING THE JULY LABEL
        lS9 = Label(BERLINTAB, text="August = 21",font='Helvetica 9', bg="white")                                                   #CREATING THE AUGUST LABLEL
        lS9.place(x=1255, y=260)                                                                                                    #DISPLAYING THE AUGUST LABEL
        lS10 = Label(BERLINTAB, text="September = 24",font='Helvetica 9', bg="white")                                               #CREATING THE SEPTEMBER LABEL
        lS10.place(x=1255, y=280)                                                                                                   #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(BERLINTAB, text="October = 17",font='Helvetica 9', bg="white")                                                 #CREATING THE OCTOBER LABEL
        lS11.place(x=1255, y=300)                                                                                                   #DISLAYING THE OCTOBER LABEL
        lS12 = Label(BERLINTAB, text="November = 18",font='Helvetica 9', bg="white")                                                #CREATING THE NOVEMBER LABEL
        lS12.place(x=1255, y=320)                                                                                                   #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(BERLINTAB, text="December = 16",font='Helvetica 9', bg="white")                                                #CREATING THE DECEMBER LABEL
        lS13.place(x=1255, y=340)                                                                                                   #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(BERLINTAB, text="Berlin 2020 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                #CREATING THE HIGHEST MONTHLY AVERAGE LABEL
        lS14.place(x=1255, y=380)                                                                                                   #DISPLAYING THE LABEL
        lS15 = Label(BERLINTAB, text="September = 24",font='Helvetica 9', bg="white")                                               #CREATING THE DATA LABEL
        lS15.place(x=1255, y=400)                                                                                                   #DISPLAYING THE LABEL
        
        lS16 = Label(BERLINTAB, text="Berlin 2020 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")                 #CREATING THE LOWEST MONTHLY AVERAGE LABEL
        lS16.place(x=1255, y=420)                                                                                                   #DISPLAYING THE LABEL
        lS17 = Label(BERLINTAB, text="December = 16",font='Helvetica 9', bg="white")                                                #CREATING THE DATA LABEL
        lS17.place(x=1255, y=440)                                                                                                   #DISPLAYING THE LABEL

        lS18 = Label(BERLINTAB, text="Berlin 2020 Yearly Average",font='Helvetica 10 bold', bg="white")                             #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=1255, y=460)                                                                                                   #DISPLAYING THE LABEL
        lS19 = Label(BERLINTAB, text="NO2 Yearly Average Was 20",font='Helvetica 9', bg="white")                                    #CREATING THE DATA LABEL
        lS19.place(x=1255, y=480)                                                                                                   #DISPLAYING THE LABEL
        
    BERLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(BERLINTAB, text="Line Graphs", command=BERLINEGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(BERLINTAB, text="Area Graphs", command=BERAREAGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(BERLINTAB, text="Written Statistics", command=BERSTATS)                                                             #CREATING THE BUTTON THAT DISPLAYS THE WRITTEN STATISTICS FOR THE CITY
    b1.place(x=720, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=795, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=872, y=50)                                                                                                           #DISPLAYING THE YEARLY STATISTICS BUTTON



    BARCELONATAB = ttk.Frame(style="W.TFrame")                                                                                      #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(BARCELONATAB, text=" ",bg="white")                                                                                   #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL                                                                                                   
    l1 = Label(BARCELONATAB, text="COVID-19 & Air Pollution Levels - Barcelona", font='Helvetica 12 bold',bg="white")               #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                       #DISPLAYING THE LABEL
    s3 = Label(BARCELONATAB, text=" ",bg="white")                                                                                   #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

    def BARLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BARCELONATAB)                                                                     #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Barcelona',ax=ax)                                                    #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BARCELONATAB)                                                                    #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Barcelona',ax=ax)                                          #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Barcelona\\Barcelona Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                       #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BARCELONATAB)                                                                     #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Barcelona',ax=ax)                                                    #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def BARAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BARCELONATAB)                                                                     #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Barcelona',ax=ax)                                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BARCELONATAB)                                                                    #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Barcelona',ax=ax)                                     #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Barcelona\\Barcelona Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                       #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BARCELONATAB)                                                                     #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Barcelona',ax=ax)                                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def BARSTATS():
        canvas = tk.Canvas(BARCELONATAB, width=1690, height=600, bg="white")                                                        #CREATING THE CANVAS FOR THE WRITTEN STATISTICS TO GO
        canvas.place(x=0, y=90)                                                                                                     #DISPLAYING THE CANVAS AND ITS LOCATION IN THE WINDOW

        lS1 = Label(BARCELONATAB, text="Barcelona 2019 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                  #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS 
        lS1.place(x=145, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(BARCELONATAB, text="January = 20",font='Helvetica 9', bg="white")                                               #CREATING THE JANUARY LABEL
        lS2.place(x=145, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(BARCELONATAB, text="February = 23",font='Helvetica 9', bg="white")                                              #CREATING THE FEBRUARY LABEL
        lS3.place(x=145, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(BARCELONATAB, text="March = 19",font='Helvetica 9', bg="white")                                                 #CREATING THE MARCH LABEL
        lS4.place(x=145, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(BARCELONATAB, text="April = 14",font='Helvetica 9', bg="white")                                                 #CREATING THE APRIL LABEL
        lS5.place(x=145, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(BARCELONATAB, text="May = 17",font='Helvetica 9', bg="white")                                                   #CREATING THE MAY LABEL
        lS6.place(x=145, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(BARCELONATAB, text="June = 17",font='Helvetica 9', bg="white")                                                  #CREATING THE JUNE LABEL
        lS7.place(x=145, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(BARCELONATAB, text="July = 16",font='Helvetica 9', bg="white")                                                  #CREATING THE JULY LABEL
        lS8.place(x=145, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(BARCELONATAB, text="August = 13",font='Helvetica 9', bg="white")                                                #CREATING THE AUGUST LABLE
        lS9.place(x=145, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(BARCELONATAB, text="September = 15",font='Helvetica 9', bg="white")                                            #CREATING THE SEPTEMBER LABEL
        lS10.place(x=145, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(BARCELONATAB, text="October = 18",font='Helvetica 9', bg="white")                                              #CREATING THE OCTOBER LABEL
        lS11.place(x=145, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(BARCELONATAB, text="November = 16",font='Helvetica 9', bg="white")                                             #CREATING THE NOVEMBER LABEL
        lS12.place(x=145, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(BARCELONATAB, text="December = 18",font='Helvetica 9', bg="white")                                             #CREATING THE DECEMBER LABEL
        lS13.place(x=145, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(BARCELONATAB, text="Barcelona 2019 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")          #CREATING THE HIGHEST MONTHLY AVERAGE LABEL  
        lS14.place(x=145, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(BARCELONATAB, text="February = 23",font='Helvetica 9', bg="white")                                             #CREATING THE DATA LABEL
        lS15.place(x=145, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(BARCELONATAB, text="Barcelona 2019 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")           #CREATING THE LOWEST MONTHLY AVERAGE LABEL  
        lS16.place(x=145, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(BARCELONATAB, text="August = 13",font='Helvetica 9', bg="white")                                               #CREATING THE DATA LABEL
        lS17.place(x=145, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(BARCELONATAB, text="Barcelona 2019 Yearly Average",font='Helvetica 10 bold', bg="white")                       #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=145, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(BARCELONATAB, text="NO2 Yearly Average Was 17.17",font='Helvetica 9', bg="white")                              #CREATING THE DATA LABEL
        lS19.place(x=145, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(BARCELONATAB, text="Barcelona NO2 Monthly Changes",font='Helvetica 10 bold', bg="white")                        #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS  
        lS1.place(x=700, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(BARCELONATAB, text="January On Average Had The Same NO2 Levels",font='Helvetica 9', bg="white")                 #CREATING THE JANUARY LABEL
        lS2.place(x=700, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(BARCELONATAB, text="February = 13.95% DECREASE",font='Helvetica 9', bg="white")                                 #CREATING THE FEBRUARY LABEL
        lS3.place(x=700, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(BARCELONATAB, text="March = 53.33% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE MARCH LABEL
        lS4.place(x=700, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(BARCELONATAB, text="April = 54.55% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE APRIL LABEL
        lS5.place(x=700, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(BARCELONATAB, text="May = 51.85% DECREASE",font='Helvetica 9', bg="white")                                      #CREATING THE MAY LABEL
        lS6.place(x=700, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(BARCELONATAB, text="June = 51.85% DECREASE",font='Helvetica 9', bg="white")                                     #CREATING THE JUNE LABEL
        lS7.place(x=700, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(BARCELONATAB, text="July = 37.04% DECREASE",font='Helvetica 9', bg="white")                                     #CREATING THE JULY LABEL
        lS8.place(x=700, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(BARCELONATAB, text="August = 26.09% DECREASE",font='Helvetica 9', bg="white")                                   #CREATING THE AUGUST LABLEL
        lS9.place(x=700, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(BARCELONATAB, text="September On Average Had The Same NO2 Levels",font='Helvetica 9', bg="white")              #CREATING THE SEPTEMBER LABEL
        lS10.place(x=700, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(BARCELONATAB, text="October = 11.76% DECREASE",font='Helvetica 9', bg="white")                                 #CREATING THE OCTOBER LABEL
        lS11.place(x=700, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(BARCELONATAB, text="November = 6.06% INCREASE",font='Helvetica 9', bg="white")                                 #CREATING THE NOVEMBER LABEL
        lS12.place(x=700, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(BARCELONATAB, text="December = 18.18% DECREASE",font='Helvetica 9', bg="white")                                #CREATING THE DECEMBER LABEL
        lS13.place(x=700, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(BARCELONATAB, text="Barcelona's Largest Monthy Change (DECREASE)",font='Helvetica 10 bold', bg="white")        #CREATING THE HIGHEST MONTHLY CHANGE (DECREASE) LABEL  
        lS14.place(x=700, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(BARCELONATAB, text="April = 54.55% DECREASE",font='Helvetica 9', bg="white")                                   #CREATING THE DATA LABEL
        lS15.place(x=700, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(BARCELONATAB, text="Barcelona's Largest Monthy Change (INCREASE)",font='Helvetica 10 bold', bg="white")        #CREATING THE HIGHEST MONTHLY CHANGE (INCREASE) LABEL  
        lS16.place(x=700, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(BARCELONATAB, text="November = 6.06% INCREASE",font='Helvetica 9', bg="white")                                 #CREATING THE DATA LABEL
        lS17.place(x=700, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(BARCELONATAB, text="Barcelona Yearly Average Change",font='Helvetica 10 bold', bg="white")                     #CREATING THE YEARLY CHANGE LABEL 
        lS18.place(x=700, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(BARCELONATAB, text="Yearly Average Change Was A 23.35% DECREASE In NO2 Levels",font='Helvetica 9', bg="white") #CREATING THE DATA LABEL
        lS19.place(x=700, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(BARCELONATAB, text="Barcelona 2020 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                  #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS   
        lS1.place(x=1255, y=100)                                                                                                    #DISPLAYING THE HEADING LABEL

        lS2 = Label(BARCELONATAB, text="January = 20",font='Helvetica 9', bg="white")                                               #CREATING THE JANUARY LABEL
        lS2.place(x=1255, y=120)                                                                                                    #DISPLAYING THE JANUARY LABEL
        lS3 = Label(BARCELONATAB, text="February = 20",font='Helvetica 9', bg="white")                                              #CREATING THE FEBRUARY LABEL
        lS3.place(x=1255, y=140)                                                                                                    #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(BARCELONATAB, text="March = 11",font='Helvetica 9', bg="white")                                                 #CREATING THE MARCH LABEL
        lS4.place(x=1255, y=160)                                                                                                    #DISPLAYING THE MARCH LABEL
        lS5 = Label(BARCELONATAB, text="April = 8",font='Helvetica 9', bg="white")                                                  #CREATING THE APRIL LABEL
        lS5.place(x=1255, y=180)                                                                                                    #DISPLAYING THE APRIL LABEL
        lS6 = Label(BARCELONATAB, text="May = 10",font='Helvetica 9', bg="white")                                                   #CREATING THE MAY LABEL
        lS6.place(x=1255, y=200)                                                                                                    #DISPLAYING THE MAY LABEL
        lS7 = Label(BARCELONATAB, text="June = 10",font='Helvetica 9', bg="white")                                                  #CREATING THE JUNE LABEL
        lS7.place(x=1255, y=220)                                                                                                    #DISPLAYING THE JUNE LABEL
        lS8 = Label(BARCELONATAB, text="July = 11",font='Helvetica 9', bg="white")                                                  #CREATING THE JULY LABEL
        lS8.place(x=1255, y=240)                                                                                                    #DISPLAYING THE JULY LABEL
        lS9 = Label(BARCELONATAB, text="August = 10",font='Helvetica 9', bg="white")                                                #CREATING THE AUGUST LABLEL
        lS9.place(x=1255, y=260)                                                                                                    #DISPLAYING THE AUGUST LABEL
        lS10 = Label(BARCELONATAB, text="September = 15",font='Helvetica 9', bg="white")                                            #CREATING THE SEPTEMBER LABEL
        lS10.place(x=1255, y=280)                                                                                                   #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(BARCELONATAB, text="October = 16",font='Helvetica 9', bg="white")                                              #CREATING THE OCTOBER LABEL
        lS11.place(x=1255, y=300)                                                                                                   #DISLAYING THE OCTOBER LABEL
        lS12 = Label(BARCELONATAB, text="November = 17",font='Helvetica 9', bg="white")                                             #CREATING THE NOVEMBER LABEL
        lS12.place(x=1255, y=320)                                                                                                   #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(BARCELONATAB, text="December = 15",font='Helvetica 9', bg="white")                                             #CREATING THE DECEMBER LABEL
        lS13.place(x=1255, y=340)                                                                                                   #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(BARCELONATAB, text="Barcelona 2020 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")          #CREATING THE HIGHEST MONTHLY AVERAGE LABEL
        lS14.place(x=1255, y=380)                                                                                                   #DISPLAYING THE LABEL 
        lS15 = Label(BARCELONATAB, text="January = 20 / February = 20",font='Helvetica 9', bg="white")                              #CREATING THE DATA LABEL
        lS15.place(x=1255, y=400)                                                                                                   #DISPLAYING THE LABEL
        
        lS16 = Label(BARCELONATAB, text="Barcelona 2020 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")           #CREATING THE LOWEST MONTHLY AVERAGE LABEL
        lS16.place(x=1255, y=420)                                                                                                   #DISPLAYING THE LABEL
        lS17 = Label(BARCELONATAB, text="April = 8",font='Helvetica 9', bg="white")                                                 #CREATING THE DATA LABEL
        lS17.place(x=1255, y=440)                                                                                                   #DISPLAYING THE LABEL

        lS18 = Label(BARCELONATAB, text="Barcelona 2020 Yearly Average",font='Helvetica 10 bold', bg="white")                       #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=1255, y=460)                                                                                                   #DISPLAYING THE LABEL
        lS19 = Label(BARCELONATAB, text="NO2 Yearly Average Was 13.58",font='Helvetica 9', bg="white")                              #CREATING THE DATA LABEL
        lS19.place(x=1255, y=480)                                                                                                   #DISPLAYING THE LABEL
        
    BARLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(BARCELONATAB, text="Line Graphs", command=BARLINEGRAPHS)                                                            #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(BARCELONATAB, text="Area Graphs", command=BARAREAGRAPHS)                                                            #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(BARCELONATAB, text="Written Statistics", command=BARSTATS)                                                          #CREATING THE BUTTON THAT DISPLAYS THE WRITTEN STATISTICS FOR THE CITY
    b1.place(x=720, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=795, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=872, y=50)                                                                                                           #DISPLAYING THE YEARLY STATISTICS BUTTON



    AMSTERDAMTAB = ttk.Frame(style="W.TFrame")                                                                                      #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(AMSTERDAMTAB, text=" ",bg="white")                                                                                   #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL                                                                                                    
    l1 = Label(AMSTERDAMTAB, text="COVID-19 & Air Pollution Levels - Amsterdam", font='Helvetica 12 bold',bg="white")               #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                       #DISPLAYING THE LABEL
    s3 = Label(AMSTERDAMTAB, text=" ",bg="white")                                                                                   #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

    def AMSLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, AMSTERDAMTAB)                                                                     #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Amsterdam',ax=ax)                                                    #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, AMSTERDAMTAB)                                                                    #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Amsterdam',ax=ax)                                          #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Amsterdam\\Amsterdam Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                       #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, AMSTERDAMTAB)                                                                     #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Amsterdam',ax=ax)                                                    #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def AMSAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, AMSTERDAMTAB)                                                                     #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Amsterdam',ax=ax)                                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, AMSTERDAMTAB)                                                                    #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Amsterdam',ax=ax)                                     #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Amsterdam\\Amsterdam Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                       #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, AMSTERDAMTAB)                                                                     #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Amsterdam',ax=ax)                                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def AMSSTATS():
        canvas = tk.Canvas(AMSTERDAMTAB, width=1690, height=600, bg="white")                                                        #CREATING THE CANVAS FOR THE WRITTEN STATISTICS TO GO
        canvas.place(x=0, y=90)                                                                                                     #DISPLAYING THE CANVAS AND ITS LOCATION IN THE WINDOW

        lS1 = Label(AMSTERDAMTAB, text="Amsterdam 2019 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                  #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS 
        lS1.place(x=145, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(AMSTERDAMTAB, text="January = 22",font='Helvetica 9', bg="white")                                               #CREATING THE JANUARY LABEL
        lS2.place(x=145, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(AMSTERDAMTAB, text="February = 27",font='Helvetica 9', bg="white")                                              #CREATING THE FEBRUARY LABEL
        lS3.place(x=145, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(AMSTERDAMTAB, text="March = 19",font='Helvetica 9', bg="white")                                                 #CREATING THE MARCH LABEL
        lS4.place(x=145, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(AMSTERDAMTAB, text="April = 22",font='Helvetica 9', bg="white")                                                 #CREATING THE APRIL LABEL
        lS5.place(x=145, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(AMSTERDAMTAB, text="May = 17",font='Helvetica 9', bg="white")                                                   #CREATING THE MAY LABEL
        lS6.place(x=145, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(AMSTERDAMTAB, text="June = 20",font='Helvetica 9', bg="white")                                                  #CREATING THE JUNE LABEL
        lS7.place(x=145, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(AMSTERDAMTAB, text="July = 17",font='Helvetica 9', bg="white")                                                  #CREATING THE JULY LABEL
        lS8.place(x=145, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(AMSTERDAMTAB, text="August = 19",font='Helvetica 9', bg="white")                                                #CREATING THE AUGUST LABLE
        lS9.place(x=145, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(AMSTERDAMTAB, text="September = 17",font='Helvetica 9', bg="white")                                            #CREATING THE SEPTEMBER LABEL
        lS10.place(x=145, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(AMSTERDAMTAB, text="October = 20",font='Helvetica 9', bg="white")                                              #CREATING THE OCTOBER LABEL
        lS11.place(x=145, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(AMSTERDAMTAB, text="November = 23",font='Helvetica 9', bg="white")                                             #CREATING THE NOVEMBER LABEL
        lS12.place(x=145, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(AMSTERDAMTAB, text="December = 20",font='Helvetica 9', bg="white")                                             #CREATING THE DECEMBER LABEL
        lS13.place(x=145, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(AMSTERDAMTAB, text="Amsterdam 2019 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")          #CREATING THE HIGHEST MONTHLY AVERAGE LABEL  
        lS14.place(x=145, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(AMSTERDAMTAB, text="February = 27",font='Helvetica 9', bg="white")                                             #CREATING THE DATA LABEL
        lS15.place(x=145, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(AMSTERDAMTAB, text="Amsterdam 2019 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")           #CREATING THE LOWEST MONTHLY AVERAGE LABEL  
        lS16.place(x=145, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(AMSTERDAMTAB, text="May = 17 / July = 17 / September = 17",font='Helvetica 9', bg="white")                     #CREATING THE DATA LABEL
        lS17.place(x=145, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(AMSTERDAMTAB, text="Amsterdam 2019 Yearly Average",font='Helvetica 10 bold', bg="white")                       #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=145, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(AMSTERDAMTAB, text="NO2 Yearly Average Was 20.21",font='Helvetica 9', bg="white")                              #CREATING THE DATA LABEL
        lS19.place(x=145, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(AMSTERDAMTAB, text="Amsterdam NO2 Monthly Changes",font='Helvetica 10 bold', bg="white")                        #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS   
        lS1.place(x=700, y=100)                                                                                                     #DISPLAYING THE HEADING LABEL

        lS2 = Label(AMSTERDAMTAB, text="January = 14.63% DECREASE",font='Helvetica 9', bg="white")                                  #CREATING THE JANUARY LABEL
        lS2.place(x=700, y=120)                                                                                                     #DISPLAYING THE JANUARY LABEL
        lS3 = Label(AMSTERDAMTAB, text="February = 57.14% DECREASE",font='Helvetica 9', bg="white")                                 #CREATING THE FEBRUARY LABEL
        lS3.place(x=700, y=140)                                                                                                     #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(AMSTERDAMTAB, text="March = 17.14% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE MARCH LABEL
        lS4.place(x=700, y=160)                                                                                                     #DISPLAYING THE MARCH LABEL
        lS5 = Label(AMSTERDAMTAB, text="April = 31.58% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE APRIL LABEL
        lS5.place(x=700, y=180)                                                                                                     #DISPLAYING THE APRIL LABEL
        lS6 = Label(AMSTERDAMTAB, text="May = 12.5% DECREASE",font='Helvetica 9', bg="white")                                       #CREATING THE MAY LABEL
        lS6.place(x=700, y=200)                                                                                                     #DISPLAYING THE MAY LABEL
        lS7 = Label(AMSTERDAMTAB, text="June = 22.22% DECREASE",font='Helvetica 9', bg="white")                                     #CREATING THE JUNE LABEL
        lS7.place(x=700, y=220)                                                                                                     #DISPLAYING THE JUNE LABEL
        lS8 = Label(AMSTERDAMTAB, text="July = 26.67% DECREASE",font='Helvetica 9', bg="white")                                     #CREATING THE JULY LABEL
        lS8.place(x=700, y=240)                                                                                                     #DISPLAYING THE JULY LABEL
        lS9 = Label(AMSTERDAMTAB, text="August = 5.40% DECREASE",font='Helvetica 9', bg="white")                                    #CREATING THE AUGUST LABLEL
        lS9.place(x=700, y=260)                                                                                                     #DISPLAYING THE AUGUST LABEL
        lS10 = Label(AMSTERDAMTAB, text="September = 16.22% INCREASE",font='Helvetica 9', bg="white")                               #CREATING THE SEPTEMBER LABEL
        lS10.place(x=700, y=280)                                                                                                    #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(AMSTERDAMTAB, text="October = 16.22% DECREASE",font='Helvetica 9', bg="white")                                 #CREATING THE OCTOBER LABEL
        lS11.place(x=700, y=300)                                                                                                    #DISLAYING THE OCTOBER LABEL
        lS12 = Label(AMSTERDAMTAB, text="November = 13.95% DECREASE",font='Helvetica 9', bg="white")                                #CREATING THE NOVEMBER LABEL
        lS12.place(x=700, y=320)                                                                                                    #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(AMSTERDAMTAB, text="December = 5.13% DECREASE",font='Helvetica 9', bg="white")                                 #CREATING THE DECEMBER LABEL
        lS13.place(x=700, y=340)                                                                                                    #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(AMSTERDAMTAB, text="Amsterdam's Largest Monthy Change (DECREASE)",font='Helvetica 10 bold', bg="white")        #CREATING THE HIGHEST MONTHLY CHANGE (DECREASE) LABEL  
        lS14.place(x=700, y=380)                                                                                                    #DISPLAYING THE LABEL
        lS15 = Label(AMSTERDAMTAB, text="February = 57.14% DECREASE",font='Helvetica 9', bg="white")                                #CREATING THE DATA LABEL
        lS15.place(x=700, y=400)                                                                                                    #DISPLAYING THE LABEL
        
        lS16 = Label(AMSTERDAMTAB, text="Amsterdam's Largest Monthy Change (INCREASE)",font='Helvetica 10 bold', bg="white")        #CREATING THE HIGHEST MONTHLY CHANGE (INCREASE) LABEL  
        lS16.place(x=700, y=420)                                                                                                    #DISPLAYING THE LABEL
        lS17 = Label(AMSTERDAMTAB, text="September = 16.22% INCREASE",font='Helvetica 9', bg="white")                               #CREATING THE DATA LABEL
        lS17.place(x=700, y=440)                                                                                                    #DISPLAYING THE LABEL

        lS18 = Label(AMSTERDAMTAB, text="Amsterdam Yearly Average Change",font='Helvetica 10 bold', bg="white")                     #CREATING THE YEARLY CHANGE LABEL
        lS18.place(x=700, y=460)                                                                                                    #DISPLAYING THE LABEL
        lS19 = Label(AMSTERDAMTAB, text="Yearly Average Change Was A 17.25% DECREASE In NO2 Levels",font='Helvetica 9', bg="white") #CREATING THE DATA LABEL
        lS19.place(x=700, y=480)                                                                                                    #DISPLAYING THE LABEL


        lS1 = Label(AMSTERDAMTAB, text="Amsterdam 2020 NO2 Monthly Averages",font='Helvetica 10 bold', bg="white")                  #CREATING A LABEL THAT WILL ACT AS THE HEADING FOR THE WRITTEN STATISTICS   
        lS1.place(x=1255, y=100)                                                                                                    #DISPLAYING THE HEADING LABEL

        lS2 = Label(AMSTERDAMTAB, text="January = 19",font='Helvetica 9', bg="white")                                               #CREATING THE JANUARY LABEL
        lS2.place(x=1255, y=120)                                                                                                    #DISPLAYING THE JANUARY LABEL
        lS3 = Label(AMSTERDAMTAB, text="February = 15",font='Helvetica 9', bg="white")                                              #CREATING THE FEBRUARY LABEL
        lS3.place(x=1255, y=140)                                                                                                    #DISPLAYING THE FEBRUARY LABEL
        lS4 = Label(AMSTERDAMTAB, text="March = 16",font='Helvetica 9', bg="white")                                                 #CREATING THE MARCH LABEL
        lS4.place(x=1255, y=160)                                                                                                    #DISPLAYING THE MARCH LABEL
        lS5 = Label(AMSTERDAMTAB, text="April = 16",font='Helvetica 9', bg="white")                                                 #CREATING THE APRIL LABEL
        lS5.place(x=1255, y=180)                                                                                                    #DISPLAYING THE APRIL LABEL
        lS6 = Label(AMSTERDAMTAB, text="May = 15",font='Helvetica 9', bg="white")                                                   #CREATING THE MAY LABEL
        lS6.place(x=1255, y=200)                                                                                                    #DISPLAYING THE MAY LABEL
        lS7 = Label(AMSTERDAMTAB, text="June = 16",font='Helvetica 9', bg="white")                                                  #CREATING THE JUNE LABEL
        lS7.place(x=1255, y=220)                                                                                                    #DISPLAYING THE JUNE LABEL
        lS8 = Label(AMSTERDAMTAB, text="July = 13",font='Helvetica 9', bg="white")                                                  #CREATING THE JULY LABEL
        lS8.place(x=1255, y=240)                                                                                                    #DISPLAYING THE JULY LABEL
        lS9 = Label(AMSTERDAMTAB, text="August = 18",font='Helvetica 9', bg="white")                                                #CREATING THE AUGUST LABLEL
        lS9.place(x=1255, y=260)                                                                                                    #DISPLAYING THE AUGUST LABEL
        lS10 = Label(AMSTERDAMTAB, text="September = 20",font='Helvetica 9', bg="white")                                            #CREATING THE SEPTEMBER LABEL
        lS10.place(x=1255, y=280)                                                                                                   #DISPLAYING THE SEPTEMBER LABEL
        lS11 = Label(AMSTERDAMTAB, text="October = 17",font='Helvetica 9', bg="white")                                              #CREATING THE OCTOBER LABEL
        lS11.place(x=1255, y=300)                                                                                                   #DISLAYING THE OCTOBER LABEL
        lS12 = Label(AMSTERDAMTAB, text="November = 20",font='Helvetica 9', bg="white")                                             #CREATING THE NOVEMBER LABEL
        lS12.place(x=1255, y=320)                                                                                                   #DISPLAYING THE NOVEMBER LABEL
        lS13 = Label(AMSTERDAMTAB, text="December = 19",font='Helvetica 9', bg="white")                                             #CREATING THE DECEMBER LABEL
        lS13.place(x=1255, y=340)                                                                                                   #DISPLAYING THE DECEMBER LABEL

        lS14 = Label(AMSTERDAMTAB, text="Amsterdam 2020 Highest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")          #CREATING THE HIGHEST MONTHLY AVERAGE LABEL
        lS14.place(x=1255, y=380)                                                                                                   #DISPLAYING THE LABEL
        lS15 = Label(AMSTERDAMTAB, text="September = 20 / November = 20",font='Helvetica 9', bg="white")                            #CREATING THE DATA LABEL
        lS15.place(x=1255, y=400)                                                                                                   #DISPLAYING THE LABEL
        
        lS16 = Label(AMSTERDAMTAB, text="Amsterdam 2020 Lowest NO2 Monthly Average",font='Helvetica 10 bold', bg="white")           #CREATING THE LOWEST MONTHLY AVERAGE LABEL
        lS16.place(x=1255, y=420)                                                                                                   #DISPLAYING THE LABEL
        lS17 = Label(AMSTERDAMTAB, text="July = 13",font='Helvetica 9', bg="white")                                                 #CREATING THE DATA LABEL
        lS17.place(x=1255, y=440)                                                                                                   #DISPLAYING THE LABEL

        lS18 = Label(AMSTERDAMTAB, text="Amsterdam 2020 Yearly Average",font='Helvetica 10 bold', bg="white")                       #CREATING THE YEARLY AVERAGE LABEL  
        lS18.place(x=1255, y=460)                                                                                                   #DISPLAYING THE LABEL
        lS19 = Label(AMSTERDAMTAB, text="NO2 Yearly Average Was 17",font='Helvetica 9', bg="white")                                 #CREATING THE DATA LABEL
        lS19.place(x=1255, y=480)                                                                                                   #DISPLAYING THE LABEL
        
    AMSLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(AMSTERDAMTAB, text="Line Graphs", command=AMSLINEGRAPHS)                                                            #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(AMSTERDAMTAB, text="Area Graphs", command=AMSAREAGRAPHS)                                                            #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(AMSTERDAMTAB, text="Written Statistics", command=AMSSTATS)                                                          #CREATING THE BUTTON THAT DISPLAYS THE WRITTEN STATISTICS FOR THE CITY
    b1.place(x=720, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=795, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=872, y=50)                                                                                                           #DISPLAYING THE YEARLY STATISTICS BUTTON


    MAPTAB = ttk.Frame()                                                                                                            #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(MAPTAB, text=" ")                                                                                                    #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL                                                                                                
    l1 = Label(MAPTAB, text="COVID-19 & Air Pollution Levels - European Map", font='Helvetica 12 bold')                             #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                       #DISPLAYING THE LABEL
    s2 = Label(MAPTAB, text=" ")                                                                                                    #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL
    
    def MAPVIEW():
        def London():
            LONDON = Tk()                                                                                                                   #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

            s1 = Label(LONDON, text=" ", bg="white")                                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
            s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL
            l1 = Label(LONDON, text="COVID-19 & Air Pollution Levels - London", font='Helvetica 12 bold', bg="white")                       #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
            l1.pack()                                                                                                                       #DISPLAYING THE LABEL
            s3 = Label(LONDON, text=" ", bg="white")                                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
            s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

            LONDON.resizable(0,0)                                                                                                           #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
            LONDON.resizable(width=FALSE, height=FALSE)                                                                                     #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
            LONDON.title("COVID-19 APL - London")                                                                                           #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
            LONDON.geometry("1690x600")                                                                                                     #GENERATING THE SIZE OF THE WINDOW 
            LONDON.configure(background='white')                                                                                            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

            def LONLINEGRAPHS():
        
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, LONDON)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - London',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, LONDON)                                                                          #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - London',ax=ax)                                             #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('London\\London Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, LONDON)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot(color='#3498db', title='NO2 Levels In 2020 - London',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
                
            def LONAREAGRAPHS():
                
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, LONDON)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - London',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, LONDON)                                                                          #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - London',ax=ax)                                        #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('London\\London Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, LONDON)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - London',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

            LONLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
            b1 = Button(LONDON, text="Line Graphs", command=LONLINEGRAPHS)                                                                  #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
            b2 = Button(LONDON, text="Area Graphs", command=LONAREAGRAPHS)                                                                  #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
            b1.place(x=760, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
            b2.place(x=835, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON

            
        def Madrid():
            MADRID = Tk()                                                                                                                   #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

            s1 = Label(MADRID, text=" ", bg="white")                                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
            s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL
            l1 = Label(MADRID, text="COVID-19 & Air Pollution Levels - Madrid", font='Helvetica 12 bold', bg="white")                       #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
            l1.pack()                                                                                                                       #DISPLAYING THE LABEL
            s3 = Label(MADRID, text=" ", bg="white")                                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
            s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

            MADRID.resizable(0,0)                                                                                                           #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
            MADRID.resizable(width=FALSE, height=FALSE)                                                                                     #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
            MADRID.title("COVID-19 APL - Madrid")                                                                                           #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
            MADRID.geometry("1690x600")                                                                                                     #GENERATING THE SIZE OF THE WINDOW 
            MADRID.configure(background='white')                                                                                            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

            def MADLINEGRAPHS():
        
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, MADRID)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Madrid',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, MADRID)                                                                          #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Madrid',ax=ax)                                             #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Madrid\\Madrid Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, MADRID)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot(color='#3498db', title='NO2 Levels In 2020 - Madrid',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
                
            def MADAREAGRAPHS():
                
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, MADRID)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Madrid',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, MADRID)                                                                          #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Madrid',ax=ax)                                        #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Madrid\\Madrid Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, MADRID)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Madrid',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

            MADLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
            b1 = Button(MADRID, text="Line Graphs", command=MADLINEGRAPHS)                                                                  #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
            b2 = Button(MADRID, text="Area Graphs", command=MADAREAGRAPHS)                                                                  #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
            b1.place(x=760, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
            b2.place(x=835, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
            

            
        def Milan():
            MILAN = Tk()                                                                                                                    #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

            s1 = Label(MILAN, text=" ", bg="white")                                                                                         #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
            s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL
            l1 = Label(MILAN, text="COVID-19 & Air Pollution Levels - Milan", font='Helvetica 12 bold', bg="white")                         #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
            l1.pack()                                                                                                                       #DISPLAYING THE LABEL
            s3 = Label(MILAN, text=" ", bg="white")                                                                                         #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
            s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

            MILAN.resizable(0,0)                                                                                                            #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
            MILAN.resizable(width=FALSE, height=FALSE)                                                                                      #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
            MILAN.title("COVID-19 APL - Milan")                                                                                             #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
            MILAN.geometry("1690x600")                                                                                                      #GENERATING THE SIZE OF THE WINDOW 
            MILAN.configure(background='white')                                                                                             #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

            def MILLINEGRAPHS():
        
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")                                       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, MILAN)                                                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Milan',ax=ax)                                                        #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")                                      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")                                      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, MILAN)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Milan',ax=ax)                                              #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Milan\\Milan Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")                                       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, MILAN)                                                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot(color='#3498db', title='NO2 Levels In 2020 - Milan',ax=ax)                                                        #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
                
            def MILAREAGRAPHS():
                
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")                                       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, MILAN)                                                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Milan',ax=ax)                                                   #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")                                      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")                                      #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, MILAN)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Milan',ax=ax)                                         #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Milan\\Milan Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")                                       #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, MILAN)                                                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Milan',ax=ax)                                                   #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

            MILLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
            b1 = Button(MILAN, text="Line Graphs", command=MILLINEGRAPHS)                                                                   #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
            b2 = Button(MILAN, text="Area Graphs", command=MILAREAGRAPHS)                                                                   #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
            b1.place(x=760, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
            b2.place(x=835, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
            
        def Berlin():
            BERLIN = Tk()                                                                                                                   #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

            s1 = Label(BERLIN, text=" ", bg="white")                                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
            s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL
            l1 = Label(BERLIN, text="COVID-19 & Air Pollution Levels - Berlin", font='Helvetica 12 bold', bg="white")                       #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
            l1.pack()                                                                                                                       #DISPLAYING THE LABEL
            s3 = Label(BERLIN, text=" ", bg="white")                                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
            s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL


            BERLIN.resizable(0,0)                                                                                                           #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
            BERLIN.resizable(width=FALSE, height=FALSE)                                                                                     #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
            BERLIN.title("COVID-19 APL - Berlin")                                                                                           #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
            BERLIN.geometry("1690x600")                                                                                                     #GENERATING THE SIZE OF THE WINDOW 
            BERLIN.configure(background='white')                                                                                            #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

            def BERLINEGRAPHS():
     
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, BERLIN)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Berlin',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, BERLIN)                                                                          #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Berlin',ax=ax)                                             #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Berlin\\Berlin Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, BERLIN)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot(color='#3498db', title='NO2 Levels In 2020 - Berlin',ax=ax)                                                       #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
                
            def BERAREAGRAPHS():
                 
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, BERLIN)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Berlin',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")                                    #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, BERLIN)                                                                          #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Berlin',ax=ax)                                        #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Berlin\\Berlin Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                             #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")                                     #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, BERLIN)                                                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Berlin',ax=ax)                                                  #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

            BERLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
            b1 = Button(BERLIN, text="Line Graphs", command=BERLINEGRAPHS)                                                                  #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
            b2 = Button(BERLIN, text="Area Graphs", command=BERAREAGRAPHS)                                                                  #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
            b1.place(x=760, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
            b2.place(x=835, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON

        def Barcelona():
            BARCELONA = Tk()                                                                                                                #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

            s1 = Label(BARCELONA, text=" ", bg="white")                                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
            s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL
            l1 = Label(BARCELONA, text="COVID-19 & Air Pollution Levels - Barcelona", font='Helvetica 12 bold', bg="white")                 #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
            l1.pack()                                                                                                                       #DISPLAYING THE LABEL
            s3 = Label(BARCELONA, text=" ", bg="white")                                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
            s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

            BARCELONA.resizable(0,0)                                                                                                        #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
            BARCELONA.resizable(width=FALSE, height=FALSE)                                                                                  #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
            BARCELONA.title("COVID-19 APL - Barcelona")                                                                                     #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
            BARCELONA.geometry("1690x600")                                                                                                  #GENERATING THE SIZE OF THE WINDOW 
            BARCELONA.configure(background='white')                                                                                         #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 

            def BARLINEGRAPHS():
        
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, BARCELONA)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Barcelona',ax=ax)                                                    #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, BARCELONA)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Barcelona',ax=ax)                                          #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Barcelona\\Barcelona Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                       #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, BARCELONA)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot(color='#3498db', title='NO2 Levels In 2020 - Barcelona',ax=ax)                                                    #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
                
            def BARAREAGRAPHS():
                
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, BARCELONA)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Barcelona',ax=ax)                                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, BARCELONA)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Barcelona',ax=ax)                                     #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Barcelona\\Barcelona Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                       #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, BARCELONA)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Barcelona',ax=ax)                                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

            BARLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
            b1 = Button(BARCELONA, text="Line Graphs", command=BARLINEGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
            b2 = Button(BARCELONA, text="Area Graphs", command=BARAREAGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
            b1.place(x=760, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
            b2.place(x=835, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON

        def Amsterdam():
            AMSTERDAM = Tk()                                                                                                                #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA

            s1 = Label(AMSTERDAM, text=" ", bg="white")                                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
            s1.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL
            l1 = Label(AMSTERDAM, text="COVID-19 & Air Pollution Levels - Amsterdam", font='Helvetica 12 bold', bg="white")                 #CREATING A MAIN HEADING FOR THE WINDOW THAT WILL BE AT THE TOP
            l1.pack()                                                                                                                       #DISPLAYING THE LABEL
            s3 = Label(AMSTERDAM, text=" ", bg="white")                                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
            s3.pack()                                                                                                                       #DISPLAYING THE SPCAE LABEL

            AMSTERDAM.resizable(0,0)                                                                                                        #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW
            AMSTERDAM.resizable(width=FALSE, height=FALSE)                                                                                  #STOPPING THE USER FROM RESIZING THE CURRENT WINDOW 
            AMSTERDAM.title("COVID-19 APL - Amsterdam")                                                                                     #GIVING THE WINDOW A TITLE THAT WILL BE AT THE VERY TOP ALONGSIDE THE '- O X' BUTTONS 
            AMSTERDAM.geometry("1690x600")                                                                                                  #GENERATING THE SIZE OF THE WINDOW 
            AMSTERDAM.configure(background='white')                                                                                         #GIVING THE WINDOW A SPECIFIC BACKGROUND COLOUR 


            def AMSLINEGRAPHS():
                
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, AMSTERDAM)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Amsterdam',ax=ax)                                                    #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, AMSTERDAM)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot(color='#d5d8dc',ax=ax)                                                                                           #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Amsterdam',ax=ax)                                          #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Amsterdam\\Amsterdam Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                       #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, AMSTERDAM)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot(color='#3498db', title='NO2 Levels In 2020 - Amsterdam',ax=ax)                                                    #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000015',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
                
            def AMSAREAGRAPHS():
                
                figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
                df19 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2019.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart2019 = FigureCanvasTkAgg(figure2019, AMSTERDAM)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2019.get_tk_widget().place(x=20, y=100)                                                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Amsterdam',ax=ax)                                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
                
                figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
                df191 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
                df201 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")                              #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
                ax = figure1920.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME 
                Chart20201 = FigureCanvasTkAgg(figure1920, AMSTERDAM)                                                                       #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart20201.get_tk_widget().place(x=575, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df191.plot.area(color='#d5d8dc',ax=ax)                                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
                df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Amsterdam',ax=ax)                                     #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

                figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                                              #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
                LD = pd.read_csv('Amsterdam\\Amsterdam Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")                       #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
                df20 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")                               #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
                ax = figure2020.add_subplot(111)                                                                                            #ADDING THE GRAPH TO THE FRAME
                Chart2020 = FigureCanvasTkAgg(figure2020, AMSTERDAM)                                                                        #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
                Chart2020.get_tk_widget().place(x=1130, y=100)                                                                              #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
                 
                ax.set_ylabel("NO2 Level")                                                                                                  #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
                df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Amsterdam',ax=ax)                                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
                LD.plot.area(color='#FF000025',ax=ax)                                                                                       #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA 

            AMSLINEGRAPHS()                                                                                                                 #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
            b1 = Button(AMSTERDAM, text="Line Graphs", command=AMSLINEGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
            b2 = Button(AMSTERDAM, text="Area Graphs", command=AMSAREAGRAPHS)                                                               #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
            b1.place(x=760, y=50)                                                                                                           #DISPLAYING THE LINE GRAPH BUTTON
            b2.place(x=835, y=50)                                                                                                           #DISPLAYING THE AREA GRAPH BUTTON
            

        FILENAME = 'Map\\EU.jpg'                                                                                                    #DEFING THE FILENAME LOCATION
        canvas = tk.Canvas(MAPTAB, width=700, height=600)                                                                           #CREATING THE CANVAS FOR THE MAP
        canvas.pack()                                                                                                               #DISPLAYING THE CANVAS
        global tk_img                                                                                                               #CREATING A GLOBAL VARIABLE FOR THE MAP
        global pin                                                                                                                  #CREATING A GLOBAL VARIABLE FOR THE PINS
        
        tk_img = ImageTk.PhotoImage(file = FILENAME)                                                                                #DEFING THE GLOBAL VARIABLE AS THE MAP
        canvas.create_image(400, 300, image=tk_img)                                                                                 #DISPLAYING THE MAP ON THE CANVAS
         
        pin = ImageTk.PhotoImage(file='Map\\pins.png')                                                                              #DEFINING THE LOCATION FOR THE PIN IMAGE
        
        button1 = tk.Button(MAPTAB, text = "Berlin", anchor = 'w',command = Berlin, width = 25, activebackground = "#33B5E5")       #DEFINING WHERE THE PIN WILL GO AND WHAT IT WILL DO  
        button1.config(image=pin)                                                                                                   #GIVING THE BUTTON AN IMAGE OF A PIN
        
        button2 = tk.Button(MAPTAB, text = "Amsterdam", anchor = 'w',command = Amsterdam, width = 25, activebackground = "#33B5E5") #DEFINING WHERE THE PIN WILL GO AND WHAT IT WILL DO
        button2.config(image=pin)                                                                                                   #GIVING THE BUTTON AN IMAGE OF A PIN

        button4 = tk.Button(MAPTAB, text = "London", anchor = 'w',command = London, width = 25, activebackground = "#33B5E5")       #DEFINING WHERE THE PIN WILL GO AND WHAT IT WILL DO
        button4.config(image=pin)                                                                                                   #GIVING THE BUTTON AN IMAGE OF A PIN

        button5 = tk.Button(MAPTAB, text = "Madrid", anchor = 'w',command = Madrid, width = 25, activebackground = "#33B5E5")       #DEFINING WHERE THE PIN WILL GO AND WHAT IT WILL DO
        button5.config(image=pin)                                                                                                   #GIVING THE BUTTON AN IMAGE OF A PIN

        button6 = tk.Button(MAPTAB, text = "Barcelona", anchor = 'w',command = Barcelona,width = 25, activebackground = "#33B5E5")  #DEFINING WHERE THE PIN WILL GO AND WHAT IT WILL DO
        button6.config(image=pin)                                                                                                   #GIVING THE BUTTON AN IMAGE OF A PIN
        
        button7 = tk.Button(MAPTAB, text = "Milan", anchor = 'w',command = Milan, width = 25, activebackground = "#33B5E5")         #DEFINING WHERE THE PIN WILL GO AND WHAT IT WILL DO
        button7.config(image=pin)                                                                                                   #GIVING THE BUTTON AN IMAGE OF A PIN
        
        button1.place(x=770, y=350)                                                                                                 #DISPLAYING THE BUTTON OVER THE COUNTRY
        button2.place(x=735, y=330)                                                                                                 #DISPLAYING THE BUTTON OVER THE COUNTRY
        button4.place(x=670, y=330)                                                                                                 #DISPLAYING THE BUTTON OVER THE COUNTRY
        button5.place(x=620, y=520)                                                                                                 #DISPLAYING THE BUTTON OVER THE COUNTRY
        button6.place(x=680, y=520)                                                                                                 #DISPLAYING THE BUTTON OVER THE COUNTRY
        button7.place(x=790, y=490)                                                                                                 #DISPLAYING THE BUTTON OVER THE COUNTRY
        
    MAPVIEW()


    tabControl.add(HOMEPAGETAB, text ='Homepage')                                                                                   #GIVING THE TAB ITS SPECIFIC NAME AS A HOMEPAGE
    tabControl.add(MAPTAB, text ='European Map')                                                                                    #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE MAP
    tabControl.add(LONDONTAB, text ='London - Air Pollution Data')                                                                  #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY     
    tabControl.add(MADRIDTAB, text ='Madrid - Air Pollution Data')                                                                  #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(MILANTAB, text ='Milan - Air Pollution Data')                                                                    #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(BERLINTAB, text ='Berlin - Air Pollution Data')                                                                  #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(BARCELONATAB, text ='Barcelona - Air Pollution Data')                                                            #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(AMSTERDAMTAB, text ='Amsterdam - Air Pollution Data')                                                            #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.pack(expand = 1, fill ="both")                                                                                       #ACTUALLY DISPLAYING THE DIFFERNT TABS
    
MenuMain()
