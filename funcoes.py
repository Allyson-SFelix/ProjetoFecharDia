
class Bombas:
    def __init__(self):
        self.valorLitro=0.0
        self.litroManha=0.0
        self.litroNoite=0.0
        self.RvDinheiro=0.0
        self.RvLitro=0.0
   
   
    
def salvarDados(litroEntrada):
        listaBombas=[]*6
        j=0
        for i in range(6): 
            listaBombas.append(Bombas())
            listaBombas[i].litroManha=litroEntrada[i+j]
            j+=1
            listaBombas[i].litroNoite=litroEntrada[i+j]
    

    
