"""
OPAKEEPERS(c) 2024
"""
import sqlite3
from tkinter import *
from tkinter.messagebox import *
def creobj():
    name = asne.get()
    age = asas.get()
    class_ = asce.get()
    grade = asgs.get()
    c.execute(f"""INSERT INTO students VALUES (
              '{name}',
              {age},
              '{class_}',
              {grade}
              )""")
    conn.commit()
def reaobj():
    name = lse.get()
    c.execute("SELECT * FROM students")
    li = c.fetchall()
    for count, i in enumerate(li):
        if name == li[count][0]:  
            n = name
            a = li[count][1]
            c_ = li[count][2]
            g = li[count][3]
            showinfo('MADE WITH SQLITE>~-<SQLuni>-~-<Popup>-~<MADE WITH SQLITE', f"""the student is {n}\nHis/her age is {a}\nHe/She is a {c_} grader\nShe/He (this year) got a {g}""")
#conection
conn = sqlite3.connect("StudentDatabase.db")
c = conn.cursor()
#Creating the window and naming it
win = Tk()
win.title("MADE WITH SQLITE>~-<SQLuni>-~-<Window>-~<MADE WITH SQLITE")
win.configure(bg="#007339")
#Making the LOAD STUDENT labelframe, label, entry, and button
lslf = LabelFrame(win, text="Load from Database", bg="#007339", fg="black")
lslf.grid(column = 0, row = 0, padx=20, pady=20)
lsl = Label(lslf, text="Student name", bg="#007339")
lsl.grid(column=0, row=0, padx=20, pady=20)
lse = Entry(lslf, bg="#007339")
lse.grid(column=0, row=2, padx=20, pady=20)
lsb = Button(lslf, text="LOAD FROM DATABASE", bg="#007339", activebackground="blue", padx=20, pady=20, command=reaobj)
lsb.grid(column=1, row=1, padx=40, pady=20)
#Making the ADD student Labelframe, LABELS, ENTRYS and a button
aslf = LabelFrame(win, text="Add to Database", bg="#007339", fg="black")
aslf.grid(column = 1, row = 0, padx=20, pady=20)
asnl = Label(aslf, text="Name", bg="#007339")
asnl.grid(column=0, row=0, pady=20, padx=20)
asne = Entry(aslf, bg="#007339")
asne.grid(column=0, row=1, pady=20, padx=20)
asal = Label(aslf, text="Age", bg="#007339")
asal.grid(column=1, row=0, pady=20, padx=20)
asas = Spinbox(aslf, bg="#007339", from_=17, to=25)
asas.grid(column=1, row=1, pady=20, padx=20)
ascl = Label(aslf, text="Class(1-∞)", bg="#007339")
ascl.grid(column=3, row=0, pady=20, padx=20)
asce = Entry(aslf, bg="#007339")
asce.grid(column=3, row=1, pady=20, padx=20)
asgl = Label(aslf, text="Grade(1-100)", bg="#007339")
asgl.grid(column=4, row=0, pady=20, padx=20)
asgs = Spinbox(aslf, bg="#007339", from_=1, to=100)
asgs.grid(column=4, row=1, pady=20, padx=20)
ASB = Button(aslf, text="Create table in database", padx=20, pady=20,command=creobj, bg="#007339")
ASB.grid(column=2, row=2)
win.mainloop()