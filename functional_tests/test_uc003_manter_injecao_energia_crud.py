'''
UC003 - Manter injeção de energia mensal (fluxo CRUD completo)

Objetivo: Permitir cadastrar, consultar, editar e excluir (logicamente) a injeção de
energia mensal (fatura da operadora), cobrindo as quatro operações em um único
fluxo.

Requisitos:
- RF-23849 Cadastro manual de Injeção de Energia mensal (CA 25769 a 25774) - Criar
- RF-23851 Consulta histórica de Injeção de Energia mensal (CA 24913 a 24919) - Consultar
- RF-28855 Edição de Injeção de Energia mensal (CA 28857 a 28864) - Atualizar
- RF-23853 Exclusão de Injeção de Energia mensal (CA 24920 a 24923) - Excluir
- Epic 23763 Valores Injetados na Rede da Operadora

Ator:
- Tesoureiro (cadastra e edita)
- Gestor/Administrador (consulta e exclui)

Pré-condições:
- Usuários de teste: um Tesoureiro e um Gestor.
- Existe a Usina Solar Alfa.
- Não existe fatura cadastrada para 03/2026 na Usina Solar Alfa.

Dados de teste:
- Mês/Ano: 03/2026 | Usina: Usina Solar Alfa
- Cadastro: Energia Injetada 1.250,00 kWh | Energia Consumida 980,00 kWh |
  Créditos de Energia 270,00 kWh | Valores Financeiros R$ 412,50
- Edição: Energia Injetada passa para 1.300,00 kWh
- Motivo da exclusão: "Fatura de teste lançada em duplicidade"

Resultado esperado (resumo):
A fatura é criada, aparece na consulta, tem o dado alterado refletido nas
consultas seguintes e, após a exclusão lógica, some da listagem padrão e só é
visível com o filtro de excluídas.

Autor:  Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D05] Os perfis não listados nos critérios (ex.: Tesoureiro na consulta de
      medições; Técnico de Manutenção na consulta de faturas) devem ter o
      acesso negado? De que forma (menu oculto, mensagem, redirecionamento)? E
      o usuário não autenticado?
[D07] O que significa o status "substituída" e como uma fatura passa a tê-lo?
      Como o PDF é anexado (o cadastro 25769 não prevê PDF)?
[D08] Qual o nome e a localização do "filtro específico" para faturas
      excluídas? Perfis diferentes de Gestor podem usá-lo?
[D12] O que acontece se o usuário cancelar a confirmação de exclusão?
      (comportamento não descrito)
[D13] RF-4.2.05 não foi fornecido: o que o registro de auditoria contém
      (usuário, data/hora, motivo, fatura?) e onde ele é consultado? (O CA
      25778 "log imutável" está Rejected e não será testado.)
[D14] Uma fatura excluída logicamente impede novo cadastro do mesmo mês/ano e
      usina?
[D21] Usina e PDF fazem parte do cadastro? Quais campos são obrigatórios e o
      que é "valor válido" em cada campo numérico (negativo, zero, casas
      decimais)?
[D22] Quais mensagens o sistema exibe no sucesso do cadastro e da exclusão (só
      a edição tem CA de sucesso, 28864) e nos erros (duplicidade, campo
      obrigatório, valor inválido)?
[D23] Alterar Mês/Ano para um mês já cadastrado na mesma usina é bloqueado?
      Faturas excluídas/substituídas podem ser editadas? O Gestor também
      edita? Usina e PDF são editáveis?
'''

# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# CRIAR - O Tesoureiro acessa a página de cadastro de injeção de energia
# mensal. Ele verifica que existem os campos:
# - Mês/Ano
# - Usina [D21]
# - Energia Injetada
# - Energia Consumida
# - Créditos de Energia
# - Valores Financeiros
# - Opção para salvar

# O Tesoureiro preenche os campos com os dados do cadastro. [A1][A2][A3][A8]

# O Tesoureiro seleciona a opção para salvar. [RN1][RN2]

# O sistema valida os dados, salva a fatura e confirma o cadastro [D22].

# CONSULTAR - O Tesoureiro acessa a consulta histórica de faturas e filtra
# por 03/2026 e Usina Solar Alfa.

# O sistema exibe imediatamente (CA05 25773) um item com mês/ano 03/2026,
# usina Usina Solar Alfa e status "ativa"; o indicador de PDF aparece como
# não anexado [D07].

# O Tesoureiro abre a visualização detalhada da fatura (US 28870) e verifica
# que os valores cadastrados estão corretos.

# ATUALIZAR - O Tesoureiro seleciona a fatura e a opção de editar.

# O sistema exibe a página de edição com os campos preenchidos com os dados
# da fatura.

# O Tesoureiro altera somente a Energia Injetada para 1.300,00 kWh, mantendo
# os demais campos (CA04 28860), e salva. [A4][A5][A6]

# O sistema valida, salva e informa que a edição foi realizada com sucesso
# (CA08 28864).

