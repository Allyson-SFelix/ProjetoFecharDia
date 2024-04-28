
class Bombas:
    def __init__(self):
        self.valorLitro=0.0
        self.litroTotalMedido=0.0
        self.RvDinheiro=0.0
        self.RvLitro=0.0
   
   
    
def salvarDados(litroMedida,valorLitro,dinheiroRevenda,litrosRevenda):
        listaBombas=[]*6
        for i in range(6): #alocando cada objeto para uma casa do array 
            listaBombas.append(Bombas())
        
        #chamando as funcoes de salvar
        salvarLitroMedidos(listaBombas,litroMedida)
        salvarValorLitros(listaBombas,valorLitro)
        salvarDadosRevenda(listaBombas,dinheiroRevenda,litrosRevenda)
    

def salvarDadosRevenda(listaBombas,dinheiroRevenda,litrosRevenda):
    for i in range(6): 
        listaBombas[i].RvLitros=litrosRevenda[i]
        listaBombas[i].RvDinheiro=dinheiroRevenda[i]
        print(listaBombas[i].RvLitros)
        print(listaBombas[i].RvDinheiro)


def salvarLitroMedidos(listaBombas,litroMedidaEntrada):    
    j=0
    for i in range(6): 
        litroTempManha=litroMedidaEntrada[i+j]
        j+=1
        litroTempNoite=litroMedidaEntrada[i+j] 
        listaBombas[i].litroTotalMedido=litroTempManha+litroTempNoite
        print(listaBombas[i].litroTotalMedido)
            
            
def salvarValorLitros(listaBombas,valorLitro):
    for i in range(6): 
        listaBombas.append(Bombas())
        listaBombas[i].valorLitro=valorLitro[i]
        print(listaBombas[i].valorLitro)
        
