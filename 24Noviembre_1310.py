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

class Nodo:=

class LinkedList:=

class NodoDoble:
    def __init__(self,value,siguiente=None, anterior=None):
        self.data=value
        self.next=siguiente
        self.prev=anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size==0

    def append(self,value):
        if self.is_empty():
            nuevo=NodoDoble(value)
            self.__head=nuevo
            self.__tail=nuevo
        else:
            nuevo=NodoDoble(value,self.__tail,None)
            self.__tail.next=nuevo
            self.__tail=nuevo

        self.__size+=1

    def transversal(self):
        curr_node=self.__head
        while curr_node !=None:
            print(f"<--{ curr_node.data } -->", end="")
            curr_node=curr_node.next
        print("")
    def reverse_transversal(self):
        curr_node=self.__head
        while curr_node !=None:
            print(f"<--{ curr_node.data } -->", end="")
            curr_node=curr_node.prev
        print("")
    def remove_from_head(self,value):
        curr_node=self.remove_from_head
        if self.__head.data==value:
            self.__head=self.__head.next
            self.__head.prev=None
        elif self.__tail.data == value:
            self.__tail.prev.next = None
            self.__tail=self.__tail.prev
        while curr_node!=value and curr_node!=None:
            curr_node=curr_node.next
        if curr_node.data==value:
            curr_node.prev.next=curr_node.next
            curr_node.next.prev=curr_node.prev
        curr_node.next=None
        curr_node.prev=None
        self.__size-=1
----------------------------------------
from listas import DoubleLinkedList

ld=DoubleLinkedList()
print("Esta vacia?", ld.is_empty())
ld.append(10)
ld.append(20)
ld.append(30)
print(f"La lista tiene {get_size()} elementos")
ld.transversal()
ld.reverse_transversal()
ld.remove_from_head(20)
ld.transversal()
