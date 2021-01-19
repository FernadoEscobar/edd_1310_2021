class NodoArbol:
    def __init__(self,value,left=None,right=None):
        self.data=value
        self.left=left
        self.right=right

class BinarySearchtree:
    def __init__(self):
        self.__root=None

    def insert(self,value):
        #regla 1
        if self.__root==None: #self.__root is None
            self.__root=NodoArbol(value,None,None)
        #regla 2
        else:
            self.__insert__(self.__root,value)

    def __insert__(self,nodo,value):
        if nodo.data==value:
            print("El dato ya existe, no se ingresa nada")
        elif value<nodo.data:
            #regla 1
            if nodo.left==None:
                nodo.left=NodoArbol(value)
            #regla 2
            else:
                self.__insert__(nodo.left,value)
        else:
            if nodo.right==None:
                nodo.right=NodoArbol(value)
            else:
                self.__insert__(nodo.right,value)
            #y pos ya esta
    def __recorrido_in__(self,nodo):
        if nodo!=None:
            self.__recorrido_in__(nodo.left)
            print(nodo.data, end=" , ")
            self.__recorrido_in__(nodo.right)

    def transversal(self,format="inorden"):
        if format=="inorden":
            self.__recorrido_in__(self.__root)
        elif format=="preorden":
            print("Recorrido en pre")
        elif format=="Posorden":
            print("Posorden")
        else:
            print("Error,este formato no existe")
        print("")
--------------------------------------------------------
from arboles_binarios import BinarySearchtree

abb=BinarySearchtree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)

abb.transversal()
