# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


alunoReg = namedtuple("automovelReg", "id, nome")
listaAutos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaAutos)):
        if listaAutos[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_aluno():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    
    registo = alunoReg(cod, nome)
    listaAutos.append(registo)


def pesquisar_aluno():
    cod = input("Qual o codigo do aluno a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    print "Código: ", listaAutos[pos].id
    print "Nome: ", listaAutos[pos].nome
    


def listar_alunos():
    for i in range (len(listaAutos)):
        print "Código: ", listaAutos[i].id
        print "Nome: ", listaAutos[i].nome
        
  

def eliminar_aluno():
    cod = input ("Código do aluno a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # TODO: Confirmar eliminação
    listaAutos.pop(pos)


    
def alterar_aluno():
    cod = input ("Código do aluno a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listaAutos[pos] = listaAutos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            inserir_aluno()
        elif op =='2':
            listar_alunos()
        elif op == '3':
            pesquisar_aluno()
        elif op == '4':
            alterar_aluno()
        elif op == '5':
            eliminar_aluno()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"