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
        AR 12
        Brenno: https://paste.ofcode.org/MAtq7Qh9eWJFDBrKsdqmKb

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        Brenno da sala < 3 
'''

## ==================================================================


import numpy as np

## ------------------------------------------------------------------
def main():
    
    print("======Teste operadores\n")

    imgA = NPImagem( (2,3), 5)
    imgB = NPImagem( (), np.arange(20).reshape(5,4) )
    imgC = imgB.crop(2,1,4,4)
    imgD = imgA + imgC
    print(f"imgA:\n{imgA}")
    print(f"imgB:\n{imgB}")
    print(f"imgC:\n{imgC}")
    print(f"imgD:\n{imgD}")

    print("\n===== Crop ========\n")

    lista = list(range(30))
    ar = np.array(lista).reshape(6,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 88)
    img3 = img2.crop() ## cria uma cópia
    img2[2,1] = -10
    print(f"img2[2,1]={img2[2,1]}")
    print(f"img2:\n{img2}\n")
    print(f"img3:\n{img3}\n")

    print("======Teste pinte_retangulo\n")
    img1.pinte_retangulo(1,2,3,5,77)
    print(f"img1.pinte_retangulo(1,2,3,5,77):\n{img1}\n")

    img2.pinte_retangulo(-1,-2,2,3,99)
    print(f"img2.pinte_retangulo(-1,-2,2,3,99):\n{img2}\n")

    img3.pinte_retangulo(1,0,3,4,66)
    print(f"img3.pinte_retangulo(1,0,3,4,66):\n{img3}\n")

    print("======Teste paste\n")
    img1 = NPImagem( (0, 0), ar)  # 
    img2 = NPImagem( (2, 3), 99)
    img3 = img1.crop(2,1,5,3) ## cria uma cópia
    print(f"img1:\n{img1}")
    print(f"img2:\n{img2}")
    print(f"img3:\n{img3}")

    img1.paste(img2, 2, 3)
    print(f"img1.paste(img2,2,3):\n{img1}\n")

    img1.paste(img3, 4, 2 )
    print(f"img1.paste(img3,4,2):\n{img1}\n")

    img1.paste(img3, -1, 2)
    print(f"img1.paste(img3,-1,2):\n{img1}\n")

    print("Testes da classe NPImagem\n")

## ------------------------------------------------------------------
class NPImagem():


    def __init__ (self, shape, val = 0):

        
        if type(val) == np.ndarray:
            self.data = val
            nlin = len(val)
            ncol = len(val[0])
            self.shape = (nlin,ncol)
            
        else:
            self.shape = shape
            self.nlins, self.ncols = shape
            self.val = val
            self.data = np.full((shape), val)
        

    def __str__(self):
        return f"{self.data}"
    # escreva aqui os métodos da classe NPImagem
    
    def pinte_retangulo(self, sup, esq, inf, dir, v=0):
        ''' (NPImagem, int, int, int, int, int) -> None 
    Recebe 4 inteiros que definem o canto superior-esquerdo (sup, esq) e
    o canto inferior-direito (inf,dir) de uma região retangular com 
    relação a posição (0,0) de self, ou seja, os cantos são "deslocamentos" 
    em pixeis com relação à origem.
    Esse método pinta, com o valor v, os pixeis de self que tenham sobreposição
    com o retângulo (sup,esq)x(inf,dir). '''
        primeiro = self.data[sup:inf, esq:dir] = v

    
    
    def paste(self, other, sup, esq):
        '''(NPImagem, NPImagem, int, int) -> None
     Recebe um objeto NPImagem other e um par de inteiros (sup, esq) 
     que indica um deslocamento em relação à origem de self (posição (0,0)) 
     onde a NPImagem other deve ser sobreposta sobre self. Observe que
     esse deslocamento pode ser negativo. Nesse caso, a dimensão de other
     define o canto inferior-direito do retângulo.
     ''' 
        self_nlins,  self_ncols = self.shape
        other_nlins, other_ncols = other.shape

        # [inf, dir] é a posição mais a baixa e mais a direita de um possível 
        # pixel de self que será sobreposto 
        inf = sup + other_nlins
        dir = esq + other_ncols

        # se janela da sobreposição não tem pixel de self, retorne
        if sup >= self_nlins or esq >= self_ncols\
           or inf <= 0  or dir <= 0: return

        # [self_sup, self_esq] e [self_inf, self_dir] são os cantos da janela
        # retangular de self que será sobreposta pela janela other.
        self_sup = max(0, sup)
        self_esq = max(0, esq)
        self_inf = min(inf, self_nlins)
        self_dir = min(dir, self_ncols)

        # [other_sup, other_esq] e [other_inf, other_dir] são os cantos da janela
        # retangular de other que se sobreporá a janela de self.
        other_sup = -min(0, sup)
        other_esq = -min(0, esq)
        other_inf = other_sup + self_inf - self_sup
        other_dir = other_esq + self_dir - self_esq

        # sobreponha janela de other sobre a janela de self
        self.data[self_sup:self_inf, self_esq:self_dir] = other.data[other_sup:other_inf, other_esq:other_dir]
     
    def __add__(self, other):
        '''(NPImagem, NPImagem) -> NPImagem
    Recebe dois objetos NPImagem e retorna a soma, elemento-a-elemento,
    dos pixels de self e other.
    '''
        return self.data[:] + other.data[:]

    # ---------------------------------------------------------------
    def crop(self, sup=None, esq=None, inf=None, dir=None):
        '''(NPImagem, int, int, int int) -> NPImagem
        Recebe uma referência 'self' do tipo NPImagem e quatro numeros 
        inteiros (sup, esq, inf, dir). Retorna uma variavel 'copia' do
        tipo NPimagem que tem dimensões e valores iguais a fatia do 
        tipo np.array self.data[sup:inf,esq:dir]
        '''
        if not (sup or esq or inf or dir):
            copia = self.copia()
        else:
            copia = NPImagem((0,0),self.data[sup:inf,esq:dir].copy())
        
        return copia
    
    # ---------------------------------------------------------------
    def copia(self):
        '''(NPImagem) -> NPImagem
        Recebe uma referência 'self' do tipo NPImagem.
        Retorna uma cópia de 'self'
        '''

        copia_np = NPImagem((0,0), self.data.copy())
        
        return copia_np    

    def __getitem__(self, key):
        '''(NPIMagem, tuple) -> int
        RECEBE uma NPImagem self e uma posição key de um pixels da imagem
        RETORNA o tom de cinza do pixel key.
        '''
        return self.data[key]
    
    def __setitem__(self, key, val):
        '''(NPIMagem, tuple, int) -> None
        RECEBE uma NPImagem self, uma posição key de um pixels da imagem, um tom de 
            cinza val
        MODIFICA o tom de cinza do pixel key para val.
        '''
        self.data[key] = val
    
## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()
