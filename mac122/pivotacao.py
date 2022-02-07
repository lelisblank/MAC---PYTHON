# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome:
    NUSP:

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
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas de tamanho mínimo, em ordem crescente,
        decrescente, etc.
    '''
    print("Testes do EI23 - ordenação por pivotação")

def pivote_seq(seq):
    ''' (list) -> int

    Recebe uma lista seq com n>0 elementos 
    e rearranja seus elementos para que o pivô, 
    o último elemento da lista,
    esteja na posição "ordenada" com relação aos demais 
    elementos, ou seja, todos os elementos menores fiquem
    a esquerda e todos os maiores fiquem a direita do pivô.

    Retorna um índice m tal que

        seq[:m] <= seq[m] < seq[m+1:]
    
    Exemplos:
    In [1] seq = [5, 7, 4, 3, 8, 6]
    In [2] m = pivote_seq(seq)
    In [3] m
    3
    In [4] seq
    [5, 4, 3, 6, 8, 7]

    ...

    In [11] seq = [6, 7, 5, 3, 8, 4]
    In [12] m = pivote_seq(seq)
    In [13] m
    1
    In [14] seq
    In [3, 4, 5, 6, 8, 7]

    DICAS:
    - observe que a pivotagem não ordena os elementos à 
    esquerda e à direita do pivô. Portanto, seu resultado
    pode ser diferente, desde que o pivô esteja na posição 
    correta.
    - não use sort() para resolver essa função, que tem 
    consumo de tempo O(n lg n). O consumo
    de tempo esperado para essa função é O(n) e o 
    de memória é O(1). 
    - O vídeo cujo link você encontra no enunciado dessa
    atividade ilustra uma possível solução.
    '''

    # escreva sua solução


#-----------------------------------------------        
if __name__ == '__main__':
    main()
