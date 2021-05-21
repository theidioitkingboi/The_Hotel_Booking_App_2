from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1234', database = 'hotel')

def loginscreen():
    username = "a"
    password = "a"

    def close_window():
        window2.destroy()
    
    def click():
        entered_text1 = a.get()
        entered_text2 = b.get()
        if username == entered_text1 and password == entered_text2:
            close_window()
            mycursor = mydb.cursor()
            sqlform2 = 'select * from bookings'
            mycursor.execute(sqlform2)
            records = mycursor.fetchall()
            total = mycursor.rowcount
            print("Total Bookings: " + str(total))
            
            window1 = Tk()
            window1.title("All Bookings")
            window1.geometry('650x500')
            window1.configure(background = "black")

            frm = Frame(window1)
            frm.pack()

            tv = ttk.Treeview(frm, columns = (1, 2, 3, 4, 5), show = 'headings', height = '5')
            tv.pack()

            tv.heading(1, text = "Name")
            tv.heading(2, text = "Room Number")
            tv.heading(3, text = "Phone Number")
            tv.heading(4, text = "Check In Date")
            tv.heading(5, text = "Check Out Date")
            print(records)
            for i in records:
                tv.insert('', 'end', values = i)

            window1.mainloop()
                    
        else:
            messagebox.showerror("Error", "Invalid Username/Password")

    window2 = Tk()
    window2.title("Login to look at all the bookings")
    window2.geometry("300x200")
    window2.configure(background = "black")

    Label(window2, text = 'Username', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 2, column = 0, sticky = W)
    a = Entry(window2, width = 20, bg = "White")
    a.grid(row = 3, column = 0, sticky = W)

    Label(window2, text = 'Password', bg = "black", fg = 'white', font = "arial 12 bold").grid(row = 5, column = 0, sticky = W)
    b = Entry(window2, width = 20, bg = "White")
    b.grid(row = 6, column = 0, sticky = W)

    Button(window2, text = 'Submit', cursor = "hand2", width = 6, command = click).grid(row = 7, column = 0, sticky = E)

    window2.mainloop()
