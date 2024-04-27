from tkinter import *
from frames import * 
from funcoes import *

window=Tk()

class Aplicativo():
    def __init__(self):
        self.janela=window
        self.frameBombas=[]
        self.configJanela()
        for i in range (6):
            self.framesDaJanela(i)
            print("Frames criados:", self.frameBombas)

        self.addNosFrames()
        self.janela.mainloop()

    def configJanela(self): #estiliza a janela principal
        self.janela.title("Somar/Fechar dia")
        self.janela.geometry("1600x800")
        self.janela.minsize(width=800,height=600)
        self.janela.configure(bg="#495168")
        foto=PhotoImage(file="./img/logo.png") 
        self.janela.iconphoto(FALSE,foto)
    
    def framesDaJanela(self,contador):
        cores = ["red", "green", "blue", "yellow", "orange", "purple"]
        frame=Frame(self.janela, bg=cores[contador], bd=2 , highlightbackground="#0012ff")
        frame.grid(row=1, column=contador, padx=10)
        self.frameBombas.append(frame)

    def addNosFrames(self):
        entradasTotal=[]    
        for i in range(0,6): #dentro do frame criado - - no final salvar na lista encadeada
            texto=Label(self.frameBombas[i], text=f"PAO{i}")
            texto.grid(row=1,column=0)
            entradas=Entry(self.frameBombas[i])
            entradas.grid(row=1,column=1)
            
            tempEntradas=entradas.get()
            if tempEntradas: 
                entradasTotal.append(tempEntradas)
            
            
        button=Button(self.frameBombas[i], command=lambda:salvarDados(entradasTotal))
        button.grid(row=10,column=0)
            

Aplicativo()

