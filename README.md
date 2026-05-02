# Inteligência de Mercado B2B - Bot de Captação de Obras

## O Desafio
Empresas fornecedoras da construção civil (como locação de formas e escoramentos) precisam mapear constantemente o mercado em busca de novas grandes obras, licitações e projetos de infraestrutura. Fazer essa busca manualmente demanda muito tempo operacional.

## A Solução
Desenvolvi um pipeline de dados automatizado em **Python** que:
1. Faz varredura web (Scraping) em busca de notícias e editais de grandes obras de infraestrutura.
2. Extrai, trata e padroniza as informações relevantes.
3. Armazena os dados em um banco de dados relacional (**SQL**).
4. Exporta a base automaticamente para um **Dashboard Gerencial no Power BI**.

## Tecnologias Utilizadas
* **Linguagem:** Python (Bibliotecas: `requests`, `BeautifulSoup`, `pandas`)
* **Banco de Dados:** SQLite (Linguagem SQL para inserção e extração)
* **Visualização:** Power BI

## Visualização
[Dashboard PERI](Dashboard.png)

## Como executar
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o script principal: `python main.py`
4. Abra o arquivo `dados_para_powerbi.csv` em seu software de visualização favorito.
