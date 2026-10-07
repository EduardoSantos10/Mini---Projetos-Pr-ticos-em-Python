# BLOCO 01: ENTRADA E BASE DE DADOS (TELEMETRIA DA TRANSAÇÃO)

# CRIANDO UM DICIONÁRIO ANINHADO:
conta_banco = {
    "titular": "Eduardo Silva",
    "pin": "2468",
    "saldo": 2000.00,
    "tentativas_falhas": 2,
    "bloqueado": False
}

pin_digitado = input("Insira o PIN de 4 dígitos: ")

valor_saque = float(input("Informe o valor do saque em retirada R$:"))


# BLOCO 02: REGRAS DE NEGÓCIO E CONSTANTES DE SEGURANÇA
MAX_TENTATIVAS = 3

LIMITE_SAQUE_DIARIO = 3000.00

status_transação = ""
mensagem_resposta = ""


# BLOCO 03: MOTOR DE DECISÃO (LÓGICA DE AUTENTICAÇÃO E TRANSAÇÃO)
# 1. Trava de Segurança: Verificação de Lockout
if conta_banco["bloqueado"]:
    status_transação = "NEGADA"
    mensagem_resposta = "Conta bloqueada por segurança! Procure sua agência"

# 2. Avaliação de Credencial (PIN)    
elif pin_digitado == conta_banco["pin"]:
    conta_banco["tentativas_falhas"] = 0
    
# 3. Regras de Negócio Financeiras
    if valor_saque > LIMITE_SAQUE_DIARIO:
        status_transacao = "NEGADA"
        mensagem_resposta = f"Limite máximo por operação excedido (Máx: R$ {LIMITE_SAQUE_DIARIO:.2f})."
    elif valor_saque > conta_banco["saldo"]:
        status_transacao = "NEGADA"
        mensagem_resposta = "Saldo insuficiente para realizar a transação."
    else:
        status_transacao = "APROVADA"
        conta_banco["saldo"] -= valor_saque
        mensagem_resposta = "Saque efetuado com sucesso. Retire o dinheiro no local indicado."

# 4. Tratamento de Credencial Incorreta e Política de Lockout
else:
    status_transacao = "NEGADA"
    conta_banco["tentativas_falhas"] += 1
    
    if conta_banco["tentativas_falhas"] >= MAX_TENTATIVAS:
        conta_banco["bloqueado"] = True
        mensagem_resposta = "PIN incorreto. Limite de tentativas excedido: CONTA BLOQUEADA!"
    else:
        tentativas_restantes = MAX_TENTATIVAS - conta_banco["tentativas_falhas"]
        mensagem_resposta = f"PIN incorreto. Você ainda tem {tentativas_restantes} tentativa(s) antes do bloqueio."

# BLOCO 04: PAINEL DE APRESENTAÇÃO E COMPROVANTE (ATM OUTPUT)
print(f"Titular da Conta   : {conta_banco['titular']}")
print(f"Status da Operação : {status_transacao}")
print(f"Mensagem do Sistema: {mensagem_resposta}")
print(f"Saldo Atualizado   : R$ {conta_banco['saldo']:.2f}")
print(f"Estado da Conta    : {'BLOQUEADA' if conta_banco['bloqueado'] else 'ATIVA'}")