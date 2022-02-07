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

ABRE = '([{'
FECHA = ')]}'

def main():
    ''' função para teste da função bem_formada
    '''
    a = bem_formada( "(a+ {b })-{2*[3+4]}" )
    print(f"{a} deve retornar --> True")
    b = bem_formada( "( ( (  ) " )
    print(f"{b} deve retornar --> False")
    c = bem_formada( " { ( { x } )  } [ y ]" )
    print(f"{c} deve retornar --> True")
    d = bem_formada( " { ( { x }  } [ y ] )" )
    print(f"{a} deve retornar --> False")

# ---------------------------------------------------------

def bem_formada( seq ):
    ''' (str) -> bool
    Recebe uma string seq contendo uma sequência formada pelos
    caracteres '()[]{}'. 
    Retorna True caso a sequência esteja bem formada e False em
    caso contrário.
    A função deve ignorar caracteres diferentes de '()[]{}' 
    sem resultar em erro.
    Exemplos:
    >>> bem_formada( "(a+ {b })-{2*[3+4]}" )
    True
    >>> bem_formada( "( ( (  ) " )
    False
    >>> bem_formada( " { ( { x } )  } [ y ]" )
    True
    >>> bem_formada( " { ( { x }  } [ y ] )" )
    False
    '''
    seqnovo = ''
    for i in range(len(seq)):
        if seq[i] in '({[]})':
            seqnovo += seq[i]
            
    lst = list(seqnovo)
    n = len(lst)
    a = 0
    
    coiso = ('(' or '{' or '[')   
    contrario = (')' or '}' or ']')
    
    
    print(f"lst = {lst}")
    
    
    while a < n-1 :
                
        # retorna False se começa com contrario
        if lst[a] in contrario:
            return False
        
        # começa a procurar os iguais    
        if lst[a] == '(':
            if ')' in lst:
                b = lst.index(')')
                lst.pop(b)
                lst.pop(a)
        
        if lst[a] == '{':
            if ')' in lst:
                b = lst.index('}')
                lst.pop(b)
                lst.pop(a)
                
        if lst[a] == '[':
            if lst[b] == ']':
                lst.pop(b)      
                lst.pop(a)
                
        a+=1
        
    if len(lst) == 0:
        return True
    else:
        return False    

    
# ---------------------------------------------------------

if __name__ == '__main__':
    main()