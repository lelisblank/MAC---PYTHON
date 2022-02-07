# -*- coding: utf-8 -*-
"""EG_bem_formada

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IREtq1zVT2vFo-B_Xq-WxE3vD3dwxwte
"""

# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Leticia Maia
    NUSP: 11781715


    grupo: Matheus Laureano Bezerra
    Melissa Tiemi Tanaka
    Lucas Antonio de Sousa Ribeiro - 10298478

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
    print("Teste 01", bem_formada('(')," = False")
    print("Teste 02a", bem_formada(')')," = False")
    print("Teste 02b", bem_formada(']')," = False")
    print("Teste 02c", bem_formada('}')," = False")
    print("Teste 03", bem_formada('(()))(')," = False")
    print("Teste 04", bem_formada('()()')," = True")
    print("Teste 05", bem_formada('(())')," = True")
    print("Teste 06", bem_formada('')," = True")
    print("Teste 07a", bem_formada('([')," = False")
    print("Teste 07b", bem_formada('[')," = False")
    print("Teste 07c", bem_formada('{')," = False")
    print("Teste 08", bem_formada(')]')," = False")
    print("Teste 09", bem_formada('([()))(')," = False")
    print("Teste 10", bem_formada('({2})({a})')," = True")
    print("Teste 11", bem_formada('(([]{x}))')," = True")
    print("Teste 12", bem_formada('')," = True")
    print("Teste 13", bem_formada('((((())[)]()))')," = False")
    print("Teste 14", bem_formada('{((([(())])()))}')," = True")
    print("Teste 15", bem_formada('{([(([(([]))])({}))[])}')," = False")
    print("Teste 16", bem_formada('')," = True")
    print("Teste 17", bem_formada('(a+ {b })-{2*[3+4]}')," = True")
    print("Teste 18", bem_formada('{ ( { x } )  } [ y ]')," = True")
    print("Teste 19", bem_formada(' { ( { x }  } [ y ] )')," = False")
    print("Teste 20", bem_formada('0')," = True")
    print("Teste 21", bem_formada('abc')," = True")
    print("Teste 22", bem_formada('')," = True")
    print("Teste 23", bem_formada(')(')," = False")
    print("Teste 24", bem_formada('$ $ { }')," = True")
    print("Teste 25", bem_formada('[ $ { } $ ] $ ( $ $ $ $ ) $')," = True")
    print("Teste 26", bem_formada('$ $ $')," = False")
    print("Teste 27", bem_formada('$ { $ }')," = False")
    print("Teste 28", bem_formada('( $ $ $ ) $')," = False")
    
    
    #print("Vixe, ainda não fiz nenhum teste!")

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
    ABRE = '([{'
    FECHA = ')]}'
    lista = []
    balanceada = True
    contagem = 0
    aberta = True
    i = 0

    while i < len(seq) and balanceada:
        simbolo = seq[i]
        
        if simbolo == '$':
            contagem += 1
            
            #if contagem % 2 != 0 and balanceada == True:
                #aberta = False
                
                
            #else: 
 #               aberta = False
        
        if simbolo in ABRE or (contagem % 2 != 0 and simbolo == '$'):
            lista.append(simbolo)
        
        elif simbolo in FECHA or simbolo == '$':
            
            if len(lista) == 0:
                balanceada = False
            
            else:
                topo = lista.pop()
                
                if simbolo == '$' or topo == '$':
                    if (topo != '$' and simbolo == '$'):
                        balanceada = False
                
                else:
                    if ABRE.index(topo) != FECHA.index(simbolo):
                        balanceada = False

        i = i + 1

    if balanceada and len(lista) == 0:
        return True

    else:
        return False
    #print("Vixe, ainda não fiz a função bem_formada!")


def dec2bin( dec ):
    ''' (int) -> int
    Recebe um inteiro que representa um número na base decimal e 
    retorna outro inteiro que representa o mesmo número na base binária.
    Exemplo:
    >>> dec2bin( 11 )
    1101
    >>> dec2bin( 5 )
    101
    
    11 // 2 = 5
    11 % 2 = 1
    lst [1]
    
    5 // 2 = 2
    5 % 2 = 1
    lst [1,1]'''
    
  x = dec // 2
  y = dec % 2
  pilha = [y]

  while x != 0:
      y = x % 2
      x = x //2
      pilha += [y]
        
  return pilha

# ---------------------------------------------------------

if __name__ == '__main__':
    main()

