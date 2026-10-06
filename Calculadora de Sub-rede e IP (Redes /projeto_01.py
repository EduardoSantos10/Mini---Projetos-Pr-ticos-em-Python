# BLOCO 01: ENTRADAS E TELEMETRIA (VÁRIAVEIS DE PACOTE)
ip_destino = input("Informe o IP completo: ")

cidr = int(input("Informe os bits de rede: "))

primeiro_octeto = int(input("Informe o primeiro octeto: "))

segundo_octeto = int(input("Informe o segundo octeto: "))


# BLOCO 02: REGRAS DE NEGÓCIO E LIMIARES DE REDE

# CONSTANTES
BITS_TOTAL_IPV4 = 32

# VARIAVEIS AUXILIARES PARA ARMAZENAMENTO
classe = ""

tipo_escopo = ""

hosts_validos = 0


# BLOCO 03: MOTOR DE DECISÃO (LÓGICA SEQUENCIAL DE REDES)
if primeiro_octeto <= 127:
    classe = "Classe A"

elif primeiro_octeto <= 191:
    classe = "Classe B"

else:
    classe = "Classe C"

if primeiro_octeto == 10:
    tipo_escopo = "Privado (Rede Local)"

elif primeiro_octeto == 172 and 16 <= segundo_octeto <= 31:
        tipo_escopo = "Privado (Rede Local)"

elif primeiro_octeto == 192 and segundo_octeto == 168:
            tipo_escopo = "Privado (Rede Local)"

else:
    tipo_escopo = "Público (Internet)"


# CÁLCULOS DE HOSTS:
bits_hosts = BITS_TOTAL_IPV4 - cidr

hosts_validos = (2 ** bits_hosts) - 2


# BLOCO 04: PAINEL DE APRESENTAÇÃO E DIAGNÓSTICO (RELATÓRIO)
print(f"O IP análisado foi {ip_destino}")

print(f"O CIDR verificado foi {cidr}")

print(f"A classe correspondente é a {classe}")

print(f"O tipo de escopo seria o {tipo_escopo}")

print(f"A quantidade de hosts válidos foram {hosts_validos}")