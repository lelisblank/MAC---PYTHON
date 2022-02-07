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

## ==================================================================

def main():
    print("Teste 2R:", fibonacciR(2))
    print("Teste 5R:", fibonacciR(5))
    print("Teste 10R:", fibonacciR(10))
    print("Teste 20R:", fibonacciR(20))
    print("Teste 30R:", fibonacciR(30))
    print("Teste 40R:", fibonacciR(40))
    
    print ("\n")
    
    print("Teste 2I:", fibonacciI(2))
    print("Teste 5I:", fibonacciI(5))
    print("Teste 10I:", fibonacciI(10))
    print("Teste 20I:", fibonacciI(20))
    print("Teste 30I:", fibonacciI(30))
    print("Teste 40I:", fibonacciI(40))
    
    

def fibonacciR(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma recursiva.
    Retorna o valor calculado.

    Exemplos:
    fibonacciR(5) = 5
    fibonacciR(10) = 55
    fibonacciR(20) = 6765
    fibonacciR(30) = 832040
    fibonacciR(40) = 102334155
    '''

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibonacciR(n-2) + fibonacciR(n-1)
    # F = Fn-1 + Fn-2


## ==================================================================

def fibonacciI(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma iterativa.
    Retorna o valor calculado.
    '''
    lista = [0,1,1]
    i = 3
    while i<=n:
        soma = lista[i-2] + lista[i-1]
        lista+= [soma]
        i+=1
        
    return lista[-1]




if __name__ == '__main__':
    main()