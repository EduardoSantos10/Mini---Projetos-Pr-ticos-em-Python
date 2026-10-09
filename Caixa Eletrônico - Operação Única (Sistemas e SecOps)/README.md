# 🏦 Projeto 03: Caixa Eletrônico - Operação Única (SecOps & Sistemas)

> Módulo de autorização transacional e controle de estado para caixas eletrônicos (ATM) aplicando políticas de lockout de segurança (prevenção a força bruta) e validações financeiras.

---

## 📌 Visão Geral do Projeto

Em sistemas de missão crítica, como caixas eletrônicos e gateways de pagamento, a validação de uma operação financeira depende do **estado atual da conta** e do cumprimento rigoroso de **travas de segurança em hierarquia**.

Este projeto implementa o motor de decisão em Python para autorização de saque em operação única. O script manipula um diretório de identidades em memória (dicionário aninhado), valida credenciais (PIN), gerencia o número de tentativas falhas consecutivas e aciona o **bloqueio preventivo da conta (lockout)** caso o limite de erros seja atingido.

---

## 🎯 Fundamentos de TI & SecOps Aplicados

* **Gerenciamento de Estado em Memória:** Uso de estruturas de dados do tipo dicionário (`dict`) para armazenar e alterar estados em tempo de execução (`saldo`, `tentativas_falhas`, `bloqueado`).
* **Política de Lockout de Segurança (Account Lockout):** Mecanismo de defesa contra ataques de força bruta (*Brute Force*) que congela o acesso à conta após um número fixo de falhas consecutivas de autenticação.
* **Hierarquia de Decisão e Defesa em Profundidade:**
  1. **1ª Linha de Defesa:** Checagem de lockout ativo (`bloqueado == True`).
  2. **2ª Linha de Defesa:** Validação de credencial de acesso (PIN).
  3. **3ª Linha de Defesa:** Regras de negócio financeiras (limite por operação e saldo disponível).
* **Defesa contra Enumeração de Usuários (*User Enumeration*):** Padronização de respostas do sistema para evitar a exposição de informações sensíveis a potenciais atacantes.

---

## 🏗️ Arquitetura em 4 Blocos

O script segue a arquitetura em 4 blocos de processamento sequencial e defensivo:

```text
┌────────────────────────────────────────────────────────┐
│  Bloco 01: Entradas & Base de Dados (Telemetria)       │
│  - Leitura do PIN digitado e valor do saque            │
│  - Leitura da conta em dicionário aninhado (dict)      │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 02: Regras de Negócio & Constantes de SecOps    │
│  - Limite de tentativas (MAX_TENTATIVAS = 3)           │
│  - Teto máximo por saque (LIMITE_SAQUE_DIARIO = 3000)  │
│  - Inicialização de registradores de resposta          │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 03: Motor de Decisão (Hierarquia de Segurança)  │
│  - Teste de trava de lockout                           │
│  - Validação de PIN e gestão de contador de erros      │
│  - Liberação do saque e atualização do saldo           │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 04: Comprovante de Operação (ATM Output)        │
│  - Emissão do comprovante e estado final da conta      │
└────────────────────────────────────────────────────────┘


---

## 💻 Projetos do Laboratório

| # | Projeto | Domínio de TI | Conceitos Aplicados em Python | Status |
|:-:|:---|:---|:---|:-:|
| **01** | **Calculadora de Sub-rede e IP** | Redes / Infraestrutura | Parsing de IP (`.split()`), Cálculo CIDR, RFC 1918, Condicionais | ✅ Concluído |
| **02** | **Gestor de Chamados & SLA N1/N2** | ITSM / Suporte N2 | Triagem de tickets, Priorização ITIL, Matriz Impacto x Urgência | ✅ Concluído |
| **03** | **Caixa Eletrônico & Lockout de PIN** | SecOps / Sistemas | Controle de estado, Limite de tentativas, Trava de Segurança | ✅ Concluído |
| **04** | **Monitor de Saúde de Servidores** | SysAdmin / SRE | Avaliação de métricas de CPU/RAM, Classificação de Alertas | 🔄 Em Breve |
| **05** | **Auditor de Fortitude de Senhas** | Cybersecurity | Análise estática de strings, Validação de políticas de acesso | 🔄 Em Breve |





























