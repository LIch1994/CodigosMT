from Tkinter import *   #Tkinter con mayuscula debido a la version de python 2.7
import time 
import tkMessageBox

def saludar():
    print 'Hola'

def parpadear():
	w.iconify()
	time.sleep(3)
	w.deiconify()

def imprime():
	print("Acabas de presionar imprimir")

def saludar():
	print("Hola" + nombre.get() + " " + apellido.get() + " " + apellidoM.get())

def operacion():
	numero = num.get()
	if opcion.get()==1:
		total = numero * 10
	elif opcion.get()==2:
		total = numero * 20
	elif opcion.get()==3:
		total = numero * 30
	elif opcion.get()==4:
		total = numero * 40
	elif opcion.get()==5:
		total = numero * 50
	else:
		total = numero * numero
	print("El total de la operacion es: " + str(total))

def obtenerSpinbox():
	#print(valor.get())
	tkMessageBox.showinfo("Mensaje","Tu seleccionaste " + valor.get())
	tkMessageBox.showwarning("Advertencia","Esto es un mensaje de Advertencia")
	tkMessageBox.askquestion("Pregunta 1", "Cualquier cosa")
	tkMessageBox.askokcancel("Pregunta 2", "Cualquier cosa")
	tkMessageBox.askyesno("Pregunta 3", "Cualquier cosa") #Responde en boleano a diferencia del question
	tkMessageBox.askretrycancel("Pregunta 1", "Cualquier cosa")
w = Tk() #Objeto contructor que crea la ventana

w.title("Reconocimiento de rostros en tiempo Real usando Plataforma Raspberry Pi")
w.geometry("1366x768")
l = Label(w, text='Reconocimientos de rostros usando RPi') #Creacion de la etiqueta(parametro, y texto de la etiqueta)
l.pack() #Adaptamos la etiqueta a la ventana

b1 = Button(w, text='Saludar', command=parpadear) #Creacion de un boton, El command es el comando que va a pasar cuando se de click al boton
b1.pack() #command = ventana.iconify --> minimiza la ventana

b2 = Button(w, text='Salir', command=exit)
b2.pack()

b3 = Button(w, text='Quitar', fg="red",command=w.quit)
b3.pack(side=LEFT)

b4 = Button(w, text='Imprimir', fg="blue",  command=imprime)
b4.pack(side=RIGHT)

#3
b5 = Button(w, text ='Posicinamiento diferente', command=saludar).place(x=100,y=100)
nombre = StringVar()
nombre.set("Escribe tu nombre")  #Set coloca la variable que yo quiera
apellido = StringVar()
apellidoM = StringVar()
nombreCaja = Entry(w, textvariable=nombre).place(x=120,y=160)
apellidoCaja = Entry(w,textvariable=apellido).place(x=120,y=190)
apellidoMCaja = Entry(w,textvariable=apellidoM).place(x=120,y=210)

#5

opcion = IntVar()
num = IntVar()
etiqueta1 = Label(w, text="Escribe el numero: ").place(x=120,y=230)
cajaNumero = Entry(w, textvariable=num).place(x=120,y=250)
etiqueta2 = Label(w, text="Escribe el opcion: ").place(x=220,y=230)
x10 = Radiobutton(w,text="X10",value=1,variable=opcion).place(x=120,y=280) #value es el valor interno y lo va a almacenar en opcion
x20 = Radiobutton(w,text="X20",value=2,variable=opcion).place(x=120,y=300)
x30 = Radiobutton(w,text="X30",value=3,variable=opcion).place(x=120,y=320)
x40 = Radiobutton(w,text="X40",value=4,variable=opcion).place(x=120,y=340)
x50 = Radiobutton(w,text="X50",value=5,variable=opcion).place(x=120,y=360)
cuadrado = Radiobutton(w,text="Cuadrado",value=6,variable=opcion).place(x=120,y=380)
boton = Button(w,text="Realizar operacion", command=operacion).place(x=120, y=400)


#6 Spinbox
valor = StringVar()
etiquetaSpinbox= Label(w,text="Ejemplo1 Spinbox").place(x=120,y=420)
combo =Spinbox(w,values=("Uno","Dos","Tres","Cuatro","Cinco")).place(x=120,y=440)
etiquetaSpinbox2= Label(w,text="Ejemplo2 Spinbox").place(x=120,y=460)
combo2= Spinbox(w,from_=1,to=10,textvariable=valor).place(x=120,y=480)
BotonSpinBox = Button(w,text="Obtener Valor Spinbox", command=obtenerSpinbox).place(x=120,y=500)

#7 Messagebox



#imagen = PhotoImage(file="caraGIF2.gif")
#imgbtn = PhotoImage(file="caraGIF3.gif")
#fondo = Label(w, image=imagen).place(x=0,y=0)
#boton = Button(w,imagen=imgbtn).place(x=20,y=20)



x = StringVar()  #Tambien se puede intVar, booleanVar
e = Entry(w, textvariable=x)
e.pack()

a = StringVar()
b = StringVar()
a.set(5)                # es convertido a string
b.set(8)                # es convertido a string
print a.get() + b.get()             # imprime 58
print int(a.get()) + int(b.get())   # imprime 13

w.mainloop() # Con esto interactuamos con la ventana.