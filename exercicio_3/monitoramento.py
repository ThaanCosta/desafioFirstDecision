import os
import subprocess
import psutil
import shutil
import platform
from datetime import datetime

# Função para verificar status dos serviços
def check_services():
    if platform.system() == 'Windows':
        services = ['Apache2.4', 'MySQL56', 'W3SVC']  # Atualize com os nomes corretos
        for service in services:
            try:
                status = subprocess.check_output(['sc', 'query', service]).decode()
                if 'RUNNING' in status:
                    print(f"{service} está em execução.")
                else:
                    print(f"{service} não está em execução.")
            except subprocess.CalledProcessError:
                print(f"Erro ao verificar o status do serviço {service}.")
    else:  # Linux
        services = ['apache2', 'mysql']
        for service in services:
            status = subprocess.call(['systemctl', 'is-active', '--quiet', service])
            if status == 0:
                print(f"{service} está em execução.")
            else:
                print(f"{service} não está em execução.")

# Função para realizar backups
def backup_files():
    backup_dir = 'C:/path/to/backup'  # Atualize com o caminho real
    important_files = ['C:/path/to/file1', 'C:/path/to/file2']  # Atualize com o caminho real
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    for file in important_files:
        if os.path.exists(file):
            shutil.copy(file, backup_dir)
            print(f"Backup de {file} realizado com sucesso.")
        else:
            print(f"Arquivo {file} não encontrado.")

# Função para monitorar uso de recursos
def monitor_resources():
    print(f"Uso de CPU: {psutil.cpu_percent()}%")
    print(f"Uso de memória: {psutil.virtual_memory().percent}%")
    print(f"Espaço em disco: {psutil.disk_usage('/').percent}%")

# Função para verificar e instalar atualizações de segurança
def check_updates():
    if platform.system() == 'Windows':
        subprocess.call(['powershell', '-Command', 'winget upgrade --all'])
    else:  # Linux
        subprocess.call(['sudo', 'apt-get', 'update'])
        subprocess.call(['sudo', 'apt-get', 'upgrade', '-y'])

# Função para gerar relatórios periódicos
def generate_report():
    report_path = 'C:/path/to/report.txt'  # Atualize com o caminho real
    with open(report_path, 'w') as report_file:
        report_file.write(f"Relatório Gerado em: {datetime.now()}\n")
        report_file.write(f"Uso de CPU: {psutil.cpu_percent()}%\n")
        report_file.write(f"Uso de memória: {psutil.virtual_memory().percent}%\n")
        report_file.write(f"Espaço em disco: {psutil.disk_usage('/').percent}%\n")
        report_file.write("Verificação de serviços:\n")
        if platform.system() == 'Windows':
            services = ['Apache2.4', 'MySQL56', 'W3SVC']  # Atualize com os nomes corretos
            for service in services:
                try:
                    status = subprocess.check_output(['sc', 'query', service]).decode()
                    report_file.write(f"{service}: {'RUNNING' if 'RUNNING' in status else 'NOT RUNNING'}\n")
                except subprocess.CalledProcessError:
                    report_file.write(f"{service}: ERRO AO VERIFICAR STATUS\n")
        else:  # Linux
            services = ['apache2', 'mysql']
            for service in services:
                status = subprocess.call(['systemctl', 'is-active', '--quiet', service])
                report_file.write(f"{service}: {'RUNNING' if status == 0 else 'NOT RUNNING'}\n")

