#arquivo teste_escrita.py
arquivo = open('teste.txt', 'a')
arquivo.write('Python rocks \n')
arquivo.close()

logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()