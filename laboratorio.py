'''

    Nome: Letícia Maia
    NUSP: 11781715

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que trabalhos sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    
    Estou ciente que os casos de plágio e desonestidade acadêmica
    estarão sujeitos às penalidades descritas na página da disciplina
    na seção "Sobre colaboração em MAC0122".

    Reconheço que utilizei as seguintes fontes externas ao conteúdo 
    utilizado e recomendado em MAC0122, ou recebi auxílio das pessoas
    listadas abaixo.

    - LISTA de fontes externas utilizadas (links ou referências como livros)
        - 

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''
# https://docs.python.org/3/library/random.html
import random

#------------------------------------------------
DATAS    = 365
SUCESSO  = True
FRACASSO = False

## ==================================================================
# 
def main():
    '''
    Testes da classe Aniversario

    inclua mais 10 testes usando valores distintos de n e t.
    '''
    '''
    print("Testes do EG27 - Paradoxo do Aniversário")
    a = Aniversario(10,10)
    print (f'teste 1 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(10,100)
    print (f'teste 2 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(10,1000)
    print (f'teste 3 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(10,10000)
    print (f'teste 4 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(20,100)
    print (f'teste 5 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(20,1000)
    print (f'teste 6 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(45,100)
    print (f'teste 7 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(45,1000)
    print (f'teste 8 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(364,10000)
    print (f'teste 9 ({a.n} pessoas e {a.t} tentativas)= {a}')
    print('-------------------------------------------------')
    a = Aniversario(2,100000)
    print (f'teste 10 ({a.n} pessoas e {a.t} tentativas)= {a}')
'''
    
    print("Testes do EG27 - Colecionadora de Figurinhas")
    b = Colecionadora(10,2)
    print (f'teste 1 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

    b = Colecionadora(10,20)
    print (f'teste 2 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')
    

    b = Colecionadora(10,200)
    print (f'teste 3 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

    b = Colecionadora(10,20000)
    print (f'teste 4 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

    b = Colecionadora(45,100)
    print (f'teste 5 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

    b = Colecionadora(45,1000)
    print (f'teste 6 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

    b = Colecionadora(1000,10)
    print (f'teste 7 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

    b = Colecionadora(1000,1)
    print (f'teste 8 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

    b = Colecionadora(20,100)
    print (f'teste 9 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

    b = Colecionadora(0,100)
    print (f'teste 10 ({b.n} figurinhas e {b.t} tentativas)= {b}')
    print('-------------------------------------------------')

#--------------------------------------------------------------------
#
#  ANIVERSARIO
#
#--------------------------------------------------------------------
class Aniversario:
    #------------------------------------------
    def __init__(self, n, t):
        '''(Aniversario, int, int) -> None
        RECEBE um inteiro n e um inteiro t;
        REALIZA t experimentos em que n datas são selecionadas uniformemente ao acaso.
        CALCULA a probabilidade observada de que dentre as n datas haja pelo menos 
                duas iguais.
        '''        
        self.n = n
        self.t = t
        sucessos = 0
        for i in range(t): sucessos += self.experimento()
        self.p = sucessos/t    
        
    #------------------------------------------    
    def __str__(self):
        return f"Aniversario({self.n}, {self.t}) = {self.p}"

    #------------------------------------------    
    def mean(self):
        return self.p

    #-----------------------------------------
    def experimento(self):
        ''' (Aniversario) -> bool

        Executa um experimento como descrito no enunciado,
        para uma sala com até 
        * self.n pessoas e 
        * self.t tentativas (trials)
        Retorna SUCESSO ou FRACASSO.

        DICA: para esse método, conjuntos são mais 
        eficientes que listas.
        '''
        aniversarios = set() 
        
        for j in range(self.n):
            a = random.randrange(DATAS)
            if a in aniversarios: return True
            aniversarios.add(a)
        return False
       
   
#----------------------------------------
def prob_aniversario(n):
    '''(int) -> float
    RECEBE um inteiro n.
    RETORNA a probabilidade de em um grupo de n pessoas haja
       pelo menos 2 que fazem aniversário em um mesmo dia.

    Implementação alternativa:
    import math
    num = math.factorial(DATAS)
    den = math.factorial(DATAS-n)
    prob_c = num/(DATAS**n * den)
    '''
    prob_c = 1
    for i in range(n):
        prob_c *= (1 - i/DATAS)
    return 1 - prob_c

#--------------------------------------------------------------------
#
#  COLECIONADORA
#
#--------------------------------------------------------------------
class Colecionadora:
    #------------------------------------------
    def __init__(self, n, t):
        '''(Colecionadora, int, int) -> None
        RECEBE um inteiro n e um inteiro t;
        REALIZA t experimentos em que figurinhas entre 0 e n são compradas 
           uniformemente ao acaso até que tenhamos as n figurinhas.
        CALCULA o número medio de figurinhas compradas no experimento.
        '''
        self.n = n
        self.t = t
        no_figurinhas = 0
        for i in range(t): no_figurinhas += self.experimento()
        self.n_medio = no_figurinhas/t    

    #------------------------------------------
    def __str__(self):
        return f"Colecionadora({self.n}, {self.t}) = {self.n_medio}"

    #------------------------------------------    
    def mean(self):
        return self.n_medio

    #-----------------------------------------
    def experimento(self):
        ''' (Colecionadora) -> int
        EXECUTA um experimento em que figurinhas entre 0 e self.n são 
           compradas até que tenhamos as n figurinhas.
        RETORNA o número k de figurinhas compradas.
        '''
        figurinhas = set()
        k = 0
        while len(figurinhas) < self.n:
            figurinhas.add(random.randrange(self.n))
            k += 1
        return k
        
        # implemente sua solução

#----------------------------------------------------------------------
def no_figurinhas(n):
    '''(int) -> float
    RECEBE um inteiro. 
    RETORNA o número experado de figurinhas que devem ser compradas para
        completarmos um álbum de n figurinhas. 
    '''
    hn = 0
    for i in range(n,0,-1): hn += 1/i
    return n*hn
    
## ==================================================================
# 
if __name__ == '__main__':
    main()
