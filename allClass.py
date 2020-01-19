class Info:
    def __init__(self, nome):
        self.__nome = nome
        self.__registro = None
        self.__grad = None
        self.__espec = None
        self.__mest = None
        self.__dout = None
        self.__posDout = None

    def getReg(self):
        return self.__registro

    def setReg(self,newReg):
        self.__registro = newReg   

    def getNome(self):
        return self.__nome

    def getGrad(self):
        return self.__grad

    def setGrad(self,newGrad):
        self.__grad = newGrad    

    def getEspec(self):
        return self.__espec

    def setEspec(self,newEspec):
        self.__espec = newEspec    

    def getMest(self):
        return self.__mest

    def setMest(self,newMest):
        self.__mest = newMest  
    
    def getDout(self):
        return self.__dout

    def setDout(self,newDout):
        self.__dout = newDout

    def getPosDout(self):
        return self.__posDout

    def setPosDout(self,newPosDout):
        self.__posDout = newPosDout    


class MyException(Exception):
	def __init__(self,message):
		super().__init__(message)


class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None
    
    def getData(self):
        return self.__data    
    
    def getNext(self):
        return self.__next
    
    def setData(self,newData):
        self.__data = newData
    
    def setNext(self,newNext):
        self.__next = newNext

    
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def getHead(self):    
        return self.__head

    def setHead(self,newValue):
        self.__head = newValue 
    
    def insertion(self,position,element):
        try:
            assert position > 0 and position <= self.__size + 1
            
            #Condição 1: lista vazia
            if self.__head == None:
                if position != 1:
                    raise MyException('A lista está vazia. A posição correta é 1')
                newNode = Node(element)
                self.__head = newNode
                self.__size += 1
                return

            #Condição 2: inserção na primeira posição
            if position == 1:
                newNode = Node(element)
                newNode.setNext(self.__head)
                self.__head = newNode
                self.__size += 1
                return

            #Inserção após a primeira posição
            if position > 1 and position <= self.__size + 1:
                newNode = Node(element)
                aux = self.__head
                count = 1
                while aux != None and count != position - 1:
                    aux = aux.getNext()
                    count += 1
                if aux == None:
                    raise MyException('A posição {position} é inválida na lista atual')
                
                newNode = Node(element)            
                newNode.setNext(aux.getNext())
                aux.setNext(newNode)
                self.__size += 1
                
        except TypeError:
            raise MyException('A posição deve ser um número inteiro')        
        except AssertionError:
            raise MyException(f'A posição deve ser um número entre 1 e {self.__size + 1}')
        except:
            raise
    