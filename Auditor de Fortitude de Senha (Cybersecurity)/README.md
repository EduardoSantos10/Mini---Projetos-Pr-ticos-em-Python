# 🔑 Projeto 05: Auditor de Fortitude de Senha (Cybersecurity)

> Módulo de análise estática e auditoria de políticas de credenciais corporativas baseadas nas diretrizes de segurança da informação (NIST / ISO 27001).

---

## 📌 Visão Geral do Projeto

Na Gestão de Identidade e Acesso (IAM - *Identity and Access Management*), a aplicação de políticas rígidas de senhas é a primeira linha de defesa contra ataques de força bruta (*Brute Force*) e engenharia social. Este projeto constrói o motor de verificação de complexidade de credenciais no momento da definição de senha pelo usuário.

O script analisa a string recebida de forma estática e sem iteração, avaliando requisitos de extensão e diversidade de caixa de caracteres, calculando um **score de segurança** e emitindo a conformidade da credencial.

---

## 🎯 Fundamentos de TI & Cybersecurity Aplicados

* **Política de Complexidade de Credenciais:**
  * **Comprimento Mínimo:** Proteção contra ataques de dicionário e tabelas de hash pré-calculadas (*Rainbow Tables*).
  * **Variabilidade de Caixa (Upper/Lower):** Aumento do espaço amostral de busca de caracteres para mitigar ataques automatizados.
* **Segurança na Exibição de Dados (Privacy by Design):**
  * Mascaramento de credenciais no painel de saída terminal para estar em conformidade com as diretrizes de proteção de dados (LGPD / GDPR).

---

## 🏗️ Arquitetura em 4 Blocos

```text
┌────────────────────────────────────────────────────────┐
│  Bloco 01: Entradas & Telemetria                       │
│  - Captura da senha e medição de tamanho com len()     │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 02: Regras de Negócio & Políticas IAM           │
│  - Definição do TAMANHO_MINIMO = 8                     │
│  - Inicialização do score e flags booleanas            │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 03: Motor de Decisão (Auditoria Estática)       │
│  - Validação de comprimento                            │
│  - Análise de caixa alta e baixa (.lower() / .upper()) │
│  - Cálculo do score (0 a 3) e relatório de pendências  │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 04: Security Output (Relatório Mascarado)       │
│  - Impressão formatada e mascarada da auditoria        │
└────────────────────────────────────────────────────────┘


---

### 🏆 Tabela Final Completa do Repositório (`README.md` Principal)

Copie o código Markdown abaixo para atualizar a tabela principal do seu repositório no GitHub. **Todos os 5 projetos estão oficialmente concluídos e documentados!**

```markdown
## 💻 Projetos do Laboratório

| # | Projeto | Domínio de TI | Conceitos Aplicados em Python | Status |
|:-:|:---|:---|:---|:-:|
| **01** | **Calculadora de Sub-rede e IP** | Redes / Infraestrutura | Parsing de IP (`.split()`), Cálculo CIDR, RFC 1918, Condicionais | ✅ Concluído |
| **02** | **Gestor de Chamados & SLA N1/N2** | ITSM / Suporte N2 | Triagem de tickets, Priorização ITIL, Matriz Impacto x Urgência | ✅ Concluído |
| **03** | **Caixa Eletrônico & Lockout de PIN** | SecOps / Sistemas | Controle de estado em `dict`, Lockout de PIN, Limites Financeiros | ✅ Concluído |
| **04** | **Monitor de Saúde de Servidores** | SysAdmin / SRE | Avaliação de métricas de CPU/RAM/Disco, Classificação NOC | ✅ Concluído |
| **05** | **Auditor de Fortitude de Senhas** | Cybersecurity / IAM | Análise estática de strings, Score de segurança, Regras NIST | ✅ Concluído |