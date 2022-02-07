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

import numpy as np

## ==================================================================

def main():
    x = [    
            8, 8, 8, 8, 1, 4,
            1, 8, 1, 1, 1, 4,
            1, 8, 8, 1, 4, 4,
            1, 1, 1, 1, 4, 4,
            1, 9, 1, 4, 1, 4,
            9, 9, 9, 9, 1, 4
        ]

    img = np.array(x).reshape(6,6)
    print('Imagem\n', img)

    # cria um objeto Blobs usando img
    blobs = Blobs(img)

    # vamos ver as blobs
    dt = blobs.data
    n = len(dt)
    for i in range(n):
        elem = list(dt[i])[0] # pega um elemento do conjunto
        print(f'blob {i} tem tamanho {len(dt[i])} e cor {img[elem]}')
        print(f'   {dt[i]}')
        
        
class Blobs:

    def __init__(self, img):
        ''' (Blobs, array) -> None 
        construtor da classe Blobs.
        '''

        self.data = []
        self.segmente(img) # deve carregar self.data
        ## inclua outros atributos que desejar

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Blobs) -> str
        retorna uma string com a descrição das blobs.
        '''
        
        txt = ''
        dt = self.data
        n = len(dt)
        for i in range(n):
            txt += f'blob {i} tem tamanho {len(dt[i])}\n'
            txt += f'   {dt[i]}\n'
        return txt

    # ---------------------------------------------------------------
    def segmente(self, img):
        ''' (Blobs, array) -> None
        Método usado pelo construtor para segmentar todas
        as blobs da imagem img.
        '''
        cop = []
        for lin in range (len(img)):
            
            for col in range (len(img[0])):
                semente = (lin,col)
                
                if semente not in cop:
                    y = self.segmente_blob(img, semente)
                    self.data+= [y]
                    cop += y

    # ---------------------------------------------------------------
    def segmente_blob( self, img, semente ):
        ''' (Blobs, ndarray, tuple) -> set

            interface para o método self.segmente_blob_RM.
            Cria um conjunto vazio que é carregado
            de forma recursiva.  
            
            Não altere esse método.
        '''
        return self.segmente_blob_RM( img, semente, set() )

    # ---------------------------------------------------------------
    def segmente_blob_RM(self, img, semente, visitados ):
        ''' (Blobs, ndarray, tuple, set) -> set

        Recebe, além de self, um ndarray img e uma tupla semente contendo a
        coordenada de um pixel de img. Recebe também o conjunto
        visitados, que contém as coordenadas dos pixels já 
        visitados.

        Adapte esse método da função de mesmo nome implementada
        no exercício anterior.
        '''
        i,j = semente
        atual = img[i][j]
        
        if semente in visitados:
            return None
        
        else: 
            visitados.add(semente)

        # cima baixo esq dir
        if i>0 and i < len(img):
            superior = img[i-1][j]
            y = (i-1, j)
            # adicionando ao visitados:
            if superior == atual and y not in visitados:
                self.segmente_blob_RM(img, y, visitados)
                
        if j > 0 and j < len(img[0]):
            esq = img [i][j-1]
            y = (i, j-1) 
            
            if esq == atual and y not in visitados:
                self.segmente_blob_RM(img, y, visitados)
            
        if j < len(img[0])-1:
            dir = img[i][j+1]
            y = (i, j+1) 
            
            if dir == atual and y not in visitados:
                self.segmente_blob_RM(img, y, visitados)
        
        if i < len(img)-1:
            inf = img[i+1][j]
            y = (i+1, j)   
            
            if inf == atual and y not in visitados:
                self.segmente_blob_RM(img, y, visitados)
        
        # ler elementos de visitados para saber se dá para adc mais:
            # !!!! CAUSA LOOPING INFINITO !!!!
        # for leitura in (visitados):
        #    return self.segmente_blob_RM(img, leitura, visitados)
        
        # quando acaba leitura de visitados:
        return visitados

    ## ==================================================================

    def pinte_blob( self, img, blob, nova_cor = 0):
        ''' (Blobs, ndarray, set, int) -> None

        Recebe, além de self, um ndarray img e um conjunto de pixels blob
        e pinta esses pixels com a nova_cor.

        Adapte esse método da função de mesmo nome implementada
        no exercício anterior.
        '''

        for elemento in blob:
            img[elemento] = nova_cor
        
        return img

## ==================================================================
## Coloque aqui outras funções e métodos que desejar

if __name__ == '__main__':
    main()
