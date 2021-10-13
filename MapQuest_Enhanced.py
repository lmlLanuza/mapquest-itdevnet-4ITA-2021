from tkinter import*
root = Tk()
root.geometry("500x500")
root.title("Map Quest")


heading = Label(text="Map Quest", bg ="black", fg="white", width="500", height="3")
heading.pack()

LabelLocation = Label(text="Enter your Current Location* ", font="Arial 15")
location = Entry(root, width=50)

LabelDestination = Label(text="Enter your Destination Location* ", font="Arial 15")
destination = Entry(root, width=50)
LabelLocation.pack()
location.pack()


def myClick():
    hello = "Your current Location is " + location.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
myButton = Button(root, text="Submit", command=myClick)

myButton.pack()
def myClick2():
    hello2 = "Your Destination Location is " + destination.get()
    myLabel2 = Label(root, text=hello2)
    myLabel2.pack()

LabelDestination.pack()
destination.pack()
myButton2 = Button(root, text="Submit", command=myClick2)

myButton2.pack()

root.mainloop()