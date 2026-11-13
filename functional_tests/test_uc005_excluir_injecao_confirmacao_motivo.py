'''
UC005 - Excluir injeção de energia mensal com confirmação e motivo

Objetivo: Permitir que o Gestor exclua logicamente uma fatura, informando
o motivo e confirmando a operação, e impedir a exclusão de fatura já Excluída
ou inexistente.

Requisitos:
- RF-23853 Exclusão de Injeção de Energia mensal (Epic 23763)
- CA02 (24921) confirmação e motivo obrigatório antes de efetivar
- CA03 (24922) exclusão lógica preservando dados, motivo, usuário e data e hora
- CA06 (36169) cancelar a confirmação mantém a fatura
- CA07 (36170) mensagem de sucesso
- CA08 (36171) fatura Excluída ou inexistente não pode ser excluída
- US 24960 - Excluir Injeção de Energia mensal (Sprint 04)

Ator:
- Gestor

Pré-condições:
- Usuário autenticado como Gestor.
- Fatura ativa 04/2026 da Usina Solar Alfa, já cadastrada (pré-condição de
  dados; o cadastro está no UC003).
- Fatura 05/2026 da Usina Solar Alfa com status Excluída (para o A3).

Dados de teste:
- Fatura: 04/2026 | Usina Solar Alfa
- Motivo: "Mês de referência lançado incorretamente"

Resultado esperado (resumo):
Só com motivo e confirmação a exclusão é efetivada; o registro continua no
banco com a flag "excluída" e o sistema exibe a mensagem de sucesso.

Autor: Odilon Francelino de Pontes Neto
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a consulta histórica e localiza a fatura 04/2026 da Usina
# Solar Alfa.

# O ator seleciona a opção "Excluir".

# O sistema exibe a confirmação da exclusão e o campo obrigatório de motivo.
# [A1][A2][A3]

# O ator informa o motivo e confirma a exclusão. [RN1]

# O sistema efetiva a exclusão lógica e exibe a mensagem "Fatura excluída
# com sucesso.".

# O ator consulta a listagem padrão com o filtro 04/2026 e Usina Solar Alfa.

# O sistema não exibe a fatura excluída.

# O ator ativa o filtro "Exibir faturas excluídas" e verifica que a fatura
# aparece com status Excluída.

# Verificação no banco: o registro da fatura permanece, com a flag
# "excluída", o motivo informado, o usuário responsável e a data e a hora da
# exclusão (CA03).

# 🟠 [A1] - CONFIRMAR SEM INFORMAR O MOTIVO [CA02]
# ---------------------------------------------------------------

# O ator seleciona "Excluir" e confirma sem preencher o motivo.

# O sistema não efetiva a exclusão. Exibe a mensagem "Motivo não pode ser vazio".

# A fatura continua na listagem padrão com status Ativa.

# 🟠 [A2] - CANCELAR A CONFIRMAÇÃO [CA06 36169]
# ---------------------------------------------------------------

# O ator seleciona "Excluir" e cancela a confirmação.

# O sistema não exclui a fatura, que permanece com o status Ativa e continua
# na listagem padrão.

# 🟠 [A3] - FATURA JÁ EXCLUÍDA OU INEXISTENTE [CA08 36171]
# ---------------------------------------------------------------

# O ator ativa o filtro "Exibir faturas excluídas" e localiza a fatura
# 05/2026, já com status Excluída.

# O sistema não oferece a opção de exclusão para essa fatura.

# O ator tenta excluí-la por acesso direto.

# O sistema informa que o registro não está disponível e não efetiva nova
# exclusão.

# 🟣 [RN1] - MOTIVO OBRIGATÓRIO
# ---------------------------------------------------------------

# A exclusão exige confirmação e motivo preenchido antes de ser efetivada.

# 🟣 [RN2] - EXCLUSÃO LÓGICA
# ---------------------------------------------------------------

# O registro não é apagado do banco; recebe a flag "excluída" e preserva
# dados, motivo, usuário e data e hora.
