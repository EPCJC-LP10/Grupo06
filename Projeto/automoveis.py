# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


AutomoveisReg = namedtuple("automovelReg", "id, marca, modelo, cor, cilindrada, ano_aquisicao, matricula, valor_aluguer_por_dia, alugado")
listaAutos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaAutos)):
        if listaAutos[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_Autos():
    cod = input("Qual o id? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "id já existe"
        return

    #ler dados
    marca= raw_input("Qual a marca?")
    modelo= raw_input("Qual é o modelo")
    cor= raw_input("Qual a cor?")
    cilindrada= raw_input("Qual a cilindrada")
    ano_aquisicao= raw_input("Qual o ano de aquisição?")
    matricula= raw_input("Qual a matricula?")
    valor_aluguer_por_dia= raw_input ("Qual o ano de aquisição?")
    alugado = True
    
    
    
    registo = AutomoveisReg(cod, marca, modelo, cor, cilindrada, ano_aquisicao, matricula, valor_aluguer_por_dia, alugado)
    listaAutos.append(registo)


def pesquisar_Autos():
    cod = input("Qual o id do automovel a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existem automoveis com esse código"
        return

    print "Código: ", listaAutos[pos].id
    print "marca ", listaAutos[pos].marca
    print "modelo",listaAutos[pos].modelo
    print "cor",listaAutos[pos].cor
    print "cilindrada",listaAutos[pos].cilindrada
    print "matricula",listaAutos[pos].matricula
    print "ano_aquisicao",listaAutos[pos].ano_aquisicao
    print "valor_aluguer_por_dia",listaAutos[pos].valor_aluguer_por_dia
    


def listar_Autos():
    for i in range (len(listaAutos)):
        print "="*50
        print "Código: ", listaAutos[i].id
        print listaAutos[i].marca.upper(),
        print listaAutos[i].modelo.upper(),
        print "\t","matricula",listaAutos[i].matricula
        print        
        print "cor",listaAutos[i].cor
        print "cilindrada",listaAutos[i].cilindrada

        print "ano_aquisicao",listaAutos[i].ano_aquisicao
        print "valor_aluguer_por_dia",listaAutos[i].valor_aluguer_por_dia
        
        
  

def eliminar_Autos():
    cod = input ("Código do automovel a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe automovel com esse código"
        return

    # TODO: Confirmar eliminação
    listaAutos.pop(pos)


    
def alterar_Autos():
    cod = input ("Código do automovel a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe automovel com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listaAutos[pos] = listaAutos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.automovel()

        if op == '1':
            inserir_Autos()
        elif op =='2':
            listar_Autos()
        elif op == '3':
            pesquisar_Autos()
        elif op == '4':
            alterar_Autos()
        elif op == '5':
            eliminar_Autos()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"