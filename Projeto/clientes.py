# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


clienteReg = namedtuple("clienteReg", "id, nome, morada, bi, carta_de_conducao")
listaclientes = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaclientes)):
        if listaclientes[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_clientes():
    cod = input("Qual o id? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "id já existe"
        return

    #ler dados
    nome= raw_input("Qual é o nome?")
    morada= raw_input("Qual a morada?")
    bi= raw_input("Qual o bi")
    carta_de_conducao= raw_input("Qual a carta de condução?")
    
    
    
    
    registo =clienteReg(cod, nome, morada, bi, carta_de_conducao)
    listaclientes.append(registo)


def pesquisar_clientes():
    cod = input("Qual o id do cliente a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existem clientes com esse código"
        return

    print "Código", listaclientes[pos].id
    print "nome", listaclientes[pos].nome
    print "morada",listaclientes[pos].morada
    print "bi",listaclientes[pos].bi
    print "carta_de_conducao",listaclientes[pos].carta_de_conducao
    


def listar_clientes():
    for i in range (len(listaclientes)):       
        print "cod", listaclientes[i].id
        print "nome", listaclientes[i].nome
        print "morada",listaclientes[i].morada
        print "bi",listaclientes[i].bi
        print "carta_de_conducao",listaclientes[i].cadef pesquisar_Autos():
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
    print "Este programa não deve ser executado diretamente"rta_de_conducao
        
        
  

def eliminar_clientes():
    cod = input ("Código do cliente a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existem clientes com esse código"
        return

    # TODO: Confirmar eliminação
    listaclientes.pop(pos)


    
def alterar_clientes():
    cod = input ("Código do cliente a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existem clientes com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome?")
    lista.clientes[pos]==lista.clientes[pos]_replace(nome=novonome)



        
    
def gerir():

    terminar = False

    while not terminar:
        op = menu.clientes()

        if op == '1':
            inserir_clientes()
        elif op =='2':
            listar_clientes()
        elif op == '3':
            pesquisar_clientes()
        elif op == '4':
            alterar_clientes()
        elif op == '5':
            eliminar_clientes()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"