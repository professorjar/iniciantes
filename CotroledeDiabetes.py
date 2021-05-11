import sqlite3
from Class_aula import *
print("\n" * 1)
# Autor: José Alberto Rodrigues 26 Dezembro 2020
# Para gerar .exe PyInstaller nomedoseuarquivo.py
print("="*62)
print("* CONTROLE DE DIABETES VERSÃO 2.0.2 *")
print("MENU 4 Liberdades VERSÃO 1.0.3 https://github.com/professorjar ")
print("="*62)
print(" ")
registro = float(input('Pressione 0 para continuar : '))
if registro == 0:
     print()
     print('=' * 50)
     print('CONTROLE DE DIABETES VERSÃO 1.0.1')
     print('=' * 50)
     print()
     nome = input("Nome do paciente: ")
     telefone = input("Fone : ")
     prontuario = input("Prontuário : ")
     rg = input("RG  : ")
     cpf = input("CPF : ")
     email = input("E-mail  : ")
     destro = input("Valor do destro : ")
     print("\n" *1)
     print("* A.V.A & S.A.E   2021 Versão 1.0.2  *")
     print (" ")
     print ("="*62)
     conexão = sqlite3.connect("diabetes.db")
     cursor = conexão.cursor()
     cursor.execute('''
           create table if not exists c_diabetes (
            Nome text,
         Telefone text,prontuario text, RG text, Cpf text, email text,destro text)
            ''')
     cursor.execute('INSERT INTO c_diabetes (Nome,Telefone,prontuario,RG,Email,Cpf,destro) VALUES (?,?,?,?,?,?,?)',(nome,telefone,prontuario,rg,email,cpf,destro))
     conexão.commit()
     cursor.close()
     conexão.close()
