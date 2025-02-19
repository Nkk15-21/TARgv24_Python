from queue import Empty
from tkinter import *
from Grafikud_Matplotlib import *
global värv

def värvi_valik():
    global värv
    värv = "black"  # Цвет по умолчанию
    if tekst.get() != "":
        tekst.configure(bg="yellow")
        värv = tekst.get()
    else:
        tekst.configure(bg="red")
    return värv



def figuur(värv:str):
    #värv = värvi_valik()  
    valik = var.get()
    if valik == 1:
        Kit(värv)
    elif valik == 2:
        Liblikas(värv)
    else:
        Vihmavari()
        print("Joonista hiljem")





aken=Tk()
aken.geometry("400x800")
aken.title("Graafikud")
pealkiri=Label(aken, text = "Erinevad pildid Matplotlib abil", font = "Algerian 24", fg = "green", bg = "yellow", pady=20, width=300)

var=IntVar()
r1=Radiobutton(aken, text="Kit", font = "Algerian 18", variable=var, value=1, command=lambda:figuur(värv=värvi_valik()))
r2=Radiobutton(aken, text="Liblikas", font = "Algerian 18", variable=var, value=2, command=lambda:figuur(värv=värvi_valik()))
r3=Radiobutton(aken, text="Vihmavari", font = "Algerian 18", variable=var, value=3, command=lambda:figuur(värv=värvi_valik()))
tekst=Entry(aken, font = "Algerian 24", fg = "green", bg = "yellow", width=100)
nupp=Button(aken, text="Värvi valik", font="Alderian 20", command=värvi_valik)



pealkiri.pack()
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()

