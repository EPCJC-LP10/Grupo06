# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 10:47:10 2014

@author: i13358
"""

from collections import namedtuple

import menu_alugueres


AlugueresReg = namedtuple("alugueresReg", "id, identificacao_do_automovel, identificacao_do_cliente, data_de_inicio, data_de_fim, alugado")
listaAluguer = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaAluguer)):
        if listaAluguer[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_Aluguer():
    cod = input("Qual o id? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "id já existe"
        return

    #ler dados
    identificacao_do_automovel= raw_input("Qual a indentificacao do automovel?")
    identificacao_do_cliente= raw_input("Qual é a identificação do cliente")
    data_de_inicio= raw_input("Qual a data de inicio?")
    data_de_fim= raw_input("Qual a data de fim")
    alugado = True
    
    
    registo = AlugueresReg(cod, identificacao_do_automovel, identificacao_do_cliente, data_de_inicio, data_de_fim, alugado)
    listaAluguer.append(registo)


def pesquisar_Aluguer():
    cod = input("Qual o id do aluguer a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existem alugueres com esse código"
        return

    print "indentificacao_do_automovel: ", listaAluguer[pos].id
    print "identificacao_do_cliente ", listaAluguer[pos].marca
    print "data_de_inicio",listaAluguer[pos].modelo
    print "data_de_fim",listaAluguer[pos].cor
        

def listar_Aluguer():
    for i in range (len(listaAluguer)):
        print "="*50
        print "Código: ", listaAluguer[i].id
        print listaAluguer[i].identificacao_do_automovel.upper(),
        print listaAluguer[i].identificacao_do_cliente.upper(),
        print "\t","data_de_inicio",listaAluguer[i].data_de_inicio
        print        
        print "data_de_fim",listaAluguer[i].data_de_fim
        print      
        
        
  

def eliminar_Aluguer():
    cod = input ("Código do Aluguer a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existem Alugueres com esse código"
        return

    # TODO: Confirmar eliminação
    listaAluguer.pop(pos)


    
def alterar_Aluguer():
    cod = input ("Código do Aluguer a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existem Alugueres com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listaAluguer[pos] = listaAluguer[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu_alugueres.Aluguer()

        if op == '1':
            inserir_Aluguer()
        elif op =='2':
            listar_Aluguer()
        elif op == '3':
            pesquisar_Aluguer()
        elif op == '4':
            alterar_Aluguer()
        elif op == '5':
            eliminar_Aluguer()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"