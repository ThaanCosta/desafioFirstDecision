# %%

#importando as bibliotecas a serem usadas nessa 1 etapa
import pandas as pd 
import numpy as np 
import os

# Configurações
dir_path = 'dados_vendas'
os.makedirs(dir_path, exist_ok=True)

# Dados Sintéticos
regioes = ['Norte', 'Sul', 'Sudeste', 'Nordeste', 'Centro-Oeste']
produtos = ['Produto_A', 'Produto_B', 'Produto_C', 'Produto_D', 'Produto_E']

# Quantidade de registros para cada região
quantidade_regioes = {
    'Norte': 10000,
    'Sul': 20000,
    'Sudeste': 30000,
    'Nordeste': 15000,
    'Centro-Oeste': 25000
}

# Quantidade de registros para cada produto
quantidade_por_produto = {
    'Produto_A': 15000,
    'Produto_B': 20000,
    'Produto_C': 5000,
    'Produto_D': 25000,
    'Produto_E': 35000
}

data = []

for region in regioes:
    for product in produtos:
        # Calcular o número de registros para cada combinação de 
        # região e produto
        num_registros = min(
            quantidade_regioes[region] // len(produtos), 
            quantidade_por_produto[product]
        )
        for _ in range(num_registros):
            data.append({
                'Regiao': region,
                'Produto': product,
                'Vendas': np.random.randint(1, 5000)  # Vendas aleatórias entre 1 e 5000
            })

df_sintetico = pd.DataFrame(data)

# Dividindo em múltiplos arquivos CSV
num_chunks = 4
chunk_size = len(df_sintetico) // num_chunks

for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = None if i == num_chunks - 1 else (i + 1) * chunk_size
    df_sintetico.iloc[start_idx:end_idx].to_csv(f'{dir_path}/vendas_{i+1}.csv', index=False)

print(f'Dados gerados e salvos em {dir_path}')


# %%
##
# Agora vamos criar um script para ler todos os arquivos CSV do diretório e combiná-los em um único DataFrame.
# ####

# Leitura e combinação dos arquivos CSV
def combine_csv_files(diretorio):
    arquivos_csv = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith('.csv')]
    df = pd.concat((pd.read_csv(f) for f in arquivos_csv), ignore_index=True)
    return df

# Executa a combinação
df_vendas = combine_csv_files(dir_path)

#Print para retornar o dataframe de vendas e analisar os 5 primeiros registros
print(df_vendas.head())

# %%

# Analise exploratoria dos dados

#Total de vendas por Região
vendas_por_regiao = df_vendas.groupby('Regiao')['Vendas'].sum().reset_index()

#Produtos mais vendidos
produtos_mais_vendidos = df_vendas.groupby('Produto')['Vendas'].sum().reset_index()

print(vendas_por_regiao)
print(produtos_mais_vendidos)