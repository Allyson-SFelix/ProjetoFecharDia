from funcoesFuncionalidades import *

class Bombas:
    def __init__(self):
        self.valorLitro=0.0
        self.litroTotalMedido=0.0
        self.RvDinheiro=0.0
        self.RvLitro=0.0
        self.dinheiroCaixa=0.0
        self.valesCaixa=0.0
        
    @classmethod
    def salvarValoresCaixa(cls,dinheiro,vale):
                cls.dinheiroCaixa=dinheiro
                cls.valesCaixa=vale

   
    
def salvarDados(litroMedida,valorLitro,dinheiroRevenda,litrosRevenda,dinheiroCaixa,valesCaixa):
        listaBombas=[]*6
        for i in range(6): #alocando cada objeto para uma casa do array 
            listaBombas.append(Bombas())
        
        #chamando as funcoes de salvar
        salvarLitroMedidos(listaBombas,litroMedida)
        salvarValorLitros(listaBombas,valorLitro)
        salvarDadosRevenda(listaBombas,dinheiroRevenda,litrosRevenda)
        Bombas.salvarValoresCaixa(dinheiroCaixa,valesCaixa)
        trabalharNosDados(listaBombas,Bombas)

def salvarDadosRevenda(listaBombas,dinheiroRevenda,litrosRevenda):
    for i in range(0,6): 
        listaBombas[i].RvLitro=litrosRevenda[i]
        listaBombas[i].RvDinheiro=dinheiroRevenda[i]
        


def salvarLitroMedidos(listaBombas,litroMedidaEntrada):    
    j=0
    for i in range(6): 
        litroTempManha=litroMedidaEntrada[i+j]
        j+=1
        litroTempNoite=litroMedidaEntrada[i+j] 
        listaBombas[i].litroTotalMedido=abs(litroTempManha-litroTempNoite)
            
            
def salvarValorLitros(listaBombas,valorLitro):
    for i in range(6): 
        listaBombas.append(Bombas())
        listaBombas[i].valorLitro=valorLitro[i]
        
