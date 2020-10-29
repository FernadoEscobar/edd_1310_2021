class array:

     def __init__(self, tam):
         self.__info=[0 for x in range(tam)]

     def get_item(self,posicion):
         dato=0
         try:
            dato=self.__info[posicion]
         except Exception as e:
            print("Error de posicion")
            dato="Error"
         return dato

     def set_item(self,dato,posicion):
         try:
            self.__info[posicion]=dato
         except Exception as e:
            print("Error de posicion")

     def get_lenght(self):
         return len(self.__info)

     def clear(self, dato):
         self.__info=[dato for x in range(len(self.__info))]

     def __iter__(self):
        return Iteradorarreglo()

class Iteradorarreglo:

    def __init__(self, arr):
        self.__arr=arr
        self.__indice=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice<len(self.__arr):
            dato=self.__arr[self.__indice]
            self.__indice +=1
            return dato
        else:
            raise StopIteration
from arrays import array
algo=array(10)
print(algo.get_item(6363))
algo.set_item(553,3)
print(algo.get_item(3))
print(f"el arreglo tiene {algo.get_lenght()} elementos")
algo.clear(777)
print(algo.get_item(3))
print("------------")
for x in range(algo.get_lenght()):
    print(f"{x}-->{algo.get_item(x)}")
