import tkinter as tk 
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "YXcZ6xIdAdBfJEijDlGasOPJoGrqf9GV"  
root= tk.Tk() 
root.geometry("1500x1500")
 
canvas1 = tk.Canvas(root, width = 1000)
canvas1.pack()

canvas2 = tk.Canvas(root, width = 1000)
canvas2.pack()


location = tk.Label(root, text='Type your Location: ')
canvas1.create_window(0, 50, window=location)
entry1 = tk.Entry (root)

destination = tk.Label(root, text='Type your Destination: ')
canvas1.create_window(0, 100, window=destination)
entry2 = tk.Entry (root)
canvas1.create_window(200, 50, window=entry1)
canvas1.create_window(200, 100, window=entry2)

def button():
    global destination
    global location
    location = entry2.get()
    destination = entry1.get()
  # You should use your own key 
    while True:
        url = main_api + urllib.parse.urlencode({"key":key, "from":location, "to":destination})
        print ("URL ", (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            argument = "\nAPI Status: " + str(json_status) + " = A successful route call.\n"\
            "\n============================================="+ "\nDirections from " + (location) + " to " + (destination)\
            +"\nTrip Duration: " + (json_data["route"]["formattedTime"])\
            +"\nKilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6))\
            +"\nFuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))\
            + "\n=============================================\n"
            Label1 = tk.Label(root, text= argument, bg='yellow')
            canvas1.create_window(700, 100, window=Label1)
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                argument2 = (each["narrative"]) + " \n(" + ("{:.2f}".format((each["distance"])*1.61) + " km)")
                Label2 = tk.Label(root, text= argument2, bg='yellow')
                canvas2.create_window(700,0,window=Label2)
                
        elif json_status == 402:
            argument3 ="**********************************************"\
            +"Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations."\
            +"**********************************************\n"
            Label3 = tk.Label(root, text= argument3, bg='yellow')
            canvas1.create_window(500, 200, window=Label3)
        
        elif json_status == 611:
            argument4 ="**********************************************"\
            + "Status Code: " + str(json_status) + "; Missing an entry for one or bothlocations."\
            +"**********************************************\n"
            Label4 = tk.Label(root, text= argument4, bg='yellow')
            canvas2.create_window(500, 200, window=Label4)

        else:
            argument5 ="************************************************************************"\
            + "For Staus Code: " + str(json_status) + "; Refer to:"\
            + "https://developer.mapquest.com/documentation/directions-api/status-codes"\
            + "************************************************************************\n"   
            Label5 = tk.Label(root, text= argument5, bg='yellow')
            canvas2.create_window(500, 200, window=Label5)
     
        break

button1 = tk.Button (root, text='Find your Destination',command=button, bg='orange') # button to call the 'values' command above 
canvas1.create_window(200,150, window=button1)
 

root.mainloop()