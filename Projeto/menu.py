# -*- coding: iso8859-1 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gest�o de Autom�veis"
    print "   2. Gest�o de Clientes"
    print "   3. Efetuar Aluguer"
    print 
    print "   0. Sair"
    print 

    op = raw_input("Op��o: ")
    return op


def automovel():
    print
    print " *** Menu Automoveis **** "
    print
    print "1. Inserir novo automovel"
    print "2. Listar todos automovel"
    print "3. Pesquisar automovel"
    print "4. Alterar dados de um automovel"
    print "5. Eliminar automovel"
    print 
    print "0. Menu Anterior"

    op = raw_input("Op��o: ")
    return op



if __name__ == "__main__":
    print "Este programa n�o deve ser executado diretamente"