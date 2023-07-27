# python-api-dadosabertos-camara
O código utiliza a biblioteca requests para fazer solicitações HTTP à API e a biblioteca pprint para imprimir os resultados de forma mais legível.

A seguir, uma explicação das principais partes do código:

Inicialização da Classe:

O construtor __init__(self) é chamado quando uma instância da classe é criada. Ele inicializa duas variáveis:
self.dados_deputados: Armazena os dados de todos os deputados obtidos da API.
self.quantidade_deputados: Armazena o número total de deputados obtidos na consulta.
Recebendo Dados dos Deputados:

O método recebe_dados_deputados(self) é responsável por fazer uma requisição à API para obter os dados de todos os deputados da Câmara dos Deputados e retorna esses dados em formato JSON.
Identificando os 5 Deputados que mais Gastam por Estado:

O método top_5_deputados_que_mais_gastam_por_estado(self, sigla: str) recebe como parâmetro a sigla de um estado brasileiro.
Ele utiliza a lista de deputados já obtida na inicialização para filtrar os deputados que pertencem ao estado informado.
Para cada deputado do estado, é feita uma consulta na API para obter suas despesas.
As despesas são então somadas para encontrar o total de gastos de cada deputado.
Os resultados são armazenados em um dicionário dicionario_relacao_deputados_gasto_total, onde a chave é o nome do deputado e o valor é o total de gastos.
Os 5 deputados que mais gastam são selecionados com base nesse dicionário e exibidos na saída.
Analisando os 5 Deputados que Menos Gastam em Regiões Específicas:

O código também inclui outros métodos para analisar os 5 deputados que menos gastam em regiões específicas do Brasil, como norte, nordeste, centro-oeste, sudeste e sul.
Escolhendo a Região e Mostrando Resultados:

O método escolhe_regiao(self, regiao: str) permite ao usuário escolher uma região do Brasil para obter os 5 deputados que menos gastam nessa região.
Ele invoca os métodos específicos para cada região com base na escolha do usuário.
Exibindo os Top 5 Fornecedores que mais Receberam no Brasil:

O método top_5_Fornecedores_que_mais_receberam_verbas_no_brasil(self) identifica e exibe os 5 fornecedores que mais receberam verbas da Câmara dos Deputados no Brasil. Ele agrupa as despesas por fornecedor e mostra os resultados ordenados pelo valor total recebido.
Criação do Objeto e Chamada de Métodos:

Por fim, o código cria um objeto objeto_dados_abertos da classe Dados_Abertos e chama o método top_5_deputados_que_mais_gastam_por_estado() para permitir que o usuário insira a sigla do estado e obtenha os resultados.
Nota: Algumas partes do código estão comentadas. Para que os métodos sejam executados é só descomentar a linha correspondente.
