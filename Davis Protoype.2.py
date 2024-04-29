#Davis weather app prototype 
from tkinter import *
from tkinter import messagebox 


def openNewWindow():
    global NewWindow

    #Creates a new window using Toplevel
    NewWindow = Toplevel(master_window)

    #Sets the title of Toplevel widget
    NewWindow.title("Dave's weather app")

    #Sets the geometry of Toplevel
    NewWindow.geometry('350x350')

#Label widget to show in Toplevel
    Label(NewWindow, text = "Temperature Conversion", fg = 'gold', bg = 'dark blue', font = ('bold, 12')).pack()

#Configures window color
    NewWindow.configure(bg = 'dark blue')

#Temperature input block that allows the user to input a number within the program
    label = Label(NewWindow, text = "Enter Temperature:").pack()

    entry = Entry(NewWindow).pack()

    #Convert button acts as an enter key and allows the program to process the number
    convert_btn = Button(NewWindow, text = "Convert", command = convert_temperature).pack()

    #Result label outputs
    result_label = Label(NewWindow, text = "").pack()

#Defines the formula to convert Celsius to Fahrenheit
def Celsius_to_Fahrenheit(Celsius):
    return (1.8) * Celsius + 32
#Defines the formula to convert Fahrenheit to Celsius
def Fahrenheit_to_Celsius(Fahrenheit):
    return (0.55) * (Fahrenheit - 32)


  







#Main NewWindow welcome screen
master_window = Tk()
master_window.title("Welcome Screen")
master_window.configure(bg = 'dark blue')
master_window.geometry('200x200')


#Welcome label for the master window
label = Label(master_window, text = "Welcome!")
label.pack( pady = 10)

#Button to open Dave's weather app 
btn1 = Button(master_window, text = "Click to open Dave's Weather app", command = openNewWindow)
btn1.pack(expand = True)

#Welcome screen exit button
btn2 = Button(master_window, text = "Exit", command = exit)
btn2.pack(expand = True)


mainloop()