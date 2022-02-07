# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Emanuel Victor Vendramini
    NUSP: 12556757

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
def main():

    t1 = Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = Horario(23,59,59)
    t6 = Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')

    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')


class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.
 
       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve se "comportar" ilustrados no enunciado.
    '''
    def __init__( self , horas = 0 , minutos = 0 , segundos = 0 ):
        if 24*60*horas + 60*minutos + segundos >= 0:
            self.dados = [ segundos%60 , ( segundos//60 + minutos )%60 , ( ( segundos//60 + minutos )//60 + horas )%24 ]
        else:
            self.dados = [0,0,0]
    def __add__( self , other ):
        H = self.dados[2] + other.dados[2]
        M = self.dados[1] + other.dados[1]
        S = self.dados[0] + other.dados[0]
        return Horario( H , M , S )
    def __str__( self ):
        H = f"{self.dados[2]//10}" + f"{self.dados[2]%10}"
        M = f"{self.dados[1]//10}" + f"{self.dados[1]%10}"
        S = f"{self.dados[0]//10}" + f"{self.dados[0]%10}"
        return H + ':' + M + ':' + S
    def __gt__( self , other ):
        for i in range(2,-1,-1):
            if self.dados[i] <= other.dados[i]:
                return False
            if self.dados[i] > other.dados[i]:
                return True
    def __lt__( self , other ):
        return other > self
    def __ge__( self , other ):
        for i in range(2,-1,-1):
             if self.dados[i] < other.dados[i]:
                return False
             if self.dados[i] >= other.dados[i]:
                return True
    def __le__( self , other ):
        return other >= self
    def __eq__( self , other ):
        for i in range(3):
            if self.dados[i] != other.dados[i]:
                return False
        return True
    def __sub__( self , other ):
        H = self.dados[2] - other.dados[2]
        M = self.dados[1] - other.dados[1]
        S = self.dados[0] - other.dados[0]
        return Horario( H , M , S )
if __name__ == 'horario':
    main()