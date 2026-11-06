'''
UC005 - Consultar injeção de energia mensal sem resultados

Objetivo: Garantir que o sistema exiba mensagem informativa quando nenhuma fatura é
encontrada para os filtros aplicados.

Requisitos:
- RF-23851 Consulta histórica de Injeção de Energia mensal (Epic 23763)
- CA04 (24917) mensagem informativa quando nenhuma fatura é encontrada
- CA06 (25776) exibir mensagem quando nenhuma fatura for encontrada (duplica o CA04)

Ator:
- Gestor

Pré-condições:
- Usuário autenticado como Gestor.
- Não existe fatura cadastrada para 12/2020.

Dados de teste:
- Mês/Ano: 12/2020 | Usina: Usina Solar Alfa

Resultado esperado (resumo):
O sistema exibe mensagem informativa e nenhuma linha de fatura.

Autor:  Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D09] Qual o texto da mensagem quando nenhuma fatura é encontrada? Os
      critérios 24917 e 25776 são duplicados: manter só um?
'''

# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a consulta histórica de faturas.

# O ator informa o mês/ano 12/2020 e seleciona a usina "Usina Solar Alfa".
# [A1]

# O ator aplica os filtros.

# O sistema exibe uma mensagem informativa de que nenhuma fatura foi
# encontrada [D09].

# O ator verifica que nenhuma linha de fatura é exibida.

# [A1] - SEM RESULTADO SOMENTE COM FILTRO DE USINA
# ---------------------------------------------------------------

# O ator seleciona uma usina sem nenhuma fatura cadastrada.

# O sistema exibe a mesma mensagem informativa [D09].

# [RN1] - CRITÉRIOS DUPLICADOS
# ---------------------------------------------------------------

# Os CAs 24917 e 25776 descrevem o mesmo comportamento; um único cenário os
# cobre [D09].

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------