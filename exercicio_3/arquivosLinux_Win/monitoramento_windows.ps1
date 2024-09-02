# Função para verificar o status dos serviços principais
function Verificar-Servicos {
    Write-Host "Verificando status dos serviços..."
    $servicos = @("w3svc", "MySQL")
    foreach ($servico in $servicos) {
        $status = Get-Service -Name $servico -ErrorAction SilentlyContinue
        if ($status -and $status.Status -eq 'Running') {
            Write-Host "$servico está ativo"
        } else {
            Write-Host "$servico está inativo"
        }
    }
}

# Função para realizar backups dos arquivos importantes
function Backup {
    Write-Host "Realizando backup dos arquivos importantes..."
    $data = Get-Date -Format "yyyy-MM-dd"
    Compress-Archive -Path "C:\diretorio\para\backup\*" -DestinationPath "C:\backup\backup_$data.zip"
}

# Função para monitorar o uso de recursos
function Monitorar-Recurso {
    Write-Host "Monitorando uso de recursos..."
    Write-Host "Uso de CPU:"
    Get-WmiObject -Query "SELECT * FROM Win32_Processor" | ForEach-Object { $_.LoadPercentage }
    Write-Host "Uso de memória:"
    Get-WmiObject -Query "SELECT * FROM Win32_OperatingSystem" | ForEach-Object { $_.FreePhysicalMemory / 1MB }
    Write-Host "Espaço em disco:"
    Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{Name="Used(GB)";Expression={[math]::round($_.Used/1GB,2)}}, @{Name="Free(GB)";Expression={[math]::round($_.Free/1GB,2)}}
}

# Função para verificar e instalar atualizações de segurança
function Atualizar-Sistema {
    Write-Host "Verificando e instalando atualizações de segurança..."
    Install-WindowsUpdate -AcceptAll -AutoReboot
}

# Função para gerar relatórios periódicos
function Gerar-Relatorio {
    Write-Host "Gerando relatório..."
    $data = Get-Date -Format "yyyy-MM-dd"
    $relatorio = "C:\log\relatorio_$data.txt"
    Add-Content $relatorio "Status dos serviços:`n"
    Verificar-Servicos | Out-File -Append -FilePath $relatorio
    Add-Content $relatorio "`nUso de recursos:`n"
    Monitorar-Recurso | Out-File -Append -FilePath $relatorio
}

# Executar as funções
Verificar-Servicos
Backup
Monitorar-Recurso
Atualizar-Sistema
Gerar-Relatorio
