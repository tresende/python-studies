from models import *
# perfil = Perfil_Vip('Thiago','(31)9-9768-0765','IBM', 1)
# perfil.curtir()
# perfil.curtir()
# perfil.curtir()
# perfil.obter_creditos()

perfis = []
arquivo = open('perfis.csv','r')
linha = arquivo.readline()
for linha in arquivo:
     valores = linha.split(',')
     perfil = Perfil(*valores)
     perfis.append(perfil)
arquivo.close()
print perfis