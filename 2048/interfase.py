import gi
import random
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,GdkPixbuf,Gdk



#----------------------------------------------------------------------------------------------------------------------------------------------------
#Grafico de pagina 1

window1 = Gtk.Window(title="2048")
window1.set_default_size(500,460)#establecer tamaño pantalla
window1.set_resizable(False)#definir si se puede cambiar de tamaño

#vertical box
VBox1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
window1.add(VBox1)
#horizantal box
HBox1=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
HBox1.set_halign(Gtk.Align.CENTER)
VBox1.pack_end(HBox1,False,False,15)

#agregar textoo label
textTaller=Gtk.Label(label="Bienvenidos al juego 2048,con diferentes bases decimales, INSTRUCCIONES , A,W,S,D se mueve y tienes 5 minutos para ganar ") 
#VBox.pack_start(child,expand,fill,padding)
VBox1.pack_start(textTaller,False,False,15)

Grid1=Gtk.Grid()
Grid1.set_halign(Gtk.Align.CENTER)
VBox1.pack_end(Grid1,False,False,15)

#agregar  entry
entryTaller=Gtk.Entry()
entryTaller.set_text("Ingrese su nombre")
VBox1.pack_start(entryTaller,False,False,5)


def fileR():
    file=open("progra.txt","r")
    texto=file.read()
    datos=eval(texto)
    file.close()
    return datos    


#lista puntaje

people=fileR()

#convert list data to liststore
people_list_store=Gtk.ListStore(str,int)
for item in people:
    people_list_store.append(list(item))

#tree_view
people_tree_view=Gtk.TreeView(people_list_store)
for i,col_title in enumerate(["Nombre","Puntaje"]):
    renderer=Gtk.CellRendererText()
    
    #crear columnas
    column=Gtk.TreeViewColumn(col_title,renderer,text=i)

    #add columna al treeview
    people_tree_view.append_column(column)
HBox1.pack_start(people_tree_view,True,True,0)
#----------------------------------------------------------------------------------------------------------------------------------------------------
#Programacion de pagina

def on_open_clicked1(button1):
    
    x=entryTaller.get_text()
    if(buscar_en_lista(x,0)):
        print("El nombre ya ha sido ingresado,por favor ingrese un nuevo nombre")
        window4 = Gtk.Window(title="2048")
        window4.set_default_size(200,50)#establecer tamaño pantalla
        window4.set_resizable(False)#definir si se puede cambiar de tamaño

        #vertical box
        VBox4=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        window4.add(VBox4)
        #horizantal box
        HBox4=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        HBox4.set_halign(Gtk.Align.CENTER)
        VBox4.pack_end(HBox4,False,False,15)
        

        textTaller4=Gtk.Label(label="El nombre ya ha sido ingresado,por favor ingrese un nuevo nombre")
        #VBox.pack_start(child,expand,fill,padding)
        VBox4.pack_start(textTaller4,True,True,20)

        def salir1(salir):
            window4.destroy()
            
            
            
        #crear botton
        salir=Gtk.Button()
        salir.set_label("Cerrar")
        salir.connect("clicked",salir1)
        HBox4.pack_start(salir,False,False,5)
        window4.show_all()
        
    else:
        global y
        y=x
        window.show_all()
        window1.destroy()
        print("que ha pasado")

def fileW(com):
    com=str(com)
    newfile=open("progra.txt","w")
    newfile.write(com)
    newfile.close()

def tabla_puntaje(com):
    temp=fileR()
    fileW(ordenar(com))
    return fileR()

def fileR2():
    file=open("puntaje final.txt","r")
    texto=file.read()
    datos=eval(texto)
    file.close()
    return datos

    
def ordenar(com):
    TEMP=fileR()
    i=0
    lista=[]
    lista2=[]
    return aux_ordenar(lista,lista2,TEMP,com,i)

def aux_ordenar(lista,lista2,TEMP,com,i):
    temp1=TEMP[i]
    if(i==len(TEMP)-1):
        
        lista2.append(com)
        lista2.append(fileR2())
        lista.append(temp1)
        lista.append(lista2)
        return lista
    else:
        lista.append(temp1)
        return aux_ordenar(lista,lista2,TEMP,com,i+1)


#crear botton
button1=Gtk.Button()
button1.set_label("Iniciar")
button1.connect("clicked",on_open_clicked1)
HBox1.pack_start(button1,False,False,5)

def buscar_en_lista(x,t):
    x=str(x)
    if(t==len(people)-1):
        if(x==people[t][0]):
            return True
        else:
            return False
    else:
        if(x==people[t][0]):
            return True
        else:
            return buscar_en_lista(x,t+1)
    

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Grafico de pagina 2

window = Gtk.Window(title="2048")
window.set_default_size(300,200)#establecer tamaño pantalla
window.set_resizable(False)#definir si se puede cambiar de tamaño

#vertical box
VBox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
window.add(VBox)
#horizantal box
HBox=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
HBox.set_halign(Gtk.Align.CENTER)
VBox.pack_end(HBox,False,False,5)


#Grid
Grid=Gtk.Grid()
Grid.set_halign(Gtk.Align.CENTER)
VBox.pack_end(Grid,False,False,5)

#insertart en un grid
button1=Gtk.Button(label="     Binario     ")
button2=Gtk.Button(label="Octal")
button3=Gtk.Button(label="Hexadecimal")
button4=Gtk.Button(label="Decimal")



Grid.add(button1)
#grid.attach(widget,column,row,width,span,height,span)

Grid.attach(button3,0,2,6,1)
Grid.attach(button1,0,0,6,1)
Grid.attach(button2,0,1,6,1)
Grid.attach(button4,0,3,6,1)


def binario(button1):
    global y
    import binario
    binario.GameGrid()
    tabla_puntaje(y)
    
   
#crear botton

button1.connect("clicked",binario)
HBox.pack_start(button1,False,False,5)

def Octal(button2):
    global y
    import Octal
    Octal.GameGrid()
    tabla_puntaje(y)
    
   
#crear botton

button2.connect("clicked",Octal)
HBox.pack_start(button2,False,False,5)

def Hexadecimal(button3):
    global y
    import Hexadecimal
    Hexadecimal.GameGrid()
    tabla_puntaje(y)
   
#crear botton

button3.connect("clicked",Hexadecimal)
HBox.pack_start(button3,False,False,5)

def decimal(button4):
    global y
    import puzzle
    puzzle.GameGrid()
    tabla_puntaje(y)
#crear botton

button4.connect("clicked",decimal)
HBox.pack_start(button4,False,False,5)



   


window.connect("destroy", Gtk.main_quit)


#----------------------------------------------------------------------------------------------------------------------------------------------------



window.connect("destroy", Gtk.main_quit)

window1.show_all()

Gtk.main()
