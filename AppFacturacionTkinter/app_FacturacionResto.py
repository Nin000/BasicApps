from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = resultado

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variable_comida[x].get() == 1:
            cuadros_comida[x].config(state= NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state= DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variable_bebidas[x].get() == 1:
            cuadros_bebida[x].config(state= NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state= DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variable_postres[x].get() == 1:
            cuadros_postre[x].config(state= NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state= DISABLED)
            texto_postre[x].set('0')
        x += 1

def total():

    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre 
    impuestos = sub_total * 0.7
    total = sub_total + impuestos

    var_costo_comida .set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida .set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre .set(f'$ {round(sub_total_postre, 2)}')
    var_costo_subtotal .set(f'$ {round(sub_total, 2)}')
    var_impuesto .set(f'$ {round(impuestos, 2)}')
    var_total .set(f'$ {round(total, 2)}')

def recibo():
    text_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    text_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    text_recibo.insert(END, f'*' * 47 + '\n')
    text_recibo.insert(END, f'Items\t\tCant.\tPrecio\n')
    text_recibo.insert(END, f'-' * 54 + '\n')

    x = 0 

    for comida in texto_comida:
        if comida.get() != '0':
            text_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                               f'${int(comida.get())*precios_comida[x]}\n')
        x += 1

    x = 0 

    for bebida in texto_bebida:
        if bebida.get() != '0':
            text_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                               f'${int(bebida.get())*precios_bebida[x]}\n')
        x += 1

    x = 0 

    for postres in texto_postre:
        if postres.get() != '0':
            text_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                               f'${int(postres.get())*precios_postres[x]}\n')
        x += 1

    text_recibo.insert(END, f'-' * 54 + '\n')
    text_recibo.insert(END, f'Costo de la comida:\t\t\t{var_costo_comida.get()}\n')
    text_recibo.insert(END, f'Costo de la bebida:\t\t\t{var_costo_bebida.get()}\n')
    text_recibo.insert(END, f'Costo de la postres:\t\t\t{var_costo_postre.get()}\n')
    text_recibo.insert(END, f'Subtotal:\t\t\t{var_costo_subtotal.get()}\n')
    text_recibo.insert(END, f'Impuestos:\t\t\t{var_impuesto.get()}\n')
    text_recibo.insert(END, f'Total:\t\t\t{var_total.get()}\n')
    text_recibo.insert(END, f'-' * 54 + '\n')
    text_recibo.insert(END, f'Gracias por comer en Ninos\n')
    text_recibo.insert(END, f'-' * 54 + '\n')

def guardar():
    info_recibo = text_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo a sido guardado')

def resetear():
    text_recibo.delete(1.0, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state= DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state= DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state= DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebidas:
        v.set(0)
    for v in variable_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_costo_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

app = Tk() 

app.geometry('1020x630+0+0')

#evitar maximizar
app.resizable(0, 0)

app.title('Mi restaurante - Sistema de Facturacion')

app.config(bg='bisque')

#panel superior
panel_superior = Frame(app, bd=1, relief=FLAT)
panel_superior.pack (side=TOP)

#panel izquierdo
panel_izquierdo = Frame(app, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos(inf.)
panel_costos = Frame(panel_izquierdo, bd = 1, relief= FLAT, bg="azure4", padx=50)
panel_costos.pack(side=BOTTOM)

panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd = 1, relief=FLAT, fg = "azure4")
panel_comidas.pack(side=LEFT)

panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd = 1, relief=FLAT, fg = "azure4")
panel_bebidas.pack(side=LEFT)

panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd = 1, relief=FLAT, fg = "azure4")
panel_postres.pack(side=LEFT)

#panel derecha calc, recibo, botones

panel_derecha = Frame(app, bd = 1, relief=FLAT)
panel_derecha.pack(side= RIGHT)

panel_calculadora = Frame(panel_derecha, bd = 1, relief=FLAT, bg='bisque')
panel_calculadora.pack()

panel_recibo = Frame(panel_derecha, bd = 1, relief=FLAT, bg='bisque')
panel_recibo.pack()

panel_botonera = Frame(panel_derecha, bd = 1, relief=FLAT, bg='bisque')
panel_botonera.pack()

lista_comidas = ['Pollo', 'Cordero', 'Cerdo', 'Res', 'Cabra', 'Pavita','Conejo', 'Cangrejo']
lista_bebidas = ['Malbec', 'Cabernet', 'Merlot', 'Pinot Noit', 'Organico', 'Agua', 'Gaseosa', 'Cerveza']
lista_postres = ['Tiramisu', 'Gelatto', 'Cheesecake', 'Marquesse', 'Rogel', 'Mousse', 'Selva Negra', 'Frutas']

