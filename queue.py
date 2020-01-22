"""
Queue

Coded by Ömer Miraç Kökçam
omermirac.kokcam@gmail.com
"""


class Queue:

    def __init__(self):
        #yapılandırıcı
        self.items = []


    def isEmpty(self):
        #Queue bos mu oldugunu kontrol edecek
        return self.items == [] #boolean dondurur


    def insert(self,item):
        #Queue ye eleman ekleme
        self.items.insert(0, item)


    def remove(self):
        #Queue den eleman silme
        return self.items.pop()


    def size(self):
        #Queue nun boyutunu alma
        return len(self.items)


    def front(self):
        #Queue nun en başındaki elemanı ceker ve gosterir
        return self.items[-1]



queue=Queue()
print(queue.isEmpty())
queue.insert('ankara')
queue.insert('istanbul')
queue.insert('izmir')
queue.insert('antalya')
queue.insert('konya')
queue.insert('elazig')
print(queue.size())
print(queue.remove())
print(queue.size())
print(queue.front())