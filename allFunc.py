import csv, ast, textdistance
from allClass import *

def damerau(nivel,area):
    with open('curriculos-lattes.csv') as dataset:
        leitor_dataset = csv.DictReader(dataset,delimiter=',')
        contador = 1
        lista = LinkedList()

        #Verificação do nível de conhecimento
        if nivel == 'GRADUAÇÃO':
            for linha in leitor_dataset:
                #Caso a linha atual possua graduação
                if linha["graduacao"] == 'SIM' and linha["area_graduacao"]:
                    aux = linha["area_graduacao"]
                    #Caso possua mais de uma graduação converte de string p/ lista
                    if aux[0] is '[' and aux[-1] is ']':            
                        gradList = ast.literal_eval(aux)
                        #Percorre a lista de graduações
                        for i in gradList:
                            #Distância de edição
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result <= 0.33:
                                #Cria uma instância da classe Info e insere na lista
                                dados = Info(linha["nome"])
                                dados.setGrad(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
                    #Caso possua apenas uma graduação
                    else:
                        #Distância de edição
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result <= 0.33:
                            #Cria uma instância da classe Info e insere na lista
                            dados = Info(linha["nome"])
                            dados.setGrad(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    #Caso a linha atual não possua graduação
                    continue    
        #A partir daqui os códigos seguem iguais para os outros níveis de formação alterando nome de variáveis,
        #informações inseridas na classe Info etc

        elif nivel == 'ESPECIALIZAÇÃO':
            for linha in leitor_dataset:
                if linha["especializacao"] == 'SIM' and linha["area_especializacao"]:
                    aux = linha["area_especializacao"]
                    if aux[0] is '[' and aux[-1] is ']':            
                        especList = ast.literal_eval(aux)
                        for i in especList:
                            result = textdistance.damerau_levenshtein.normalized_distance(i,area)
                            if result <= 0.33:
                                dados = Info(linha["nome"])
                                dados.setEspec(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result <= 0.33:
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
                            if result <= 0.33:
                                dados = Info(linha["nome"])
                                dados.setMest(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result <= 0.33:
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
                            if result <= 0.33:
                                dados = Info(linha["nome"])
                                dados.setDout(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result <= 0.33:
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
                            if result <= 0.33:
                                dados = Info(linha["nome"])
                                dados.setPosDout(i)
                                dados.setReg(contador)
                                lista.insertion(contador,dados)
                                contador += 1
            
                    else:
                        result = textdistance.damerau_levenshtein.normalized_distance(aux,area)
                        if result <= 0.33:
                            dados = Info(linha["nome"])
                            dados.setPosDout(aux)
                            dados.setReg(contador)
                            lista.insertion(contador,dados)
                            contador += 1
                else:
                    continue                     
                 
            
        print(showData(lista,nivel))


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
    print('(e) Estatísticas da base de dados\n(i) Busca\n(s) Sobre\n(q) Sair')

def main():
    menu()
    option = input('Escolha uma opção: ')
    while option != 'q':
        if option == 'e':
            print('\n- A base de dados é formada por informações relativas a docentes,possuindo campos que informam o nível e a área de formação do mesmo;')
            print('- Os campos presentes na base são: Área de Graduação; Área de Especialização; Área de Mestrado; Área de Doutorado; Área de Pós-Doutorado;')
            print('- Nenhum dos registros possui Pós-Doutorado, porém a busca nessa área está disponível caso seja necessário em uso futuro;')
            print('- A base de dados possui um total de 1630 registros.\n')
            break

        elif option == 'i':
            print()
            qualNv = ('GRADUAÇÃO','ESPECIALIZAÇÃO','MESTRADO','DOUTORADO','PÓS-DOUTORADO')
            qual = input('Qualificação(q p/ voltar):', ).upper()
            if qual == 'Q':
                break
            
            while qual not in qualNv and qual != 'Q':
                print('\nQualificação Inválida\nDisponíveis: Graduação | Especialização | Mestrado | Doutorado | Pós-Doutorado')
                qual = input('Nova Qualificação(q p/ voltar):', ).upper()
            if qual == 'Q':
                break
            area = input('Área do Conhecimento:', )
            try:
                damerau(qual,area)
            except MyException as me:
                print(me)
            except Exception as ex:
                print(ex)
                print('Tivemos um problema e trabalharemos para resolvê-lo')        
        
        elif option == 's':
            print('\n-Adrianderson Lira\n-Guilherme Alves\n-Hidekazu Takayama\n')
            print('- A solução adotada foi a distância de edição normalizada Damerau-Levenshtein através da biblioteca textdistance;')
            print('- A área de formação fornecida pelo usuário é comparada com a(s) área de formação dos docentes presentes na base de dados;')
            print('- Os registros que atenderem um determinado requisito será visualizado pelo usuário com o nome do docente e a respectiva formação.\n')
            break
        
        elif option == 'q':
            break

        else:
            print('\nOpção Inválida\n')  
    if option != 'q':        
        main()        


