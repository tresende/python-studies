from models import *
arquivo = None
try:
    arquivo = open('perfis.csv', 'r')
    valores = arquivo.readline().split('.')
    Perfil(*valores)
    print('arquivo aberto')
    arquivo.close()
except (IOError, TypeError) as erro:
    print ('Deu IOError')      
# except IOError as erro:
#     print ('Deu IOError')
# except TypeError as erro:
#     print ('Deu TypeError')  
finally:
    if(arquivo is not None)
        print('fechado arquivo')
        arquivo.close()