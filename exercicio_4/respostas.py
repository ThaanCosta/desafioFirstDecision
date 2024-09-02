# 1. Como você gerenciaria exceções em um script Python?
# 
# Gerenciar exceções em Python é crucial para garantir que seu código se comporte de maneira previsível, 
# mesmo quando ocorrem erros inesperados. Você pode usar `try` e `except` para capturar exceções.
#
# Isso captura o erro de divisão por zero e imprime uma mensagem de erro, sem interromper a execução do programa. 
# Além disso, você pode usar `finally` para garantir que algum código seja executado, 
# independentemente de uma exceção ocorrer ou não.


try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")

# 2. Explique a diferença entre uma função e um método em Python.
# Uma função é um bloco de código independente que realiza uma 
# tarefa específica e pode ser chamado em qualquer lugar do código.

def saudacao(nome):
    return f"Olá, {nome}!"

# Um método, por outro lado, é uma função que está associada a um objeto e 
# é chamada em um contexto de objeto. Métodos são definidos dentro de uma classe.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def saudacao(self):
        return f"Olá, {self.nome}!"

