#Aptiekas kases aparāts
#Funkcijas:
#Ievadīt preču skaitu, Aprēķīnā pirkuma summu, Pievieno atlaidi pie pirkuma, Izveido un izdruka čeku, Radā pirkumu ar PVN

from tkinter import *  
logs = Tk() 
logs.title('Kases aparāts')
logs.geometry('1150x670')
logs.configure(bg = 'aquamarine')

#rindu nosaukumi
Zales = LabelFrame(logs, text = 'Par zālem', font = ('Book Antiqua', 18, 'bold', 'italic'), fg = 'orange', bg = 'aquamarine')
Zales.place(x=5, y=10, width=700,height=500)

preces = Label(Zales, text = 'Zales', font = ('Calibri', 20, 'bold', 'italic'), fg = 'blue', bg = 'aquamarine')
preces.grid(row=0,column=0,padx=20,pady=15)

Preces_skaits = Label(Zales, text = 'Preču skaits', font = ('Calibri', 20, 'bold', 'italic'), fg = 'blue', bg = 'aquamarine')
Preces_skaits.grid(row=0,column=1,padx=20,pady=15)

cena = Label(Zales, text = 'Cena', font = ('Calibri', 20, 'bold', 'italic'), fg = 'blue', bg = 'aquamarine')
cena.grid(row=0,column=2,padx=20,pady=15)

#Produktu saraksts
Nurofen=Label(Zales, text = 'Nurofen', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
Nurofen.grid(row=1,column=0,padx=10,pady=15)
N_sk = Entry(Zales, font = 'Helvetica 15 bold', relief = SUNKEN, bd=6, justify = CENTER)
N_sk.grid(row=1,column=1,padx=9,pady=15)
N_cena = Label(Zales, text = '5,81 eiro', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
N_cena.grid(row=1,column=2,padx=9,pady=15)

Paracetamol=Label(Zales, text = 'Paracetamol', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
Paracetamol.grid(row=2,column=0,padx=9,pady=15)
P_sk = Entry(Zales, font = 'Helvetica 15 bold', relief = SUNKEN, bd=6, justify = CENTER)
P_sk.grid(row=2,column=1,padx=9,pady=15)
P_cena = Label(Zales, text = '2,09 eiro', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
P_cena.grid(row=2,column=2,padx=9,pady=15)

Xyzal=Label(Zales, text = 'Xyzal', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
Xyzal.grid(row=3,column=0,padx=9,pady=15)
X_sk = Entry(Zales, font = 'Helvetica 15 bold', relief = SUNKEN, bd=6, justify = CENTER)
X_sk.grid(row=3,column=1,padx=9,pady=15)
X_cena = Label(Zales, text = '13,95 eiro', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
X_cena.grid(row=3,column=2,padx=9,pady=15)

Espumizan=Label(Zales, text = 'Espumizan', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
Espumizan.grid(row=4,column=0,padx=10,pady=15)
E_sk = Entry(Zales, font = 'Helvetica 15 bold', relief = SUNKEN, bd=6, justify = CENTER)
E_sk.grid(row=4,column=1,padx=9,pady=15)
E_cena = Label(Zales, text = '8,76 eiro', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
E_cena.grid(row=4,column=2,padx=9,pady=15)

Strepsils=Label(Zales, text = 'Strepsils', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
Strepsils.grid(row=5,column=0,padx=10,pady=15)
S_sk = Entry(Zales, font = 'Helvetica 15 bold', relief = SUNKEN, bd=6, justify = CENTER)
S_sk.grid(row=5,column=1,padx=9,pady=15)
S_cena = Label(Zales, text = '5,03 eiro', font = ('Helvetica',15,'bold'), fg = 'dodger blue', bg = 'aquamarine')
S_cena.grid(row=5,column=2,padx=9,pady=15)

#čeks
Ceks = Frame(logs, relief = GROOVE, bd=10, bg = 'white')
Ceks.place(x=750, y=10, width=350, height=640)
Ceks_nosaukums = Label(Ceks, text = 
"""Meness Aptieka
A/S SENTOR FARM APTIEKAS
Stacijas laukums 2, Rīga, LV-1050""", font = 'Helvetica 10', bd=6, bg = 'white').pack()
CEKS = Scrollbar(logs, orient = VERTICAL)
CEKS.pack(side = RIGHT, fill = Y)

#pogas
Poga = LabelFrame(logs, relief = GROOVE, bd=10, bg = 'aquamarine')
Poga.place(x=5, y=530, width=700, height=120)

poga1 = Button(Poga, text = 'Kopā', font = 'Helvetica 13 bold', bg = 'gold', fg = 'crimson')
poga1.grid(row=0, column=0,padx=10,pady=20)


logs.mainloop()