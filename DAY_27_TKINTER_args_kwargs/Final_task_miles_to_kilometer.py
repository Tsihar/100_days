from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

miles_text = Label(text="Miles", font=("Arial", 10))
miles_text.grid(column=2, row=0)

equal_to = Label(text="is equal to", font=("Arial", 10))
equal_to.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 10))
result.grid(column=1, row=1)
# result.config(pady=0, padx=10)

km = Label(text="Km", font=("Arial", 10))
km.grid(column=2, row=1)

def calculation():
    miles = int(input_miles.get())
    kilometers = round((miles * 1.609), 1)
    result.config(text=kilometers)

button_calc = Button(text='Calculate', command=calculation)
button_calc.grid(column=1, row=2)

window.mainloop()