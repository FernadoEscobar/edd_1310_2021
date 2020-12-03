
class Array2D:

    def __init__(self,rows, cols, value):
        self.__cols = cols
        self.__rows = rows
        self.__array=[[value for x in range(self.__cols)] for y in range(self.__rows)]

    def to_string(self):
        [print("---",end="") for x in range(self.__cols)]
        print("")
        for ren in self.__array:
            print(ren)
        [print("---",end="") for x in range(self.__cols)]
        print("")

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_item(self,row,col):
        return self.__array[row][col]

    def set_item( self , row , col , valor ):
        self.__array[row][col]=valor

    def clearing(self, valor=0):
        for ren in range(self.__rows):
            for col in range(self.__cols):
                self.__array[ren][col]=valorbacktracking
------------------------------------------------------------
class Stack:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def lenght(self):
        return len(self.__data)

    def pop(self):
        if self.is_empty():
            print('Pila vacía')

        else:
            return self.__data.pop()

    def push(self, value):
        self.__data.append(value)

    def peek(self):
        return self.__data[len(self.__data)-1]

     def to_string(self):
        print('-------')
        for item in self.__data[::-1]:
            print(f'|  {item}  |')
            print('-------')
        print('\n')
---------------------------------------------------
from array2d import Array2D

from stack import Stack

class laberintoADT:

    """
    0 pasillo, 1 pared, S salida y E entrada
    pasillo es una tupla ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
    entrada en una tupla
    """

    def __init__(self,rens,cols,pasillos,entrada,salida):
        self.__laberinto=Array2D(rens,cols,'1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1],'0')
            self.set_entrada(entrada[0],entrada[1])
            self.set_salida(salida[0],salida[1])
            self.__camino=Stack()
            self.__previa=None

    def to_string(self):
        self.__laberinto.to_string()

    """
    establece la entrada 'E' en la matriz, verificar limites perifericos
    """

    def set_entrada(self,ren,col):
    #Terminar la validacion de las coordenadas
        self.__laberinto.set_item(ren,col,'E')

    """
    Establecer salida, dentro de los limites perifericos de la matriz
    """

    def set_salida(self,ren,col):
    #Terminar las validaciones
        self.__laberinto.set_item(ren,col,'S')

    def es_salida(self,ren,col):
        return self.__laberinto.get_item(ren,col)=='S'

    def buscar_entrada(self):
        encontrado=False
        for reglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                tope=self.__camino.peek() #tupla
                if self.__laberinto.get_item(reglon,columna)=='E':
                    self.__camino.push(tuple(reglon,columna))
                    encontrado=True
        return encontrado

    def set_previa(self,pos_previa):
        self.__previa=pos_previa

    def get_previa(self):
        return self.__previa

    def resolver_laberinto(self):
        #Aplicar reglas
------------------------------------------------------------------
from backtracking import laberintoADT
pasillos_inicial=((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab=laberintoADT(6,6,pasillos_inicial,(5,2),(2,5))
lab.to_string()
