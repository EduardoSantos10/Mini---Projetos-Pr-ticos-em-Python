# BLOCO 01: ENTRADAS E TELEMETRIA (DADOS DO TICKET)
id_chamado = input("Informe o código identificador do chamado: ")

categoria = input("Informe o tipo do problema: ").upper()

impacto = int(input("Informe o nível do impacto (1 a 3): "))

urgencia = int(input("Qual o nivel de urgência (1/3): "))


# BLOCO 02: REGRAS DE NEGÓCIO E TABELA DE SLA
prioridade = ""

sla_horas = 0

equipe_destino = ""

status_sla = "DENTRO_DO_PADRAO"


# BLOCO 03: MOTOR DE DECISÃO (MATRIZ ITIL & ROTEAMENTO)
if impacto == 1 and urgencia == 1:
    prioridade = ("P1 - CRÍTICA")
    sla_horas = 2

elif impacto == 1 or urgencia == 1:
    prioridade = ("P2 - ALTA")
    sla_horas = 4
    
elif impacto == 2 and urgencia == 2:
    prioridade = ("P3 - MÉDIA")
    sla_horas = 8
    
else:
    prioridade = ("P4 - BAIXA")
    sla_horas = 24
    

# ROTEAMENTE DE EQUIPE (N1 vs N2):
if categoria == "SENHA" or prioridade == "P4 - BAIXA":
    equipe_destino = "N1 - Service Desk"

else:
    equipe_destino = "N2 - Suporte Especializado"
    
    
# BLOCO 04:  PAINEL DE APRESENTAÇÃO E DIAGNÓSTICO (TICKET CARD)

print(f"ID do Chamado   : {id_chamado}")
print(f"Categoria       : {categoria}")
print(f"Impacto / Urg   : Nível {impacto} / Nível {urgencia}")
print(f"Prioridade ITIL : {prioridade}")
print(f"SLA Resolução   : {sla_horas} Horas")
print(f"Fila / Equipe   : {equipe_destino}")
print(f"Status SLA      : {status_sla}")