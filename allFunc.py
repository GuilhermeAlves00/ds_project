import csv, ast, textdistance
from allClass import *

def dlLoad(nivel,area):
    with open('curriculos-lattes.csv') as dataset:
        leitor_dataset = csv.DictReader(dataset,delimiter=',')
        contador = 1
        lista = LinkedList()

        #Para nível de graduação
        if nivel == 'GRADUAÇÃO':
            for linha in leitor_dataset:
                if linha["graduacao"] == 'SIM' and linha["area_graduacao"]:
                    aux = linha["area_graduacao"]
                    #Caso possua mais de uma graduação converte de string p/ lista
                    if aux[0] is '[' and aux[-1] is ']':            
                        gradList = ast.literal_eval(aux)
                        for i in gradList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.5:
                                dados = Info(linha["nome"])
                                dados.setGrad(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
                    #Caso possua apenas uma graduação...
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.5:
                            dados = Info(linha["nome"])
                            dados.setGrad(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue    
        #A partir daqui os códigos seguem semelhantes mudando o nível de conhecimento, nome de variáveis e
        #informações inseridas na classe Info

        elif nivel == 'ESPECIALIZAÇÃO':
            for linha in leitor_dataset:
                if linha["especializacao"] == 'SIM' and linha["area_especializacao"]:
                    aux = linha["area_especializacao"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        especList = ast.literal_eval(aux)
                        for i in especList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.5:
                                dados = Info(linha["nome"])
                                dados.setEspec(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.5:
                            dados = Info(linha["nome"])
                            dados.setEspec(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue     

        elif nivel == 'MESTRADO':
            for linha in leitor_dataset:
                if linha["mestrado"] == 'SIM' and linha["area_mestrado"]:
                    aux = linha["area_mestrado"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        mestList = ast.literal_eval(aux)
                        for i in mestList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.5:
                                dados = Info(linha["nome"])
                                dados.setMest(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.5:
                            dados = Info(linha["nome"])
                            dados.setMest(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue     
                    
        elif nivel == 'DOUTORADO':
            for linha in leitor_dataset:
                if linha["doutorado"] == 'SIM' and linha["area_doutorado"]:
                    aux = linha["area_doutorado"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        doutList = ast.literal_eval(aux)
                        for i in doutList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.5:
                                dados = Info(linha["nome"])
                                dados.setDout(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.5:
                            dados = Info(linha["nome"])
                            dados.setDout(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue 

        elif nivel == 'PÓS-DOUTORADO':
            for linha in leitor_dataset:
                if linha["pos_doutorado"] == 'SIM' and linha["area_pos_doutorado"]:
                    aux = linha["area_pos_doutorado"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        posDoutList = ast.literal_eval(aux)
                        for i in posDoutList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.5:
                                dados = Info(linha["nome"])
                                dados.setPosDout(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.5:
                            dados = Info(linha["nome"])
                            dados.setPosDout(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue                     
                 
            
        print(showData(lista,nivel))
'''
def jdLoad(nivel,area):
    with open('curriculos-lattes.csv') as dataset:
        leitor_dataset = csv.DictReader(dataset,delimiter=',')
        contador = 1
        lista = LinkedList()

        #Para nível de graduação
        if nivel == 'GRADUAÇÃO':
            for linha in leitor_dataset:
                if linha["graduacao"] == 'SIM' and linha["area_graduacao"]:
                    aux = linha["area_graduacao"]
                    #Caso possua mais de uma graduação converte de string p/ lista
                    if aux[0] is '[' and aux[-1] is ']':            
                        gradList = ast.literal_eval(aux)
                        for i in gradList:
                            result = textdistance.jaro.distance(i,area)
                            if result <= 0.3:
                                dados = Info(linha["nome"])
                                dados.setGrad(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
                    #Caso possua apenas uma graduação...
                    else:
                        result = textdistance.jaro.distance(aux,area)
                        if result <= 0.3:
                            dados = Info(linha["nome"])
                            dados.setGrad(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue    
        #A partir daqui os códigos seguem semelhantes mudando o nível de conhecimento, nome de variáveis e
        #informações inseridas na classe Info

        elif nivel == 'ESPECIALIZAÇÃO':
            for linha in leitor_dataset:
                if linha["especializacao"] == 'SIM' and linha["area_especializacao"]:
                    aux = linha["area_especializacao"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        especList = ast.literal_eval(aux)
                        for i in especList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.3:
                                dados = Info(linha["nome"])
                                dados.setEspec(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.3:
                            dados = Info(linha["nome"])
                            dados.setEspec(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue     

        elif nivel == 'MESTRADO':
            for linha in leitor_dataset:
                if linha["mestrado"] == 'SIM' and linha["area_mestrado"]:
                    aux = linha["area_mestrado"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        mestList = ast.literal_eval(aux)
                        for i in mestList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.3:
                                dados = Info(linha["nome"])
                                dados.setMest(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.3:
                            dados = Info(linha["nome"])
                            dados.setMest(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue     
                    
        elif nivel == 'DOUTORADO':
            for linha in leitor_dataset:
                if linha["doutorado"] == 'SIM' and linha["area_doutorado"]:
                    aux = linha["area_doutorado"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        doutList = ast.literal_eval(aux)
                        for i in doutList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.3:
                                dados = Info(linha["nome"])
                                dados.setDout(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.3:
                            dados = Info(linha["nome"])
                            dados.setDout(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue 

        elif nivel == 'PÓS-DOUTORADO':
            for linha in leitor_dataset:
                if linha["pos_doutorado"] == 'SIM' and linha["area_pos_doutorado"]:
                    aux = linha["area_pos_doutorado"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        posDoutList = ast.literal_eval(aux)
                        for i in posDoutList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result < 0.3:
                                dados = Info(linha["nome"])
                                dados.setPosDout(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result < 0.3:
                            dados = Info(linha["nome"])
                            dados.setPosDout(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue                     
                 
            
        print(showData(lista,nivel))
'''


def showData(linkedList,nivel):
    all = linkedList.getHead()
    try:
        assert all is not None
        print()
        while all.getData():
            print('=' * 50)
            print(f'Docente: {all.getData().getNome()}')
            if nivel == 'GRADUAÇÃO':
                print(f'Área de Formação: {all.getData().getGrad()}')
            if nivel == 'ESPECIALIZAÇÃO':
                print(f'Área de Formação: {all.getData().getEspec()}')
            if nivel == 'MESTRADO':
                print(f'Área de Formação: {all.getData().getMest()}')    
            if nivel == 'DOUTORADO':
                print(f'Área de Formação: {all.getData().getDout()}')        
            if nivel == 'PÓS-DOUTORADO':
                print(f'Área de Formação: {all.getData().getPosDout()}')        
            
            print(f'Registro: {all.getData().getReg()}')
            if all.getNext():
                all = all.getNext()
            else:
                return '=' * 50               
                
    except AssertionError:
        raise MyException('Não há registros compatíveis com a respectiva área de conhecimento.')
    except:
        raise

def menu():
    print('(c) Carregar dados\n(e) Estatísticas da base de dados\n(i) Busca\n(s) Sobre\n(q) Sair')

def main():
    menu()
    option = input('Escolha uma opção:', )
    while True:
        if option == 'i':
            print()
            qualNv = ('GRADUAÇÃO','ESPECIALIZAÇÃO','MESTRADO','DOUTORADO','PÓS-DOUTORADO')
            qual = input('Qualificação:', ).upper()
            while qual not in qualNv:
                print('\nQualificação Inválida\nDisponíveis: Graduação | Especialização | Mestrado | Doutorado | Pós-Doutorado')
                qual = input('Nova Qualificação:', ).upper()
            area = input('Área do Conhecimento:', )
            try:
                dlLoad(qual,area)
            except MyException as me:
                print(me)
            except Exception as ex:
                print(ex)
                print('Tivemos um problema e trabalharemos para resolvê-lo')        
        
        elif option == 'q':
            break

        else:
            pass    

