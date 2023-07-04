import requests
from pprint import pprint

class Dados_Abertos:
    def __init__(self):
        self.dados_deputados = self.recebe_dados_deputados()
        self.quantidade_deputados = len(self.dados_deputados['dados'])        

    def recebe_dados_deputados(self):
        dados = requests.get(url='https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome').json()
        return dados
    
    def top_5_deputados_que_mais_gastam_por_estado(self, sigla: str):       
        dicionario_relacao_deputados_gasto_total = {}

        for deputado in self.dados_deputados['dados']:
            if deputado['siglaUf'] == sigla:
                deputado_id = deputado['id']
                despesas = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas?ordem=ASC&ordenarPor=ano').json()               
                dicionario_deputado_gastos = {}               

                for despesa in despesas['dados']:                   
                    if despesa['codDocumento'] not in dicionario_deputado_gastos:
                        dicionario_deputado_gastos[despesa['codDocumento']] = despesa['valorLiquido']
                    else:
                        dicionario_deputado_gastos[despesa['codDocumento']] += despesa['valorLiquido']  

                total_valorLiquido_por_deputado = sum(dicionario_deputado_gastos.values())         

                total_valorLiquido_por_deputado = round(total_valorLiquido_por_deputado, 2)             

                dicionario_relacao_deputados_gasto_total[deputado['nome']] = total_valorLiquido_por_deputado

        top_5_deputados_que_mais_gastam_por_estado = dict(sorted(dicionario_relacao_deputados_gasto_total.items(), key=lambda item: item[1], reverse = True)[:5])

        for nome in top_5_deputados_que_mais_gastam_por_estado.keys():
            dep_nome = nome
            dados = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados?nome={dep_nome}&ordem=ASC&ordenarPor=nome').json()

            for deputado in dados['dados']:
                print(
                    '\nNome: ' + deputado['nome'] +
                    '\nSigla do Partido: ' + deputado['siglaPartido'] +
                    '\nEstado: ' + deputado['siglaUf'] + 
                    '\nTotal de gastos: ' + 'R$ ' + str(top_5_deputados_que_mais_gastam_por_estado[deputado['nome']])
                    )
            
                

    def top_5_deputados_que_menos_gastam_no_norte(self):
        print('\nREGIÃO NORTE')
        dicionario_relacao_deputados_gasto_total = {}

        for deputado in self.dados_deputados['dados']:
            if deputado['siglaUf'] == 'AM' or deputado['siglaUf'] == 'RR' or deputado['siglaUf'] == 'AP' or deputado['siglaUf'] == 'PA' or deputado['siglaUf'] == 'TO' or deputado['siglaUf'] == 'RO' or deputado['siglaUf'] == 'AC':                   
                deputado_id = deputado['id']
                despesas = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas?ordem=ASC&ordenarPor=ano').json()               
                dicionario_deputado_gastos = {}  

                for despesa in despesas['dados']:                   
                    if despesa['codDocumento'] not in dicionario_deputado_gastos:
                        dicionario_deputado_gastos[despesa['codDocumento']] = despesa['valorLiquido']
                    else:
                        dicionario_deputado_gastos[despesa['codDocumento']] += despesa['valorLiquido']         
                                
                total_valorLiquido_por_deputado = sum(dicionario_deputado_gastos.values())               

                total_valorLiquido_por_deputado = round(total_valorLiquido_por_deputado, 2)               

                dicionario_relacao_deputados_gasto_total[deputado['nome']] = total_valorLiquido_por_deputado

        top_5_deputados_que_mais_gastam_por_estado = dict(sorted(dicionario_relacao_deputados_gasto_total.items(), key=lambda item: item[1],)[:5])

        for nome in top_5_deputados_que_mais_gastam_por_estado.keys():
            dep_nome = nome
            dados = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados?nome={dep_nome}&ordem=ASC&ordenarPor=nome').json()

            for deputado in dados['dados']:
                print(
                    '\nNome: ' + deputado['nome'] +
                    '\nSigla do Partido: ' + deputado['siglaPartido'] +
                    '\nEstado: ' + deputado['siglaUf'] + 
                    '\nTotal de gastos: ' + 'R$ ' + str(top_5_deputados_que_mais_gastam_por_estado[deputado['nome']])
                    )

    def top_5_deputados_que_menos_gastam_no_nordeste(self):
        print('\nREGIÃO NORDESTE')
        dicionario_relacao_deputados_gasto_total = {}

        for deputado in self.dados_deputados['dados']:
            if deputado['siglaUf'] == 'MA' or deputado['siglaUf'] == 'PI' or deputado['siglaUf'] == 'CE' or deputado['siglaUf'] == 'RN' or deputado['siglaUf'] == 'PE' or deputado['siglaUf'] == 'PB' or deputado['siglaUf'] == 'SE' or deputado['siglaUf'] == 'AL' or deputado['siglaUf'] == 'BA':                   
                deputado_id = deputado['id']
                despesas = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas?ordem=ASC&ordenarPor=ano').json()               
                dicionario_deputado_gastos = {}               
                
                for despesa in despesas['dados']:                   
                    if despesa['codDocumento'] not in dicionario_deputado_gastos:
                        dicionario_deputado_gastos[despesa['codDocumento']] = despesa['valorLiquido']
                    else:
                        dicionario_deputado_gastos[despesa['codDocumento']] += despesa['valorLiquido']    

                total_valorLiquido_por_deputado = sum(dicionario_deputado_gastos.values())     
                          
                total_valorLiquido_por_deputado = round(total_valorLiquido_por_deputado, 2)         

                dicionario_relacao_deputados_gasto_total[deputado['nome']] = total_valorLiquido_por_deputado

        top_5_deputados_que_mais_gastam_por_estado = dict(sorted(dicionario_relacao_deputados_gasto_total.items(), key=lambda item: item[1],)[:5])

        for nome in top_5_deputados_que_mais_gastam_por_estado.keys():
            dep_nome = nome
            dados = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados?nome={dep_nome}&ordem=ASC&ordenarPor=nome').json()

            for deputado in dados['dados']:
                print(
                    '\nNome: ' + deputado['nome'] +
                    '\nSigla do Partido: ' + deputado['siglaPartido'] +
                    '\nEstado: ' + deputado['siglaUf'] + 
                    '\nTotal de gastos: ' + 'R$ ' + str(top_5_deputados_que_mais_gastam_por_estado[deputado['nome']])
                    )

    def top_5_deputados_que_menos_gastam_no_centro_oeste(self):
        print('\nREGIÃO CENTRO-OESTE')
        dicionario_relacao_deputados_gasto_total = {}

        for deputado in self.dados_deputados['dados']:
            if deputado['siglaUf'] == 'MT' or deputado['siglaUf'] == 'MS' or deputado['siglaUf'] == 'GO':                   
                deputado_id = deputado['id']
                despesas = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas?ordem=ASC&ordenarPor=ano').json()               
                dicionario_deputado_gastos = {}            

                for despesa in despesas['dados']:                   
                    if despesa['codDocumento'] not in dicionario_deputado_gastos:
                        dicionario_deputado_gastos[despesa['codDocumento']] = despesa['valorLiquido']
                    else:
                        dicionario_deputado_gastos[despesa['codDocumento']] += despesa['valorLiquido']                  
                total_valorLiquido_por_deputado = sum(dicionario_deputado_gastos.values())               
                total_valorLiquido_por_deputado = round(total_valorLiquido_por_deputado, 2)               
                dicionario_relacao_deputados_gasto_total[deputado['nome']] = total_valorLiquido_por_deputado
        top_5_deputados_que_mais_gastam_por_estado = dict(sorted(dicionario_relacao_deputados_gasto_total.items(), key=lambda item: item[1],)[:5])

        for nome in top_5_deputados_que_mais_gastam_por_estado.keys():
            dep_nome = nome
            dados = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados?nome={dep_nome}&ordem=ASC&ordenarPor=nome').json()

            for deputado in dados['dados']:
                print(
                    '\nNome: ' + deputado['nome'] +
                    '\nSigla do Partido: ' + deputado['siglaPartido'] +
                    '\nEstado: ' + deputado['siglaUf'] + 
                    '\nTotal de gastos: ' + 'R$ ' + str(top_5_deputados_que_mais_gastam_por_estado[deputado['nome']])
                    )

    def top_5_deputados_que_menos_gastam_no_sudeste(self):
        print('\nREGIÃO SUDESTE')
        dicionario_relacao_deputados_gasto_total = {}
        
        for deputado in self.dados_deputados['dados']:
            if deputado['siglaUf'] == 'SP' or deputado['siglaUf'] == 'RJ' or deputado['siglaUf'] == 'ES' or deputado['siglaUf'] == 'MG':                   
                deputado_id = deputado['id']
                despesas = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas?ordem=ASC&ordenarPor=ano').json()               
                dicionario_deputado_gastos = {}       

                for despesa in despesas['dados']:                   
                    if despesa['codDocumento'] not in dicionario_deputado_gastos:
                        dicionario_deputado_gastos[despesa['codDocumento']] = despesa['valorLiquido']
                    else:
                        dicionario_deputado_gastos[despesa['codDocumento']] += despesa['valorLiquido']    

                total_valorLiquido_por_deputado = sum(dicionario_deputado_gastos.values())             

                total_valorLiquido_por_deputado = round(total_valorLiquido_por_deputado, 2)     

                dicionario_relacao_deputados_gasto_total[deputado['nome']] = total_valorLiquido_por_deputado

        top_5_deputados_que_mais_gastam_por_estado = dict(sorted(dicionario_relacao_deputados_gasto_total.items(), key=lambda item: item[1],)[:5])
        
        for nome in top_5_deputados_que_mais_gastam_por_estado.keys():
            dep_nome = nome
            dados = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados?nome={dep_nome}&ordem=ASC&ordenarPor=nome').json()

            for deputado in dados['dados']:
                print(
                    '\nNome: ' + deputado['nome'] +
                    '\nSigla do Partido: ' + deputado['siglaPartido'] +
                    '\nEstado: ' + deputado['siglaUf'] + 
                    '\nTotal de gastos: ' + 'R$ ' + str(top_5_deputados_que_mais_gastam_por_estado[deputado['nome']])
                    )

    def top_5_deputados_que_menos_gastam_no_sul(self):
        print('\nREGIÃO SUL')
        dicionario_relacao_deputados_gasto_total = {}

        for deputado in self.dados_deputados['dados']:
            if deputado['siglaUf'] == 'PR' or deputado['siglaUf'] == 'RS' or deputado['siglaUf'] == 'SC':                   
                deputado_id = deputado['id']
                despesas = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas?ordem=ASC&ordenarPor=ano').json()               
                dicionario_deputado_gastos = {}

                for despesa in despesas['dados']:
                    if despesa['codDocumento'] not in dicionario_deputado_gastos:
                        dicionario_deputado_gastos[despesa['codDocumento']] = despesa['valorLiquido']
                    else:
                        dicionario_deputado_gastos[despesa['codDocumento']] += despesa['valorLiquido']    

                total_valorLiquido_por_deputado = sum(dicionario_deputado_gastos.values())     

                total_valorLiquido_por_deputado = round(total_valorLiquido_por_deputado, 2)  

                dicionario_relacao_deputados_gasto_total[deputado['nome']] = total_valorLiquido_por_deputado

        top_5_deputados_que_mais_gastam_por_estado = dict(sorted(dicionario_relacao_deputados_gasto_total.items(), key=lambda item: item[1],)[:5])

        for nome in top_5_deputados_que_mais_gastam_por_estado.keys():
            dep_nome = nome
            dados = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados?nome={dep_nome}&ordem=ASC&ordenarPor=nome').json()

            for deputado in dados['dados']:
                print(
                    '\nNome: ' + deputado['nome'] +
                    '\nSigla do Partido: ' + deputado['siglaPartido'] +
                    '\nEstado: ' + deputado['siglaUf'] + 
                    '\nTotal de gastos: ' + 'R$ ' + str(top_5_deputados_que_mais_gastam_por_estado[deputado['nome']])
                    )

    def escolhe_regiao(self, regiao: str):
        if regiao == 'norte':
            self.top_5_deputados_que_menos_gastam_no_norte()
        elif regiao == 'nordeste':
            self.top_5_deputados_que_menos_gastam_no_nordeste()
        elif regiao == 'centro oeste' or regiao == 'centro-oeste' or regiao == 'centro_oeste' or regiao == 'centrooeste':
            self.top_5_deputados_que_menos_gastam_no_centro_oeste()
        elif regiao == 'sudeste':
            self.top_5_deputados_que_menos_gastam_no_sudeste()
        elif regiao == 'sul':
            self.top_5_deputados_que_menos_gastam_no_sul()
        else:
            print('Região inválida...')

    def top_5_Fornecedores_que_mais_receberam_verbas_no_brasil(self):
        print('Top 5 fornecedores que mais receberam no Brasil')
        dicionario_relacao_fornecedor_gasto_total = {}

        for deputado in self.dados_deputados['dados']:
            deputado_id = deputado['id']
            despesas = requests.get(url=f'https://dadosabertos.camara.leg.br/api/v2/deputados/{deputado_id}/despesas?ordem=ASC&ordenarPor=ano').json()

            for despesa in despesas['dados']:
                nome_fornecedor = despesa['nomeFornecedor']
                cnpj_cpf_fornecedor = despesa['cnpjCpfFornecedor'] 

                if nome_fornecedor not in dicionario_relacao_fornecedor_gasto_total:
                    dicionario_relacao_fornecedor_gasto_total[nome_fornecedor] = despesa['valorLiquido']
                else:
                    dicionario_relacao_fornecedor_gasto_total[nome_fornecedor] += despesa['valorLiquido']

        top_5_fornecedores_que_mais_receberam_no_brasil = dict(sorted(dicionario_relacao_fornecedor_gasto_total.items(), key=lambda item: item[1], reverse=True)[:5])

        for fornecedor, valor in top_5_fornecedores_que_mais_receberam_no_brasil.items():
            print(
                '\nNome do Fornecedor: ' + fornecedor +
                '\nCNPJ`/`CPF: ' + cnpj_cpf_fornecedor +
                '\nValor recebido: R$ ' + str(round(valor, 2))
            )
       

objeto_dados_abertos = Dados_Abertos()

objeto_dados_abertos.top_5_deputados_que_mais_gastam_por_estado(sigla = input('Digite a sigla do estado para anialisar o top 5 Deputados que mais gastam: ').upper())
#objeto_dados_abertos.escolhe_regiao(regiao=input('Digite o nome da região: ').lower())
#objeto_dados_abertos.top_5_Fornecedores_que_mais_receberam_verbas_no_brasil()
#objeto_dados_abertos.top_5_Fornecedores_que_mais_receberam_verbas_no_brasil()