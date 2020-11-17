import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk


def varIntDeclaration():
    var="Inicial"
    if var is not None:
        var = simpledialog.askstring("Input", "Insertar nombre de variable",parent=app)
        addValue = messagebox.askyesno("Question","¿Desea darle valor a? " + var)
        if addValue == True:
            varValue = simpledialog.askstring("Input", "Inserta valor de la variable",parent=app)
            text.insert(INSERT, "int " + var + "= " +varValue)
        else:
            text.insert(INSERT, "int " + var)
        anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
        while anotherVar != False:
            var = simpledialog.askstring("Input", "Insertar nombre de variable",parent=app)
            addValue = messagebox.askyesno("Question","¿Desea darle valor a? " + var)
            if addValue == True:
                varValue = simpledialog.askstring("Input", "Inserta valor de la variable",parent=app)
                text.insert(INSERT, ", " + var + "= " +varValue)
                anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
            else:
                text.insert(INSERT, ", " + var)
                anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
        text.insert(INSERT, "; \n")

def varFloatDeclaration():
    var="Inicial"
    if var is not None:
        var = simpledialog.askstring("Input", "Insertar nombre de variable",parent=app)
        addValue = messagebox.askyesno("Question","¿Desea darle valor a? " + var)
        if addValue == True:
            varValue = simpledialog.askstring("Input", "Inserta valor de la variable",parent=app)
            text.insert(INSERT, "float " + var + "= " +varValue)
        else:
            text.insert(INSERT, "float " + var)
        anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
        while anotherVar != False:
            var = simpledialog.askstring("Input", "Insertar nombre de variable",parent=app)
            addValue = messagebox.askyesno("Question","¿Desea darle valor a? " + var)
            if addValue == True:
                varValue = simpledialog.askstring("Input", "Inserta valor de la variable",parent=app)
                text.insert(INSERT, ", " + var + "= " +varValue)
                anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
            else:
                text.insert(INSERT, ", " + var)
                anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
        text.insert(INSERT, "; \n")

def varCharDeclaration():
    var="Inicial"
    if var is not None:
        var = simpledialog.askstring("Input", "Insertar nombre de variable",parent=app)
        addValue = messagebox.askyesno("Question","¿Desea darle valor a? " + var)
        if addValue == True:
            varValue = simpledialog.askstring("Input", "Inserta valor de la variable",parent=app)
            text.insert(INSERT, "char " + var + "= " +varValue)
        else:
            text.insert(INSERT, "char " + var)
        anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
        while anotherVar != False:
            var = simpledialog.askstring("Input", "Insertar nombre de variable",parent=app)
            addValue = messagebox.askyesno("Question","¿Desea darle valor a? " + var)
            if addValue == True:
                varValue = simpledialog.askstring("Input", "Inserta valor de la variable",parent=app)
                text.insert(INSERT, ", " + var + "= " +varValue)
                anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
            else:
                text.insert(INSERT, ", " + var)
                anotherVar = messagebox.askyesno("Question","¿Desea agregar otra variable?")
        text.insert(INSERT, "; \n")
def prueba():
    text.insert(INSERT, "INSERTAFDO\n")

def openNewWindow(): 
    window = tk.Tk() 
   # window = Toplevel(app)
    window.title('Combobox') 
    window.geometry('500x250') 
  
    # label text for title 
    ttk.Label(window, text = "GFG Combobox Widget",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
# label 
    ttk.Label(window, text = "Select variable Type:", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
    n = tk.StringVar() 
    monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
    monthchoosen['values'] = (' int',  
                          ' float', 
                          ' char') 
    monthchoosen.grid(column = 1, row = 5) 
    monthchoosen.current() 
    btn2 = tk.Button(window,text ="ClicktoAddtext", command=prueba).pack()


app = Tk()
app.geometry("1100x700")
app.title("PAR++")
heading = Label(text="PAR++",fg="black",bg="pink",width="500",height="3",font="10")

heading.pack()
varIntLabel = Label(text="AGREGAR VARIABLE ENTERA")
varIntLabel.place(x=15,y=70)

text = Text(app)
text.insert(INSERT, "var\n")
text.pack()

btnAddIntVar = Button(app,text="Add Integer Variable",command=varIntDeclaration , width="30",height="2",bg="grey")
btnAddfloatVar = Button(app,text="Add Float Variable",command=varFloatDeclaration , width="30",height="2",bg="grey")
btnAddCharVar = Button(app,text="Add Char Variable",command=varCharDeclaration , width="30",height="2",bg="grey")
btnPrueba = Button(app,text="Add Char Variable" , command = openNewWindow, width="30",height="2",bg="grey")

btnAddIntVar.place(x=15,y=500)
btnAddfloatVar.place(x=200, y = 500)
btnAddCharVar.place(x=400, y=500)
btnPrueba.place(x=600,y=500)
mainloop()