import sqlite3
import __init__
#print("\n" * 1)
# Autor: José Alberto Rodrigues 26 Dezembro 2020 10/05/2021
# Para gerar .exe PyInstaller nomedoseuarquivo.py
print("="*100)
print("* Bolsa de valores sociais versão 1.0.1 *")
print("Site do projeto.................: https://professorjar.github.io/gerenciamentodeprojetos/index.html")
print("="*100)
print(" ")
registro = float(input('Pressione 0 para continuar : '))
if registro == 0:
     print()
     print('=' * 62)
     print('')
     print('=' * 62)
     print()
     nome = input("Nome do solicitante............: ")
     telefone = input("Fone...........................: ")
     prontuario = input("Prontuário.....................: ")
     rg = input("RG.............................: ")
     cpf = input("CPF............................: ")
     email = input("E-mail.........................: ")
     destro = input("Valor da ação social...........: ")
     print("\n" *1)
     print("* Faça parte da nossa bolsa de valores sociais 15/05/2021 versão 1.0.1  *")
     print (" ")
     print ("="*62)
     conexão = sqlite3.connect("bvs.db")
     cursor = conexão.cursor()
     cursor.execute('''
           create table if not exists cad_bvs (
            Nome text,
         Telefone text,prontuario text, RG text, Cpf text, email text,destro text)
            ''')
     cursor.execute('INSERT INTO cad_bvs (Nome,Telefone,prontuario,RG,Email,Cpf,destro) VALUES (?,?,?,?,?,?,?)',(nome,telefone,prontuario,rg,email,cpf,destro))
     conexão.commit()
     cursor.close()
     conexão.close()