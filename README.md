# 📋 Documentação de Casos de Teste  
## Sistema de Checkout Inteligente — API ViaCEP

---

## 🎯 Objetivo

Este documento tem como objetivo descrever os principais cenários de teste para a funcionalidade de preenchimento automático de endereço no **Checkout Inteligente**.

A proposta é garantir que o sistema responda corretamente às diferentes entradas de CEP, evitando falhas que possam impactar a experiência do usuário durante o processo de compra.

---

## 📊 Casos de Teste

| ID   | Cenário                         | Entrada     | Ação            | Resultado Esperado                                      |
|------|--------------------------------|-------------|-----------------|---------------------------------------------------------|
| CT01 | Caminho feliz (CEP válido)     | 01001000    | Consulta à API  | Retorna status 200 com dados completos do endereço       |
| CT02 | CEP válido com hífen           | 01001-000   | Consulta à API  | Retorna status 200 e mantém consistência dos dados       |
| CT03 | CEP inexistente               | 99999999    | Consulta à API  | Retorna indicação de erro sem falha no sistema           |
| CT04 | CEP com letras                | ABCDEFGH    | Consulta à API  | Retorna erro ou resposta inválida controlada             |
| CT05 | CEP incompleto               | 12345       | Consulta à API  | Retorna erro ou comportamento tratado                    |
| CT06 | CEP vazio                    | ""          | Consulta à API  | Retorna erro sem comprometer a aplicação                 |

---

## 🔍 Análise dos Cenários

### ✅ CT01 — Caminho feliz
Representa o cenário ideal de uso. Este teste garante que a API está funcionando corretamente e retornando os dados esperados quando um CEP válido é informado.

### 🔄 CT02 — CEP com hífen
Avalia a flexibilidade da API ao receber entradas com formatação diferente, garantindo que o sistema aceite variações comuns inseridas pelo usuário.

### ⚠️ CT03 — CEP inexistente
Verifica como o sistema se comporta diante de um CEP válido no formato, porém inexistente na base de dados, assegurando que a resposta seja tratada corretamente.

### ❌ CT04, CT05 e CT06 — Entradas inválidas
Esses cenários representam erros comuns de digitação. O objetivo é garantir que o sistema responda de forma controlada, sem gerar falhas ou travamentos na aplicação.

---

## 🧾 Conclusão

Os testes descritos neste documento são essenciais para garantir a robustez do sistema de Checkout Inteligente.

Ao validar diferentes tipos de entrada, assegura-se que o processo de preenchimento automático de endereço seja confiável, contribuindo diretamente para uma melhor experiência do usuário e evitando possíveis perdas durante o processo de compra.

---
