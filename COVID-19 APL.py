#TEAM SOFTWARE ENGINEERING GROUP 2 - DATA ANALYSIS
#NATHAN JONES, ELA SALAH, RYAN MUSIWA, SAMUAL BAILEY, SAM DAVEY & BEN MOSS
#DEVELOPED AND CODED BY NATHAN JONES
#FEB/MAR/APR/MAY 2021

#COVID-19 AND POLUTION LEVELS TRACKER
#VERSION 1.1.4

import tkinter as tk                                             #IMPORTING THE TKINTER MODULE TO BE USED IN THE PROGRAM
import sys                                                       #ALLOWS ACCESS TO THE SYSTEM FROM WITHIN PYTHON
import os.path                                                   #ALLOWS THE PROGRAM TO OPEN OTHER SPECIFIC APPLICATIONS, IN THIS CASE THE GC PROGRAMS
import os                                                        #ALLOWS FOR CONTROL OF THE MACHINE AND IS OS INCLUDING THE LIKES OF SAVING, OPENING/CLOSING FILES, ETC.
import matplotlib.pyplot as plt                                  #IMPORTING MATPLOTLIB SO THAT GRAPHS CAN BE CREATED AND PRODUCED IN THE PROGRAM
import pandas as pd                                              #ALLOWS FOR CERTIAN MATHMATICAL FUNCTIONS AND READING OF CSV DATA TO TAKE PLACE

from tkinter import ttk                                          #IMPORTING THE TKK MODULE THAT ALLOWS FOR TABBED WIDGETS
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry  #ALLOWING FOR TKINTER TO BE ACCESSED/UTILISED FOR THE PROGRAM TO USE ALL OF ITS FUNCTIONS AND GIVING THE PROGRAM A GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  #ALLOWING FOR THE MATPLOTLIB GRAPHS TO BE INSERTED INTO THE TKINTER GUI'S

