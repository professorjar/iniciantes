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