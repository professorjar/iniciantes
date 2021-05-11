class Bvsmatrix:
    print('='*100)
    funcionario=0
    trabalhando=False
    indicado=''
    def __init__(self,f,t,i):
        self.funcionario=f
        self.trabalhando=t
        self.indicado=i
    def mostrar(self):
        print('Professor: JOSÉ ALBERTO RODRIGUES VERSÃO 1.0.3 19/04/2021:')
        print('Projetos no site do ava & sae..: https://github.com/professorjar')
        print('Funcionário....................: ' + str(self.funcionario))
        estado = 'sim' if self.trabalhando else 'Não'
        print('Trabalhando....................: ' + estado)
        print('Indicado.......................: ' + (self.indicado))
        print('Projetos..: https://professorjar.github.io/gerenciamentodeprojetos/index.html')
        print('=' *100)
fu1=Bvsmatrix(778,False,'Sim,por Morpheus')
fu1.mostrar()
#def orçamento():
# Este programa calcula a quantidade de blocos para sua construção
# print('='*100)
#  print(" ")
#  print(''' Calcula quantos blocos de cimento com a medida de 39x19\n você vai necessitar para construir uma parede informe: ''')
#  print(" ")
# largura = float(input("Qual e a largura da parede: "))
# print(" ")
# altura = float(input('Qual é a altura da parede: '))
# print(" ")
# valor = largura * altura
#    r1 = valor
#   print(f'Sua parede tem {r1} metros quadrados')
#    print(" ")
#   resultado = r1 * 12.5
#   print(f'Você vai necessitar de {resultado}')
#    print(" ")
#   print('=' * 64)
#orçamento()