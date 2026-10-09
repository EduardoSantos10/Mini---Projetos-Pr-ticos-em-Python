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