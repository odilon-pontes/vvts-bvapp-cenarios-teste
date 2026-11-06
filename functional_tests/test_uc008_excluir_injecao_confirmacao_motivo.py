'''
UC008 - Excluir injeção de energia mensal com confirmação e motivo

Objetivo: Permitir que o Gestor exclua logicamente uma fatura, informando um motivo
obrigatório e confirmando a operação.

Requisitos:
- RF-23853 Exclusão de Injeção de Energia mensal (Epic 23763)
- CA02 (24921) confirmação e motivo obrigatório antes de efetivar
- CA03 (24922) a fatura permanece no banco com flag "excluída" e sai da listagem padrão
- US 24960 - Excluir Injeção de Energia mensal (Sprint 04)

Ator:
- Gestor/Administrador

Pré-condições:
- Usuário autenticado como Gestor.
- Fatura ativa 04/2026 da Usina Solar Alfa, já cadastrada (pré-condição de
  dados; o cadastro está no UC003).

Dados de teste:
- Fatura: 04/2026 | Usina Solar Alfa
- Motivo: "Mês de referência lançado incorretamente"

Resultado esperado (resumo):
Só com motivo e confirmação a exclusão é efetivada; o registro continua no
banco com flag "excluída".

Autor:  Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D08] Qual o nome e a localização do "filtro específico" para faturas
      excluídas? Perfis diferentes de Gestor podem usá-lo?
[D11] O motivo da exclusão é texto livre? Há tamanho mínimo/máximo?
[D12] O que acontece se o usuário cancelar a confirmação de exclusão?
      (comportamento não descrito)
[D22] Quais mensagens o sistema exibe no sucesso do cadastro e da exclusão (só
      a edição tem CA de sucesso, 28864) e nos erros (duplicidade, campo
      obrigatório, valor inválido)?
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a consulta histórica e localiza a fatura 04/2026 da Usina
# Solar Alfa.

# O ator seleciona a opção "Excluir".

# O sistema pergunta se o usuário realmente deseja excluir e exibe o campo
# obrigatório de motivo. [A1][A2][A3]

# O ator informa o motivo e confirma a exclusão. [RN1]

# O sistema efetiva a exclusão lógica [D22].

# O ator consulta a listagem padrão com o filtro 04/2026 e Usina Solar Alfa.

# O sistema não exibe a fatura excluída.

# O ator ativa o filtro de excluídas [D08] e verifica que a fatura aparece
# com status "excluída".

# Verificação no banco: o registro da fatura permanece, com flag "excluída"
# (CA03).

# [A1] - CONFIRMAR SEM INFORMAR O MOTIVO [CA02]
# ---------------------------------------------------------------

# O ator seleciona "Excluir" e confirma sem preencher o motivo.

# O sistema não efetiva a exclusão e indica que o motivo é obrigatório
# [D22].

# A fatura continua na listagem padrão com status "ativa".

# [A2] - CANCELAR A CONFIRMAÇÃO
# ---------------------------------------------------------------

# O ator seleciona "Excluir" e cancela a confirmação.

# Resultado esperado: NÃO DEFINIDO [D12]. Esperado, a confirmar: fatura
# permanece ativa.

# [A3] - MOTIVO FORA DO FORMATO
# ---------------------------------------------------------------

# O ator informa um motivo muito curto (1 caractere) ou muito longo.

# Resultado esperado: NÃO DEFINIDO [D11].

# [RN1] - MOTIVO OBRIGATÓRIO
# ---------------------------------------------------------------

# A exclusão exige confirmação e motivo preenchido antes de ser efetivada.

# [RN2] - EXCLUSÃO LÓGICA
# ---------------------------------------------------------------

# O registro não é apagado do banco; recebe a flag "excluída".

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------