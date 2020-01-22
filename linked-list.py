"""

Coded by Ömer Miraç Kökçam
omermirac.kokcam@gmail.com

"""

class Node:
    def __init__(self,value):
        #yapılandırıcı node yarat
        self.value = value
        self.nextNode = None


    def setNextNode(self,node):
        #next node un ne olduğunu set eder
        self.nextNode = node


    def getNextNode(self):
        #next node u return eder
        return self.nextNode


    def getNodeValue(self):
        #next node un degerini return eder
        return self.value


Ankara = Node('06')
Istanbul = Node('34')
Adana = Node('01')
Elazig = Node('23')
Konya = Node('42')
Adiyaman = Node('02')


Ankara.setNextNode(Istanbul)
print(Ankara.getNextNode().getNodeValue())
Istanbul.setNextNode(Adana)
print(Istanbul.getNextNode().getNodeValue())
Adana.setNextNode(Elazig)
print(Adana.getNextNode().getNodeValue())
Elazig.setNextNode(Konya)
print(Elazig.getNextNode().getNodeValue())
Konya.setNextNode(Adiyaman)
print(Konya.getNextNode().getNodeValue())
Adiyaman.setNextNode(Ankara)
print(Adiyaman.getNextNode().getNodeValue())
Ankara.setNextNode(Ankara)
print(Ankara.getNextNode().getNodeValue())

print(Ankara.getNextNode().getNextNode().getNodeValue())