'''
UC005 - Consultar injeção de energia mensal sem resultados ou com falha

Objetivo: Garantir que o sistema exiba mensagem quando nenhuma fatura é encontrada e que
distinga essa situação de uma falha na obtenção da lista.

Requisitos:
- RF-23851 Consulta histórica de Injeção de Energia mensal (Epic 23763)
- CA04 (24917) mensagem quando nenhuma fatura é encontrada
- CA07 (36166) carregamento, ausência de resultados e falha na obtenção da lista

Ator:
- Gestor

Pré-condições:
- Usuário autenticado como Gestor.
- Não existe fatura cadastrada para 12/2020.

Dados de teste:
- Mês/Ano: 12/2020 | Usina: Usina Solar Alfa

Resultado esperado (resumo):
Sem resultados, o sistema exibe a mensagem de ausência; em caso de falha,
exibe a mensagem de falha, sem indicar ausência de faturas.

Versão dos requisitos: Work packages de 12/11/2026
Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D17] Como é indicado o carregamento em andamento (texto, ícone)? Qual o texto
      da mensagem de falha na comparação geração x injeção (CA14 36180 não
      define)?
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a consulta histórica de faturas.

# O ator informa o Mês/Ano 12/2020 e seleciona a Usina Solar Alfa. [A1]

# O ator aplica os filtros.

# O sistema indica o carregamento em andamento [D17] e exibe a mensagem
# "Nenhuma fatura encontrada para os filtros informados.".

# O ator verifica que nenhuma linha de fatura é exibida.

# 🟠 [A1] - SEM RESULTADO SOMENTE COM FILTRO DE USINA
# ---------------------------------------------------------------

# O ator seleciona uma usina sem nenhuma fatura cadastrada.

# O sistema exibe a mesma mensagem "Nenhuma fatura encontrada para os
# filtros informados.".

# 🟠 [A2] - FALHA NA OBTENÇÃO DA LISTA [CA07 36166]
# ---------------------------------------------------------------

# O ator aplica os filtros em um momento em que a obtenção das faturas
# falha.

# O sistema exibe a mensagem "Não foi possível obter as faturas. Tente
# novamente.".

# O sistema não informa que não existem faturas e não exibe a mensagem do
# fluxo principal.

# 🟣 [RN1] - ESTADOS DISTINTOS
# ---------------------------------------------------------------

# A consulta distingue o carregamento em andamento, a ausência de resultados
# (CA04) e a falha na obtenção da lista (CA07). A falha nunca é apresentada
# como ausência de faturas.
