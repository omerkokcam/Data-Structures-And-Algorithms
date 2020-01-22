"""
Stack

Coded by Ömer Miraç Kökçam
omermirac.kokcam@gmail.com
"""




class Stack :


    def __init__(self):
        #yapılandırıcı
        self.items = []


    def isEmpty(self):
        #boş olup olmadığını kontrol eder
        return self.items == [] #boolean


    def push(self,item):
        #stack e eleman ekler
        self.items.append(item)


    def pop(self):
        #stack'ten en son elemanı çeker ve siler
        return self.items.pop()

    def top(self):
        #stack içerisindeki en son elemanı alır ve gösterir
        return self.items[-1]


    def size(self):
        #stack'in boyutunu verir
        return len(self.items)


stack=Stack()
print(stack.isEmpty())
stack.push('Elazig')
print(stack.top())
stack.push('Ankara')
stack.push('İstanbul')
print(stack.top())
stack.push('İzmir')
print(stack.size())
print(stack.top())
print(stack.pop())
print(stack.top())
print(stack.isEmpty())
stack.pop()
print(stack.size())
stack.pop()
stack.pop()
print(stack.isEmpty())