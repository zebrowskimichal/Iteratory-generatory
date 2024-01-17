print("1. Korzystając z metod `__iter__` i `__next__`, napisz obiekt iterowalny oraz iterator, ## #które przy każdym użyciu `next()` na iteratorze będą zwracać kolejną wartość z ciągu Fibonacciego, aż do osiągnięcia górnej granicy (podawanej przy inicjalizacji obiektu iterowalnego).")
#
##1
class Fibonacci:
    def __init__(self, max) -> None:
        self.max = max

    def __iter__(self):
        return FibItter(self.max)
    
class FibItter:
    def __init__(self, max):
        self.max = max
        self.current = 0
        self.nextNumber = 1

    def __next__(self):
        if(self.current < self.max):
            result = self.current
            self.current, self.nextNumber = self.nextNumber, self.current + self.nextNumber
            return result
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self
    
#    #Uzycie
przyklad = Fibonacci(2000)
for value in przyklad:
    print(value)


print("2 Napisz iterator, który po zainicjowaniu z użyciem dwóch list, będzie w kolejnych #wywołaniach przez `next()` zwracać `tuple` z wartościami tych list będących na tych samych #indeksach.")

class listyIterator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < min(len(self.list1), len(self.list2)):
            result = (self.list1[self.index], self.list2[self.index])
            self.index += 1
            return result
        else:
            raise StopIteration

#    # Uzycie:
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']

iterator = listyIterator(list1, list2)
for value in iterator:
    print(value)


print("Lista2")
print("1 Przepisz jeden z iteratorów napisanych wcześniej (zadania 1 lub 2 z iteratorów) do postaci #generatora z użyciem wyrażenia `yield`.")

def listyIteratorYield(list1, list2):
    index = 0
    while index < min(len(list1), len(list2)):
        yield (list1[index], list2[index])
        index += 1

#Uzycie
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']

iteratorYield = listyIteratorYield(list1, list2)
for value in iteratorYield:
    print(value)


print("2 Napisz generator, który będzie zwracać `tuple` z kolejnymi wynikami działań na podanych #liczbach od `0` do `x`. Wybierz operacje spośród pierwiastków kwadratowych, kwadratów, sześcianów, silni lub sumy ciągu naturalnego. Możesz też zaimplementować własne działania.")

def generatorSzescian(x):
    for i in range(x + 1):
        yield i, i ** 3
   #Uzycie:
wynikGeneratorSzescian = generatorSzescian(10)
for value in wynikGeneratorSzescian:
    print(value)


print("3 Napisz funkcję tworzącą listę oraz generator zwracający kolejne wartości, analogiczne do takiej listy. Korzystając z biblioteki `memory-profiler` (<https://pypi.org/project/memory-profiler/>) lub podobnej, porównaj wykorzystanie pamięci obydwu funkcji - np. dla przypadku generowania miliona elementów. Wyniki analizy zużycia pamięci zamieść w komentarzu pod kodem tak napisanego skryptu / funkcji / obiektu.")

from memory_profiler import profile

@profile
def lista(x):
    result_list = []
    for i in range(x):
        result_list.append(i ** 3)
    return result_list

@profile
def generator(x):
    for i in range(x):
        yield i ** 3

#Uzycie
wynikLista = lista(1000000)
wynikGenerator = generator(1000000)
# Konwersja generatora na listę dla porównania
wynikGeneratorLista = list(wynikGenerator)

