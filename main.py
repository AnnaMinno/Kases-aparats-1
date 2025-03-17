#Aptiekas kases aparāts
#Funkcijas:
#Ievadīt preču skaitu, Aprēķīnā pirkuma summu, Pievieno atlaidi pie pirkuma, Izveido un izdruka čeku, Radā pirkumu ar PVN

from tkinter import *
from tkinter import messagebox

logs = Tk()
logs.title('Kases aparāts')
logs.geometry('1150x700')
logs.configure(bg='aquamarine')
x = []

#Pogas 1-0 un Backspace
Kalkulators = LabelFrame(logs, bg='aquamarine', relief=GROOVE, bd=10)
Kalkulators.place(x=5, y=10, width=700, height=500)

ievads = Label(Kalkulators, font="Helvetica 40 bold", relief=GROOVE, bd=10)
ievads.config(width=9, anchor="w", bg="white")
ievads.place(x=10, y=10)


def ciparsKlik(event):
    cipars = event.widget["text"]
    ievads["text"] = ievads["text"] + str(cipars)


cipari = []
skaitli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in range(10):
    cipari.append(
        Button(Kalkulators,
               text=skaitli[i],
               fg="white",
               bg="royal blue",
               width=3,
               font="Helvetica 20 bold"))
    cipari[i].place(x=100 + 90 * (i % 3), y=150 + 70 * (i // 3), anchor=CENTER)
    cipari[i].bind('<Button-1>', ciparsKlik)


def cKlik():
    global x
    ievads["text"] = str("")
    x.clear()


Backspace = Button(Kalkulators,
                   text='Dzēst',
                   font='Helvetica 19 bold',
                   bg='light slate blue',
                   fg='snow',
                   width=8)
Backspace.place(x=150, y=337)
Backspace.config(command=cKlik)

#Pogas (Total, Zales, Pirkumi, atlaide)
Pogas = Frame(Kalkulators, bg='aquamarine')
Pogas.place(x=440, y=0, width=200, height=480)


def ZalesKlik():
    global x
    global ZalesCeks
    ZalesCeks = ievads["text"]
    ZaleCeksOutput = Label(Ceks,
                           text=f'\nZales\t\t\t{ZalesCeks}€',
                           font='Helvetica 10',
                           bd=6,
                           bg='white').pack()
    ievads["text"] = str("")
    x.clear


Zales = Button(Pogas,
               text='Zāles',
               font='Helvetica 20 bold',
               bg='gold',
               fg='crimson')
Zales.grid(row=0, column=0, padx=10, pady=30)
Zales.config(command=ZalesKlik)


def PirkumiKlik():
    global x
    global PirkumiCeks
    PirkumiCeks = ievads["text"]
    PirkumiCeksOutput = Label(Ceks,
                              text=f'\nPirkumi\t\t\t{PirkumiCeks}€',
                              font='Helvetica 10',
                              bd=6,
                              bg='white').pack()
    ievads["text"] = str("")
    x.clear


Pirkumi = Button(Pogas,
                 text='Pirkumi',
                 font='Helvetica 20 bold',
                 bg='gold',
                 fg='crimson')
Pirkumi.grid(row=1, column=0, padx=10, pady=30)
Pirkumi.config(command=PirkumiKlik)


def TotalKlik():
    global PirkumiCeks
    global ZalesCeks
    global AtlaideCeks

    KopaCeks = (int(PirkumiCeks) + int(ZalesCeks) - int(AtlaideCeks))

    PVN12 = ZalesCeks
    PVN21 = PirkumiCeks

    PVNOutput_1 = Label(
        Ceks,
        text=
        """------------------------------------------------------------------------------""",
        font='Helvetica 10 bold',
        bd=6,
        bg='white').pack()
    PVN12_Output = Label(Ceks,
                         text=f'\nPreces ar PVN 12%\t\t\t{PVN12}€',
                         font='Helvetica 10',
                         bd=6,
                         bg='white').pack()
    PVN21_Output = Label(Ceks,
                         text=f'\nPreces ar PVN 21%\t\t\t{PVN21}€',
                         font='Helvetica 10',
                         bd=6,
                         bg='white').pack()
    PVNOutput_3 = Label(
        Ceks,
        text=
        """------------------------------------------------------------------------------""",
        font='Helvetica 10 bold',
        bd=6,
        bg='white').pack()
    KopaCeksOutput1 = Label(
        Ceks,
        text=
        """------------------------------------------------------------------------------""",
        font='Helvetica 10 bold',
        bd=6,
        bg='white').pack()
    KopaCeksOutput2 = Label(Ceks,
                            text=f'\nSumma\t\t\t{KopaCeks}€',
                            font='Helvetica 10',
                            bd=6,
                            bg='white').pack()
    AtlaideCeksOutput3 = Label(
        Ceks,
        text=
        """------------------------------------------------------------------------------""",
        font='Helvetica 10 bold',
        bd=6,
        bg='white').pack()


Total = Button(Pogas,
               text='Kopā',
               font='Helvetica 20 bold',
               bg='gold',
               fg='crimson')
Total.grid(row=3, column=0, padx=10, pady=30)
Total.config(command=TotalKlik)


def AtlaideKlik():
    global PirkumiCeks
    global ZalesCeks
    global AtlaideCeks

    Atlaide = ((int(PirkumiCeks) + int(ZalesCeks)) / 100 * 20)
    AtlaideCeks = round(Atlaide, 2)

    AtlaideCeksOutput1 = Label(
        Ceks,
        text=
        """------------------------------------------------------------------------------""",
        font='Helvetica 10 bold',
        bd=6,
        bg='white').pack()
    AtlaideCeksOutput2 = Label(
        Ceks,
        text=f'\nAtlaide ar Klienta karti\t\t-{AtlaideCeks}€',
        font='Helvetica 9',
        bd=6,
        bg='white').pack()
    AtlaideCeksOutput3 = Label(
        Ceks,
        text=
        """"------------------------------------------------------------------------------""",
        font='Helvetica 10 bold',
        bd=6,
        bg='white').pack()


Atlaide = Button(Pogas,
                 text='Atlaide',
                 font='Helvetica 20 bold',
                 bg='gold',
                 fg='crimson')
Atlaide.grid(row=2, column=0, padx=25, pady=30)
Atlaide.config(command=AtlaideKlik)

#Ceks
Ceks = Frame(logs, relief=GROOVE, bd=10, bg='white')
Ceks.place(x=750, y=10, width=350, height=650)
Ceks_nosaukums = Label(Ceks,
                       text="""Zvaigznes Aptieka
A/S TINY FARM APTIEKAS
Stacijas laukums 2, Rīga, LV-1050""",
                       font='Helvetica 10',
                       bd=6,
                       bg='white').pack()
Ceks_nosaukums_zemlinija = Label(Ceks,
                                 text="""*****************************""",
                                 font='Helvetica 15 bold',
                                 bd=6,
                                 bg='white').pack()
CEKS = Scrollbar(logs, orient=VERTICAL)
CEKS.pack(side=RIGHT, fill=Y)
