# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:51:11 2021

@author: letic
"""

# ===============================================================
"""
Ao incluir esse cabeçalho declaro que todas as partes originais
desse exercício individual foram desenvolvidas e implementadas por
mim e que portanto não constituem desonestidade acadêmica ou plágio.
Declaro também que sou responsável por todas as cópias desse
programa e que não distribui ou facilitei a sua distribuição.
Estou ciente que os casos de plágio e desonestidade acadêmica
serão tratados segundo os critérios divulgados na página da 
disciplina.

Entendo que exercícios sem esse cabeçalho devem receber nota zero
e, ainda assim, poderão ser punidos por desonestidade acadêmica. 

Nome: Letícia Maia
nºUSP: 11781715  
 
"""
# ===============================================================

def main():
    ''' 
    a função main é opcional. 
    Caso desejar, inclua e deixe aqui os testes que você fez 
    com as funções Hmaior e Hmenor.
    '''
    n = int(input ("Digite n: "))
    
    print("testes das funções")
    print ("H maior", Hmaior(n), "\n \n")
    
    print ("H menor", Hmenor(n))


def Hmaior(n):
    ''' escreva uma documentação para essa função
    '''
    y = 1
    soma = 0
    if y!=n:
        while y<=n:
            soma += 1/y
            print(soma)
            y+=1
        return soma
    else:
        return 1

def Hmenor(n):
    ''' escreva uma documentação para essa função
    '''
    y = n
    soma = 0
    
    if n == 1:
        return 1
    
    else:
        while y>=1:
            soma += 1/y
            y-=1
            print (soma)
        return soma

if __name__ == '__main__':
    main()    
    