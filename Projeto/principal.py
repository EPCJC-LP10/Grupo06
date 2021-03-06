# -*- coding: iso8859-1 -*-

import menu
import automoveis
import util
import clientes
import alugueres

# nome dos ficheiros
fxAutos = "fxAutos.dat"
fxClientes = "fxClientes.dat"

def ler_ficheiros():
    # adicionar todos ficheiros a ler
    automoveis.listaAutos = util.ler_ficheiro(fxAutos)
    clientes.listaClientes = util.ler_ficheiro(fxClientes)


def escrever_ficheiros():
	util.escrever_ficheiro(fxClientes, clientes.listaclientes)
	util.escrever_ficheiro(fxAutos, automoveis.listaAutos)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        automoveis.gerir()
    elif op == '2':
        clientes.gerir()
    elif op == '3':
        alugueres.gerir()    
    elif op == '0':
        terminar = True


escrever_ficheiros()
