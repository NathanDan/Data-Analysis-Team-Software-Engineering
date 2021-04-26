#TEAM SOFTWARE ENGINEERING GROUP 2 - DATA ANALYSIS
#NATHAN JONES, ELA SALAH, RYAN MUSIWA, SAMUAL BAILEY, SAM DAVEY & BEN MOSS
#DEVELOPED AND CODED BY NATHAN JONES
#FEB/MAR/APR/MAY 2021

#COVID-19 AND POLUTION LEVELS TRACKER
#VERSION 1.1.8

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
    MENU = Tk()                                                  #CREATING THE WINDOW THAT WILL BE DISPLAYED TO THE USER AND HOUSES ALL OF THE DIFFERENT TABS
    MENU.title("COVID-19 Air Polution Levels")                   #GIVING THE WINDOW A TITLE
    MENU.resizable(width=FALSE, height=FALSE)                    #THE WINDOW WILL NOT ENTER FULLSCREEN MODE
    MENU.geometry("1690x700")                                    #CONFIGURING THE FIXED SIZE OF THE WINDOW WHICH WILL ALWAYS BE THIS SIZE
    tabControl = ttk.Notebook(MENU)                              #TELLING THE PROGRAM THAT WILL WILL BE A TABBED WIDGET

    style = ttk.Style()                                                  #CREATING A TTK STYLE THAT WILL CHANGE THE COLOUR OF THE WIDGET
    style.configure("W.TFrame", foreground="white", background="white")  #SETTING THE BACKGROUND COLOUR TO BE WHITE, SO THAT THE WIDGET LOOKS SMARTER AND MORE PRESENTABLE
    
    HOMEPAGETAB = ttk.Frame(style="W.TFrame")                            #CREATING THE HOME TAB ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(HOMEPAGETAB, text=" ", bg="white")                                                                                           #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                                               #DISPLAYING THE SPCAE LABEL                                                                                                
    l1 = Label(HOMEPAGETAB, text="COVID-19 & Air Pollution Levels - Homepage", font='Helvetica 12 bold', bg="white")                        #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                                               #DISPLAYING THE LABEL
    s3 = Label(HOMEPAGETAB, text=" ",bg="white")                                                                                            #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                               #DISPLAYING THE SPCAE LABEL
    l2 = Label(HOMEPAGETAB, text="Welcome To The Homepage!", font='Helvetica 10 bold', bg="white")                                          #CREATING A SUB HEADING FOR THE DESCRIPTION 
    l2.pack()                                                                                                                               #DISPLAYING THE LABEL
    l3 = Label(HOMEPAGETAB, text=
    """This is a COVID-19 Air Pollution tracking program that looks at the correlation between COVID-19 Lockdowns
    and the overall pollution impact in certain European cities. The program utilses graphs and other visual stats to
    allow for a visual representation of a significant or minimal difference in pollution levels as a result to the on going
    pandemic.""",
    font='Helvetica 10 ', bg="white")                                                                                                       #CREATING A DESCRIPTION OF THE PROGRAM FOR THE USER TO SEE WHEN THEY FIRST LOAD PROGRAM
    l3.pack()                                                                                                                               #DISPLAYING THE LABEL
    l4 = Label(HOMEPAGETAB, text=
    """The data that is being used in this program has been sourced from the World Air Quality Index Project (WAQIP)
    and its Air Quality Historical Data Platform (https://aqicn.org/data-platform) that is a free to use service, that gathers
    Air Quality Data (AQD) from various sources and groups them together to produce a databse that consits of AQD from
    all over the World. As this program is free and for educational purposes we are allowed to use the data-sets from the
    WAQIP as we are not making a profit and are solely using the data to educate and show a trend in the data.""",
    font='Helvetica 10 ', bg="white")                                                                                                       #CREATING A DESCRIPTION OF THE DATA USED FOR THE USER TO SEE WHEN THEY FIRST LOAD PROGRAM
    l4.pack()                                                                                                                               #DISPLAYING THE LABEL
    
    l5 = Label(HOMEPAGETAB, text="Make sure to keep upto date with the latest updates and features with the website down below!",font='Helvetica 10', bg="white")  #CREATING A SUB HEADING FOR THE DESCRIPTION  
    l5.pack()                                                                                                                                                      #DISPLAYING THE LABEL
    s3 = Label(HOMEPAGETAB, text=" ", bg="white")                                                                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                                                                      #DISPLAYING THE SPCAE LABEL
    l6 = Label(HOMEPAGETAB, text="The Development Team",font='Helvetica 10 bold',bg="white")                                                                       #CREATING A SUB HEADING FOR THE DESCRIPTION  
    l6.pack()                                                                                                                                                      #DISPLAYING THE LABEL
    l7 = Label(HOMEPAGETAB, text=
    "Nathan Jones, Ben Moss, Samual Bailey, Ryan Musiwa, Sam Davey & Ela Salah", font='Helvetica 10 ', bg="white")                                 #CREATING A LABEL THAT LISTS EVERY ONE WHO IS INVOLVED WITH THE PROGRAM 
    l7.pack()                                                                                                                                      #DISPLAYING THE LABEL THAT LISTS EVERY ONE WHO IS INVOLVED WITH THE PROGRAM
    s5 = Label(HOMEPAGETAB, text=" ", bg="white")                                                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s5.pack()                                                                                                                                      #DISPLAYING THE SPCAE LABEL
    l8 = Label(HOMEPAGETAB, text="The Coding Team",font='Helvetica 10 bold',bg="white")                                                            #CREATING A SUB HEADING FOR THE DESCRIPTION  
    l8.pack()                                                                                                                                      #DISPLAYING THE LABEL
    l9 = Label(HOMEPAGETAB, text=
    "Nathan Jones, Ben Moss & Sam Davey", font='Helvetica 10 ', bg="white")                                                                        #CREATING A LABEL THAT LISTS EVERY ONE WHO CODED WITH THE PROGRAM 
    l9.pack()                                                                                                                                      #DISPLAYING THE LABEL THAT LISTS EVERY ONE WHO IS INVOLVED WITH THE PROGRAM 
    s6 = Label(HOMEPAGETAB, text=" ", bg="white")                                                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s6.pack()                                                                                                                                      #DISPLAYING THE SPCAE LABEL
    l10 = Label(HOMEPAGETAB, text="Contact Information",font='Helvetica 10 bold', bg="white")                                                      #CREATING A SUB HEADING FOR THE CONTACT INFORMATION  
    l10.pack()                                                                                                                                     #DISPLAYING THE LABEL
    l11 = Label(HOMEPAGETAB, text="Website: https://github.com/NathanDan/Data-Analysis-Team-Software-Engineering",font='Helvetica 10', bg="white") #CREATING A LABEL FOR THE DESCRIPTION OF THE CONTACT INFORMATION 
    l11.pack()                                                                                                                                     #DISPLAYING THE LABEL
    l12 = Label(HOMEPAGETAB, text="Version 1.1.8",font='Helvetica 9 bold', bg="white")                                                             #CREATING A LABEL THAT SHOWS WHAT VERSION THE USER IS ON  
    l12.place(x=1600, y=655)                                                                                                                       #DISPLAYING THE LABEL AT THE BOTTOM OF THE WINDOW
    

    MAPTAB = ttk.Frame(style="W.TFrame")                                                                           #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(MAPTAB, text=" ",bg="white")                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                      #DISPLAYING THE SPCAE LABEL                                                                                                
    l1 = Label(MAPTAB, text="COVID-19 & Air Pollution Levels - European Map", font='Helvetica 12 bold',bg="white") #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                      #DISPLAYING THE LABEL
    s2 = Label(MAPTAB, text=" ",bg="white")                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                      #DISPLAYING THE SPCAE LABEL

    Map = ImageTk.PhotoImage(Image.open('Map\\EU.png'))
    MAP = ttk.Label(MAPTAB, image=Map)
    MAP.pack()
    
    def MAPVIEW():
       
        button1 = tk.Button(MAPTAB, text = "Berlin", command = MAPVIEW, width = 6, activebackground = "#33B5E5")
        button2 = tk.Button(MAPTAB, text = "Amsterdam", command = MAPVIEW,width = 10, activebackground = "#33B5E5")
        button3 = tk.Button(MAPTAB, text = "Paris", command = MAPVIEW, width = 5, activebackground = "#33B5E5")
        button4 = tk.Button(MAPTAB, text = "London", command = MAPVIEW, width = 6, activebackground = "#33B5E5")
        button5 = tk.Button(MAPTAB, text = "Madrid", command = MAPVIEW, width = 6, activebackground = "#33B5E5")
        button6 = tk.Button(MAPTAB, text = "Barcelona", command = MAPVIEW, width = 8, activebackground = "#33B5E5")
        button7 = tk.Button(MAPTAB, text = "Milan", command = MAPVIEW, width = 6, activebackground = "#33B5E5")
        
        button1.place(x=800, y=1000)
        button2.place(x=600, y=900)
        button3.place(x=540, y=1100)
        button4.place(x=460, y=900)
        button5.place(x=400, y=1300)
        button6.place(x=540, y=1300)
        button7.place(x=800, y=1200)
    MAPVIEW()



    LONDONTAB = ttk.Frame(style="W.TFrame")                                                                     #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(LONDONTAB, text=" ",bg="white")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                   #DISPLAYING THE SPCAE LABEL                                                                                                
    l1 = Label(LONDONTAB, text="COVID-19 & Air Pollution Levels - London", font='Helvetica 12 bold',bg="white") #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                   #DISPLAYING THE LABEL
    s2 = Label(LONDONTAB, text=" ",bg="white")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                   #DISPLAYING THE SPCAE LABEL
    
    
    def LONLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, LONDONTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - London',ax=ax)                           #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, LONDONTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                               #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - London',ax=ax)                 #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('London\\London Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, LONDONTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - London',ax=ax)                           #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                           #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def LONAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, LONDONTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - London',ax=ax)                      #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, LONDONTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                          #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - London',ax=ax)            #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('London\\London Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, LONDONTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - London',ax=ax)                      #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                           #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

    def LONSTATS():
        df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH                                                                                                #DISPLAYING THE SPCAE LABEL
 
        
    LONLINEGRAPHS()                                                           #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(LONDONTAB, text="Line Graphs", command=LONLINEGRAPHS)         #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(LONDONTAB, text="Area Graphs", command=LONAREAGRAPHS)         #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(LONDONTAB, text="Yearly Statistics", command=LONSTATS)        #CREATING THE BUTTON THAT DISPLAYS THE YEARLY STATISTICS FOR THE CITY
    b4 = Button(LONDONTAB, text="Monthly Statistics", command=LONSTATS)       #CREATING THE BUTTON THAT DISPLAYS THE MONTHLY STATISTICS FOR THE CITY
    b1.place(x=665, y=50)                                                     #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=740, y=50)                                                     #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=818, y=50)                                                     #DISPLAYING THE YEARLY STATISTICS BUTTON
    b4.place(x=914, y=50)                                                     #DISPLAYING THE MONTHLY STATISTICS BUTTON
    
    

    MADRIDTAB = ttk.Frame(style="W.TFrame")                                                                     #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(MADRIDTAB, text=" ",bg="white")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                   #DISPLAYING THE SPCAE LABEL                                                                                              
    l1 = Label(MADRIDTAB, text="COVID-19 & Air Pollution Levels - Madrid", font='Helvetica 12 bold',bg="white") #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                   #DISPLAYING THE LABEL
    s3 = Label(MADRIDTAB, text=" ",bg="white")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                   #DISPLAYING THE SPCAE LABEL

    def MADLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MADRIDTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Madrid',ax=ax)                           #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MADRIDTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                               #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Madrid',ax=ax)                 #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Madrid\\Madrid Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MADRIDTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Madrid',ax=ax)                           #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                           #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def MADAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MADRIDTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Madrid',ax=ax)                      #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MADRIDTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                          #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Madrid',ax=ax)            #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Madrid\\Madrid Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MADRIDTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Madrid',ax=ax)                      #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                           #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

    def MADSTATS():
        print("Hello")
        
    MADLINEGRAPHS()                                                           #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(MADRIDTAB, text="Line Graphs", command=MADLINEGRAPHS)         #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(MADRIDTAB, text="Area Graphs", command=MADAREAGRAPHS)         #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(MADRIDTAB, text="Yearly Statistics", command=MADSTATS)        #CREATING THE BUTTON THAT DISPLAYS THE YEARLY STATISTICS FOR THE CITY
    b4 = Button(MADRIDTAB, text="Monthly Statistics", command=MADSTATS)       #CREATING THE BUTTON THAT DISPLAYS THE MONTHLY STATISTICS FOR THE CITY
    b1.place(x=665, y=50)                                                     #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=740, y=50)                                                     #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=818, y=50)                                                     #DISPLAYING THE YEARLY STATISTICS BUTTON
    b4.place(x=914, y=50)                                                     #DISPLAYING THE MONTHLY STATISTICS BUTTON
    

    
    MILANTAB = ttk.Frame(style="W.TFrame")                                                                    #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR
    
    s1 = Label(MILANTAB, text=" ",bg="white")                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                 #DISPLAYING THE SPCAE LABEL                                                                                             
    l1 = Label(MILANTAB, text="COVID-19 & Air Pollution Levels - Milan", font='Helvetica 12 bold',bg="white") #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                 #DISPLAYING THE LABEL
    s3 = Label(MILANTAB, text=" ",bg="white")                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                 #DISPLAYING THE SPCAE LABEL

    def MILLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MILANTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Milan',ax=ax)                          #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MILANTAB)                                          #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                             #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Milan',ax=ax)                #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Milan\\Milan Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MILANTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Milan',ax=ax)                          #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                         #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def MILAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, MILANTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Milan',ax=ax)                     #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, MILANTAB)                                          #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                        #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Milan',ax=ax)           #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Milan\\Milan Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                              #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, MILANTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                    #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Milan',ax=ax)                     #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                         #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def MILSTATS():
        print("Hello")
        
    MILLINEGRAPHS()                                                          #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(MILANTAB, text="Line Graphs", command=MILLINEGRAPHS)         #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(MILANTAB, text="Area Graphs", command=MILAREAGRAPHS)         #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(MILANTAB, text="Yearly Statistics", command=MILSTATS)        #CREATING THE BUTTON THAT DISPLAYS THE YEARLY STATISTICS FOR THE CITY
    b4 = Button(MILANTAB, text="Monthly Statistics", command=MILSTATS)       #CREATING THE BUTTON THAT DISPLAYS THE MONTHLY STATISTICS FOR THE CITY
    b1.place(x=665, y=50)                                                    #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=740, y=50)                                                    #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=818, y=50)                                                    #DISPLAYING THE YEARLY STATISTICS BUTTON
    b4.place(x=914, y=50)                                                    #DISPLAYING THE MONTHLY STATISTICS BUTTON
    


    BERLINTAB = ttk.Frame(style="W.TFrame")                                                                      #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR
                                                                                                                 
    s1 = Label(BERLINTAB, text=" ", bg="white")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                    #DISPLAYING THE SPCAE LABEL                                                                                                 
    l1 = Label(BERLINTAB, text="COVID-19 & Air Pollution Levels - Berlin", font='Helvetica 12 bold', bg="white") #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                    #DISPLAYING THE LABEL
    s3 = Label(BERLINTAB, text=" ", bg="white")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                    #DISPLAYING THE SPCAE LABEL

    def BERLINEGRAPHS():
         
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BERLINTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Berlin',ax=ax)                           #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BERLINTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                               #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Berlin',ax=ax)                 #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Berlin\\Berlin Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BERLINTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Berlin',ax=ax)                           #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                           #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def BERAREAGRAPHS():
         
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BERLINTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Berlin',ax=ax)                      #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BERLINTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                      #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                          #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Berlin',ax=ax)            #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                  #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Berlin\\Berlin Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BERLINTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                  #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                     #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Berlin',ax=ax)                     #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                          #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def BERSTATS():
        print("Hello")
        
    BERLINEGRAPHS()                                                           #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(BERLINTAB, text="Line Graphs", command=BERLINEGRAPHS)         #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(BERLINTAB, text="Area Graphs", command=BERAREAGRAPHS)         #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(BERLINTAB, text="Yearly Statistics", command=BERSTATS)        #CREATING THE BUTTON THAT DISPLAYS THE YEARLY STATISTICS FOR THE CITY
    b4 = Button(BERLINTAB, text="Monthly Statistics", command=BERSTATS)       #CREATING THE BUTTON THAT DISPLAYS THE MONTHLY STATISTICS FOR THE CITY
    b1.place(x=665, y=50)                                                     #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=740, y=50)                                                     #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=818, y=50)                                                     #DISPLAYING THE YEARLY STATISTICS BUTTON
    b4.place(x=914, y=50)                                                     #DISPLAYING THE MONTHLY STATISTICS BUTTON



    BARCELONATAB = ttk.Frame(style="W.TFrame")                                                                        #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(BARCELONATAB, text=" ",bg="white")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                         #DISPLAYING THE SPCAE LABEL                                                                                                   
    l1 = Label(BARCELONATAB, text="COVID-19 & Air Pollution Levels - Barcelona", font='Helvetica 12 bold',bg="white") #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                         #DISPLAYING THE LABEL
    s3 = Label(BARCELONATAB, text=" ",bg="white")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                         #DISPLAYING THE SPCAE LABEL

    def BARLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BARCELONATAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                          #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Barcelona',ax=ax)                              #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BARCELONATAB)                                              #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                        #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                     #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Barcelona',ax=ax)                    #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Barcelona\\Barcelona Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BARCELONATAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                        #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Barcelona',ax=ax)                              #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                                 #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def BARAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, BARCELONATAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                          #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Barcelona',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, BARCELONATAB)                                              #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                        #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                                #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Barcelona',ax=ax)               #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Barcelona\\Barcelona Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, BARCELONATAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                        #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Barcelona',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                                 #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def BARSTATS():
        print("Hello")
        
    BARLINEGRAPHS()                                                           #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(BARCELONATAB, text="Line Graphs", command=BARLINEGRAPHS)      #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(BARCELONATAB, text="Area Graphs", command=BARAREAGRAPHS)      #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(BARCELONATAB, text="Yearly Statistics", command=BARSTATS)     #CREATING THE BUTTON THAT DISPLAYS THE YEARLY STATISTICS FOR THE CITY
    b4 = Button(BARCELONATAB, text="Monthly Statistics", command=BARSTATS)    #CREATING THE BUTTON THAT DISPLAYS THE MONTHLY STATISTICS FOR THE CITY
    b1.place(x=665, y=50)                                                     #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=740, y=50)                                                     #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=818, y=50)                                                     #DISPLAYING THE YEARLY STATISTICS BUTTON
    b4.place(x=914, y=50)                                                     #DISPLAYING THE MONTHLY STATISTICS BUTTON



    AMSTERDAMTAB = ttk.Frame(style="W.TFrame")                                                                        #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(AMSTERDAMTAB, text=" ",bg="white")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                         #DISPLAYING THE SPCAE LABEL                                                                                                    
    l1 = Label(AMSTERDAMTAB, text="COVID-19 & Air Pollution Levels - Amsterdam", font='Helvetica 12 bold',bg="white") #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                         #DISPLAYING THE LABEL
    s3 = Label(AMSTERDAMTAB, text=" ",bg="white")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                                         #DISPLAYING THE SPCAE LABEL

    def AMSLINEGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, AMSTERDAMTAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                          #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Amsterdam',ax=ax)                              #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, AMSTERDAMTAB)                                              #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                        #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot(color='#d5d8dc',ax=ax)                                                                     #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot(color='#3498db', title='NO2 Levels In 2019 And 2020 - Amsterdam',ax=ax)                    #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Amsterdam\\Amsterdam Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, AMSTERDAMTAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                        #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot(color='#3498db', title='NO2 Levels In 2020 - Amsterdam',ax=ax)                              #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000015',ax=ax)                                                                 #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def AMSAREAGRAPHS():
        
        figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
        df19 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2019.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME 
        Chart2019 = FigureCanvasTkAgg(figure2019, AMSTERDAMTAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2019.get_tk_widget().place(x=20, y=100)                                                          #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df19.plot.area(color='#d5d8dc', title='NO2 Levels In 2019 - Amsterdam',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
        
        figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
        df191 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
        df201 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")        #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
        ax = figure1920.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME 
        Chart20201 = FigureCanvasTkAgg(figure1920, AMSTERDAMTAB)                                              #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart20201.get_tk_widget().place(x=575, y=100)                                                        #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
        
        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df191.plot.area(color='#d5d8dc',ax=ax)                                                                #PLOTTING THE DATA FROM THE 2019 CSV FILE  
        df201.plot.area(color='#3498db', title='NO2 Levels In 2019 And 2020 - Amsterdam',ax=ax)               #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

        figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                        #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
        LD = pd.read_csv('Amsterdam\\Amsterdam Lockdown Dates.csv', parse_dates=['Month'], index_col="Month") #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
        df20 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
        ax = figure2020.add_subplot(111)                                                                      #ADDING THE GRAPH TO THE FRAME
        Chart2020 = FigureCanvasTkAgg(figure2020, AMSTERDAMTAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
        Chart2020.get_tk_widget().place(x=1130, y=100)                                                        #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
         
        ax.set_ylabel("NO2 Level")                                                                            #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
        df20.plot.area(color='#3498db', title='NO2 Levels In 2020 - Amsterdam',ax=ax)                         #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
        LD.plot.area(color='#FF000025',ax=ax)                                                                 #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA
        
    def AMSSTATS():
        print("Hello")
        
    AMSLINEGRAPHS()                                                           #DISPLAYING THE LINE GRAPH AS THE FIRST GRAPH TO BEEN SEEN IN THE PROGRAM SO IT ISNT AN EMPTY SCREEN
    b1 = Button(AMSTERDAMTAB, text="Line Graphs", command=AMSLINEGRAPHS)      #CREATING THE BUTTON THAT DISPLAYS THE LINE GRAPHS FOR THE CITY
    b2 = Button(AMSTERDAMTAB, text="Area Graphs", command=AMSAREAGRAPHS)      #CREATING THE BUTTON THAT DISPLAYS THE AREA GRAPHS FOR THE CITY
    b3 = Button(AMSTERDAMTAB, text="Yearly Statistics", command=AMSSTATS)     #CREATING THE BUTTON THAT DISPLAYS THE YEARLY STATISTICS FOR THE CITY
    b4 = Button(AMSTERDAMTAB, text="Monthly Statistics", command=AMSSTATS)    #CREATING THE BUTTON THAT DISPLAYS THE MONTHLY STATISTICS FOR THE CITY
    b1.place(x=665, y=50)                                                     #DISPLAYING THE LINE GRAPH BUTTON
    b2.place(x=740, y=50)                                                     #DISPLAYING THE AREA GRAPH BUTTON
    b3.place(x=818, y=50)                                                     #DISPLAYING THE YEARLY STATISTICS BUTTON
    b4.place(x=914, y=50)                                                     #DISPLAYING THE MONTHLY STATISTICS BUTTON


    MAPTAB = ttk.Frame(style="W.TFrame")                                                                           #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA ALONG WITH ITS BACKGROUND COLOUR

    s1 = Label(MAPTAB, text=" ",bg="white")                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                                      #DISPLAYING THE SPCAE LABEL                                                                                                
    l1 = Label(MAPTAB, text="COVID-19 & Air Pollution Levels - European Map", font='Helvetica 12 bold',bg="white") #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                                      #DISPLAYING THE LABEL
    s2 = Label(MAPTAB, text=" ",bg="white")                                                                        #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s2.pack()                                                                                                      #DISPLAYING THE SPCAE LABEL
    
    def MAPVIEW():
        FILENAME = 'Map\\EU.png'
        canvas = tk.Canvas(MAPTAB, width=1000, height=950)
        canvas.pack()
        MAPIMG = ImageTk.PhotoImage(file = FILENAME)
        canvas.create_image(500, 500, image=MAPIMG)
       
        button1 = tk.Button(MAPTAB, text = "Berlin", command = MAPVIEW, anchor = 'w',
                    width = 6, activebackground = "#33B5E5")
        button2 = tk.Button(MAPTAB, text = "Amsterdam", command = MAPVIEW, anchor = 'w',
                            width = 10, activebackground = "#33B5E5")
        button3 = tk.Button(MAPTAB, text = "Paris", command = MAPVIEW, anchor = 'w',
                            width = 5, activebackground = "#33B5E5")
        button4 = tk.Button(MAPTAB, text = "London", command = MAPVIEW, anchor = 'w',
                            width = 6, activebackground = "#33B5E5")
        button5 = tk.Button(MAPTAB, text = "Madrid", command = MAPVIEW, anchor = 'w',
                            width = 6, activebackground = "#33B5E5")
        button6 = tk.Button(MAPTAB, text = "Barcelona", command = MAPVIEW, anchor = 'w',
                            width = 8, activebackground = "#33B5E5")
        button7 = tk.Button(MAPTAB, text = "Milan", command = MAPVIEW, anchor = 'w',
                            width = 6, activebackground = "#33B5E5")
        button1.place(x=400, y=500)
        button2.place(x=300, y=450)
        button3.place(x=270, y=550)
        button4.place(x=230, y=450)
        button5.place(x=200, y=650)
        button6.place(x=270, y=650)
        button7.place(x=400, y=600)
    MAPVIEW()

    tabControl.add(HOMEPAGETAB, text ='Homepage')                            #GIVING THE TAB ITS SPECIFIC NAME AS A HOMEPAGE
    tabControl.add(MAPTAB, text ='European Map')                             #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE MAP
    tabControl.add(LONDONTAB, text ='London - Air Pollution Data')           #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY     
    tabControl.add(MADRIDTAB, text ='Madrid - Air Pollution Data')           #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(MILANTAB, text ='Milan - Air Pollution Data')             #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(BERLINTAB, text ='Berlin - Air Pollution Data')           #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(BARCELONATAB, text ='Barcelona - Air Pollution Data')     #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(AMSTERDAMTAB, text ='Amsterdam - Air Pollution Data')     #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.pack(expand = 1, fill ="both")                                #ACTUALLY DISPLAYING THE DIFFERNT TABS
    
MenuMain()
