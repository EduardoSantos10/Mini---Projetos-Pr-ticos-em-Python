# 📈 Projeto 04: Diagnóstico de Saúde de Servidor (SysAdmin / SRE)

> Módulo de monitoramento contínuo de métricas computacionais (CPU, RAM e Disco) aplicando limiares de SLA/SRE para classificação de incidentes de infraestrutura.

---

## 📌 Visão Geral do Projeto

Na engenharia de confiabilidade (*Site Reliability Engineering - SRE*) e na administração de sistemas (SysAdmin), antecipar falhas é essencial para garantir a alta disponibilidade de serviços. Este projeto simula um agente de monitoramento (*Health Check*) similar aos utilizados em soluções corporativas (como Zabbix, Prometheus ou Datadog).

O script avalia os Golden Signals de telemetria de um servidor contra uma matriz de limiares de tolerância (*Thresholds*), gerando alertas preventivos antes do travamento completo do ambiente.

---

## 🎯 Fundamentos de TI & SRE Aplicados

* **Métricas Globais de Servidor:**
  * **CPU:** Processamento ativo de instrução de software.
  * **RAM:** Memória randômica de alta velocidade; o esgotamento causa intervenção do *OOM-Killer* no Linux.
  * **Disco (I/O & Espaço):** Capacidade de armazenamento persistente.
* **Classificação de Severidade de NOC:**
  * **🟢 OK:** Recursos abaixo do limiar de atenção.
  * **🟡 ALERTA (Warning):** Recursos na faixa de atenção; demanda atuação preventiva do suporte N2.
  * **🔴 CRÍTICO (Critical):** Recursos ultrapassaram a margem de segurança; risco imediato de indisponibilidade de serviço.

---

## 🏗️ Arquitetura em 4 Blocos

```text
┌────────────────────────────────────────────────────────┐
│  Bloco 01: Entradas & Telemetria                       │
│  - Leitura do Hostname, CPU%, RAM% e Disco%            │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 02: Regras de Negócio & Limiares (SRE)          │
│  - Definição de Constantes de Warning e Critical       │
│  - Inicialização de registradores de causa             │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 03: Motor de Decisão (Avaliação de Métricas)   │
│  - Teste de estouro crítico (Operador OR)              │
│  - Concatenação de diagnósticos de causa               │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Bloco 04: Painel NOC Output                           │
│  - Emissão de dashboard de saúde estruturado           │
└────────────────────────────────────────────────────────┘

---

## 💻 Projetos do Laboratório

| # | Projeto | Domínio de TI | Conceitos Aplicados em Python | Status |
|:-:|:---|:---|:---|:-:|
| **01** | **Calculadora de Sub-rede e IP** | Redes / Infraestrutura | Parsing de IP, Cálculo CIDR, RFC 1918, Condicionais | ✅ Concluído |
| **02** | **Gestor de Chamados & SLA N1/N2** | ITSM / Suporte N2 | Triagem de tickets, Priorização de SLA, Atualização de Estado | ✅ Concluído |
| **03** | **Caixa Eletrônico & Lockout de PIN** | SecOps / Sistemas | Controle de estado, Limite de tentativas, Trava de Segurança | ✅ Concluído |
| **04** | **Monitor de Saúde de Servidores** | SysAdmin / SRE | Avaliação de métricas de CPU/RAM, Classificação de Alertas | ✅ Concluído |
| **05** | **Auditor de Fortitude de Senhas** | Cybersecurity | Análise estática de strings, Validação de políticas de acesso | 🔄 Em Breve |