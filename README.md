# To-Do List Application

Esta é uma aplicação simples de lista de tarefas (to-do list) escrita em Flask e dockerizada usando Docker e Docker Compose.

## Estrutura do Projeto

- `app/`: Contém o código da aplicação Flask.
- `Dockerfile`: Arquivo de configuração do Docker para construir a imagem da aplicação Flask.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose para definir os serviços.
- `README.md`: Documentação do projeto.

## Construção e Execução

1. **Construa a imagem Docker e inicie os contêineres:**

   ```bash
   docker-compose up --build
