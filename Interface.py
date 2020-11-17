from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

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

app = Tk()
text = Text(app)
text.insert(INSERT, "var\n")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")

btnAddIntVar = Button(app,text="Add Integer Variable",command=varIntDeclaration , width="30",height="2",bg="grey")
btnAddfloatVar = Button(app,text="Add Float Variable",command=varFloatDeclaration , width="30",height="2",bg="grey")
btnAddCharVar = Button(app,text="Add Char Variable",command=varCharDeclaration , width="30",height="2",bg="grey")

btnAddIntVar.place(x=15,y=290)
btnAddfloatVar.place(x=200, y = 290)
btnAddCharVar.place(x=400, y=290)
app.mainloop()