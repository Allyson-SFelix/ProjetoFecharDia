from tkinter import *

def frameValorLitro(frameBombas):
    textoValorLitros=Label(frameBombas, text="Valor do Litro", bg="#9d9382")
    textoValorLitros.grid(row=4,column=0)
    valorLitros=Entry(frameBombas)
    valorLitros.grid(row=4,column=1)
    return valorLitros

def frameMedidasLitrosManha(frameBombas,i):
    textoLitrosMedidos=Label(frameBombas, text=f"B{i+1})",bg="#9d9382")
    textoLitrosMedidos.grid(row=1,column=0)
    #entrada
    entradaLitroManha=Entry(frameBombas)
    entradaLitroManha.grid(row=1,column=1)
    return entradaLitroManha

def frameMedidasLitrosNoite(frameBombas):
    entradaLitroNoite=Entry(frameBombas)
    entradaLitroNoite.grid(row=2,column=1)
    return entradaLitroNoite

def frameLitroRevenda(frameBombas):
    textoLitrosRevenda=Label(frameBombas, text="Litros Revenda", bg="#9d9382")
    textoLitrosRevenda.grid(row=6,column=0)
    LitrosRevenda=Entry(frameBombas)
    LitrosRevenda.grid(row=6,column=1)
    return LitrosRevenda

def frameDinheiroRevenda(frameBombas):
    textoDinheiroRevenda=Label(frameBombas, text="Dinheiro Revenda", bg="#9d9382")
    textoDinheiroRevenda.grid(row=7,column=0)
    DinheiroRevenda=Entry(frameBombas)
    DinheiroRevenda.grid(row=7,column=1)
    return DinheiroRevenda

def frameEspaco(frameBombas, linha):
        espaco=Label(frameBombas, text="----------------------------------", bg="#9d9382")
        espaco.grid(row=linha,column=1)