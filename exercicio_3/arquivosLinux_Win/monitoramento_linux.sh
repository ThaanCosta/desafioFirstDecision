#!/bin/bash

# Função para verificar o status dos serviços principais
verificar_servicos() {
    echo "Verificando status dos serviços..."
    for servico in apache2 mysql; do
        systemctl is-active --quiet $servico && echo "$servico está ativo" || echo "$servico está inativo"
    done
}

# Função para realizar backups dos arquivos importantes
backup() {
    echo "Realizando backup dos arquivos importantes..."
    tar -czf /backup/backup_$(date +%F).tar.gz /diretorio/para/backup
}

# Função para monitorar o uso de recursos
monitorar_recursos() {
    echo "Monitorando uso de recursos..."
    echo "Uso de CPU:"
    top -bn1 | grep "Cpu(s)"
    echo "Uso de memória:"
    free -h
    echo "Espaço em disco:"
    df -h
}

# Função para verificar e instalar atualizações de segurança
atualizar_sistema() {
    echo "Verificando e instalando atualizações de segurança..."
    apt-get update
    apt-get upgrade -y
}

# Função para gerar relatórios periódicos
gerar_relatorio() {
    echo "Gerando relatório..."
    echo "Status dos serviços:" > /var/log/relatorio_$(date +%F).log
    verificar_servicos >> /var/log/relatorio_$(date +%F).log
    echo "" >> /var/log/relatorio_$(date +%F).log
    echo "Uso de recursos:" >> /var/log/relatorio_$(date +%F).log
    monitorar_recursos >> /var/log/relatorio_$(date +%F).log
}

# Executar as funções
verificar_servicos
backup
monitorar_recursos
atualizar_sistema
gerar_relatorio
