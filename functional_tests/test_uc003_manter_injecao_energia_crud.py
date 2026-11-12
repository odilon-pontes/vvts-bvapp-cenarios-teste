'''
UC003 - Manter injeção de energia mensal (fluxo CRUD completo)

Objetivo: Permitir cadastrar, consultar, editar e excluir logicamente a injeção de
energia mensal (fatura da operadora), cobrindo as quatro operações em um único
fluxo.

Requisitos:
- RF-23849 Cadastro manual de Injeção de Energia mensal (CA 25769 a 25774) - Criar
- RF-23851 Consulta histórica de Injeção de Energia mensal (CA 24913, 24914, 24916, 36167, 36168) - Consultar
- RF-28855 Edição de Injeção de Energia mensal (CA 28857 a 28864, 36312 e 36314) - Atualizar
- RF-23853 Exclusão de Injeção de Energia mensal (CA 24920 a 24922, 36169 e 36170) - Excluir
- Epic 23763 Valores Injetados na Rede da Operadora

Ator:
- Tesoureiro (cadastra e edita)
- Gestor/Administrador (consulta e exclui)

Pré-condições:
- Usuários de teste: um Tesoureiro e um Gestor.
- Existem as usinas Usina Solar Alfa e Usina Solar Beta.
- Não existe fatura cadastrada para 03/2026 na Usina Solar Alfa.
- Para o A9, existe fatura ativa 04/2026 na Usina Solar Alfa.

Dados de teste:
- Mês/Ano: 03/2026 | Usina: Usina Solar Alfa
- Cadastro: Energia Injetada 1.250,00 kWh | Energia Consumida 980,00 kWh |
  Créditos de Energia 270,00 kWh | Valores Financeiros R$ 412,50
- Edição: Energia Injetada passa para 1.300,00 kWh
- Valores inválidos: "abc", "-10,00" e "1,234"
- Motivo da exclusão: "Fatura de teste lançada em duplicidade"

Resultado esperado (resumo):
A fatura é criada, aparece na consulta, tem o dado alterado refletido nas
consultas seguintes e, após a exclusão lógica, some da listagem padrão e só é
visível com o filtro "Exibir faturas excluídas".

Versão dos requisitos: Work packages de 12/11/2026
Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D04] Como o sistema recusa o acesso direto de um perfil não autorizado
      (mensagem, redirecionamento)? O que acontece com o usuário não
      autenticado? Os critérios só dizem que é "recusado".
[D07] O que significa o status "Substituída" e como uma fatura passa a tê-lo?
      Como o PDF é anexado na criação (o cadastro 25769 não prevê PDF, a
      edição 28858 prevê substituição) e qual a forma do indicador de PDF
      anexado?
[D09] Onde e por quem o registro de auditoria e o log da alteração de
      tolerância podem ser consultados? O RF-4.2.05 não foi fornecido.
[D10] "Gestor/Administrador" é o mesmo perfil de "Gestor" (usado nas Features
      23834 e 23851) ou são perfis distintos?
[D11] O cadastro não lista os campos obrigatórios nem os valores válidos (a
      edição define). Quais mensagens o sistema exibe no sucesso e nos erros
      do cadastro (duplicidade, campo obrigatório, valor inválido)? Uma fatura
      Excluída impede novo cadastro do mesmo Mês/Ano e Usina?
[D12] Quais mensagens de erro o sistema exibe na edição (campo obrigatório
      vazio, valor inválido) e como é recusada a edição de uma fatura Excluída
      ou Substituída?
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# CRIAR - O Tesoureiro acessa a página de cadastro de injeção de energia
# mensal. Ele verifica que existem os campos:
# - Mês/Ano
# - Usina [D11]
# - Energia Injetada
# - Energia Consumida
# - Créditos de Energia
# - Valores Financeiros
# - Opção para salvar

# O Tesoureiro preenche os campos com os dados do cadastro. [A1][A2][A3][A8]

# O Tesoureiro seleciona a opção para salvar. [RN1][RN2]

# O sistema valida os dados, salva a fatura e confirma o cadastro [D11].

# CONSULTAR - O Tesoureiro acessa a consulta histórica de faturas e filtra
# por 03/2026 e Usina Solar Alfa.

# O sistema exibe imediatamente (CA05 25773) um item com Mês/Ano 03/2026,
# Usina Solar Alfa e status Ativa; o indicador de PDF anexado aparece como
# não anexado [D07].

# O Tesoureiro abre a visualização detalhada da fatura (CA08 36167) e
# verifica Mês/Ano, Usina, Status, Energia Injetada 1.250,00 kWh, Energia
# Consumida 980,00 kWh, Créditos de Energia 270,00 kWh e Valores Financeiros
# R$ 412,50, sem PDF anexado.

# ATUALIZAR - O Tesoureiro seleciona a fatura e a opção de editar.
# [A10][A12]

# O sistema exibe a página de edição com os dados da fatura. O ator verifica
# que a Usina não pode ser alterada e que o PDF anexado é opcional (CA02
# 28858 e CA05 28861).

# O Tesoureiro altera somente a Energia Injetada para 1.300,00 kWh, mantendo
# os demais campos (CA04 28860), e salva. [A4][A5][A6][A9]

# O sistema valida, salva as alterações no mesmo registro da fatura, sem
# criar nova versão (CA03 28859), registra a auditoria com ID da fatura,
# usuário, data e hora (CA10 36314) e exibe a mensagem "Edição realizada com
# sucesso." (CA08 28864).

# O Tesoureiro consulta novamente a fatura e verifica na visualização
# detalhada que a Energia Injetada é 1.300,00 kWh e que os demais campos não
# mudaram.

# EXCLUIR - O Gestor autentica, acessa a consulta histórica e localiza a
# fatura 03/2026 da Usina Solar Alfa. Ele verifica que a opção de exclusão
# está visível. [A7]

# O Gestor seleciona a opção "Excluir".

# O sistema exige confirmação e um motivo obrigatório. [A11]

# O Gestor informa o motivo e confirma a exclusão.

# O sistema exclui logicamente a fatura (permanece no banco com a flag
# "excluída", com o motivo, o usuário e a data e a hora), gera o registro de
# auditoria [D09] e exibe a mensagem "Fatura excluída com sucesso." (CA07
# 36170).

# O Gestor consulta a listagem padrão e verifica que a fatura 03/2026 da
# Usina Solar Alfa não aparece.

# O Gestor ativa o filtro "Exibir faturas excluídas" e verifica que a fatura
# aparece com status Excluída.

# O Gestor abre a visualização detalhada e verifica o motivo da exclusão, o
# usuário responsável e a data e a hora da exclusão (CA09 36168).

# 🟠 [A1] - CADASTRO DUPLICADO [CA03 25771]
# ---------------------------------------------------------------

# O Tesoureiro tenta cadastrar nova fatura para 03/2026 na Usina Solar Alfa,
# já existente e ativa.

# O sistema impede o cadastro e exibe mensagem de erro [D11].

# O Tesoureiro consulta e verifica que existe apenas uma fatura para esse
# mês/ano e usina.

# Se a fatura existente estiver Excluída, o resultado esperado é NÃO
# DEFINIDO [D11].

# 🟠 [A2] - CAMPOS OBRIGATÓRIOS NÃO PREENCHIDOS NO CADASTRO [CA02 25770]
# ---------------------------------------------------------------

# O Tesoureiro deixa campos em branco e tenta salvar.

# O sistema impede o salvamento e exibe erro nos campos inválidos. Quais
# campos são obrigatórios no cadastro é NÃO DEFINIDO [D11].

# A fatura não aparece na consulta.

# 🟠 [A3] - VALOR NUMÉRICO INVÁLIDO NO CADASTRO [CA02 25770]
# ---------------------------------------------------------------

# O Tesoureiro digita "abc" no campo Energia Injetada e tenta salvar.

# O sistema impede o salvamento e exibe erro. Os valores aceitos no cadastro
# são NÃO DEFINIDOS [D11].

# 🟠 [A4] - CANCELAR A EDIÇÃO [CA07 28863]
# ---------------------------------------------------------------

# O Tesoureiro altera a Energia Injetada para 9.999,00 kWh e seleciona
# cancelar.

# O sistema não persiste a alteração.

# O Tesoureiro consulta a fatura e verifica que a Energia Injetada continua
# com o valor anterior.

# 🟠 [A5] - CAMPO OBRIGATÓRIO VAZIO NA EDIÇÃO [CA05 28861]
# ---------------------------------------------------------------

# O Tesoureiro apaga a Energia Consumida e tenta salvar.

# O sistema impede o salvamento. A mensagem de erro é NÃO DEFINIDA [D12].

# 🟠 [A6] - VALOR NUMÉRICO INVÁLIDO NA EDIÇÃO [CA06 28862]
# ---------------------------------------------------------------

# O Tesoureiro digita, em campos numéricos diferentes, "abc", "-10,00" e
# "1,234" e tenta salvar a cada vez.

# O sistema aceita apenas números maiores ou iguais a 0 com até 2 casas
# decimais: em cada tentativa gera erro e impede o salvamento. A mensagem de
# erro é NÃO DEFINIDA [D12].

# 🟠 [A7] - TESOUREIRO NÃO EXCLUI [CA01 24920]
# ---------------------------------------------------------------

# O Tesoureiro consulta a fatura.

# O sistema não exibe a opção de exclusão para o Tesoureiro.

# 🟠 [A8] - PERFIL SEM PERMISSÃO NO CADASTRO [CA04 25772]
# ---------------------------------------------------------------

# Um Operador de Usina tenta acessar a página de cadastro.

# O sistema não permite o acesso. A forma da negação é NÃO DEFINIDA [D04].

# 🟠 [A9] - EDITAR MÊS/ANO PARA UM MÊS JÁ CADASTRADO [CA09 36312]
# ---------------------------------------------------------------

# O Tesoureiro edita a fatura 03/2026 e altera o Mês/Ano para 04/2026, já
# cadastrado na Usina Solar Alfa, e tenta salvar.

# O sistema impede o salvamento e exibe a mensagem "Já existe fatura
# cadastrada para este mês/ano e usina.".

# 🟠 [A10] - EDITAR FATURA EXCLUÍDA OU SUBSTITUÍDA [CA01 28857]
# ---------------------------------------------------------------

# O ator tenta editar uma fatura com status Excluída ou Substituída.

# O sistema não permite a edição. A forma do bloqueio é NÃO DEFINIDA [D12].

# 🟠 [A11] - CANCELAR A CONFIRMAÇÃO DE EXCLUSÃO [CA06 36169]
# ---------------------------------------------------------------

# O Gestor seleciona "Excluir" e cancela a confirmação.

# O sistema não exclui a fatura, que permanece com o status anterior
# (Ativa).

# 🟠 [A12] - GESTOR NÃO EDITA [CA01 28857]
# ---------------------------------------------------------------

# O Gestor consulta a fatura e procura a opção de editar.

# O sistema não permite a edição ao Gestor: apenas o Tesoureiro tem acesso
# (forma da negação NÃO DEFINIDA [D04]).

# 🟣 [RN1] - VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------

# Na edição, Mês/Ano, Energia Injetada, Energia Consumida, Créditos de
# Energia e Valores Financeiros são obrigatórios e numéricos (maiores ou
# iguais a 0, até 2 casas decimais); o PDF é opcional. No cadastro, as
# regras não estão definidas [D11].

# 🟣 [RN2] - UNICIDADE
# ---------------------------------------------------------------

# Não pode existir mais de uma fatura para o mesmo Mês/Ano e Usina, no
# cadastro (CA03 25771) e na edição (CA09 36312).

# 🟣 [RN3] - PERFIS
# ---------------------------------------------------------------

# Cadastro e edição: Tesoureiro. Consulta: Gestor, Tesoureiro e Operador de
# Usina. Exclusão: Gestor/Administrador [D10].

# 🟣 [RN4] - EXCLUSÃO LÓGICA
# ---------------------------------------------------------------

# A fatura excluída permanece no banco com a flag "excluída" e não aparece
# na listagem padrão.

# 🟣 [RN5] - EDIÇÃO
# ---------------------------------------------------------------

# A Usina não pode ser alterada; o PDF anexado pode ser substituído; a
# edição não cria nova versão da fatura.
