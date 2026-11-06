'''
UC004 - Consultar injeção de energia mensal com filtros

Objetivo: Permitir que o usuário filtre faturas por mês/ano e/ou usina e visualize a
lista com mês/ano, usina, status e indicador de PDF anexado.

Requisitos:
- RF-23851 Consulta histórica de Injeção de Energia mensal (Epic 23763)
- CA01 (24913) filtro por mês/ano e/ou usina
- CA02 (24914) itens com mês/ano, usina, status e indicador de PDF anexado
- US 24954 - Consultar Injeção de Energia mensal (Sprint 04)

Ator:
- Gestor (também Tesoureiro e Operador de Usina, ver UC007)

Pré-condições:
- Usuário autenticado como Gestor.
- Faturas ativas: 02/2026 Alfa (com PDF anexado), 03/2026 Alfa (sem PDF),
  03/2026 Beta (sem PDF). [D07]

Dados de teste:
- Mês/Ano: 03/2026 | Usina: Usina Solar Alfa
- Usinas: Usina Solar Alfa, Usina Solar Beta

Resultado esperado (resumo):
A lista contém apenas as faturas que atendem aos filtros e cada item exibe os
quatro dados exigidos.

Autor:  Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D06] O filtro por mês/ano é um único mês ou um intervalo de meses?
[D07] O que significa o status "substituída" e como uma fatura passa a tê-lo?
      Como o PDF é anexado (o cadastro 25769 não prevê PDF)?
'''

# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a consulta histórica de faturas. Ele verifica que existem os
# filtros de mês/ano e de usina.

# O ator informa o mês/ano 03/2026 e seleciona a usina "Usina Solar Alfa".
# [A1][A2][A3]

# O ator aplica os filtros.

# O sistema exibe uma lista com um único item.

# O ator verifica que o item exibe: mês/ano 03/2026, usina Usina Solar Alfa,
# status "ativa" e o indicador de PDF como não anexado. [A4]

# [A1] - FILTRAR SOMENTE POR MÊS/ANO
# ---------------------------------------------------------------

# O ator informa apenas 03/2026 e aplica o filtro.

# O sistema exibe duas faturas: 03/2026 Alfa e 03/2026 Beta.

# [A2] - FILTRAR SOMENTE POR USINA
# ---------------------------------------------------------------

# O ator seleciona apenas "Usina Solar Alfa" e aplica o filtro.

# O sistema exibe duas faturas: 02/2026 e 03/2026 da Usina Solar Alfa.

# [A3] - MÊS/ANO COMO INTERVALO
# ---------------------------------------------------------------

# O ator tenta informar um intervalo de meses (02/2026 a 03/2026).

# Resultado esperado: NÃO DEFINIDO [D06].

# [A4] - INDICADOR DE PDF ANEXADO
# ---------------------------------------------------------------

# O ator filtra por 02/2026 e Usina Solar Alfa.

# O sistema exibe o item com o indicador de PDF anexado. A forma do
# indicador não é definida; verificar sua presença.

# [A5] - STATUS "SUBSTITUÍDA"
# ---------------------------------------------------------------

# Não há requisito que crie uma fatura substituída, nem que defina o status
# [D07]. Cenário não executável até o esclarecimento.

# [RN1] - FATURAS EXCLUÍDAS
# ---------------------------------------------------------------

# Faturas excluídas logicamente não aparecem na listagem padrão (ver UC006).

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------
