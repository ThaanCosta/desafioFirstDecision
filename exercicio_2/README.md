# Nome do Projeto

## Descrição

Uma breve descrição do projeto, explicando o objetivo principal e o que ele faz.

## Estrutura do Projeto

- `app/` - Diretório contendo o código da aplicação.
  - `config.py` - Arquivo de configuração para os bancos de dados.
  - `routes.py` - Arquivo que define as rotas da API Flask.
- `Dockerfile` - Script para construir a imagem Docker da aplicação.
- `docker-compose.yml` - Configuração dos serviços Docker, como a aplicação web e o banco de dados.
- `README.md` - Este arquivo.

## Instalação

### Pré-requisitos

- Docker
- Docker Compose

### Passos

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd seu-repositorio
    ```
3. Construa e inicie os contêineres:
    ```bash
    docker-compose up --build
    ```

## Uso

- Acesse a aplicação Flask em seu navegador através de `http://localhost:5000`.
- Para interagir com a API, utilize as seguintes rotas:
  - `GET /dados_escola` - Retorna todos os registros da tabela `DadosEscola`.
  - `POST /dados_escola` - Adiciona um novo registro.
  - `PUT /dados_escola/<id>` - Atualiza um registro existente.
  - `DELETE /dados_escola/<id>` - Remove um registro.

## Debugging

Para realizar o debug da aplicação Flask dentro do contêiner Docker, siga os passos abaixo:

1. Certifique-se de que a aplicação está rodando em modo de debug.
2. Utilize o seguinte comando para acessar o contêiner:
    ```bash
    docker exec -it seu-conteiner-web /bin/bash
    ```
3. Dentro do contêiner, você pode verificar os logs e executar comandos para inspecionar o comportamento da aplicação.

## Problemas Conhecidos

Liste aqui quaisquer problemas conhecidos ou limitações do projeto.

## Contribuição

Explique como outros desenvolvedores podem contribuir para o projeto. Inclua instruções para abertura de issues, pull requests, etc.

## Licença

Inclua a licença sob a qual o projeto está distribuído. Por exemplo:

```markdown
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
