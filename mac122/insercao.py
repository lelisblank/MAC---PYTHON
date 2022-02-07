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
        - Teste do Caio retirada no gpo

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''
import random

def main():
    '''
        Testes das suas funções
    '''

    print("Testes do EI20 - ordenação por inserção")
    
    # insira_ultimo
    
    seq = [4, 7, 11, 5, 3]
    insira_ultimo(seq, 3)
    print(f'{seq}     e deveria ser [4, 7, 11, 5, 3]')

    insira_ultimo(seq, 4)
    print(f'{seq}     e deveria ser [4, 5, 7, 11, 3]')

    insira_ultimo(seq,5)
    print(f'{seq}     e deveria ser [3, 4, 5, 7, 11]')
    
    # ordene_por_insercao    
    print ('\n-----------------------------------------------\n')
    seq = [4, 7, 5, 3]
    ordene_por_insercao(seq)
    print(f'{seq}      e deveria ser [3, 4, 5, 7] \n\n-----------------------------------------------\n')
    
    
    # teste Caio
    for i in range(6):
        seq = random.sample([i for i in range(1000) ], 10)
        print(f'seq antes de ordenar: {seq}')
        ordene_por_insercao(seq)
        print(f'depois: {seq}\n')
    


## ==================================================================

def insira_ultimo(seq, n):
    ''' (list, int) -> None

    Essa função é a base para o algoritmo de ordenação 
    por inserção, que veremos em uma próxima aula e 
    não se trata de um algoritmo completo de ordenação.

    Essa função considerar apenas a porção da lista seq 
    no intervalo [0:n].

    A ideia é visitar cada elemento, a partir do fim da 
    porção, ou seja, do elemento de índice n-1.
    Caso o elemento anterior seja maior, os elementos são
    trocados de posição, fazendo o elemento visitado "descer"
    na lista. A varredura deve persistir enquanto o elemento 
    visitado for menor que o seu anterior.

    Por exemplo,  para seq = [4, 7, 11, 5, 3] e n = 3 a
    função não precisa fazer nada pois o elemento anterior
    ao 11 já é menor. 

    Para seq = [4, 7, 11, 5, 3] e n = 4 a
    função deve deslocar o 5 até que seq se torne 
    [4, 5, 7, 11, 3]. 

    Outro exemplo, para seq = [4, 5, 7, 11, 3] e n = 5 a
    função deve deslocar o 3 até que seq se torne 
    [3, 4, 5, 7, 11]. 

    DICA: não use outras listas, nem fatias. Basta
    varrer seq, comparar com seu vizinho anterior
    e trocar enquanto necessário.

    '''
    # escreva sua solução
    visit = n-1
    while visit > 0 and ( seq[visit] < seq[visit-1] ):
        seq[visit], seq[visit-1] = seq[visit-1], seq[visit]
        visit-=1
    
        
## ==================================================================

def ordene_por_insercao(seq):
    ''' (list) -> None

    A ideia de ordenação por inserção (insertion sort)
    é considerar porções da lista, a partir de 2 elementos até n.
    Para cada porção, apenas o último elemento precisa ser 
    deslocado até sua posição correta.

    Exemplo para a lista [4, 7, 5, 3]
    - inicio com a porção da lista de tamanho 2 contendo [4, 7, ? , ?]. 
        O último elemento já está na posição correta. 
    - a ordenação continua com a porção de tamanho 3 com [4, 7, 5, ?]
        O último elemento da porção, o 5, precisa ser deslocado até
        sua posição final [4, 5, 7, ?]
    - a ordenação continua com a porção de tamanho 4, agora com 
        [4, 5, 7, 3]. O último elemento da porção, o 3, precisa ser
        deslocado até sua posição final [3, 4, 5, 7].
    - fim, pois já tratamos todas as porções até o tamanho n.

    O que você deve fazer: 

    A função recebe uma sequência de números em ordem aleatória. 
    e retorna None. Ao terminar, seq deve estar em ordem
    crescente aplicando a ideia de ordenação por inserção.

    Essa função DEVE usar a função insira_ultimo().

    '''
    # escreva sua solução
    for i in range (2,len(seq)+1):
        a = insira_ultimo(seq, i)
        
        

## ==================================================================
## Escreva outras coisas que desejar
## ==================================================================


## ==================================================================

if __name__ == '__main__':
    main()

## ==================================================================
