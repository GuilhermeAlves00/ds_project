import csv
import ast
from allClass import *

with open('curriculos-lattes.csv') as dataset:
    leitor_dataset = csv.DictReader(dataset,delimiter=',')
    contador = 1
    lista = LinkedList()
    for linha in leitor_dataset:
        nome = linha["nome"]

        if linha["graduacao"] == 'SIM' and linha["area_graduacao"]:
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

showData(lista)


                
        


       
        
        

