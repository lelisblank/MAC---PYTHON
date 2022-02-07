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
## Escreva a sua função palindromo()
def main():
    pil = Pilha()   ## cria uma Pilha vazia
    print(f"pil.dados = {pil.dados}  --> deve ser a lista vazia []")
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser True")
    pil.empilhe('todos')
    pil.empilhe(4)
    pil.empilhe('paz')
    # Pilha.topo() apenas pega o valor no topo mas sem desempilher
    print(f"pil.topo() = {pil.topo()}  --> deve ser 'paz'") 
    pil.empilhe(True)
    print(f"len(pil) = {len(pil)} --> deve ser 4")  ## implemente o método __len__
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser False")
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz', True]")
    pil.empilhe(2.7)
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser 2.7")
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser True")
    print(f"len(pil) = {len(pil)} --> deve ser 3") 
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz']")



def teste ():
    arara = palindromo ('arara')
    print(f"{arara} deve retornar --> True")
    abacate = palindromo('abacate')
    jabuticaba = palindromo ('jabuticaba')
    aaaaaa = palindromo ('aaaaa')

def palindromo( s ):
    ''' documentacao da funcao '''

    '''a = 0
    b = -1
    
    novos = s[:]
    print(novos)
    
    while abs(b) != len(s):
        if novos[a] != novos[b]:
            return False
        
        b-=1
        a+=0
        print(a,b)
        
    return True'''
    p = Pilha()
        
    for i in s:
        p.empilhe(i)
    s = p
    print(f"{p}")
        
    r = ''
    
    while not p.vazia:
        r+= p.desempilhe()
        
    print(r)
        
    if s == p:
        return True
    
    return False
        
        



## ==================================================================
##
class Pilha:

    def __init__(self, a = []):
        if a == []:
            self.dados = []
        else:
            self.dados = [a]
            
    def __str__ (self):
        return f"{self.dados}"
        
    def topo(self):
        return f"'{self.dados[-1]}'"
    
    def __len__ (self):
        return len (self.dados)
    
    def vazia (self):
        return self.dados == []
    
    def empilhe (self, other):
        if type(other) is not list:
            other = Pilha(other)

        self.dados += other.dados
        return self.dados
    
    def desempilhe (self):
        self.dados = self.dados[0:-1]
        return self.dados
    
    
    

## ==================================================================
## Escreva outras funções e classes caso desejar


## ==================================================================
if __name__ == '__main__':
    Pilha()
    palindromo( '' )
    teste()

