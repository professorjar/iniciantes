#('Professor  Alberto programa v.0.0.1 15/03/2021 cls 01olamundo.py')
print('\n'*2)
print('*'*100)
print('')
print('https://professorjar.github.io/gerenciamentodeprojetos/index.html   ')
print('')
print('Sistema de cadastro versão 1.0.1 08/05/2021  ')
print('')
print('*'*100)
print('\n'*1)
nome = input('Nome.................: ')
print('')
idade = input('Idade................: ')
print('')
print('*'*100)
file = open('cadastro.html','at+')
file.write(f'<p> {nome}                  Idade: {idade} <p>\n')
print ('Ler arquivo:            ')
file.seek(0,0)
print(file.read())
file.seek(0,0)
file.close() 
print('')
fim = input('Tecle enter: ')