def MenuMain():
    MENU = Tk()                                                 #CREATING THE WINDOW THAT WILL BE DISPLAYED TO THE USER AND HOUSES ALL OF THE DIFFERENT TABS
    MENU.title("COVID-19 Air Polution Levels")                  #GIVING THE WINDOW A TITLE
    tabControl = ttk.Notebook(MENU)                             #TELLING THE PROGRAM THAT WILL WILL BE A TABBED WIDGET


    
    LONDONTAB = ttk.Frame()                                                                          #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA

    s1 = Label(LONDONTAB, text=" ")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                        #DISPLAYING THE SPCAE LABEL                                                                                                
    l1 = Label(LONDONTAB, text="COVID-19 & Air Pollution Levels - London", font='Helvetica 12 bold') #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                        #DISPLAYING THE LABEL
    s3 = Label(LONDONTAB, text=" ")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                        #DISPLAYING THE SPCAE LABEL

    figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
    df19 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2019.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
    Chart2019 = FigureCanvasTkAgg(figure2019, LONDONTAB)                                             #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - London',ax=ax)                            #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
    
    figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
    df191 = pd.read_csv('London\\London 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
    df201 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
    ax = figure1920.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
    Chart20201 = FigureCanvasTkAgg(figure1920, LONDONTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                      #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
    
    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df191.plot(color='#d5d8dc',ax=ax)                                                                #PLOTTING THE DATA FROM THE 2019 CSV FILE  
    df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - London',ax=ax)    #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

    figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
    LD = pd.read_csv('London\\London Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")  #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
    df20 = pd.read_csv('London\\London 2020.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2020.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME
    Chart2020 = FigureCanvasTkAgg(figure2020, LONDONTAB)                                             #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
     
    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df20.plot(color='#3498db', title='NO2 Levels In 2020 - London',ax=ax)                            #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
    LD.plot.area(color='#FF000015',ax=ax)                                                            #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA



    MADRIDTAB = ttk.Frame()                                                                          #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA

    s1 = Label(MADRIDTAB, text=" ")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                        #DISPLAYING THE SPCAE LABEL                                                                                              
    l1 = Label(MADRIDTAB, text="COVID-19 & Air Pollution Levels - Madrid", font='Helvetica 12 bold') #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                        #DISPLAYING THE LABEL
    s3 = Label(MADRIDTAB, text=" ")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                        #DISPLAYING THE SPCAE LABEL

    figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
    df19 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2019.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
    Chart2019 = FigureCanvasTkAgg(figure2019, MADRIDTAB)                                             #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Madrid',ax=ax)                            #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
    
    figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
    df191 = pd.read_csv('Madrid\\Madrid 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
    df201 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
    ax = figure1920.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
    Chart20201 = FigureCanvasTkAgg(figure1920, MADRIDTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                      #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
    
    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df191.plot(color='#d5d8dc',ax=ax)                                                                #PLOTTING THE DATA FROM THE 2019 CSV FILE  
    df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Madrid',ax=ax)    #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

    figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
    LD = pd.read_csv('Madrid\\Madrid Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")  #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
    df20 = pd.read_csv('Madrid\\Madrid 2020.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2020.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME
    Chart2020 = FigureCanvasTkAgg(figure2020, MADRIDTAB)                                             #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
     
    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df20.plot(color='#3498db', title='NO2 Levels In 2020 - Madrid',ax=ax)                            #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
    LD.plot.area(color='#FF000015',ax=ax)                                                            #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA


    
    MILANTAB = ttk.Frame()
    
    s1 = Label(MILANTAB, text=" ")                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                      #DISPLAYING THE SPCAE LABEL                                                                                             
    l1 = Label(MILANTAB, text="COVID-19 & Air Pollution Levels - Milan", font='Helvetica 12 bold') #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                      #DISPLAYING THE LABEL
    s3 = Label(MILANTAB, text=" ")                                                                 #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                      #DISPLAYING THE SPCAE LABEL

    figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                 #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
    df19 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2019.add_subplot(111)                                                               #ADDING THE GRAPH TO THE FRAME 
    Chart2019 = FigureCanvasTkAgg(figure2019, MILANTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                     #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

    ax.set_ylabel("NO2 Level")                                                                     #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Milan',ax=ax)                           #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
    
    figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                 #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
    df191 = pd.read_csv('Milan\\Milan 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
    df201 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
    ax = figure1920.add_subplot(111)                                                               #ADDING THE GRAPH TO THE FRAME 
    Chart20201 = FigureCanvasTkAgg(figure1920, MILANTAB)                                           #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                    #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
    
    ax.set_ylabel("NO2 Level")                                                                     #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df191.plot(color='#d5d8dc',ax=ax)                                                              #PLOTTING THE DATA FROM THE 2019 CSV FILE  
    df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Milan',ax=ax)   #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

    figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                 #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
    LD = pd.read_csv('Milan\\Milan Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")  #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
    df20 = pd.read_csv('Milan\\Milan 2020.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2020.add_subplot(111)                                                               #ADDING THE GRAPH TO THE FRAME
    Chart2020 = FigureCanvasTkAgg(figure2020, MILANTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                     #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
     
    ax.set_ylabel("NO2 Level")                                                                     #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df20.plot(color='#3498db', title='NO2 Levels In 2020 - Milan',ax=ax)                           #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
    LD.plot.area(color='#FF000015',ax=ax)                                                          #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA

    

    BERLINTAB = ttk.Frame()                                                                          #CLOSING THE MENU AFTER THE TAB HAS BEEN LAUNCHED
                                                                                                     #CREATING THE WINDOW THAT WILL HOUSE THE CITY'S DATA
    s1 = Label(BERLINTAB, text=" ")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                        #DISPLAYING THE SPCAE LABEL                                                                                                 
    l1 = Label(BERLINTAB, text="COVID-19 & Air Pollution Levels - Berlin", font='Helvetica 12 bold') #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                        #DISPLAYING THE LABEL
    s3 = Label(BERLINTAB, text=" ")                                                                  #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                        #DISPLAYING THE SPCAE LABEL

    figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
    df19 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2019.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
    Chart2019 = FigureCanvasTkAgg(figure2019, BERLINTAB)                                             #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Berlin',ax=ax)                            #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
    
    figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
    df191 = pd.read_csv('Berlin\\Berlin 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
    df201 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
    ax = figure1920.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME 
    Chart20201 = FigureCanvasTkAgg(figure1920, BERLINTAB)                                            #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                      #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
    
    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df191.plot(color='#d5d8dc',ax=ax)                                                                #PLOTTING THE DATA FROM THE 2019 CSV FILE  
    df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Berlin',ax=ax)    #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

    figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                   #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
    LD = pd.read_csv('Berlin\\Berlin Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")  #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
    df20 = pd.read_csv('Berlin\\Berlin 2020.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2020.add_subplot(111)                                                                 #ADDING THE GRAPH TO THE FRAME
    Chart2020 = FigureCanvasTkAgg(figure2020, BERLINTAB)                                             #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                       #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
    
    ax.set_ylabel("NO2 Level")                                                                       #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df20.plot(color='#3498db', title='NO2 Levels In 2020 - Berlin',ax=ax)                            #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
    LD.plot.area(color='#FF000015',ax=ax)                                                            #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA




    BARCELONATAB = ttk.Frame()                                                                             #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA

    s1 = Label(BARCELONATAB, text=" ")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                              #DISPLAYING THE SPCAE LABEL                                                                                                   
    l1 = Label(BARCELONATAB, text="COVID-19 & Air Pollution Levels - Barcelona", font='Helvetica 12 bold') #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                              #DISPLAYING THE LABEL
    s3 = Label(BARCELONATAB, text=" ")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                              #DISPLAYING THE SPCAE LABEL

    figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                         #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
    df19 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2019.add_subplot(111)                                                                       #ADDING THE GRAPH TO THE FRAME 
    Chart2019 = FigureCanvasTkAgg(figure2019, BARCELONATAB)                                                #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                             #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

    ax.set_ylabel("NO2 Level")                                                                             #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Barcelona',ax=ax)                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
    
    figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                         #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
    df191 = pd.read_csv('Barcelona\\Barcelona 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
    df201 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
    ax = figure1920.add_subplot(111)                                                                       #ADDING THE GRAPH TO THE FRAME 
    Chart20201 = FigureCanvasTkAgg(figure1920, BARCELONATAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                            #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
    
    ax.set_ylabel("NO2 Level")                                                                             #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df191.plot(color='#d5d8dc',ax=ax)                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
    df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Barcelona',ax=ax)       #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

    figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                         #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
    LD = pd.read_csv('Barcelona\\Barcelona Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")  #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
    df20 = pd.read_csv('Barcelona\\Barcelona 2020.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2020.add_subplot(111)                                                                       #ADDING THE GRAPH TO THE FRAME
    Chart2020 = FigureCanvasTkAgg(figure2020, BARCELONATAB)                                                #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                             #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
     
    ax.set_ylabel("NO2 Level")                                                                             #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df20.plot(color='#3498db', title='NO2 Levels In 2020 - Barcelona',ax=ax)                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
    LD.plot.area(color='#FF000015',ax=ax)                                                                  #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA




    AMSTERDAMTAB = ttk.Frame()                                                                             #CREATING THE TAB THAT WILL HOUSE THE CITY'S DATA

    s1 = Label(AMSTERDAMTAB, text=" ")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE
    s1.pack()                                                                                              #DISPLAYING THE SPCAE LABEL                                                                                                    
    l1 = Label(AMSTERDAMTAB, text="COVID-19 & Air Pollution Levels - Amsterdam", font='Helvetica 12 bold') #CREATING A MAIN HEADING FOR THE TAB THAT WILL BE AT THE TOP
    l1.pack()                                                                                              #DISPLAYING THE LABEL
    s3 = Label(AMSTERDAMTAB, text=" ")                                                                     #CREATING AN EMPTY LABEL THAT WILL ACT AS A ONE LINE SPACE 
    s3.pack()                                                                                              #DISPLAYING THE SPCAE LABEL

    figure2019 = plt.Figure(figsize=(6,5), dpi=90)                                                         #CREATING THE FRAME FOR THE 2019 GRAPH TO BE DISPLAYED IN
    df19 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2019.add_subplot(111)                                                                       #ADDING THE GRAPH TO THE FRAME 
    Chart2019 = FigureCanvasTkAgg(figure2019, AMSTERDAMTAB)                                                #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2019.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                             #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW

    ax.set_ylabel("NO2 Level")                                                                             #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df19.plot(color='#d5d8dc', title='NO2 Levels In 2019 - Amsterdam',ax=ax)                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 
    
    figure1920 = plt.Figure(figsize=(6,5), dpi=90)                                                         #CREATING THE FRAME FOR THE 2019 2020 COMPARISION GRAPH TO BE DISPLAYED IN
    df191 = pd.read_csv('Amsterdam\\Amsterdam 2019.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2019 POINTS
    df201 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")         #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE 2020 POINTS
    ax = figure1920.add_subplot(111)                                                                       #ADDING THE GRAPH TO THE FRAME 
    Chart20201 = FigureCanvasTkAgg(figure1920, AMSTERDAMTAB)                                               #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart20201.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                            #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
    
    ax.set_ylabel("NO2 Level")                                                                             #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df191.plot(color='#d5d8dc',ax=ax)                                                                      #PLOTTING THE DATA FROM THE 2019 CSV FILE  
    df201.plot(color='#3498db', title='Difference In NO2 Levels In 2019 And 2020 - Amsterdam',ax=ax)       #PLOTTING THE DATA FROM THE 2020 CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH 

    figure2020 = plt.Figure(figsize=(6,5), dpi=90)                                                         #CREATING THE FRAME FOR THE 2020 GRAPH TO BE DISPLAYED IN
    LD = pd.read_csv('Amsterdam\\Amsterdam Lockdown Dates.csv', parse_dates=['Month'], index_col="Month")  #READING THE CSV FILE WITH ALL OF THE DATA ON THE LOCKDOWNS TO POPULATE THE GRAPH
    df20 = pd.read_csv('Amsterdam\\Amsterdam 2020.csv', parse_dates=['Month'], index_col="Month")          #READING THE CSV FILE WITH ALL OF THE DATA INSIDE TO POPULATE THE GRAPH
    ax = figure2020.add_subplot(111)                                                                       #ADDING THE GRAPH TO THE FRAME
    Chart2020 = FigureCanvasTkAgg(figure2020, AMSTERDAMTAB)                                                #DISPLAYING THE GRAPH IN THE TKINTER TAB FOR THE CITY
    Chart2020.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)                                             #POSITIONING THE GRAPH SO THAT THEY WILL ALL SIT ALONGSIDE EACH OTHER ON ONE ROW
     
    ax.set_ylabel("NO2 Level")                                                                             #SETTING THE Y LABEL ON THE GRAPH TO BE "NO2 Level"
    df20.plot(color='#3498db', title='NO2 Levels In 2020 - Amsterdam',ax=ax)                               #PLOTTING THE DATA FROM THE CSV FILE AND ADDING A TITLE TO THE WHOLE GRAPH
    LD.plot.area(color='#FF000015',ax=ax)                                                                  #PLOTTING THE LOCKDOWN DATES ONTO THE 2020 GRAPH TO SEE IF THERE IS A SPIKE IN THE DATA    


    tabControl.add(LONDONTAB, text ='London - Air Pollution Data')       #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY     
    tabControl.add(MADRIDTAB, text ='Madrid - Air Pollution Data')       #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(MILANTAB, text ='Milan - Air Pollution Data')         #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(BERLINTAB, text ='Berlin - Air Pollution Data')       #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(BARCELONATAB, text ='Barcelona - Air Pollution Data') #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.add(AMSTERDAMTAB, text ='Amsterdam - Air Pollution Data') #GIVING THE TAB ITS SPECIFIC NAME REGARDING THE CITY
    tabControl.pack(expand = 1, fill ="both")                            #ACTUALLY DISPLAYING THE DIFFERNT TABS
    
MenuMain()
