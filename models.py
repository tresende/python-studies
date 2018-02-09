# -*- coding: UTF-8 -*-

#perfil = Perfil_Vip(empresa='IBM', telefone='(31)9-9768-0765', nome='Thiago Resende')

class Perfil(object):
    'Classe Padrao de perfil'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0        

    def imprimir(self):
        print 'Nome: %s, Teleone: %s ,Empresa %s  ,Curtidas %s' % (self.nome, self.telefone, self.empresa, self.__curtidas) 
    
    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        perfis = []
        arquivo = open(nome_arquivo,'r')
        for linha in arquivo:
            valores = linha.split(',')
            perfis.append(Perfil(*valores))
        arquivo.close()
        return perfis

class Perfil_Vip(Perfil):
    'Classe Padrao de perfil'

    def __init__(self, nome, telefone, empresa, apelido = ''): 
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0