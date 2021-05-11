import sqlite3
from aula04.lib.ava import *
import class_aula_nova
print("\n" * 1)
# Autor: José Alberto Rodrigues 26 Dezembro 2020 10/05/2021
# Para gerar .exe PyInstaller nomedoseuarquivo.py
print("="*100)
print("* CONTROLE DE EMPRESAS VERSÃO 1.0.2*")
print(" https://professorjar.github.io/gerenciamentodeprojetos/index.html")
print("="*100)
print(" ")
registro = float(input('Pressione 0 para continuar : '))
if registro == 0:
     print()
     print('=' * 50)
     print('CADASTRO DE EMPRESAS VERSÃO 1.0.1')
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
     conexão = sqlite3.connect("tecer.db")
     cursor = conexão.cursor()
     cursor.execute('''
           create table if not exists cad_empresa (
            Nome text,
         Telefone text,prontuario text, RG text, Cpf text, email text,destro text)
            ''')
     cursor.execute('INSERT INTO cad_empresa (Nome,Telefone,prontuario,RG,Email,Cpf,destro) VALUES (?,?,?,?,?,?,?)',(nome,telefone,prontuario,rg,email,cpf,destro))
     conexão.commit()
     cursor.close()
     conexão.close()