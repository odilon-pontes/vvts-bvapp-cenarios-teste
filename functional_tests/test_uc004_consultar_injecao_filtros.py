'''
UC004 - Consultar injeção de energia mensal com filtros

Objetivo: Permitir que o usuário filtre faturas por Mês/Ano e/ou Usina e visualize a
lista com Mês/Ano, Usina, status e indicador de PDF anexado.

Requisitos:
- RF-23851 Consulta histórica de Injeção de Energia mensal (Epic 23763)
- CA01 (24913) filtro por mês/ano e/ou usina
- CA02 (24914) itens com mês/ano, usina, status e indicador de PDF anexado
- US 24954 - Consultar Injeção de Energia mensal (Sprint 04)

Ator:
- Gestor (também Tesoureiro e Operador de Usina, ver UC007)

Pré-condições:
- Usuário autenticado como Gestor.
- Faturas ativas: 02/2026 Alfa (com PDF anexado [D07]), 03/2026 Alfa (sem PDF)
  e 03/2026 Beta (sem PDF).

Dados de teste:
- Mês/Ano: 03/2026 | Usina: Usina Solar Alfa
- Usinas: Usina Solar Alfa e Usina Solar Beta

Resultado esperado (resumo):
A lista contém apenas as faturas que atendem aos filtros e cada item exibe
Mês/Ano, Usina, status e indicador de PDF anexado.

Versão dos requisitos: Work packages de 12/11/2026
Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D06] O filtro Mês/Ano é um mês único ou um intervalo de meses? O que a
      consulta exibe quando é acionada sem nenhum filtro?
[D07] O que significa o status "Substituída" e como uma fatura passa a tê-lo?
      Como o PDF é anexado na criação (o cadastro 25769 não prevê PDF, a
      edição 28858 prevê substituição) e qual a forma do indicador de PDF
      anexado?
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a consulta histórica de faturas. Ele verifica que existem os
# filtros de Mês/Ano e de Usina.

# O ator informa o Mês/Ano 03/2026 e seleciona a Usina Solar Alfa.
# [A1][A2][A3][A6]

# O ator aplica os filtros.

# O sistema exibe uma lista com um único item.

# O ator verifica que o item exibe: Mês/Ano 03/2026, Usina Usina Solar Alfa,
# status Ativa e o indicador de PDF anexado como não anexado. [A4]

# 🟠 [A1] - FILTRAR SOMENTE POR MÊS/ANO
# ---------------------------------------------------------------

# O ator informa apenas 03/2026 e aplica o filtro.

# O sistema exibe duas faturas: 03/2026 Alfa e 03/2026 Beta.

# 🟠 [A2] - FILTRAR SOMENTE POR USINA
# ---------------------------------------------------------------

# O ator seleciona apenas a Usina Solar Alfa e aplica o filtro.

# O sistema exibe duas faturas: 02/2026 e 03/2026 da Usina Solar Alfa.

# 🟠 [A3] - MÊS/ANO COMO INTERVALO
# ---------------------------------------------------------------

# O ator tenta informar um intervalo de meses (02/2026 a 03/2026).

# Resultado esperado: NÃO DEFINIDO [D06].

# 🟠 [A4] - INDICADOR DE PDF ANEXADO
# ---------------------------------------------------------------

# O ator filtra por 02/2026 e Usina Solar Alfa.

# O sistema exibe o item com o indicador de PDF anexado. A forma do
# indicador não é definida [D07]; verificar a sua presença.

# 🟠 [A5] - STATUS SUBSTITUÍDA
# ---------------------------------------------------------------

# Nenhum requisito cria uma fatura com status Substituída [D07]. Cenário não
# executável até o esclarecimento.

# 🟠 [A6] - CONSULTA SEM NENHUM FILTRO
# ---------------------------------------------------------------

# O ator aciona a consulta sem informar Mês/Ano nem Usina.

# Resultado esperado: NÃO DEFINIDO [D06].

# 🟣 [RN1] - FATURAS EXCLUÍDAS
# ---------------------------------------------------------------

# Faturas com status Excluída não aparecem na listagem padrão (ver UC006).
