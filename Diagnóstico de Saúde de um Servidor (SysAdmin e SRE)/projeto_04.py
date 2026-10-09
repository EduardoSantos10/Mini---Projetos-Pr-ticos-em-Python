# BLOCO 01: ENTRADAS E TELEMETRIA (MÉTRICAS DO SERVIDOR)
hostname = input("Informe o nome do servidor: ").upper()

cpu_pct = float(input("Qual a porcentagem do uso da CPU: "))

ram_pct = float(input("Qual a porcentagem do uso da memória RAM: "))

disk_pct = float(input("Qual a porcetagem da ocupação do Disco: "))


# BLOCO 02: REGRAS DE NEGÓCIO E LIMIARES DE TOLERÂNCIA (SRE THRESHOLDS)

# CONTANTES

# LIMIARES DE ALERTAS (WARNING):
CPU_WARN = 70.0

RAM_WARN = 75.0

DISK_WARN = 80.0

# LIMIARES CRÍTICOS (CRITICAL):
CPU_CRIT = 85.0

RAM_CRIT = 88.0

DISK_CRIT = 90.0

# VARIAVEIS AUXILIARES DE ESTADO:
status_geral = "OK"

motivos_alerta = ""  # PARA GUARDAR RECURSOS QUAIS RECURSOS ESTÃO ALTERADOS


# BLOCO 03: MOTOR DE DECISÃO (LÓGICA DE AVALIAÇÃO DE MÉTRICAS)


if (cpu_pct >= CPU_CRIT) or (ram_pct >= RAM_CRIT) or (disk_pct >= DISK_CRIT):
    status_geral = "CRITICO"
    
    # Identifica exatamente quem estourou o limite crítico
    if cpu_pct >= CPU_CRIT:
        motivos_alerta += "[CPU em nível crítico]"
    if ram_pct >= RAM_CRIT:
        motivos_alerta += "[RAM em nível crítico]"
    if disk_pct >= DISK_CRIT:
        motivos_alerta += "[Disco em nível crítico]"
    
elif (cpu_pct >= CPU_WARN) or (ram_pct >= RAM_WARN) or (disk_pct >= DISK_WARN):
    status_geral = "ALERTA"
    
    # Identifica exatamente quem entrou em atenção
    if cpu_pct >= CPU_WARN:
        motivos_alerta += "[CPU em nível de alerta] "
    if ram_pct >= RAM_WARN:
        motivos_alerta += "[RAM em nível de alerta] "
    if disk_pct >= DISK_WARN:
        motivos_alerta += "[Disco em nível de alerta] "
    
else:
    status_geral = "OK"
    motivos_alerta = "Todos os recursos operando dentro das faixas nominais."
    
    
# BLOCO 04: PAINEL DE APRESENTAÇÃO E RELATÓRIO DE NOC (HEALTH OUTPUT)
print(f"O nome do servidor é {hostname}")
print(f"A porcetagem de uso da CPU foi de: {cpu_pct}")
print(f"A porcentagem de uso da Memória RAM foi de: {ram_pct}")
print(f"A porcentagem da ocupação de disco foi de: {disk_pct}")
print(f"O estado da avaliação foi de: {status_geral}")
print(f"Diagnostico/Causa {motivos_alerta}")