# O Tesoureiro consulta novamente a fatura e verifica na visualização
# detalhada que a Energia Injetada é 1.300,00 kWh e que os demais campos não
# mudaram (CA03 28859).

# EXCLUIR - O Gestor autentica, acessa a consulta histórica e localiza a
# fatura 03/2026 da Usina Solar Alfa. Ele verifica que a opção de exclusão
# está visível. [A7]

# O Gestor seleciona a opção "Excluir".

# O sistema exige confirmação e um motivo obrigatório. [A9]

# O Gestor informa o motivo e confirma a exclusão.

# O sistema exclui logicamente a fatura (permanece no banco com flag
# "excluída") e gera registro de auditoria [D13].

# O Gestor consulta a listagem padrão e verifica que a fatura 03/2026 da
# Usina Solar Alfa não aparece.

# O Gestor ativa o filtro de faturas excluídas [D08] e verifica que a fatura
# aparece com status "excluída".

# [A1] - CADASTRO DUPLICADO [CA03 25771]
# ---------------------------------------------------------------

# O Tesoureiro tenta cadastrar nova fatura para 03/2026 na Usina Solar Alfa,
# já existente e ativa.

# O sistema impede o cadastro e exibe mensagem de erro [D22].

# O Tesoureiro consulta e verifica que existe apenas uma fatura para esse
# mês/ano e usina.

# Caso a fatura existente esteja excluída logicamente, o resultado esperado
# é NÃO DEFINIDO [D14].

# [A2] - CAMPOS OBRIGATÓRIOS NÃO PREENCHIDOS [CA02 25770]
# ---------------------------------------------------------------

# O Tesoureiro deixa campos obrigatórios em branco e tenta salvar.

# O sistema impede o salvamento e exibe erro nos campos inválidos
# [D21][D22].

# A fatura não aparece na consulta.

# [A3] - VALOR NUMÉRICO INVÁLIDO NO CADASTRO
# ---------------------------------------------------------------

# O Tesoureiro digita texto (ex.: "abc") no campo Energia Injetada e tenta
# salvar.

# O sistema impede o salvamento e exibe erro [D21][D22]. Valores como
# negativo ou zero: resultado NÃO DEFINIDO [D21].

# [A4] - CANCELAR A EDIÇÃO [CA07 28863]
# ---------------------------------------------------------------

# O Tesoureiro altera a Energia Injetada para 9.999,00 kWh e seleciona
# cancelar.

# O sistema não persiste a alteração.

# O Tesoureiro consulta a fatura e verifica que a Energia Injetada continua
# com o valor anterior.

# [A5] - EDIÇÃO COM CAMPO OBRIGATÓRIO VAZIO [CA05 28861]
# ---------------------------------------------------------------

# O Tesoureiro apaga o conteúdo de um campo obrigatório na edição e tenta
# salvar.

# O sistema impede o salvamento e informa o erro [D21][D22].

# [A6] - EDIÇÃO COM VALOR NUMÉRICO INVÁLIDO [CA06 28862]
# ---------------------------------------------------------------

# O Tesoureiro digita texto no campo Valores Financeiros e tenta salvar.

# O sistema impede o salvamento e informa o erro [D21][D22].

# [A7] - TESOUREIRO NÃO EXCLUI [CA01 24920]
# ---------------------------------------------------------------

# O Tesoureiro consulta a fatura.

# O sistema não exibe a opção de exclusão para o Tesoureiro.

# [A8] - PERFIL SEM PERMISSÃO NO CADASTRO [CA04 25772]
# ---------------------------------------------------------------

# Um Operador de Usina tenta acessar a página de cadastro.

# O sistema não permite o acesso (forma de negação NÃO DEFINIDA [D05]).

# [A9] - CANCELAR A CONFIRMAÇÃO DE EXCLUSÃO
# ---------------------------------------------------------------

# O Gestor seleciona "Excluir" e cancela a confirmação.

# Resultado esperado: NÃO DEFINIDO [D12]. Esperado, a confirmar: fatura
# permanece ativa.

# [A10] - EDITAR MÊS/ANO PARA UM MÊS JÁ CADASTRADO
# ---------------------------------------------------------------

# O Tesoureiro edita o Mês/Ano para um mês já cadastrado na mesma usina.

# Resultado esperado: NÃO DEFINIDO [D23].

# [RN1] - VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------

# Campos obrigatórios e valores numéricos válidos são validados antes de
# salvar (cadastro e edição). A lista de obrigatórios e a faixa de valores
# não foram definidas [D21].

# [RN2] - UNICIDADE
# ---------------------------------------------------------------

# Não pode existir mais de uma fatura para o mesmo mês/ano e usina (CA03
# 25771).

# [RN3] - PERFIS
# ---------------------------------------------------------------

# Cadastro e edição: Tesoureiro. Consulta: Gestor, Tesoureiro e Operador de
# Usina. Exclusão: Gestor/Administrador.

# [RN4] - EXCLUSÃO LÓGICA
# ---------------------------------------------------------------

# A fatura excluída permanece no banco com flag "excluída" e não aparece na
# listagem padrão.

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------