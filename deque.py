"""
Deque

Coded by Ömer Miraç Kökçam
omermirac.kokcam@gmail.com
"""


class Deque:
    def __init__(self):
        #yapılandırıcı
        self.items = []


    def isEmpty(self):
        #Deque boş mu kontrol eder
        return self.items == [] #boolean deger dondurur


    def addFront(self,item):
        #Deque ya önden eleman ekler
        self.items.append(item)


    def addRear(self,item):
        #Deque ya arkadan eleman ekler
        self.items.insert(0, item)


    def removeFront(self):
        #Deque nun ön tarafından eleman cıkarır
        return self.items.pop()


    def removeRear(self):
        #Deque nun arka kısmından eleman cıkarır
        return self.items.pop(0)


    def size(self):
        #Deque nun boyutunu belirtir
        return len(self.items)


    def showFront(self):
        #Deque nun ön tarafındaki elemanı gösterir
        return self.items[-1]


    def showRear(self):
        #Deque nun arka tarafındaki elemanı gösterir
        return self.items[0]


    def showAll(self):
        #Deque daki tüm elemanları gösterir
        if self.items != []:
            return self.items


deque=Deque()

print(deque.isEmpty())
deque.addFront('istanbul')
deque.addRear('34')
deque.addFront('ankara')
deque.addRear('06')
deque.addFront('izmir')
deque.addRear('35')
deque.addFront('konya')
deque.addRear('42')
deque.addFront('elazig')
deque.addRear('23')


print(deque.showFront())
print(deque.size())
print(deque.showAll())
print(deque.removeRear())
print(deque.showAll())