#generar items comida
variable_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:
    variable_comida.append('')
    variable_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Dosis', 15, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variable_comida[contador], 
                         command= revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky=W)
    
#crear los cuadros de entrada
#comidas
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font= ('Dosis', 18, 'bold'), 
                                     bd=1, 
                                     width=6,
                                     state=DISABLED, 
                                     textvariable = texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, 
                                  column = 1)    
    
    contador += 1

#generar items bebidas
variable_bebidas = []
cuadros_bebida = []
texto_bebida = []
contador = 0

for bebidas in lista_bebidas:
    variable_bebidas.append('')
    variable_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas, 
                          text=bebidas.title(), 
                          font=('Dosis', 15, 'bold'),
                          onvalue=1, 
                          offvalue=0, 
                          variable=variable_bebidas[contador],
                          command= revisar_check)
    bebidas.grid(row=contador, 
                 column=0, 
                 sticky=W)

    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font= ('Dosis', 18, 'bold'), 
                                     bd=1, 
                                     width=6,
                                     state=DISABLED, 
                                     textvariable = texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, 
                                  column = 1)    
    contador += 1

#generar items postres
variable_postres = []
cuadros_postre = []
texto_postre = []
contador = 0

for postre in lista_postres:
    variable_postres.append('')
    variable_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, 
                          text=postre.title(), 
                          font=('Dosis', 15, 'bold'),
                          onvalue=1, 
                          offvalue=0, 
                          variable=variable_postres[contador],
                          command= revisar_check)
    postres.grid(row=contador, column=0, sticky=W)

    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font= ('Dosis', 18, 'bold'), 
                                     bd=1, 
                                     width=6,
                                     state=DISABLED, 
                                     textvariable = texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, 
                                  column = 1)
    contador += 1

#Variables de entrada 
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


#etiqueta de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos, 
                              font=("Dosis", 12, 'bold'),
                              text="Costo Comida",
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'),
                           bd=1, 
                           width=10, 
                           state='readonly', 
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos, 
                              font=("Dosis", 12, 'bold'),
                              text="Costo Bebida",
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'),
                           bd=1, 
                           width=10, 
                           state='readonly', 
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(panel_costos, 
                              font=("Dosis", 12, 'bold'),
                              text="Costo Postre",
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'),
                           bd=1, 
                           width=10, 
                           state='readonly', 
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_costo_subtotal = Label(panel_costos, 
                              font=("Dosis", 12, 'bold'),
                              text="Subtotal",
                              bg='azure4',
                              fg='white')
etiqueta_costo_subtotal.grid(row=0, column=2)

texto_costo_subtotal = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'),
                           bd=1, 
                           width=10, 
                           state='readonly', 
                           textvariable=var_costo_subtotal)
texto_costo_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuesto = Label(panel_costos, 
                              font=("Dosis", 12, 'bold'),
                              text="Impuestos",
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'),
                           bd=1, 
                           width=10, 
                           state='readonly', 
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos, 
                              font=("Dosis", 12, 'bold'),
                              text="Total",
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold'),
                           bd=1, 
                           width=10, 
                           state='readonly', 
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text = "Sistema de Facturacion", fg='azure4',
                        font=('Dosis', 58), bg='bisque', width=28)
etiqueta_titulo.grid(row=0, column=0)

#botonera
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
columnas = 0
botones_creados = []

for boton in botones:
    boton = Button(panel_botonera, 
                   text = boton.title(), 
                   font= ('Dosis', 14, 'bold'),
                   fg= 'white',
                   bg= 'azure4',
                   bd=1,
                   width=9)
    
    botones_creados.append(boton)
    
    boton.grid(row=0, 
               column=columnas)
    columnas += 1

botones_creados[0].config(command= total)
botones_creados[1].config(command= recibo)
botones_creados[2].config(command= guardar)
botones_creados[3].config(command= resetear)



#Area de recido
text_recibo = Text(panel_recibo,
                   font=('Dosis', 12, 'bold'), 
                   bd=1,
                   width=42, 
                   height=10)
text_recibo.grid(row=0, 
                 column=0)

#Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          bd=1,
                          width=32)
visor_calculadora.grid(row=0,column=0, columnspan=4)

#Loop botones calculadora
botones_calc = ['7', '8', '9', '+', 
                '4', '5', '6', '-', 
                '1', '2', '3', 'x', 
                '=', 'Borrar', '0', '/']
fila = 1
columna = 0
botones_guardados = []


for boton in botones_calc:
    boton = Button(panel_calculadora, 
                   text= boton.title(), 
                   font=('Dosis', 16,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    
    botones_guardados.append(boton)
    
    boton.grid(row=fila, 
               column=columna)
    
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=lambda : obtener_resultado())
botones_guardados[13].config(command=lambda : borrar())
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))



app.mainloop()

