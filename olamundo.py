#('Professor  Alberto programa v.0.0.1 15/03/2021 cls 01olamundo.py')
print('\n'*2)
print('*'*100)
print('')
print('https://professorjar.github.io/gerenciamentodeprojetos/index.html   ')
print('')
print('Sistema de cadastro versão 1.0.2 08/05/2021  ')
print('')
print('*'*100)
print('\n'*1)
hospital = ('JOSÉ ALBERTO RODRIGUES')
nome = input('Nome.................: ')
print('')
senha = input('Senha................: ')
print('')
print('*'*100)
file = open('cadastro.html','at+')
file.write(f'<h1><MARQUEE> <p>HOSPITAL {hospital} </MARQUEE> </p></h1>\n')
file.write(f'<h1> <p>Nome..........: {nome}  </p></h1>\n')
file.write(f'<h1> <p>Senha...........: {senha} </p></h1>\n')
print('*'*100)
print('')
print ('Ler arquivo:            ')
file.seek(0,0)
print(file.read())
file.seek(0,0)
file.close() 
print('')
fim = input('Tecle enter...........: ')
import olamundo.py

