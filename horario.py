# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
#------------------------------------------------------------------

'''
    09/09/2021 - EXERCÍCIO EM GRUPO - GRUPO 19
    Nome:Sthephany de Fatima de Oliveira
    NUSP: 10694139
    
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
        -Mesclei meu código com o do amigo Carlo Chede Broggi do grupo 19. 
'''
def main():
    print("Executando a main() no arquivo horario.py")

    print("Teste da classe Horario")
    t0 = Horario()      ### 
    print("t0 = ", t0)

    print(f"__name__ dentro do arquivo horario.py = {__name__}")
    print("Fim da main() no arquivo horario.py")
    
def main_velha():

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

    h = Horario(5853, 34324114, 5324325)
    print(f'Teste adicional: h = {h} deve retornar 16:32:45')

class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.

       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve se "comportar" ilustrados no enunciado.
    '''
    def __init__(self, horas = 0, minutos = 0, segundos = 0):
        if segundos>59:
            minutos= minutos + segundos//60
            segundos=segundos%60
            
        if minutos>59:
            horas= horas + minutos//60
            minutos = minutos%60
            
        if horas>23: 
            horas=horas%24

        self.dados = [segundos, minutos, horas]

    def __str__ (self):
        ''' lista -> str

        Recebe um referência 'self' a um objeto da classe Horario e cria e 
        retorna a string que representa o objeto.

        Utilizado por prin() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe

        Exemplo:

        >>> aula = Horario(0,30,13)
        >>> print(aula)
        13:30:00
        '''
        
        s = str(self.dados[-3])
        m = str(self.dados[-2])
        h = str(self.dados[-1])
        if len(s) < 2:
            s = '0' + s
        if len(m) < 2:
            m = '0' + m
        if len(h) < 2:
            h = '0' + h
        return f'{h}:{m}:{s}'
    def __add__ (self, other):
            ''' (Horario, Horario) -> Horario
            Retorna a soma do Horario 'self' e do Horario 'other'.
            Usado pelo Python quando escrevemos Horario + Horario.
            '''
            sf = self.dados[-3] + other.dados[-3]
            sec = 0
            minutos = 0
            minutes = 0
            horas = 0
            hours = 0
            if sf > 59: #verificando se a quantidade de segundos somados excede 60
                minutos = sf//60 #guardando o excesso como minutos pra somar depois
                sec = sf % 60
                sf = str(sf%60) #guardando como str o que sobrou de segundos
            else:
                sec = sf
                sf = str(sf)

                  
            mf = self.dados[-2] + other.dados[-2] + minutos
            if mf > 59: #verificando se a quantidade de minutos somados excede 60
                horas = mf//60 #guardando o excesso como horas pra somar depois
                minutes = mf%60
                mf = str(mf%60) #guardando como str o que sobrou de minutos
            else:
                minutes = mf
                mf = str(mf)
                
                
            hf = self.dados[-1] + other.dados[-1] + horas
            if hf > 23: #verificando se a quantidade de horas somados excede 24
                hours = hf%60
                hf = str(hf%24) #guardando como str o que sobrou de horas
            else:
                hours = hf
                hf = str(hf)

            if sec < 0: #se no final os segundos forem menores que 0 ele soma 60 e desconta 1 dos minutos
                sec = sec + 60
                sf = str(sec)
                minutes = minutes - 1
                mf = str(minutes)
                if minutes < 0: #se depois disso os minutos forem negativos ele soma 60 e desconta 1 de horas
                    minutes = minutes + 60
                    mf = str(minutes)
                    hours = hours - 1
                    hf = str(hours)
                    if hours < 0: #se depois disso as horas forem negativas ele soma 24
                        hours = hours + 24
                        hf = str(hours)

            if minutes < 0: 
                minutes = minutes + 60
                mf = str(minutes)
                hours = hours - 1
                hf = str(hours)
                if hours < 0:
                    hours = hours + 24
                    hf = str(hours)
                    
            if hours < 0:
                    hours = hours + 24
                    hf = str(hours)
            
            if len(sf) < 2:
                sf = '0' + sf
            if len(mf) < 2:
                mf = '0' + mf
            if len(hf) < 2:
                hf = '0' + hf

                
            return f'{hf}:{mf}:{sf}'
    
    def __eq__(self, other):
        ''' (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario == Horario
        '''
        tempo1=tempo(self.dados)
        tempo2=tempo(other.dados)
        return tempo1==tempo2

    def __gt__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario > Horario 
        """
        return other<self
    
    def __ge__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario >= Horario 
        """
        return other<=self
    
    def __lt__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario < Horario 
        """
        tempo1=tempo(self.dados)
        tempo2=tempo(other.dados)
        
        return tempo1<tempo2
    
    def __le__(self, other):
        """ (Horario, Horario) -> bool

        Retorna a comparação do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario <= Horario 
        """
        tempo1=tempo(self.dados)
        tempo2=tempo(other.dados)
        
        return tempo1<=tempo2
        
    def __neg__(self):
        '''(Horario, Horario) -> Horario

        Retorna a subtração do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario - Horario
        '''

        s = -(self.dados[-3])
        m = -(self.dados[-2])
        h = -(self.dados[-1])
        
        return Horario (h, m, s)
         
        
    def __sub__(self, other):
        """ (Horario, Horario) -> Horario

        Retorna a subtração do Horario `self` com o Horario `other`.
        Usado pelo Python quando escrevemos Horario - Horario

        Se other for maior que self, o resultado é 00:00:00.
        """
        tempo1=tempo(self.dados)
        tempo2=tempo(other.dados)
        
        if(tempo1<=tempo2):
            
            return Horario()
        else:
            return Horario(0,0,tempo1 + (-tempo2))
            
def tempo(V):
    ''' (lista) -> int
    
    retorna o tempo total em segundos do horario analisado
    
    '''
    
    t=0
    for i in range(0,3):
        
        t=t+V[i]*60**i
        
    return t                            
                                        
    
if __name__ == '__main__':
    main()
