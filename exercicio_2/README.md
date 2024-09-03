# Lista de Compras - Flask App

Este projeto é uma aplicação web simples escrita em Python usando o framework Flask. A aplicação simula uma lista de compras, permitindo visualizar os itens, adicionar novos itens e remover itens existentes. 

## Estrutura do Projeto

- `app.py`: Contém a lógica principal da aplicação Flask.
- `Dockerfile`: Define a imagem Docker personalizada para a aplicação.
- `docker-compose.yml`: Utilizado para definir e gerenciar os serviços necessários para a aplicação.
- `requirements.txt`: Lista as dependências Python necessárias para a aplicação.

## Endpoints da API

A aplicação possui os seguintes endpoints:

- **GET** `/listadecompras`:
  - Retorna a lista completa de itens de compras.
  
- **POST** `/listadecompras`:
  - Adiciona um novo item à lista de compras. O corpo da requisição deve ser um JSON no formato: 
    ```json
    {
      "id": 6,
      "Item": "Novo Item"
    }
    ```
  
- **DELETE** `/listadecompras/<int:id>`:
  - Remove um item da lista de compras pelo seu `id`.

## Como Rodar a Aplicação

### Requisitos

- Docker e Docker Compose instalados na sua máquina.

### Passos

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/lista-de-compras.git
   cd lista-de-compras
