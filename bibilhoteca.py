#from bibilhoteca import *
#processa_convite('thiago resende')

nomes = []

def gera_nome_convite(nome_convidado):
    posicao_final = len(nome_convidado)
    posicao_inicial = posicao_final - 4
    parte1 = nome_convidado[0:4]
    parte2 = nome_convidado[posicao_final-4:posicao_final]
    return parte1 + ' ' + parte2

def envia_convite(nome_convidado):
    print "Enviando convite para %s" %(nome_convidado)

def processa_convite(nome_convidado):
    nome_formatado = gera_nome_convite(nome_convidado)
    envia_convite(nome_formatado)

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def ano_como_string():
    print 'Digite o ano:'
    ano = raw_input()
    ano = int(ano)
    idade = 2017 - ano
    print idade

def remover(nomes):
    print 'Qual nome voce gostaria de remover'
    nome = raw_input()      
    nomes.remove(nome)  