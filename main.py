import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
from datetime import datetime

def conectar_banco():
    
    conn = sqlite3.connect("inteligencia_obras_peri.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS potenciais_obras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            link TEXT,
            data_extracao TEXT
        )
    ''')
    conn.commit()
    return conn

def buscar_novas_obras():
    
    print("Iniciando varredura por novas obras...")
    
    
    url = "https://news.google.com/rss/search?q=construção+civil+grandes+obras+infraestrutura&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    resposta = requests.get(url, headers=headers)
    sopa = BeautifulSoup(resposta.content, "xml") 
    
    obras_encontradas = []
    
    for item in sopa.find_all("item")[:15]:
        titulo = item.title.text
        link = item.link.text
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        obras_encontradas.append((titulo, link, data_atual))
        
    print(f"{len(obras_encontradas)} potenciais obras encontradas.")
    return obras_encontradas


def salvar_dados(obras):
    
    conn = conectar_banco()
    cursor = conn.cursor()
    
    cursor.executemany('''
        INSERT INTO potenciais_obras (titulo, link, data_extracao)
        VALUES (?, ?, ?)
    ''', obras)
    
    conn.commit()
    print("Dados salvos no banco de dados SQL com sucesso!")
    df = pd.read_sql_query("SELECT * FROM potenciais_obras", conn)
    df.to_csv("dados_para_powerbi.csv", index=False, encoding='utf-8')
    print("Arquivo 'dados_para_powerbi.csv' gerado para leitura no Power BI.")
    
    conn.close()

if __name__ == "__main__":
    print("--- Robô de Inteligência de Mercado B2B ---")
    dados = buscar_novas_obras()
    salvar_dados(dados)
    print("--- Processo Finalizado ---")