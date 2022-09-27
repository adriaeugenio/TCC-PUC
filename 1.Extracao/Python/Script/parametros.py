import datetime

########################################################################################

                            #Parametros de Caminho

########################################################################################

caminhoPasta = 'C:/Users/adria.eugenio/Desktop/Adria/Pós/TCC/ANAC/1.Extracao/Python'

caminhoPastaAlternativo = 'C:\\Users\\adria.eugenio\\Desktop\\Adria\\Pós\\TCC\\ANAC\\1.Extracao\\Python\\'

urlOrigem = "https://sistemas.anac.gov.br/"

urlOrigemCidadesEstados = "http://blog.mds.gov.br/redesuas/wp-content/uploads/2018/06/"

ourAirports = "https://ourairports.com/data/"

#0- Só gera o ano atual
#1 - Gera todos os anos de Historico conforme a lista(listaAnosGeradosBaseHistorica), 
geraTodoHistorico = 0

########################################################################################

                            #Parametros de Data

########################################################################################

listaAnosGeradosBaseHistorica = [2019,2020,2021,2022]

listaMeses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

listaMesesNumerico = [1,2,3,4,5,6,7,8,9,10,11,12]

listaMeses31Dias = [1,3,5,7,8,10,12]

pastaDados = caminhoPasta + '/Dados'

dataAtual = datetime.date.today()

MesAtual = dataAtual.month

AnoAtual = dataAtual.year