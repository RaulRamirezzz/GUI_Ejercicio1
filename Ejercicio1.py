from tkinter import *
from tkinter import ttk

raiz=Tk()
raiz.title('Ejercicio1')
raiz.geometry("600x450")

#-------------------------------------------------------------------------------------------------------------------

# Crear un notebook (panel tabulado)
tabPanel = ttk.Notebook(raiz)

# Crear pestañas dentro del notebook
add = ttk.Frame(tabPanel)
delete = ttk.Frame(tabPanel)
search = ttk.Frame(tabPanel)
services = ttk.Frame(tabPanel)
help = ttk.Frame(tabPanel)

# Agregar las pestañas al notebook
tabPanel.add(add, text="                Add               ")
tabPanel.add(delete, text="             Delete               ")
tabPanel.add(search, text="             Search               ")
tabPanel.add(services, text="               Services               ")
tabPanel.add(help, text="               Help               ")

# Empaquetar el notebook en la ventana
tabPanel.pack(expand=True, fill="both")

style = ttk.Style()
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "sky blue", "foreground": "black"},
        "map": {"background": [("selected", "dodger blue")], "foreground": [("selected", "white")]}
    }
})
style.theme_use("MyStyle")

#--------------------------------------------- FRAME 1 ------------------------------------------------------------------------------
Frame1 = ttk.Frame(add, padding="5 5 5 5", relief="groove")
Frame1.grid(column=0, row=1, pady=0)
ttk.Label (Frame1, text="").grid(column=0, row=0, padx=292, pady=10)

#--------------------------------------------- FRAME 2 ------------------------------------------------------------------------------
Frame2 = ttk.Frame(add, padding="10 5 87 5", relief="groove")
Frame2.grid(column=0, row=2, pady=0, sticky=(W))
ttk.Label (Frame2, text="First Name: ").grid(column=0, row=0, padx=10, pady=10, sticky=(W))
firstNameEntry = ttk.Entry(Frame2, width=25).grid(column=1, row=0, padx=10, pady=10, columnspan=3)
ttk.Label (Frame2, text="Birth Date: ").grid(column=0, row=1, padx=10, pady=10, sticky=(W))
ttk.Label (Frame2, text="Last Name: ").grid(column=4, row=0, padx=10, pady=10, sticky=(W))
lastNameEntry = ttk.Entry(Frame2, width=25).grid(column=5, row=0, padx=0, pady=10)
ttk.Label (Frame2, text="Country: ").grid(column=4, row=1, padx=10, pady=10, sticky=(W))
contryEntry = ttk.Entry(Frame2, width=15).grid(column=5, row=1, padx=0, pady=10, sticky=(W))

DiaBox = ttk.Combobox(Frame2, width=3)
DiaBox.grid(column=1, row=1, sticky=(W))
DiaBox['values'] = ("1","2","3","4","5","6","7","8",
                    "9","10","11","12","13","14","15",
                    "16","17","18","19","20","21","22",
                    "23","24","25","26","27","28","29",
                    "30","31")

MesBox = ttk.Combobox(Frame2, width=8)
MesBox.grid(column=2, row=1, sticky=(W), padx=2)
MesBox['values'] = ("January","February","March","April","May","June","July","August","September",
                    "Octuber","November","December")

AnoBox = ttk.Combobox(Frame2, width=5)
AnoBox.grid(column=3, row=1, sticky=(W), padx=2)
AnoBox['values'] = tuple(range(1900, 2024))


#--------------------------------------------- FRAME 3 ------------------------------------------------------------------------------
Frame3 = ttk.Frame(add, padding="10 5 292 5", relief="groove")
Frame3.grid(column=0, row=3, pady=0, sticky=(W))

ttk.Label (Frame3, text="Credit Card(if any): ").grid(column=0, row=0, padx=10, pady=10, sticky=(W))
cardEntry = ttk.Entry(Frame3, width=20).grid(column=1, row=0, padx=0, pady=10, columnspan=2)
ttk.Label (Frame3, text="Credit Card Type(if any): ").grid(column=0, row=1, padx=10, pady=10, sticky=(W))
ttk.Radiobutton(Frame3, text="Visa").grid(column=1, row=1, padx=5, pady=5, sticky=(W))
ttk.Radiobutton(Frame3, text="MasterCard").grid(column=2, row=1, padx=5, pady=5, sticky=(W))

#--------------------------------------------- FRAME 4 ------------------------------------------------------------------------------
Frame4 = ttk.Frame(add, padding="10 5 159 5", relief="groove")
Frame4.grid(column=0, row=4, pady=0, sticky=(W))

ttk.Label (Frame4, text="RoomType: ").grid(column=0, row=0, padx=10, pady=5)
ttk.Radiobutton(Frame4, text="Normal").grid(column=1, row=0, padx=10, pady=5, sticky=(W))
ttk.Radiobutton(Frame4, text="Familiar").grid(column=1, row=1, padx=10, pady=5, sticky=(W))
ttk.Radiobutton(Frame4, text="Special").grid(column=1, row=2, padx=10, pady=5, sticky=(W))
ttk.Label (Frame4, text="").grid(column=3, row=0, padx=35, pady=5)
ttk.Label (Frame4, text="Total Staying Time(days)").grid(column=4, row=0, padx=0, pady=5, sticky=(W))
stayingEntry = ttk.Entry(Frame4, width=5).grid(column=5, row=0, padx=10, pady=5)


#--------------------------------------------- FRAME 5 ------------------------------------------------------------------------------
Frame5 = ttk.Frame(add, padding="273 44 273 44", relief="groove")
Frame5.grid(column=0, row=5, pady=0)
boton = ttk.Frame(Frame5, padding="3 3 3 3", relief="groove")
boton.grid(column=0, row=0, pady=0, padx=0)
botonSubmit = ttk.Button(boton, text="Submit")
botonSubmit.grid(column=0, row=0, padx=0, pady=0)






raiz.mainloop()