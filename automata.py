from cgitb import text
import tkinter as tk
from tkinter import messagebox
from tkinter.tix import INTEGER
from turtle import bgcolor, width
from tkinter import *
from tkinter import ttk
window= Tk()
window.geometry('900x675')
window.configure(bg='#707070')
window.resizable(0,0)
window.title('Lenguajes')
global cirCount
cirCount=0
fonttxt = 'Arial'
posx=20
posy=30
colorbg="#ABB2B9"

flog = Frame(window,width=1200,height=675,bg=colorbg)
flog.place(x=0, y=0)
def ingreso(cadena):
   print("holamundo")
def create_circle(x, y, r, canvasName,cont): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    conct="q"+str(cont)
    canvasName.create_text(x,y,text=conct)
    return canvasName.create_oval(x0, y0, x1, y1)
def Create_Lines(x1,y1,x2,y2,r,canvasNameL):
   x0=x1+r
   x=x2-r
   return canvasNameL.create_line(x0,y1,x,y2)

def Correcto():
   cadena=cad.get()
   for i in range ( len (cadena) ):
      if not ((ord(cadena[i])>64 and ord(cadena[i])<91) or (ord(cadena[i])>96 and ord(cadena[i])<123)):
         
         if not (cadena[i]=='|' or cadena[i]=='*' or cadena[i]=='(' or cadena[i]==')' or cadena[i]==' '):
            messagebox.askretrycancel(message="Caracter(es) invalido", title="ERROR")
   if(cad.get()!=""):
      ingreso(cad.get())
            


#labels
#user label
Label1=Label(flog,text='Ingrese una cadena de texto')
Label1.place(x=posx-3,y=0)
Label1.config(bg=colorbg,font=(fonttxt,15))

#cad enrty
cad=tk.StringVar()
cad_entry = ttk.Entry(flog,textvariable=cad)
cad_entry.config(width=75,font=(fonttxt,12))
cad_entry.place(x=posx,y=posy)
#button
Enter=Button(flog, text="Entrar",font=(fonttxt,13),width=10,command=Correcto)
Enter.place(x=750,y=posy)
#lienzo
lienzo = Canvas(width=1200, height=575, bg='white') 
lienzo.place(x=0,y=100)
#crear texto
#crear circulo
cirCount=0
create_circle(40,40,30,lienzo,cirCount)
cirCount=cirCount+1
create_circle(200,40,30,lienzo,cirCount)
Create_Lines(40,40,200,40,30,lienzo)
window.mainloop()
