
def trabalharNosDados(listaBombas,Bombas):
    litrosTotalPorBomba=[] #litro no total apos reduzir com litro revenda
    dinheiroPorBombaDosLitros=[]
    dinheiroPorBombaTotal=[]
    dinheiroTotalBombas=0

    for i in range(0,6):
        litrosTotalPorBomba.append(somaLitroFinal(i,listaBombas))
        dinheiroPorBombaDosLitros.append(somaDinheiroPorBomba(i,listaBombas,litrosTotalPorBomba))
        dinheiroPorBombaTotal.append(somaDosDinheiros(i,listaBombas,dinheiroPorBombaDosLitros))
        dinheiroTotalBombas+=dinheiroPorBombaTotal[i]
    
    valorCaixa=Bombas.dinheiroCaixa + Bombas.valesCaixa
    diferencaDinheiro=0.0
    diferencaDinheiro=valorCaixa-dinheiroTotalBombas 
    escreverNoArquivo(listaBombas,valorCaixa,diferencaDinheiro,dinheiroTotalBombas)
    
    
    
def somaLitroFinal(contador,listaBombas):
    tempPorBombas=listaBombas[contador].litroTotalMedido - listaBombas[contador].RvLitro 
    return tempPorBombas

def somaDinheiroPorBomba(contador, listaBombas,litrosPorBomba):
    tempValores=litrosPorBomba[contador] * listaBombas[contador].valorLitro
    return tempValores

def somaDosDinheiros(contador,listaBombas,dinheiroPorBombasLitros):
    tempDinheiroBomba=listaBombas[contador].RvDinheiro + dinheiroPorBombasLitros[contador]
    return tempDinheiroBomba


def escreverNoArquivo(listaBombas,valorCaixa,diferencaDinheiro,dinheiroTotalBombas):
    with open("resultadoCaixa.txt","w") as arquivo:
        arquivo.write(f"Valor do dinheiro do caixa do dia: {valorCaixa:.2f}\n")
        arquivo.write(f"Valor do dinheiro das Bombas: {dinheiroTotalBombas:.2f}\n")
        arquivo.write(f"Diferenca: \n\t( Se for positivo -> ESTA PASSANDO \t Se for negativo -> ESTA FALTANDO):\n\t\t{diferencaDinheiro:.2f}\n\n")
        for i in range (0,6):
            arquivo.write(f"Bomba {i+1}\tLitros:{listaBombas[i].litroTotalMedido}\tLitros Revenda: {listaBombas[i].RvLitro}\n")