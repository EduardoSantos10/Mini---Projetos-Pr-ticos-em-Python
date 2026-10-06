# 🎟️ Projeto 02: Triagem de Chamados e SLA N1/N2 (ITSM / ITIL)

> Módulo de Automação e Roteamento de Tickets de Suporte aplicando Governança ITIL, Matriz de Prioridade e Acordo de Nível de Serviço (SLA).

---

## 📌 Visão Geral do Projeto

Na gestão de serviços de TI (ITSM - *IT Service Management*), o atendimento de suporte não opera por ordem de chegada simples, mas por **matriz de criticidade do negócio**. Este projeto simula o motor de decisão de ferramentas corporativas de ITSM (como ServiceNow, Jira Service Management ou Zendesk).

O script em Python recebe os dados de telemetria de um incidente (categoria, impacto e urgência) e realiza a triagem automática para determinar a **prioridade ITIL**, o **SLA contratual de resolução** e o **escalonamento para a fila adequada (N1 vs N2)**.

---

## 🎯 Fundamentos de TI & Governança Aplicados

* **ITIL v4 (Information Technology Infrastructure Library):** Aplicação prática dos conceitos de Gestão de Incidentes e Classificação de Serviços.
* **Matriz de Priorização (Impacto x Urgência):**
  * **Impacto:** Abrangência do problema no negócio (afeta 1 usuário, um setor ou a empresa inteira).
  * **Urgência:** Velocidade necessária para a solução (trabalho totalmente parado vs contornável).
* **Escalonamento N1/N2:**
  * **N1 (Service Desk / First-Line):** Resolução de solicitações padrão, resetting de credenciais e dúvidas de baixa complexidade.
  * **N2 (Suporte Especializado / Field):** Tratamento de falhas de infraestrutura, indisponibilidade de sistemas e incidentes de alta prioridade.

---

## 🏗️ Arquitetura em 4 Blocos

O script segue estritamente a arquitetura defensiva em 4 blocos de processamento sequencial:

┌────────────────────────────────────────────────────────┐
│  Bloco 01: Entradas & Telemetria                       │
│  - Leitura do ID, Categoria, Nível de Impacto e Urgência│
│  - Sanitização de strings (.upper())                   │
└───────────────────────────┬────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────┐
│  Bloco 02: Regras de Negócio & Tabela de SLA           │
│  - Inicialização de variáveis de estado                │
│  - Definição dos parâmetros contratuais de resposta    │
└───────────────────────────┬────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────┐
│  Bloco 03: Motor de Decisão (Matriz ITIL & Roteamento) │
│  - Cálculo de Prioridade (P1 Crítica a P4 Baixa)       │
│  - Atribuição de SLA em horas (2h, 4h, 8h ou 24h)      │
│  - Regra de Escalonamento de Fila (N1 vs N2)          │
└───────────────────────────┬────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────┐
│  Bloco 04: Painel de Apresentação (Ticket Card)        │
│  - Exibição formatada do relatório de triagem no terminal│
└────────────────────────────────────────────────────────┘

Plaintext
==================================================
             FICHA DE ROTEAMENTO ITSM
==================================================
ID do Chamado   : INC-8821
Categoria       : INFRA
Impacto / Urg   : Nível 1 / Nível 1
Prioridade ITIL : P1 - CRÍTICA
SLA Resolução   : 2 Horas
Fila / Equipe   : N2 - Suporte Especializado
Status SLA      : DENTRO_DO_PADRAO
==================================================

---

🛠️ Aprendizados Principais de Programação:

Atribuição de Estado: Atribuir valores a variáveis internas (prioridade, sla_horas) em vez de realizar apenas impressões de tela com print().

Tratamento de Strings (.upper()): Padronização de entradas de texto para evitar inconsistências (case sensitivity).

Tomada de Decisão Multicritério: Combinação dos operadores lógicos and e or para implementar a matriz de prioridade de negócio.

---

## 💻 Projetos do Laboratório

| # | Projeto | Domínio de TI | Conceitos Aplicados em Python | Status |
|:-:|:---|:---|:---|:-:|
| **01** | **Calculadora de Sub-rede e IP** | Redes / Infraestrutura | Parsing de IP (`.split()`), Cálculo CIDR, RFC 1918, Condicionais | ✅ Concluído |
| **02** | **Gestor de Chamados & SLA N1/N2** | ITSM / Suporte N2 | Triagem de tickets, Priorização ITIL, Matriz Impacto x Urgência | ✅ Concluído |
| **03** | **Caixa Eletrônico & Lockout de PIN** | SecOps / Sistemas | Controle de estado, Limite de tentativas, Trava de Segurança | 🔄 Em Breve |
| **04** | **Monitor de Saúde de Servidores** | SysAdmin / SRE | Avaliação de métricas de CPU/RAM, Classificação de Alertas | 🔄 Em Breve |
| **05** | **Auditor de Fortitude de Senhas** | Cybersecurity | Análise estática de strings, Validação de políticas de acesso | 🔄 Em Breve |

---

---

## 🔗 Repositório e Links

* **📂 Repositório do Projeto no GitHub:** [github.com/seu-usuario/ti-python-lab](https://github.com/seu-usuario/ti-python-lab)
* **👤 Perfil do Desenvolvedor:** [github.com/seu-usuario](https://github.com/seu-usuario)
* **✉️ Contato / Feedback:** Sinta-se à vontade para abrir uma *Issue* ou enviar sugestões de melhoria!