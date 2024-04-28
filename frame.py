from tkinter import *
from funcoes import *
from funcoesFrames import *

window=Tk()

class Aplicativo():
    def __init__(self):
        self.janela=window

        #variavel da array dos frames
        self.litrosMedidoTodos=[0]*12  #valores das medidas dos litros  
        self.valorLitro=[0]*6 #valor dos litros
        self.dinheiroRevendas=[0]*6
        self.litroRevendas=[0]*6
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
        self.janela.geometry("1980x300")
        self.janela.minsize(width=800,height=600)
        self.janela.configure(bg="#495168")
        foto=PhotoImage(file="./img/logo.png") 
        self.janela.iconphoto(FALSE,foto)
    
    def framesDaJanela(self,contador):
        cores = ["red", "green", "blue", "yellow", "orange", "purple"]
        frame=Frame(self.janela, bg="#9d9382", bd=2 , highlightbackground="#0012ff")
        
        frame.grid(row=1, column=contador, padx=5)
        self.frameBombas.append(frame)

    def addNosFrames(self):
        #falta pensar na logica para colocar na posicao certa da array cada entry (0-1) (2-3) (4-5) ... (10-11)
        j=0
        for i in range(0,6): #dentro do frame criado - - no final salvar na lista encadeada
            #Bloco 1
            entradaLitroManha=frameMedidasLitrosManha(self.frameBombas[i],i)
            entradaLitroManha.bind("<FocusOut>", lambda event,contador=i+j,entrada=entradaLitroManha : self.pegandoLitrosMedidos(contador, entrada))
            
            j+=1
            
            entradaLitroNoite=frameMedidasLitrosNoite(self.frameBombas[i])
            entradaLitroNoite.bind("<FocusOut>", lambda event,contador_2=i+j,entrada_2=entradaLitroNoite : self.pegandoLitrosMedidos(contador_2, entrada_2))
            
            #Bloco 2 - espaco
            frameEspaco(self.frameBombas[i],3)
            
            # Bloco 3 - valor litro
            valorLitros=frameValorLitro(self.frameBombas[i])
            valorLitros.bind("<FocusOut>", lambda event,contador_3=i,entrada_3=valorLitros : self.pegandoValorLitros(contador_3, entrada_3))
            
            #Bloco 4 - espaco
            frameEspaco(self.frameBombas[i],5)
            
            #Bloco 5 - valor litro e dinheiro revenda
            litroRevenda=frameLitroRevenda(self.frameBombas[i])
            litroRevenda.bind("<FocusOut>", lambda event,contador=i,entrada=litroRevenda : self.pegandoLitrosRevenda(contador, entrada))
            dinheiroRevenda=frameDinheiroRevenda(self.frameBombas[i])
            dinheiroRevenda.bind("<FocusOut>", lambda event,contador=i,entrada=dinheiroRevenda : self.pegandoDinheiroRevenda(contador, entrada))
            
            #Bloco 6 - espaco
            frameEspaco(self.frameBombas[i],8)
            
            #Bloco 7 -
            
            
        #botao de execucao do programa    
        self.botaoEnvia()
            
            
    def pegandoLitrosRevenda(self,i,litroRevenda):
        tempValor= litroRevenda.get()
        if tempValor!="":
            self.litroRevendas[i]=float(tempValor)
        else:
            print("VAZIO")

    def pegandoDinheiroRevenda(self,i,dinheiroRevenda):
        tempValor= dinheiroRevenda.get()
        if tempValor!="":
            self.dinheiroRevendas[i]=float(tempValor)
        else:
            print("VAZIO")
            
            
    def pegandoValorLitros(self,i,valorLitro):
        tempValor= valorLitro.get()
        if tempValor!="":
            self.valorLitro[i]=float(tempValor)
        else:
            print("VAZIO")

    
    def pegandoLitrosMedidos(self, i, LitroMedido):     
        #salvando na array os litros medido
        tempValor= LitroMedido.get()
        if tempValor!="":
            self.litrosMedidoTodos[i]=float(tempValor)
        else:
            print("VAZIO")

    def botaoEnvia(self):
        button=Button(self.janela, command=lambda:salvarDados(self.litrosMedidoTodos,self.valorLitro, self.dinheiroRevendas,self.litroRevendas))
        button.grid(row=10,column=0)
        # dar o foco ao botao ao ser clicado evento de ser clicado pelo mouse que executa a funcao focus_set no botao
        button.bind("<Button-1>", lambda event :button.focus_set())
        
            
if __name__ == "__main__":
    Aplicativo()

