'''
UC006 - Visualizar injeções de energia excluídas logicamente

Objetivo: Permitir que o Gestor visualize as faturas excluídas logicamente ativando um
filtro específico, sem que elas apareçam na listagem padrão.

Requisitos:
- RF-23851 Consulta histórica de Injeção de Energia mensal (Epic 23763)
- CA03 (24916) faturas excluídas não aparecem na listagem padrão; o Gestor as visualiza com filtro específico

Ator:
- Gestor
- Tesoureiro / Operador de Usina (verificação)

Pré-condições:
- Usuário autenticado como Gestor.
- Fatura 03/2026 Alfa ativa e fatura 03/2026 Beta excluída logicamente.

Dados de teste:
- Mês/Ano: 03/2026
- Fatura excluída: 03/2026 Usina Solar Beta

Resultado esperado (resumo):
A fatura excluída só aparece com o filtro específico, com status "excluída".

Autor:  Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D08] Qual o nome e a localização do "filtro específico" para faturas
      excluídas? Perfis diferentes de Gestor podem usá-lo?
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a consulta histórica de faturas e filtra por 03/2026 sem
# ativar o filtro de excluídas.

# O sistema exibe somente a fatura 03/2026 Usina Solar Alfa.

# O ator verifica que a fatura 03/2026 Usina Solar Beta não aparece.

# O ator ativa o filtro específico para faturas excluídas [D08] e aplica a
# consulta.

# O sistema exibe a fatura 03/2026 Usina Solar Beta com o status "excluída".

# O ator verifica que o item continua exibindo mês/ano, usina, status e
# indicador de PDF. [A1]

# [A1] - OUTROS PERFIS E O FILTRO DE EXCLUÍDAS
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro (ou Operador de Usina) e acessa a
# consulta.

# Resultado esperado: NÃO DEFINIDO [D08]. O CA diz apenas que o Gestor pode
# visualizar; não diz se o filtro fica oculto para os demais.

# [RN1] - LISTAGEM PADRÃO
# ---------------------------------------------------------------

# Faturas excluídas logicamente não aparecem na listagem padrão.

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------
