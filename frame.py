from tkinter import *
from funcoes import *

window=Tk()

class Aplicativo():
    def __init__(self):
        self.janela=window

        #variavel da array dos frames
        self.entradasTotal=[0]*12  #valores litros  

        #configura a tela principal
        self.configJanela()

        #criacao dos 6 frames
        self.frameBombas=[] 
        for i in range (6):
            self.framesDaJanela(i)

        #personaliza os 6 frames
        self.addNosFrames()

        #loop de execucao para aparecer a tela
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
        #falta pensar na logica para colocar na posicao certa da array cada entry (0-1) (2-3) (4-5) ... (10-11)
        j=0
        for i in range(0,6): #dentro do frame criado - - no final salvar na lista encadeada
            #label entrada
            texto=Label(self.frameBombas[i], text=f"B{i})")
            texto.grid(row=1,column=0)
            #entrada
            entradas1=Entry(self.frameBombas[i])
            entradas1.grid(row=1,column=1)
            # no momento em que tira o foco da caixinha ele salva o valor indo la pra funcao de pegar os dados
            entradas1.bind("<FocusOut>", lambda event,contador=i+j,entrada=entradas1 : self.pegarOsDados(contador, entrada))
            j+=1
            entradas2=Entry(self.frameBombas[i])
            entradas2.grid(row=2,column=1)
            # no momento em que tira o foco da caixinha ele salva o valor indo la pra funcao de pegar os dados
            entradas2.bind("<FocusOut>", lambda event,contador_2=i+j,entrada_2=entradas2 : self.pegarOsDados(contador_2, entrada_2))
            

        #botao de execucao do programa    
        self.botaoEnvia()
            
    def pegarOsDados(self, i, entrada):     
        #salvando na array
        tempValor= entrada.get()
        if tempValor!="":
            self.entradasTotal[i]=float(tempValor)
        else:
            print("VAZIO")

    def botaoEnvia(self):
        button=Button(self.janela, command=lambda:salvarDados(self.entradasTotal))
        button.grid(row=10,column=0)
        # dar o foco ao botao ao ser clicado evento de ser clicado pelo mouse que executa a funcao focus_set no botao
        button.bind("<Button-1>", lambda event :button.focus_set())
        
            

Aplicativo()

