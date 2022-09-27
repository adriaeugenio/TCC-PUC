import requests
import os
import parametros as p
import pandas as pd
import juntarPlanilhas as jp
import juntarPlanilhasHistorico as jph
import apagaArquivoPasta as apagaarquivos

#Declara o caminho da Pasta
caminhoPasta = p.pastaDados + '/Tarifas Internacionais/'

#Verifica se o Arquivo Existe na Pasta
if os.path.exists(caminhoPasta + 'TarifasInternacionaisGeral.csv'):

    #Para gerar um novo histórico
    if p.geraTodoHistorico == 1:  

        #Apaga a Planilha do Histórico Para Gerar um Novo
        apaga = apagaarquivos.apagaArquivoPasta(caminhoPasta)

#Caso Não Exista ele obriga gerar um novo histórico, mesmo que o parametro estejá para não gerar       
else: 
    p.geraTodoHistorico = 1

#Loop para Gerar os Arquivos Por Ano
for i in p.listaAnosGeradosBaseHistorica:

    indiceAnos = p.listaAnosGeradosBaseHistorica.index(i)

    for a in p.listaMeses:

        indiceMeses = p.listaMeses.index(a)

        mesesNumerico = str(p.listaMesesNumerico[indiceMeses])

        if(p.geraTodoHistorico == 1 and p.listaAnosGeradosBaseHistorica[indiceAnos] != p.AnoAtual) \
           or (p.geraTodoHistorico == 1 and p.listaAnosGeradosBaseHistorica[indiceAnos] == p.AnoAtual and p.listaMesesNumerico[indiceMeses] < p.MesAtual) \
           or (p.geraTodoHistorico == 0 and p.listaAnosGeradosBaseHistorica[indiceAnos] == p.AnoAtual and p.listaMesesNumerico[indiceMeses] == p.MesAtual):

            if p.listaMesesNumerico[indiceMeses] < 10: 
                
                codigoMes = "0" 

            else:

                codigoMes = ""
 
            nomeArquivo = "INTERNACIONAL_" + str(p.listaAnosGeradosBaseHistorica[indiceAnos]) + "-" + codigoMes + mesesNumerico  + ".csv"          

            urlMes = str(p.listaAnosGeradosBaseHistorica[indiceAnos]) + "/" + nomeArquivo

            urlCaminho = str(p.listaAnosGeradosBaseHistorica[indiceAnos]) + "/"

            #Define a Url de Origem do Arquivo
            remote_url = p.urlOrigem + "sas/tarifainternacional/" + urlMes

            #Define a Url o Local de Salvamento do Arquivo
            local_file = p.pastaDados + '/Tarifas Internacionais/' + nomeArquivo

            if os.path.isdir(caminhoPasta):

                teste = ""

            else: 

                os.makedirs(caminhoPasta)
            
            #Requisição HTTP
            data = requests.get(remote_url)

            print(remote_url)

            #Salva o Arquivo
            with open(local_file, 'wb') as file:

                file.write(data.content) 
            
            df = pd.read_csv(local_file,sep=';',encoding='latin-1',on_bad_lines='skip')

            headerList = ['Ano de Referência','Mês de Referência','ICAO Empresa Aérea','ICAO Aeródromo Origem','ICAO Aeródromo Destino','ICAO Aeródromo Retorno','Classe de Ida','Classe de Volta','Tarifa-N','Assentos Comercializados'] 

            totalColunas = len(df.axes[1])

            #Caso o arquivo venha nulo
            if totalColunas == 1:

                df.to_csv(local_file, sep=';',index=None, header=None,  encoding='utf-8-sig')
                os.remove(caminhoPasta + nomeArquivo) 

            #Caso quantidade certa de campos do Arquivo
            if totalColunas == 10:

                df.to_csv(local_file, sep=';',index=None, header=headerList,  encoding='utf-8-sig')
                os.rename(local_file, p.pastaDados + '/Tarifas Internacionais/'+ 'TarifasInternacionais_' + str(p.listaAnosGeradosBaseHistorica[indiceAnos]) + "-" + codigoMes + mesesNumerico  + ".csv") 

            #Caso quantidade venha com campo a mais (Existe alguns arquivos Vem)
            if totalColunas == 11:   
                
                first_column = df.columns[0]
                df = df.drop([first_column], axis=1)
                df.to_csv(local_file, sep=';',index=None, header=headerList,  encoding='utf-8-sig')
                os.rename(local_file, p.pastaDados + '/Tarifas Internacionais/'+ 'TarifasInternacionais_' + str(p.listaAnosGeradosBaseHistorica[indiceAnos]) + "-" + codigoMes + mesesNumerico  + ".csv")

#Define o Caminho de Pasta
os.chdir(p.pastaDados + '/Tarifas Internacionais')              

if p.geraTodoHistorico == 0:  
                
    #Juntas as Fontes de Dados
    v = jp.juntaPlanilhas('Tarifas Internacionais','TarifasInternacionaisNovo',headerList) 
    v1 = jph.juntaPlanilhasHistorico('Tarifas Internacionais','TarifasInternacionaisHistorico') 

else:

    #Juntas as Fontes de Dados
    v = jp.juntaPlanilhas('Tarifas Internacionais','TarifasInternacionaisHistorico',headerList)  

#Renomeia o arquivo
os.rename('TarifasInternacionaisHistorico.csv', 'TarifasInternacionaisGeral.csv')