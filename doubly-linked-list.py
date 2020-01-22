"""

Coded by ÖMER MİRAÇ KÖKÇAM
omermirac.kokcam@gmail.com

"""


class Node(object):


    def __init__(self,value):
        # Node yarat (yapılandırıcı)
        self.value = value
        self.prevNode = None
        self.nextNode = None


    def setNextNode(self,Node):
        # next node un ne olduğunu set eder
        self.nextNode = Node


    def setPrevNode(self,Node):
        # prev node un ne olduğunu set eder
        self.prevNode = Node


    def getNextNode(self):
        # next node u return eder
        return self.nextNode


    def getPrevNode(self):
        # prev node u return eder
        return self.prevNode


    def getNodeValue(self):
        # next node un degerini return eder
        return self.value



Ankara = Node('06')
Bolu = Node('14')
Istanbul = Node('34')
# Ankara => Bolu
Ankara.setNextNode(Bolu)
# Bolu => Ankara
Bolu.setPrevNode(Ankara)
# Ankara <=> Bolu
print(Bolu.prevNode.getNodeValue())
print(Ankara.nextNode.getNodeValue())

