from tkinter import *

FONT = "Arial",14,"bold"

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=30)

inputText = Entry(width=10)
inputText.insert("end",string="0")
inputText.grid(column=1,row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal", font=FONT)
is_equal_label.grid(column=0, row=1)

placehold_label = Label(text="0", font=FONT)
placehold_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)


def calculation():
    value_in_miles = float(inputText.get())
    value = value_in_miles * 1.609
    placehold_label["text"] = value


button = Button(text="Calculate", font=("Arial",18,"bold"), command=calculation)
button.grid(column=1,row=2)



window.mainloop()
