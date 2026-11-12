'''
UC006 - Visualizar injeções de energia excluídas logicamente

Objetivo: Permitir que o Gestor visualize as faturas Excluídas ativando o filtro "Exibir
faturas excluídas", sem que elas apareçam na listagem padrão e sem que o
filtro seja oferecido aos demais perfis.

Requisitos:
- RF-23851 Consulta histórica de Injeção de Energia mensal (Epic 23763)
- CA03 (24916) faturas Excluídas fora da listagem padrão; filtro "Exibir faturas excluídas" só para o Gestor

Ator:
- Gestor
- Tesoureiro e Operador de Usina (verificação)

Pré-condições:
- Usuário autenticado como Gestor.
- Fatura 03/2026 Alfa ativa e fatura 03/2026 Beta com status Excluída.

Dados de teste:
- Mês/Ano: 03/2026
- Fatura Excluída: 03/2026 Usina Solar Beta

Resultado esperado (resumo):
A fatura Excluída só aparece com o filtro específico, com status Excluída, e
apenas para o Gestor.

Versão dos requisitos: Work packages de 12/11/2026
Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
- Nenhuma: os requisitos cobrem todos os passos deste cenário.
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a consulta histórica de faturas e filtra por 03/2026 sem
# ativar o filtro "Exibir faturas excluídas".

# O sistema exibe somente a fatura 03/2026 Usina Solar Alfa.

# O ator verifica que a fatura 03/2026 Usina Solar Beta não aparece.

# O ator ativa o filtro "Exibir faturas excluídas" e aplica a consulta.

# O sistema exibe a fatura 03/2026 Usina Solar Beta com o status Excluída.

# O ator verifica que o item continua exibindo Mês/Ano, Usina, status e
# indicador de PDF. [A1]

# 🟠 [A1] - OUTROS PERFIS E O FILTRO DE EXCLUÍDAS
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro e acessa a consulta.

# O sistema não disponibiliza o filtro "Exibir faturas excluídas" e a fatura
# Excluída não aparece.

# O ator repete o procedimento como Operador de Usina, com o mesmo
# resultado.

# 🟣 [RN1] - LISTAGEM PADRÃO
# ---------------------------------------------------------------

# Faturas com status Excluída não aparecem na listagem padrão.

# 🟣 [RN2] - FILTRO DO GESTOR
# ---------------------------------------------------------------

# O filtro "Exibir faturas excluídas" não é disponibilizado aos demais
# perfis.
