import tkinter


# My first GUI programm


# creating a new window and configurations
window = tkinter.Tk()
window.title("My first GUI programm")
window.minsize(width=500, height= 300)
window.config(padx=20,pady=20) #padding


# label - text
my_label = tkinter.Label(text="This is old text",font=("Arial",24,"bold")) #create label
my_label['text'] = 'This is new text'  #access to text property
# my_label.pack(side="bottom") #place label into the screen and centered
my_label.place(x=0, y=0)
# my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50) #padding

# button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="New New Text") #access to text property
    my_label.config(text=inputEntry.get())

#calls action() when pressed
button = tkinter.Button(text="Click me", command=button_clicked) # without ()
button.pack()


# input - entry
inputEntry = tkinter.Entry(width=10)
inputEntry.insert("end", string="Some text to begin with.") #Add some text to begin with
inputEntry.get()   #return the input
print( inputEntry.get() )
inputEntry.pack()


#  text entry box
text = tkinter.Text(height=5, width=30)
text.focus() #Puts cursor in textbox.
text.insert("end", "Example of multi-line text entry.") #Adds some text to begin with.
print(text.get("1.0", "end")) #Get's current value in textbox at line 1, character 0
text.pack()


# spinbox
def spinbox_used():
    print(spinbox.get()) #gets the current value in spinbox.
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# scale
def scale_used(value): #Called with current scale value.
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# checkbox
def checkbutton_used():
    print(checked_state.get()) #Prints 1 if On button checked, otherwise 0.
checked_state = tkinter.IntVar() #variable to hold on to checked state, 0 is off, 1 is on.
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# radiobtn
def radio_used():
    print(radio_state.get()) #Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection())) # Gets current selection from listbox
listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop() # keep wimdow on screen and listen to user's actions
