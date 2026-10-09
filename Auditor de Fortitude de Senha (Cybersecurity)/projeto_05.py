# BLOCO 01: ENTRADAS E TELEMETRIA (ENTRADAS A SER AUDITADA)
senha_avaliada = input("Informe a sua senha: ")

# BLOCO 02: REGRAS DE NEGÓCIO E POLÍTICAS CORPORATIVA DE SENHAS
TAMANHO_MINIMO = 8

# VARIAVEIS DE CONTROLE E PONTUAÇÃO DE CRITÉRIO
possui_tamanho = False
possui_maiuscula = False
possui_minuscula = False
score_pontuacao = 0
classificacao_forca = ""
requisitos_faltantes = ""


# BLOCO 03: MOTOR DE DECISÃO (AUDITORIA ESTÁTICA DE SEGURANÇA)
if len(senha_avaliada) >= TAMANHO_MINIMO:
    possui_tamanho = True
    score_pontuacao += 1
else:
    requisitos_faltantes += "[Mínimo de 8 caracteres] "
    
if senha_avaliada != senha_avaliada.lower():
    possui_maiuscula = True
    score_pontuacao += 1
else:
    requisitos_faltantes += "[Ao menos 1 letra maiúscula] "

if senha_avaliada != senha_avaliada.upper():
    possui_minuscula = True
    score_pontuacao += 1
else:
    requisitos_faltantes += "[Ao menos 1 letra minuscula] "
    
if score_pontuacao == 3:
    classificacao_forca = "FORTE - Conforme com a política de segurança"

elif score_pontuacao == 2:
    classificacao_forca = "MÉDIA - (Atende parcialmente)"
    
else:
    classificacao_forca = "FRACA - Insegura / Não conforme"
    
    
# BLOCO 04: PAINEL DE APRESENTAÇÃO E RELATÓRIO DE AUDITORIA (SECUTIRY OUTPUT)
# Mascaramento de segurança para não expor a senha em tela
senha_mascarada = "*" * len(senha_avaliada)

print(f" Senha Avaliada (Masked) : {senha_mascarada} ({len(senha_avaliada)} chars)")
print(f" [✓] Tamanho Mínimo (>=8): {possui_tamanho}")
print(f" [✓] Letra Maiúscula     : {possui_maiuscula}")
print(f" [✓] Letra Minúscula     : {possui_minuscula}")
print(f" Score de Segurança      : {score_pontuacao} / 3")
print(f" Classificação Final     : {classificacao_forca}")
print(f" Pendências Encontradas  : {requisitos_faltantes}")
