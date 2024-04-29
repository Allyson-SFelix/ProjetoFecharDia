from funcoesSobDados import *
def trabalharNosDados(listaBombas,Bombas):
    litrosFinaisPorBomba=[0]*6
    dinheiroPorBombaDosLitros=[0]*6
    dinheiroPorBombaTotal=[0]*6
    dinheiroTotalBombas=0
    for i in range(0,6):
        litrosFinaisPorBomba.append(somaLitroFinal(i,listaBombas))
        dinheiroPorBombaDosLitros.append(somaDinheiroPorBomba(i,listaBombas,litrosFinaisPorBomba))
        dinheiroPorBombaTotal.append(somaDosDinheiros(i,listaBombas,dinheiroPorBombaDosLitros))
        dinheiroTotalBombas+=dinheiroPorBombaTotal[i]
    
    valorCaixa=Bombas.dinheiroCaixa + Bombas.valesCaixa
    diferencaDinheiro=dinheiroTotalBombas - valorCaixa
    print(valorCaixa,diferencaDinheiro,dinheiroTotalBombas)
    escreverNoArquivo(valorCaixa,diferencaDinheiro,dinheiroTotalBombas)
    
    
def escreverNoArquivo(valorCaixa,diferencaDinheiro,dinheiroTotalBombas):
    with open("resultadoCaixa.txt","w") as arquivo:
        arquivo.write(f"Valor do dinheiro do caixa do dia: {dinheiroTotalBombas}\nValor do dinheiro das Bombas: {valorCaixa}\nDiferenca ( Se for positivo -> ESTA PASSANDO \t Se for negativo -> ESTA FALTANDO): {diferencaDinheiro}")
    
def somaLitroFinal(contador,listaBombas):
    tempPorBombas=listaBombas[contador].litroTotalMedido - listaBombas[contador].RvLitro 
    print(tempPorBombas)
    return tempPorBombas

def somaDinheiroPorBomba(contador, listaBombas,litrosPorBomba):
    tempValores=litrosPorBomba[contador] * listaBombas[contador].valorLitro
    print(tempValores)
    return tempValores

def somaDosDinheiros(contador,listaBombas,dinheiroPorBombasLitros):
    tempDinheiroBomba=listaBombas[contador].RvDinheiro + dinheiroPorBombasLitros[contador]
    return tempDinheiroBomba