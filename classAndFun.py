'''class Info:
    def __init__(self, nome, grad, espec, mest, dout, posDout):
        self.__nome = nome
        self.__grad = grad
        self.__espec = espec
        self.__mest = mest
        self.__dout = dout
        self.__posDout = posDout

    def getNome(self):
        return self.__nome
    def getGrad(self):
        return self.__grad
    def getEspec(self):
        return self.__espec
    def getMest(self):
        return self.__mest
    def getDout(self):
        return self.__dout
    def getPosDout(self):
        return self.__posDout                    

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

    def getSize(self):
        return self.__size          

    def insertion(self,position,element):
        try:
            assert position > 0 and position <= self.__size + 1
            
            '''Condição 1: lista vazia'''
            if self.__head == None:
                if position != 1:
                    raise MyException('A lista está vazia. A posição correta é 1')
                newNode = Node(element)
                self.__head = newNode
                self.__size += 1
                return

            '''Condição 2: inserção na primeira posição'''
            if position == 1:
                newNode = Node(element)
                newNode.setNext(self.__head)
                self.__head = newNode
                self.__size += 1
                return

            '''Inserção após a primeira posição'''
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

    
    def remove(self,position):
        if self.__head == None:
            raise MyException('A lista está vazia,é impossível realizar a remoção')
        try:
            assert position > 0 and position <= self.__size
            aux = self.__head
            counter = 1
            while counter < position:
                previous = aux
                aux = aux.getNext()
                counter += 1

            data = aux.getData()    

            if position == 1:
                self.setHead(aux.getNext())
                self.__size -= 1
            else:
                previous.setNext(aux.getNext())
                self.__size -= 1
            return data    

        except TypeError:
            raise MyException('A posição deve ser um número inteiro')
        except AssertionError:
            raise MyException(f'A posição deve ser um número entre 1 e {self.__size}')            
        except:
            raise

    def __str__(self):
        res = ''
        aux = self.__head
        count = 1
        while aux != None and count <= self.__size:
            res += str(aux.getData())
            res += '->'
            aux = aux.getNext()
            count += 1
        return res 

    def showList(self):
        return self.__str__()'''

def menu():
    print('(c) Carregar dados\n(e) Estatísticas da base de dados\n(i) Busca\n(s) Sobre\n(q) Sair')     


def showData(linkedList):
    all = linkedList.getHead()
    count = 2
    while all.getData():
        print()
        print(f'Nome: {all.getData().getNome()}')
        print(f'Graduação: {all.getData().getGrad()}')
        print(f'Especialização: {all.getData().getEspec()}')
        print(f'Mestrado: {all.getData().getMest()}')
        print(f'Doutorado: {all.getData().getDout()}')
        print(f'Pós-Doutorado: {all.getData().getPosDout()}')
        print(f'Registro de número: {count}')
        print()
        print('=' * 100)
        if all.getNext():
            all = all.getNext()
        else:
            break    
        count += 1

import csv
#import ast
def load():
    with open('curriculos-lattes.csv') as dataset:
        leitor_dataset = csv.DictReader(dataset,delimiter=',')
        #contador = 1
        #lista = LinkedList()
        for linha in leitor_dataset:
            nome = linha["nome"]
            print(nome)

            '''if linha["graduacao"] == 'SIM' and linha["area_graduacao"]:
                aux = linha["area_graduacao"]
                #Caso possua mais de uma graduação converte de string p/ lista
                if aux[0] == '[':            
                    graduacao = ast.literal_eval(aux) 
                #Caso possua apenas uma graduação...
                else:
                    graduacao = aux
            else:
                graduacao = 'Não possui graduação'     

            if linha["especializacao"] == 'SIM' and linha["area_especializacao"]:
                aux = linha["area_especializacao"]
                #Caso possua mais de uma especialização converte de string p/ lista
                if aux[0] == '[':
                    especializacao = ast.literal_eval(aux)
                #Caso possua apenas uma especialização...
                else:
                    especializacao = aux
            else:
                especializacao = 'Não possui especialização'

            if linha["mestrado"] == 'SIM' and linha["area_mestrado"]:
                aux = linha["area_mestrado"]
                #Caso possua mais de um mestrado converte de string p/ lista
                if aux[0] == '[':            
                    mestrado = ast.literal_eval(aux)
                #Caso possua apenas um mestrado...
                else:
                    mestrado = aux    
            else:
                mestrado = 'Não possui mestrado'                                    

            if linha["doutorado"] == 'SIM' and linha["area_doutorado"]:
                aux = linha["area_doutorado"]
                #Caso possua mais de um doutorado converte de string p/ lista
                if aux[0] == '[':            
                    doutorado = ast.literal_eval(aux)
                #Caso possua apenas um doutorado...
                else:
                    doutorado = aux        
            else:
                doutorado = 'Não possui doutorado'                                         

            if linha["pos_doutorado"] == 'SIM' and linha["area_pos_doutorado"]:
                aux = linha["area_pos_doutorado"]
                #Caso possua mais de um pós-doutorado converte de string p/ lista
                if aux[0] == '[':            
                    posDout = ast.literal_eval(aux)
                #Caso possua apenas um pós-doutorado...
                else:
                    posDout = aux    
            else:
                posDout = 'Não possui pós-doutorado'                                                                                 

            dados = Info(nome,graduacao,especializacao,mestrado,doutorado,posDout)
            lista.insertion(contador,dados)
            contador += 1
        return lista'''    

def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

    return d[lenstr1-1,lenstr2-1]

