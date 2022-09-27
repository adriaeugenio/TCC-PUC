import requests
import os
import parametros as p
import verificaPastaExiste as ve
import transformaCSVExcel as csvexcel

#Verifica se a Pasta Existe (Caso Não Exista, Ela é criada)
v = ve.verificaPasta(p.pastaDados + '/Cidades')

#Define a Url de Origem do Arquivo
remote_url = p.urlOrigemCidadesEstados + "Lista_Municípios_com_IBGE_Brasil_Versao_CSV.csv"

#Define a Url o Local de Salvamento do Arquivo
local_file = p.pastaDados + '/Cidades/' + 'Cidades.csv'

#Requisição HTTP
data = requests.get(remote_url)

print(remote_url)

#Salva o Arquivo
with open(local_file, 'wb') as file:

    file.write(data.content)

#Define o Caminho de Pasta
os.chdir(p.pastaDados + '/Cidades')  

#Transforma o Arquivo CSV em Excel
ce = csvexcel.transformaCSVExcel('Cidades')        