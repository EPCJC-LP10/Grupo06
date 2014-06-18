# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 10:43:27 2014

@author: i13358
"""

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Automóveis"
    print "   2. Gestão de Clientes"
    print "   3. Efetuar Aluguer"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def automovel():
    print
    print " *** Menu Alugueres **** "
    print
    print "1. Inserir novo Aluguer"
    print "2. Listar todos Alugueres"
    print "3. Pesquisar Alugueres"
    print "4. Alterar dados de um Aluguer"
    print "5. Eliminar Aluguer"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"