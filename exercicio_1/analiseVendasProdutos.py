import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

def criar_dados_sinteticos(dir_path):
    """Gera dados sintéticos de vendas e os salva em arquivos CSV."""
    os.makedirs(dir_path, exist_ok=True)

    regioes = ['Norte', 'Sul', 'Sudeste', 'Nordeste', 'Centro-Oeste']
    produtos = ['Produto_A', 'Produto_B', 'Produto_C', 'Produto_D', 'Produto_E']
    data = []

    for regiao in regioes:
        for produto in produtos:
            num_registros = np.random.randint(1000, 5000)
            data.extend([
                {'Regiao': regiao, 'Produto': produto, 'Vendas': np.random.randint(1, 5000)}
                for _ in range(num_registros)
            ])

    df_sintetico = pd.DataFrame(data)
    num_arquivos = 4
    chunk_size = len(df_sintetico) // num_arquivos

    for i in range(num_arquivos):
        start_idx = i * chunk_size
        end_idx = None if i == num_arquivos - 1 else (i + 1) * chunk_size
        df_sintetico.iloc[start_idx:end_idx].to_csv(f'{dir_path}/vendas_{i+1}.csv', index=False)
    
    print(f'Dados sintéticos gerados e salvos com sucesso em {dir_path}.')

def combinar_csv(directory):
    """Combina todos os arquivos CSV em um diretório em um único DataFrame."""
    all_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]
    df_combined = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
    print(f'Todos os arquivos CSV combinados com sucesso.')
    return df_combined

def analisar_dados(df):
    """Realiza análise dos dados e retorna os resultados."""
    vendas_por_regiao = df.groupby('Regiao')['Vendas'].sum().reset_index()
    produtos_mais_vendidos = df.groupby('Produto')['Vendas'].sum().reset_index().sort_values(by='Vendas', ascending=False)
    return vendas_por_regiao, produtos_mais_vendidos

def plotar_resultados(vendas_por_regiao, produtos_mais_vendidos):
    """Cria gráficos dos resultados da análise."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Regiao', y='Vendas', data=vendas_por_regiao)
    plt.title('Total de Vendas por Região')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Produto', y='Vendas', data=produtos_mais_vendidos)
    plt.title('Produtos Mais Vendidos')
    plt.show()

def exportar_resultados(vendas_por_regiao, produtos_mais_vendidos, dir_destino):
    """Exporta os resultados da análise para arquivos CSV no diretório especificado."""
    os.makedirs(dir_destino, exist_ok=True)
    vendas_por_regiao.to_csv(f'{dir_destino}/total_vendas_por_regiao.csv', index=False)
    produtos_mais_vendidos.to_csv(f'{dir_destino}/produtos_mais_vendidos.csv', index=False)
    print(f'Resultados exportados com sucesso para {dir_destino}.')

if __name__ == '__main__':
    dir_path = 'dados_vendas'
    dir_destino = 'resultados_analise'

    criar_dados_sinteticos(dir_path)
    df_vendas = combinar_csv(dir_path)
    vendas_por_regiao, produtos_mais_vendidos = analisar_dados(df_vendas)
    plotar_resultados(vendas_por_regiao, produtos_mais_vendidos)
    exportar_resultados(vendas_por_regiao, produtos_mais_vendidos, dir_destino)
