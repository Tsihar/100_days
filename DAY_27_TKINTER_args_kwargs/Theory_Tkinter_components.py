from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.") # END - это штука на которую ссылается tkinter, не надо ее трогать, она должна быть
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END)) # 1.0 значит, получить текст начиная с первой строки и с 0-вого символа
text.pack()

#Spinbox - нажимаешь на стрелочки увеличивая или уменьшая текущее значение в поле
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale - дрэгдропный регулятор, тянешь вверх или вниз увеличивая или уменьшая значение
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar() # этот объект является параметром в объекте checkbutton, ткинтер так отслеживает состояние чекбокса 1 или 0
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get()) # выводит текущий чекнутый радиобатон 1 или 2
#Variable to hold on to which radio button value is checked.
radio_state = IntVar() # этот объект является параметром в объекте radiobutton1 и radiobutton2, ткинтер так отслеживает состояние радиобатона, какой чекнут в данный момент
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4) # 4 значения
fruits = ["Apple", "Pear", "Orange", "Banana"] # список
for item in fruits:
    listbox.insert(fruits.index(item), item) # вставляет каждый элемент в listbox исходя из индекса и его значения в начальном списке fruits
listbox.bind("<<ListboxSelect>>", listbox_used) # вызывает функцию которая выведет текущеее выбранной значение в списке
listbox.pack()
window.mainloop()