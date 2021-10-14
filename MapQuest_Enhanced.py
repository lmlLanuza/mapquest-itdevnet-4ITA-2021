from tkinter import*
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "YXcZ6xIdAdBfJEijDlGasOPJoGrqf9GV"    # You should use your own key 
root = Tk()
root.geometry("1000x1000")
root.title("Map Quest")

heading = Label(text="Map Quest", bg ="black", fg="white", width="500", height="3")
heading.pack()

LabelLocation = Label(text="Enter your Current Location* ", font="Arial 15")
location = Entry(root, width=50)

LabelDestination = Label(text="Enter your Destination Location* ", font="Arial 15")
destination = Entry(root, width=50)
LabelLocation.pack()
location.pack()

LabelDestination.pack()
destination.pack()
def myClick():
    while True:

        url = main_api + urllib.parse.urlencode({"key":key, "from":location, "to":destination})
        print ("URL ", (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            argument = "\nAPI Status: " + str(json_status) + " = A successful route call.\n"\
            "\n============================================="+ "\nDirections from " + (location.get()) + " to " + (destination.get())\
            +"\nTrip Duration: " + (json_data["route"]["formattedTime"])\
            +"\nKilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6))\
            +"\nFuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))\
            + "\n============================================="
            myLabel = Label(root, text=argument)
            myLabel.pack()
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                argument2 = (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")
                myLabel2 = Label(root, text=argument2,font="Times 10",justify=LEFT)
                myLabel2.pack()
        elif json_status == 402:
            argument3 ="**********************************************"\
            +"Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations."\
            +"**********************************************\n"
            myLabel3 = Label(root, text=argument3)
            mylabel3.pack()
        elif json_status == 611:
            argument4 ="**********************************************"\
            + "Status Code: " + str(json_status) + "; Missing an entry for one or bothlocations."\
            +"**********************************************\n"
            myLabel4 = Label(root, text=argument4)
            mylabel4.pack()
        else:
            argument5 ="************************************************************************"\
            + "For Staus Code: " + str(json_status) + "; Refer to:"\
            + "https://developer.mapquest.com/documentation/directions-api/status-codes"\
            + "************************************************************************\n"   
            myLabel5 = Label(root, text=argument5)
            mylabel5.pack()
        break
       
    
myButton = Button(root, text="Submit", command=myClick)
myButton.pack()

  
root.mainloop()