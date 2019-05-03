import random
from tkinter import *
import threading
import logic
import constants as c
import time


import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,GdkPixbuf,Gdk



class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.minsize(1300,400)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        # self.gamelogic = gamelogic
        self.commands = {c.KEY_UP: logic.up, c.KEY_DOWN: logic.down,
                         c.KEY_LEFT: logic.left, c.KEY_RIGHT: logic.right,
                         c.KEY_UP_ALT: logic.up, c.KEY_DOWN_ALT: logic.down,
                         c.KEY_LEFT_ALT: logic.left,
                         c.KEY_RIGHT_ALT: logic.right}

       
        
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.thread_reloj()
        self.thread_puntaje()
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()
        
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
        a=Label(self.master, text=("Puntaje: "),justify=LEFT, font=("Verdana", 20, "bold"))
        a.place(x=840,y=100)
        b=Label(self.master, text=("Tiempo: "),justify=LEFT, font=("Verdana", 20, "bold"))
        b.place(x=840,y=300)
        
        self.t = StringVar()
        self.t.set("00:00")
        self.lb = Label(self.master,textvariable=self.t)
        self.lb.config(font=("Courier 40 bold"))
        self.lb.place(x=1000,y=350)

        self.score = StringVar()
        self.score.set("0")
        self.scorelb = Label(self.master,textvariable=self.score)
        self.scorelb.config(font=("Courier 40 bold"))
        self.scorelb.place(x=1000,y=150)
        
    def gen(self):
        return random.randint(0, c.GRID_LEN - 1)

    def init_matrix(self):
        self.matrix = logic.new_game(4)
        self.history_matrixs = list()
        self.matrix = logic.add_two(self.matrix)
        self.matrix = logic.add_two(self.matrix)
        
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=logic.hexadecimal(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def key_down(self, event):
        key = repr(event.char)
        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_grid_cells()
            print('back on step total step:', len(self.history_matrixs))
        elif key in self.commands:
            self.matrix, done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = logic.add_two(self.matrix)
                # record last move
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                done = False
                if logic.estado_juego(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.estado_juego(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2

    
    def puntaje(self):
        
        while (logic.estado_juego(self.matrix)=='not over'): 
            temp=logic.actualizar(self.matrix)
            logic.fileW(temp)
            self.score.set(temp)
        if(logic.estado_juego(self.matrix)=='lose'):
           logic.fileW(temp)
           time.sleep(2)
           self.master.destroy()
            
     
    def thread_puntaje(self):
        p=threading.Thread(target=self.puntaje)
        p.start()
                
    
            
    def timer(self):
        count=0
        if(count==0):
            self.d = str(self.t.get())
            m,s = map(int,self.d.split(":"))
            
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1

            if(m==5 and s==00):
                return self.master.destroy(),window6.show_all(),True
            
            
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=m+":"+s
            
            
            self.t.set(self.d)
            if(count==0):
                self.master.after(930,self.timer)
                
    def thread_reloj(self):
        x=threading.Thread(target=self.timer)
        x.start()


    



            

final=0    
window6 = Gtk.Window(title="2048")
window6.set_default_size(200,100)
window6.set_resizable(False)
window6.connect("destroy", Gtk.main_quit)

VBox6=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
window6.add(VBox6)
#horizantal box
HBox6=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
HBox6.set_halign(Gtk.Align.CENTER)
VBox6.pack_end(HBox6,False,False,15)
textTaller=Gtk.Label(label='p13971209836')
VBox6.pack_start(textTaller,False,False,15)

gamegrid = GameGrid()
Gtk.main()
