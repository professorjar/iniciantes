#('Professor Alberto programa v.0.0.1 15/03/2021 cls 01olamundo.py')
print('\n'*2)
print('*'*40)
print('\n'*1)
print('   Sistema de cadastro  ')
print('\n'*1)
nome = input(' Nome: ')
print('')
idade = input(' Idade: ')
print('')
print('*'*40)
file = open('cadastro.txt','at+')
file.write(f'<p> {nome}                  Idade: {idade} <p>\n')
print ('Ler arquivo:            ')
file.seek(0,0)
print(file.read())
file.seek(0,0)
file.close() 
print('')
fim = input('Tecle enter: ')
