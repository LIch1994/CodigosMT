from Tkinter import *

ventana = Tk()
c = Canvas(ventana, width=500,height=500)
ventana.geometry("500x500")
color = "#F0F" 
#c.create_oval(10,10,100,100,fill=color)
#c.create_oval(20,20,80,80,fill="yellow")
for i in range (0,10):
	if i%2 == 0:
		c.create_oval(i*10,i*10,200-(i*10),200-(i*10),fill="red")
	else:
		c.create_oval(i*10,i*10,200-(i*10),200-(i*10),fill="white")
	i = i+1

c.create_rectangle(0,0,200,200,fill="blue")
c.create_rectangle(200,0,400,200,fill="yellow")
c.create_line(50,250,80,250, width=4.0)
c.create_polygon(100,0,150,200,50,200,fill="green")
c.place(x=0,y=0)




ventana.mainloop()
