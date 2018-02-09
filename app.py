# -*- coding: UTF-8 -*-

#arquivo app.py

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print(resultados)

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome = raw_input()
    if(nome in nomes):
        index = nomes.index(nome)
        print 'Qual o novo valor?'
        nomes[index] = raw_input()
    else:
        print 'nao existe'

def procurar(nomes):
    print 'Digite o nome a procurar:'
    nome = raw_input()
    if(nome in nomes):
        print "Nome %s está cadastrado" % (nome)
    else:
        print "Nome %s não está cadastrado" % (nome)

def menu():
    nomes = ['a', 'b', 'c']
    escolha = ''
    
    while(escolha != '0'):    
        print '1 para cadastrar'
        print '2 para listar'
        print '3 para remover'
        print '4 Alterar'
        print '5 procurar'
        print '0 para terminar'
        print ''
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            remover(nomes)

        if(escolha == '4'):
            alterar(nomes)    

        if(escolha == '5'):
            procurar(nomes)                        


menu()