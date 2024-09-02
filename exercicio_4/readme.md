```markdown
# README

Desafio Técnico :: Analista de Dados Sênior :: Thaan Costa

## 1. Gerenciamento de Exceções em Python

Gerenciar exceções em Python é crucial para garantir que seu código se comporte de maneira previsível, mesmo quando ocorrem erros inesperados. Você pode usar `try` e `except` para capturar exceções.

```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")
```

O código acima captura o erro de divisão por zero e imprime uma mensagem de erro, sem interromper a execução do programa. Use `finally` para garantir que algum código seja executado, independentemente de uma exceção ocorrer ou não.

## 2. Função vs. Método em Python

- **Função**: Um bloco de código independente que realiza uma tarefa específica e pode ser chamado em qualquer lugar do código.

```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

- **Método**: Uma função associada a um objeto e chamada em um contexto de objeto. Métodos são definidos dentro de uma classe.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def saudacao(self):
        return f"Olá, {self.nome}!"
```

## 3. Automatizando Tarefas em Ambiente Linux

Para fazer backup diário de um diretório importante para um servidor remoto, você pode usar um script Bash e configurar um cron job:

```bash
#!/bin/bash
tar -czf /backup/$(date +%Y%m%d)_backup.tar.gz /diretorio/importante
scp /backup/$(date +%Y%m%d)_backup.tar.gz user@remote:/backup/
```

Adicione o script ao cron job para execução automática:

```
0 2 * * * /caminho/do/script/backup.sh
```

## 4. Lidando com Dados Ausentes em um DataFrame do Pandas

Para lidar com dados ausentes, você pode:

- Remover linhas ou colunas com dados ausentes:

```python
df.dropna()        # Remove linhas com qualquer valor vazio
df.dropna(axis=1)  # Remove colunas com qualquer valor vazio
```

- Preencher valores ausentes com um valor específico ou a média:

```python
df.fillna(0)            # Preenche valores ausentes com 0
df.fillna(df.mean())    # Preenche valores ausentes com a média da coluna
```

- Interpolação:

```python
df.interpolate()       # Preenche valores ausentes usando interpolação
```

## 5. Diferença Entre API RESTful e API SOAP

- **RESTful**: Estilo arquitetônico que utiliza métodos HTTP (GET, POST, PUT, DELETE) e geralmente retorna dados no formato JSON ou XML. É mais leve e ideal para a web moderna.

- **SOAP**: Protocolo baseado em XML que usa HTTP ou SMTP para transporte. É mais pesado e complexo, com recursos adicionais como segurança e transações. Comum em ambientes corporativos.

## 6. Autenticando Solicitações de API em Python

A autenticação pode ser feita de várias maneiras:

- **Autenticação básica**:

```python
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.example.com/data', auth=HTTPBasicAuth('username', 'password'))
```

- **Token Bearer**:

```python
headers = {'Authorization': 'Bearer your_token_here'}
response = requests.get('https://api.example.com/data', headers=headers)
```

## 7. Conflito de Merge em Git e Reversão de Commit

- **Conflito de Merge**: Ocorre quando Git não consegue unir alterações automaticamente. Resolva usando uma ferramenta de merge ou editando manualmente os arquivos conflitantes.

```bash
git add arquivo_conflitado
git commit
```

- **Reverter um Commit**:

```bash
git revert <commit_hash>
```

Cria um novo commit que desfaz as alterações do commit especificado.

## 8. Diferença Entre Banco de Dados SQL e NoSQL

- **SQL**: Relacional, usa tabelas e esquema fixo. Ideal para dados estruturados e relacionamentos complexos. Exemplos: MySQL, PostgreSQL.

- **NoSQL**: Não relacional, pode ser document-oriented, key-value, column-family ou graph-based. Ideal para dados não estruturados ou semi-estruturados e escalabilidade horizontal. Exemplos: MongoDB, Redis.

## 9. Técnicas Comuns de Debugging em Python

- **Print Statements**: Adicione print em diferentes pontos para verificar valores.

- **PDB (Python Debugger)**: Use `import pdb; pdb.set_trace()` para criar um ponto de interrupção e inspecionar o estado do programa.

- **Logging**: Use o módulo logging para registrar mensagens e estados.

- **IDEs**: Use recursos de depuração integrados em IDEs como PyCharm ou VSCode.

## 10. Importância da Documentação de Código

Documentar o código é importante para que outros desenvolvedores possam entender o propósito e o funcionamento do código. Elementos-chave incluem:

- Descrição do que o código faz.
- Como usar o código (exemplos de uso).
- Explicação de funções e métodos.
- Notas sobre lógica complexa ou decisões de design.
- Informações sobre configuração e execução.

## 11. Usando Docker em um Ambiente de Desenvolvimento

No desenvolvimento, Docker cria ambientes isolados e reproduzíveis para suas aplicações. Use um Dockerfile para definir a configuração do ambiente e um docker-compose.yml para definir e orquestrar múltiplos contêineres.

## 12. Considerações ao Desenvolver Aplicações Multiplataforma

- **Portabilidade**: Use tecnologias e bibliotecas compatíveis com múltiplas plataformas.
- **Dependências**: Gerencie dependências de forma que sejam facilmente instaláveis em diferentes sistemas.
- **Testes**: Teste a aplicação em todas as plataformas alvo.
- **Ambientes**: Utilize contêineres (como Docker) para garantir consistência entre ambientes.

## 13. Escrevendo Testes Unitários em Python e Ciclo Básico de TDD

Para escrever um teste unitário:

```python
import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positiva(self):
        self.assertEqual(soma(1, 2), 3)
    
    def test_soma_negativa(self):
        self.assertEqual(soma(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

**Ciclo Básico de TDD**:

- **Red**: Escreva um teste que falhe porque o código ainda não existe.
- **Green**: Escreva o código necessário para passar o teste.
- **Refactor**: Melhore o código sem alterar sua funcionalidade, mantendo os testes verdes.

## 14. Diferenças na Configuração de Servidores Linux e Windows

- **Interface de Configuração**: Linux usa linha de comando e arquivos de configuração; Windows usa GUI e ferramentas como PowerShell.
- **Gerenciamento de Pacotes**: Linux usa apt ou yum; Windows usa instaladores executáveis ou Windows Package Manager.
- **Segurança**: Linux é mais configurável em termos de permissões e segurança por padrão; Windows pode ter mais configurações padrão que requerem ajustes para segurança avançada.

## 15. Diferença Entre Django e Flask

- **Django**: Framework completo "baterias incluídas" que oferece muitos recursos integrados. Ideal para projetos grandes e complexos.

- **Flask**: Micro-framework minimalista que oferece flexibilidade e controle, ideal para projetos menores ou mais simples.

```