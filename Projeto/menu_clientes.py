# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 11:38:24 2014

@author: i13358
"""

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Automóveis"
    print "   2. Gestão de Clientes"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Opção: ")
    return op


def automovel():
    print
    print " *** Menu Automoveis **** "
    print
    print "1. Inserir novo clientel"
    print "2. Listar todos clientes"
    print "3. Pesquisar cliente"
    print "4. Alterar dados de um cliente"
    print "5. Eliminar cliente"
    print 
    print "0. Menu Anterior"

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"