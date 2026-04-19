from tkinter import * #Importamos la librerias y todos su módulos

windows1 = Tk() #Inicializamos la ventana

windows1.geometry("500x500") #Le damos dimensión (Ancho, alto)

windows1.title("EzcraftPython") #Le dasmo el título

icono = PhotoImage(file="VSCode-Git-GitHub-Pr-ctica/icono_1.png") #Convertimos la imagen
windows1.iconphoto(True, icono)

windows1.config(background="#000") #Dasmo un color negro al fondo

windows1.mainloop() #Mantemos abrierto la ventana