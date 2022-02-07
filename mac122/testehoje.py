# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:29:33 2021

@author: letic
"""

    lst = list(seqnovo)
    n = len(lst)
    a = 0
    
    coiso = ('(' or '{' or '[')   
    contrario = (')' or '}' or ']')
    
    
    print(f"lst = {lst}")
    
    
    while a < n-1 :
                
        # retorna False se começa com contrario
        if lst[a] == contrario:
            return False
        
        # começa a procurar os iguais    
        if lst[a] == '(':
            b = a+1
            while b < n:
                if lst[b] == ')':
                    lst.pop(b)
                else:
                    b+=1
        
            print(f"lst() = {lst}")

        n = len(lst)
        
        if lst[a] == '{':
            b = a+1
            while b < n:
                if lst[b] == '}':
                    lst.pop(b)
                else:
                    b+=1
            print(f"lst.cu = {lst}")
                    
        n = len(lst)
        
        if lst[a] == '[':
            b = a+1
            while b < n:
                if lst[b] == ']':
                    lst.pop(b)
                else:
                    b+=1
            print(f"lst[] = {lst}")

        
        else:            
            a+=1
        
    if len(lst) == 0:
        return True
    else:
        return False