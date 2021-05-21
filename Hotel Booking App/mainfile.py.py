from tkinter import *
from tkinter import ttk
import login
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1234', database = 'hotel')

def click():
    entered_text1 = a.get()
    entered_text2 = b.get()
    entered_text3 = c.get()
    entered_text4 = d.get()
    entered_text5 = e.get()
    mycursor = mydb.cursor()
    sqlform = 'insert into bookings values(%s, %s, %s, %s, %s)'
    visitors = [(entered_text1, int(entered_text2), int(entered_text3), entered_text4, entered_text5)]
    mycursor.executemany(sqlform, visitors)
    mydb.commit()
    output.delete(0.0, END)
    output.insert(END, entered_text1 + " You are Booked!")
    
def click1():
    entered_name = check_out_name.get()
    entered_number = int(check_out_number.get())
    mycursor = mydb.cursor()
    sqlform1 = 'delete from bookings where name = %s and phoneNumber = %s'
    delete = [(entered_name, entered_number)]
    mycursor.executemany(sqlform1, delete)
    mydb.commit()
    output1.delete(0.0, END)
    output1.insert(END, entered_name + " Thanks for the stay")

def click2():
    login.loginscreen()
    
window = Tk()
window.title("Booking Window")  

logo = PhotoImage(file = "Hotel logo.png")
Label(window, image = logo, bg = "black").grid(row = 0, column = 0, sticky = W)

booking = PhotoImage(file = "Booking.png")
Label(window, image = booking, bg = "black").grid(row = 1, column = 0, sticky = W)

check_out = PhotoImage(file = 'x.png')
Label(window, image = check_out, bg = "black").grid(row = 1, column = 5, sticky = W)

window.configure(background = "black")

Label(window, text = 'Enter Name: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 2, column = 0, sticky = W)
a = Entry(window, width = 20, bg = "White")
a.grid(row = 3, column = 0, sticky = W)

Label(window, text = 'Enter Room Number: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 5, column = 0, sticky = W)
b = Entry(window, width = 20, bg = "White")
b.grid(row = 6, column = 0, sticky = W)

Label(window, text = 'Phone Number: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 8, column = 0, sticky = W)
c = Entry(window, width = 20, bg = "White")
c.grid(row = 9, column = 0, sticky = W)

Label(window, text = 'Check In Date ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 11, column = 0, sticky = W)
d = Entry(window, width = 20, bg = "White")
d.grid(row = 12, column = 0, sticky = W)

Label(window, text = 'Check Out Date ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 14, column = 0, sticky = W)
e = Entry(window, width = 20, bg = "White")
e.grid(row = 15, column = 0, sticky = W)

Button(window, text = 'Submit', width = 6, command = click).grid(row = 20, column = 0, sticky = W)

output = Text(window, width = 40, height = 1,wrap = WORD, background = "white")
output.grid(row = 25, column = 0, sticky = W)

Label(window, text = 'Enter Name: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 2, column = 5, sticky = W)
check_out_name = Entry(window, width = 20, bg = "White")
check_out_name.grid(row = 3, column = 5, sticky = W)

Label(window, text = 'Enter Phone Number: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 5, column = 5, sticky = W)
check_out_number = Entry(window, width = 20, bg = "White")
check_out_number.grid(row = 6, column = 5, sticky = W)

Button(window, text = 'Submit', width = 6, command = click1).grid(row = 8, column = 5, sticky = W)

output1 = Text(window, width = 40, height = 1,wrap = WORD, background = "white")
output1.grid(row = 10, column = 5, sticky = W)

Button(window, text = 'Show All Bookings', width = 17, command = click2).grid(row = 1, column = 9, sticky = W)

def close_window():
    window.destroy()
    exit()

Label(window, text = 'Click to exit: ', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 26, column = 0, sticky = W)
Button(window, text = 'Exit', width = 14, command = close_window).grid(row = 27, column = 0, sticky = W)

window.mainloop()
