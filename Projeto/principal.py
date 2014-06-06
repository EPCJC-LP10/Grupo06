# -*- coding: iso8859-1 -*-

import menu
import automoveis
import util


# nome dos ficheiros
fxAutos = "fxAutos.dat"
fxClientes = "fxClientes.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	automoveis.listaAutos = util.ler_ficheiro(fxAutos)
     clientes.listaClientes = util.ler_ficheiro(fxClientes)


def escrever_ficheiros():
	util.escrever_ficheiros(fxclientes, clientes.listaclientes)
1	util.escrever_ficheiro(fxAutos, automoveis.listaAutos)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        automoveis.gerir()
    elif op == '2':
        clientes.gerir()    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()