EG(torto)
def bem_formada(seq):
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
    # Cria lista vazia, index e determina bem_formada;
    lst = []
    bem_formada = True
    i = 0
    ds = 0
    # Percorre a string seq;
    while i < (len(seq)) and bem_formada:
        s = seq[i]
        print(lst, i, 'ssssd')
        # Adiciona "([{" à lista lst, caso encontre "([{";
        if s in ABRE:
            lst.append(s)
            i += 1
            print(lst, 'a')
            if s in '$':
                ds += 1
                print(lst, 'ds1', ds)
                if ds % 2 == 0 and ds != 1:
                    abre = lst.pop()
                    ds -= 1
                    combo = ABRE.index(abre) == FECHA.index(s)
                    print(lst, 'ds2', ds)
                    if not combo:
                        bem_formada = False
        # Caso não encontre "([{" checa se a lst está vazia, caso esteja
        # retorna False, caso contrário pega o último item da lst checa se
        # é ")]}" e se combina ((),[] ou {}) com seq[i] em questão;
        # elif s in ' abcdefghijklmopkrstuvwxyz.+-*/,;:?´~':
        elif s in FECHA:
            if lst == [] and i == len(seq)-1:
                bem_formada = False
                print(lst, 'b')
            else:
                print(lst, 'c', 'aaaaaaaaaa')
                abre = lst.pop()
                combo = ABRE.index(abre) == FECHA.index(s)
                if not combo:
                    bem_formada = False
            i += 1
        elif s not in ABRE or FECHA:
            i += 1
    # Retorna se a seq é bem formada ou não.
    if bem_formada and lst == []:
        return True
    else:
        return False

# ---------------------------------------------------------


if __name__ == '__main__':
    main()

#EI
def bem_formada(seq):
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
    # Cria lista vazia, index e determina bem_formada;
    lst = []
    bem_formada = True
    i = 0
    # Percorre a string seq;
    while i < (len(seq)) and bem_formada:
        s = seq[i]
        # Adiciona "([{" à lista lst, caso encontre "([{";
        if s in ABRE:
            lst.append(s)
            i += 1
        # Caso não encontre "([{" checa se a lst está vazia, caso esteja
        # retorna False, caso contrário pega o último item da lst checa se
        # é ")]}" e se combina ((),[] ou {}) com seq[i] em questão;
        # elif s in ' abcdefghijklmopkrstuvwxyz.+-*/,;:?´~':
        elif s in FECHA:
            if lst == []:
                bem_formada = False
            else:
                abre = lst.pop()
                combo = ABRE.index(abre) == FECHA.index(s)
                if not combo:
                    bem_formada = False
            i += 1
        elif s not in ABRE or FECHA:
            i += 1
    # Retorna se a seq é bem formada ou não.
    if bem_formada and lst == []:
        return True
    else:
        return False

# ---------------------------------------------------------


if __name__ == '__main__':
    main()

#EI Matheus
ABRE = '([{'
FECHA = ')]}'
def main():
    print("Teste 24", bem_formada('$ $ { }')," = True")
    print("Teste 25", bem_formada('[ $ { } $ ] $ ( $ $ $ $ ) $')," = True")
    print("Teste 26", bem_formada('$ $ $')," = False")
    print("Teste 27", bem_formada('$ { $ }')," = False")
    print("Teste 28", bem_formada('( $ $ $ ) $')," = False")

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
    
    s = []
    c = 0
    '''ACRESCENTA ITENS (ABRE) NA LISTA QUE FUNCIONA COMO UMA PILHA'''
    i = 0
    while i < len(seq): 
        x = seq[i]
        if x in ABRE:
            s += [[seq[i],i]]
            
        i+=1
    i=0
    '''CONTADOR DE 'FECHAS' '''
    while i < len(seq): 
        x = seq[i]
        if x in FECHA:
            c += 1
            
        i+=1
    

    '''COMPARA SE O ULTIMO 'ABRE' DA PILHA E O PROXIMO 'FECHA' SÃO CORRESPONDENTES, SE FOR VERDADE
       REMOVE O TOPO DA 'PILHA', REMOVE O 'FECHA' DA STRING seq E SUBTRAI 1 DO CONTADOR DE 'FECHAS'  '''
    ENTRADA = True
    while s != [] and c > 0 and ENTRADA: 
        x = s[len(s)-1][1]
        abre = s[len(s)-1][0]
        ENTRADA = False
        for j in range(x+1,len(seq),1):
            ENTRADA = True
            y = seq[j]
            if y in FECHA:
                if abre == '(' and y == ')':
                        s = s[:-1]
                        c -= 1
                        seq = seq[:j-1]+seq[j+1:]
                        break
                elif abre == '[' and y == ']':
                        s = s[:-1]
                        c -= 1
                        seq = seq[:j-1]+seq[j+1:]
                        break
                elif abre == '{' and y == '}':
                        s = s[:-1]
                        c -= 1
                        seq = seq[:j-1]+seq[j+1:]
                        break
                elif abre == '$' and y == '$':
                        s = s[:-1]
                        c -= 1
                        seq = seq[:j-1]+seq[j+1:]
                        break
                else:
                    return False

    if s == [] and c == 0:        
        return True
    
    else:
        return False

main()