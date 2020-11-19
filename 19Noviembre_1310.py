class Nodo:
   def __init__(self,value,siguiente=None):
       self.data=value  #falta encapsulamiento
       self.siguiente=siguiente

class LinkedList:
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head==None

    def append(self,value):
        nuevo=Nodo(value)
        if self.__head==None: #self.is_empty()
           self.__head=nuevo
        else:
           curr_node=self.__head
           while curr_node.siguiente!=None:
               curr_node=curr_node.siguiente
           curr_node.siguiente=nuevo

    def transversal(self):
        curr_node=self.__head
        while curr_node!=None:
            print(f"{curr_node.data}-->",end="")
            curr_node=curr_node.siguiente
        print("")

    def tail(self):
        curr_node=self.__head
        while curr_node.siguiente!=None:
            curr_node=curr_node.siguiente
        return curr_node

    def remove(self,value):
        curr_node=self.__head
        if self.__head.data==value:
            self.__head=self.__head.siguiente
        else:
            anterior=None
            while curr_node.data!=value and curr_node.siguiente!=None:
               anterior=curr_node
               curr_node=curr_node.siguiente
            if curr_node.data==value:
               anterior.siguiente=curr_node.siguiente
            else:
               print("El dato no existe en la lista")

    def preppend(self,value):
        nuevo=Nodo(value,self.__head)
        self.__head=nuevo

    def get(self,posicion=None):
        contador=0
        dato=None
        if posicion==None:
            dato=self.tail().data
        else:
            pass

        return dato
------------------------------------
from listas import LinkedList

l = LinkedList()
print(f'L está vacía? { l.is_empty()}')
l.append(10)
l.append(5)
l.append(6)
l.append(20)
print(f'L está vacía? { l.is_empty()}')
l.transversal()
l.remove(10)
l.transversal()
l.preppend(3)
l.transversal()
x=l.tail()
print(x.data)
print(l.get())
