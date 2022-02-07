# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

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
    def __init__(self, a=00, b=00, c=00):
        dados = [c,b,a]
        self.dados = dados
        self.hora = dados[2]
        self.minuto = dados[1]
        self.segundo =  dados[0]
        
        
        m = 0
        h = 0
        
        while self.segundo > 59:
            self.segundo -= 60
            m +=1
            
        self.minuto += m

        while self.minuto > 59:
            self.minuto -= 60
            h += 1
        
        self.hora += h
        
        while self.hora > 23:
            self.hora -= 24
                    
            
    def __str__ (self):
            
        return f"'{self.hora}:{self.minuto}:{self.segundo}'"
        
    
    def __add__ (self, other):
        segundo = self.segundo + other.segundo
        minuto = self.minuto + other.minuto
        hora = self.hora + other.hora
        
        return Horario(hora,minuto,segundo)
    
    def __sub__ (self, other):
        
        hora = 0
        minuto = 0
        segundo = (self.segundo - other.segundo)
        
        while segundo <= 0:
            segundo += 60
            minuto -= 1
            
            minuto += (self.minuto - other.minuto)
            while minuto < 0:
                minuto += 60
                hora -= 1
        
                hora += (self.hora - other.hora)
                while hora < 0:
                    hora += 24
                
        
        return Horario (hora,minuto,segundo)
        
        
    
    def __lt__ (self, other):
        if self.hora < other.hora :
            return True
        
        return False    

if __name__ == '__main__':
    main()
        
