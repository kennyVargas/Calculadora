from tkinter import *
from tkinter import messagebox
ventana = Tk()
miFrame = Frame(ventana)
miFrame.pack()

numero=StringVar()
operacion = ""
primerNumero=0.0
resultado=0.0
suich=False
opAux=operacion
accpunto=False
#-------------------Funciones()-----------
def limpiar():
    global resultado
    global suich
    global operacion
    global accpunto
    numero.set("0")
    operacion = ""
    resultado=0
    suich=False
    accpunto=False
    
def ventaEmegerte():
    messagebox.showinfo("Error de calculo","No es posible dividir entre 0")
    
def OpeAritmetica(ope):
    global resultado
    global operacion
    global suich
    global opAux
    global primerNumero
    if suich is True:
        opAux=ope
        operacion=ope
        primerNumero=float(numero.get())
        suich=False
        
        
def Igual():
    
    global opAux
    global resultado
    global primerNumero
    
    
    print(opAux)
    if opAux  == "suma":
        
        resultado=float(numero.get())
        ans=Sum(primerNumero,resultado)
        numero.set(str(ans))
        
    if opAux  == "resta":
        
        resultado=float(numero.get())
        ans=Resta(primerNumero,resultado)
        numero.set(str(ans))
    if opAux  == "multiplicacion":
        resultado=float(numero.get())
        ans=Multiplicacion(primerNumero,resultado)
        numero.set(str(ans))
    if opAux  == "division":
        resultado=float(numero.get())
        ans=Division(primerNumero,resultado)
        numero.set(str(ans))
    
    

def numeroPulsado(num):
    num1 = float(num)
    ans=float(numero.get())
    
    global operacion
    global suich
    global accpunto
    suich = True
    
    if operacion!="":
         numero.set(num)
         accpunto=False
         operacion=""
         
    else:
        if (numero.get() is "0") and (num is "0"):
            pass
        elif accpunto:
            
            ansR = numero.get()+num
            #print(ans)
            numero.set(str(ansR))
        else:
            ans = ans*10 + num1
            #print(ans)
            numero.set(str(ans)) 

def Punto():
    global accpunto
    accpunto=True
    

def Sum(num1,num2):
    return (num1+num2)
    
def Resta(num1,num2):
    return (num1-num2)

def Multiplicacion(num1,num2):
    
    return (num1*num2)

def Division(num1,num2):
    res=0
    try:
        
        res=num1/num2
    except ZeroDivisionError:
        ventaEmegerte()
        res=0
    finally:
        return res
        

#--------------Pantalla---------------
pantalla  = Entry(miFrame,textvariable=numero)
pantalla.grid(row=1, column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="#03f943",justify="right")
#--------------Pantalla---------------

#--------------fila 1 ---------------
buton7 = Button(miFrame,text="7",width=5,command=lambda:numeroPulsado("7"))
buton7.grid(row=2,column=1,padx=5,pady=10)

buton8 = Button(miFrame,text="8",width=5,command=lambda:numeroPulsado("8"))
buton8.grid(row=2,column=2,padx=5,pady=10)

buton9 = Button(miFrame,text="9",width=5,command=lambda:numeroPulsado("9"))
buton9.grid(row=2,column=3,padx=5,pady=10)

botonDiv = Button(miFrame,text="/",width=5,command=lambda:OpeAritmetica("division"))
botonDiv.grid(row=2,column=4,padx=5,pady=10)

#--------------fila 2 ---------------
buton4 = Button(miFrame,text="4",width=5,command=lambda:numeroPulsado("4"))
buton4.grid(row=3,column=1,padx=5,pady=10)

buton5 = Button(miFrame,text="5",width=5,command=lambda:numeroPulsado("5"))
buton5.grid(row=3,column=2,padx=5,pady=10)

buton6 = Button(miFrame,text="6",width=5,command=lambda:numeroPulsado("6"))
buton6.grid(row=3,column=3,padx=5,pady=10)

botonMul = Button(miFrame,text="*",width=5,command=lambda:OpeAritmetica("multiplicacion"))
botonMul.grid(row=3,column=4,padx=5,pady=10)

#--------------fila 3 ---------------
buton1 = Button(miFrame,text="1",width=5,command=lambda:numeroPulsado("1"))
buton1.grid(row=4,column=1,padx=5,pady=10)

buton2 = Button(miFrame,text="2",width=5,command=lambda:numeroPulsado("2"))
buton2.grid(row=4,column=2,padx=5,pady=10)

buton3 = Button(miFrame,text="3",width=5,command=lambda:numeroPulsado("3"))
buton3.grid(row=4,column=3,padx=5,pady=10)

botonRes = Button(miFrame,text="-",width=5,command=lambda:OpeAritmetica("resta"))
botonRes.grid(row=4,column=4,padx=5,pady=10)

#--------------fila 4 ---------------
buton0 = Button(miFrame,text="0",width=5,command=lambda:numeroPulsado("0"))
buton0.grid(row=5,column=1,padx=5,pady=10)

butonComa = Button(miFrame,text=",",width=5,command=lambda:Punto())
butonComa.grid(row=5,column=2,padx=5,pady=10)

butonIgual = Button(miFrame,text="=",width=5 ,command=lambda:Igual())
butonIgual.grid(row=5,column=3,padx=5,pady=10)

botonSum = Button(miFrame,text="+",width=5 ,command=lambda:OpeAritmetica("suma"))
botonSum.grid(row=5,column=4,padx=5,pady=10)

botonClean = Button(miFrame,text="Limpiar",width=5,command=lambda:limpiar())
botonClean.grid(row=6,column=2,padx=5,pady=10)

numero.set("0")

ventana.mainloop()
