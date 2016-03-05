from Tkinter import * 

ventana = Tk()
ventana.geometry("500x500")
# .png .gif Solo esos formatos
imagen = PhotoImage(file="photobooth01.png")
imgbtn = PhotoImage(file="photobooth01.png")
fondo = Label(ventana, image=imagen).place(x=0,y=0)
boton = Button(ventana,imagen=imgbtn).place(x=20,y=20)
ventana.mainloop()