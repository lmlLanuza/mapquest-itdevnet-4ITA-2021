import tkinter as tk 
from tkinter import ttk
from tkinter import *
import urllib.parse
import requests
import sys
import os


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "YXcZ6xIdAdBfJEijDlGasOPJoGrqf9GV"  
root= tk.Tk() 
root.geometry("1500x1000")

main_frame = tk.Frame(root)
main_frame.pack(fill=BOTH, expand=1)

canvas1 = tk.Canvas(main_frame)
canvas1.pack(side=LEFT, fill=BOTH, expand=1)

second_frame = tk.Frame(canvas1)
canvas1.create_window((170,200), window=second_frame, anchor="nw")

location = tk.Label(root, text='Type your Location: ')
canvas1.create_window(100, 50, window=location)
entry1 = tk.Entry (root)

destination = tk.Label(root, text='Type your Destination: ')
canvas1.create_window(107, 100, window=destination)
entry2 = tk.Entry (root)

canvas1.create_window(270, 50, window=entry1)
canvas1.create_window(270, 100, window=entry2)

#Two radio buttons to select unit of measurement
#Variable that will store the selected value of chosen Radio button
selected = tk.StringVar()

metric = tk.Radiobutton(root, text = "Metric", variable = selected, value = "metric")
canvas1.create_window(90, 150, window=metric)

imperial = tk.Radiobutton(root, text = "Imperial", variable = selected, value = "imperial")
canvas1.create_window(250, 150, window=imperial)

def button():
    #gets values and translates
    global destination
    global location
    location = entry1.get()
    destination = entry2.get()
    while True:
        url = main_api + urllib.parse.urlencode({"key":key, "from":location, "to":destination})
        print ("URL ", (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            argument = "\nAPI Status: " + str(json_status) + " = A successful route call.\n"\
            "============================================="+ "\nDirections from " + (location) + " to " + (destination)\
            +"\nTrip Duration: " + (json_data["route"]["formattedTime"])\
            +"\nKilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6))\
            +"\nFuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))\
            + "\n=============================================\n"
            Label1 = tk.Label(root, text= argument,font="Times 15")
            canvas1.create_window(900, 100, window=Label1)
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                argument2 = (each["narrative"]) + "(" + ("{:.2f}".format((each["distance"])*1.61) + " km)")
                Label2 = tk.Label(second_frame, text= argument2, font="Times 15",anchor='n').pack(fill='both')
               
            
        elif json_status == 402:
            argument3 ="***Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations."\
            +"***\n"
            Label3 = tk.Label(root, text= argument3, bg='yellow')
            canvas1.create_window(900, 50, window=Label3)
        
        elif json_status == 611:
            argument4 ="**********************************************"\
            + "Status Code: " + str(json_status) + "; Missing an entry for one or both locations."\
            +"**********************************************\n"
            Label4 = tk.Label(root, text= argument4, bg='yellow')
            canvas1.create_window(900, 50, window=Label4)

        else:
            argument5 ="************************************************************************"\
            + "For Staus Code: " + str(json_status) + "; Refer to:"\
            + "https://developer.mapquest.com/documentation/directions-api/status-codes"\
            + "************************************************************************\n"   
            Label5 = tk.Label(root, text= argument5, bg='yellow')
            canvas1.create_window(900, 50, window=Label5)
        break



def clear():
    #clears all values
    python = sys.executable
    os.execl(python, python, * sys.argv)


#Submits the Values
button1 = tk.Button (root, text='Find your Destination',command=button, bg='orange', width = 20) # button to call the 'values' command above 
canvas1.create_window(270,220, window=button1)

#Clears any input fields
ButtonClear=Button(root, text="Clear", command=clear, bg='orange', width = 20)
canvas1.create_window(270,270, window=ButtonClear)

#Closes the Program
button_quit = Button(root, text="Quit", command=root.destroy, bg='orange', width = 20)
canvas1.create_window(270,320, window=button_quit)

root.mainloop()