'''
UC003 - Manter injeção de energia mensal (fluxo CRUD completo)

Objetivo: Permitir cadastrar, consultar (com filtros, estados da consulta e detalhe),
editar e excluir logicamente a injeção de energia mensal (fatura da
operadora), cobrindo as quatro operações em um único fluxo.

Requisitos:
- RF-23849 Cadastro manual de Injeção de Energia mensal (CA 25769 a 25774) - Criar
- RF-23851 Consulta histórica de Injeção de Energia mensal (CA 24913, 24914, 24916, 24917, 36166, 36167 e 36168) - Consultar
- RF-28855 Edição de Injeção de Energia mensal (CA 28857 a 28864, 36312 e 36314) - Atualizar
- RF-23853 Exclusão de Injeção de Energia mensal (CA 24920 a 24922, 36169 e 36170) - Excluir
- US 24954 - Consultar Injeção de Energia mensal (Sprint 04)
- US 28870 - Visualização detalhada da Injeção de Energia (Sprint 04)
- Epic 23763 Valores Injetados na Rede da Operadora

Ator:
- Tesoureiro (cadastra e edita)
- Gestor (consulta e exclui)

Pré-condições:
- Usuários de teste: um Tesoureiro e um Gestor.
- Existem as usinas Usina Solar Alfa e Usina Solar Beta.
- Não existe fatura cadastrada para 03/2026 na Usina Solar Alfa.
- Para os fluxos de consulta A5 a A6, existem também as faturas ativas 02/2026
  Alfa (com PDF anexado ) e 03/2026 Beta (sem PDF). A fatura 02/2026 Alfa
  serve ainda ao A14.
- Para o A7, não existe fatura cadastrada para 12/2020.

Dados de teste:
- Mês/Ano: 03/2026 | Usina: Usina Solar Alfa
- Cadastro: Energia Injetada 1.250,00 kWh | Energia Consumida 980,00 kWh |
  Créditos de Energia 270,00 kWh | Valores Financeiros R$ 412,50
- Edição: Energia Injetada passa para 1.300,00 kWh
- Valores inválidos: "abc", "-10,00" e "1,234"
- Consulta sem resultado: Mês/Ano 12/2020 | Usina Solar Alfa
- Motivo da exclusão: "Fatura de teste lançada em duplicidade"

Resultado esperado (resumo):
A fatura é criada, aparece na consulta (com filtros, estados e detalhe), tem o
dado alterado refletido nas consultas seguintes e, após a exclusão lógica,
some da listagem padrão e só é visível com o filtro "Exibir faturas
excluídas".

Autor: Odilon Francelino de Pontes Neto
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# CRIAR - O Tesoureiro acessa a página de cadastro de injeção de energia
# mensal. [A4] Ele verifica que existem os campos:
# - Mês/Ano
# - Usina
# - Energia Injetada
# - Energia Consumida
# - Créditos de Energia
# - Valores Financeiros
# - PDF da fatura
# - Opção para salvar
# - Opção de cancelar

# O Tesoureiro preenche os campos com os dados do cadastro. [A1][A2][A3]

# O Tesoureiro seleciona a opção para salvar. [RN1][RN2]

# O sistema valida os dados, salva a fatura e confirma o cadastro.

# CONSULTAR - O Tesoureiro acessa a consulta histórica de faturas e filtra
# por 03/2026 e Usina Solar Alfa. [A5][A6][A7][A8]

# O sistema exibe imediatamente (CA05 25773) um item com Mês/Ano 03/2026,
# Usina Solar Alfa e status Ativa; o indicador de PDF anexado aparece como
# não anexado. 

# O Tesoureiro abre a visualização detalhada da fatura (CA08 36167) e
# verifica Mês/Ano, Usina, Status, Energia Injetada 1.250,00 kWh, Energia
# Consumida 980,00 kWh, Créditos de Energia 270,00 kWh e Valores Financeiros
# R$ 412,50, sem PDF anexado.

# ATUALIZAR - O Tesoureiro seleciona a fatura e a opção de editar.
# [A14][A15]

# O sistema exibe a página de edição com os dados da fatura. O ator verifica
# que a Usina não pode ser alterada e que o PDF anexado é opcional (CA02
# 28858 e CA05 28861).

# O Tesoureiro altera somente a Energia Injetada para 1.300,00 kWh, mantendo
# os demais campos (CA04 28860), e salva. [A10][A11][A12][A13]

# O sistema valida, salva as alterações no mesmo registro da fatura, sem
# criar nova versão (CA03 28859), registra a auditoria com ID da fatura,
# usuário, data e hora (CA10 36314) e exibe a mensagem "Edição realizada com
# sucesso." (CA08 28864).

# O Tesoureiro consulta novamente a fatura e verifica na visualização
# detalhada que a Energia Injetada é 1.300,00 kWh e que os demais campos não
# mudaram.

# EXCLUIR - O Gestor autentica, acessa a consulta histórica e localiza a
# fatura 03/2026 da Usina Solar Alfa. Ele verifica que a opção de exclusão
# está visível. [A16]

# O Gestor seleciona a opção "Excluir".

# O sistema exige confirmação e um motivo obrigatório. [A17]

# O Gestor informa o motivo e confirma a exclusão.

# O sistema exclui logicamente a fatura (permanece no banco com a flag
# "excluída", com o motivo, o usuário e a data e a hora), gera o registro de
# auditoria e exibe a mensagem "Fatura excluída com sucesso." (CA07 36170).

# O Gestor consulta a listagem padrão e verifica que a fatura 03/2026 da
# Usina Solar Alfa não aparece.

# O Gestor ativa o filtro "Exibir faturas excluídas" e verifica que a fatura
# aparece com status Excluída. [A9]

# O Gestor abre a visualização detalhada e verifica o motivo da exclusão, o
# usuário responsável e a data e a hora da exclusão (CA09 36168).

# 🟠 [A1] - CRIAR - CADASTRO DUPLICADO [CA03 25771]
# ---------------------------------------------------------------

# O Tesoureiro tenta cadastrar nova fatura para 03/2026 na Usina Solar Alfa,
# já existente e ativa.

# O sistema impede o cadastro e exibe mensagem de erro "já existe uma fatura
# existente e ativa".

# O Tesoureiro consulta e verifica que existe apenas uma fatura para esse
# mês/ano e usina.

# 🟠 [A2] - CRIAR - CAMPOS OBRIGATÓRIOS NÃO PREENCHIDOS [CA02 25770]
# ---------------------------------------------------------------

# O Tesoureiro deixa campos em branco e tenta salvar.

# O sistema impede o salvamento e exibe erro nos campos inválidos.

# A fatura não aparece na consulta.

# 🟠 [A3] - CRIAR - VALOR NUMÉRICO INVÁLIDO [CA02 25770]
# ---------------------------------------------------------------

# O Tesoureiro digita "abc" no campo Energia Injetada e tenta salvar.

# O sistema impede o salvamento e exibe erro.

# 🟠 [A4] - CRIAR - PERFIL SEM PERMISSÃO [CA04 25772]
# ---------------------------------------------------------------

# Um Operador de Usina tenta acessar a página de cadastro.

# O sistema não permite o acesso.

# 🟠 [A5] - CONSULTAR - FILTRAR SOMENTE POR MÊS/ANO OU SOMENTE POR USINA [CA01 24913]
# ---------------------------------------------------------------

# O ator informa apenas o Mês/Ano 03/2026 e aplica o filtro.

# O sistema exibe duas faturas: 03/2026 Alfa e 03/2026 Beta.

# O ator limpa o filtro, seleciona apenas a Usina Solar Alfa e aplica o
# filtro.

# O sistema exibe duas faturas: 02/2026 e 03/2026 da Usina Solar Alfa.

# 🟠 [A6] - CONSULTAR - INDICADOR DE PDF [CA02 24914]
# ---------------------------------------------------------------

# O ator filtra por 02/2026 e Usina Solar Alfa.

# O sistema exibe o item com o indicador de PDF anexado.


# 🟠 [A7] - CONSULTAR - NENHUM RESULTADO [CA04 24917]
# ---------------------------------------------------------------

# O ator informa o Mês/Ano 12/2020 e seleciona a Usina Solar Alfa e aplica
# os filtros.

# O sistema indica o carregamento em andamento e exibe a mensagem
# "Nenhuma fatura encontrada para os filtros informados.".

# O ator verifica que nenhuma linha de fatura é exibida.

# O ator seleciona uma usina sem nenhuma fatura cadastrada e aplica o
# filtro.

# O sistema exibe a mesma mensagem.

# 🟠 [A8] - CONSULTAR - FALHA NA OBTENÇÃO DA LISTA [CA07 36166]
# ---------------------------------------------------------------

# O ator aplica os filtros em um momento em que a obtenção das faturas
# falha.

# O sistema exibe a mensagem "Não foi possível obter as faturas. Tente
# novamente.".

# O sistema não informa que não existem faturas e não exibe a mensagem do
# A8.

# 🟠 [A9] - CONSULTAR - OUTROS PERFIS E O FILTRO DE EXCLUÍDAS [CA03 24916]
# ---------------------------------------------------------------

# Após a exclusão do fluxo principal, o ator autentica como Tesoureiro e
# consulta 03/2026 na Usina Solar Alfa.

# O sistema não disponibiliza o filtro "Exibir faturas excluídas" e a fatura
# 03/2026 não aparece.

# O ator repete o procedimento como Operador de Usina, com o mesmo
# resultado.

# 🟠 [A10] - ATUALIZAR - CANCELAR A EDIÇÃO [CA07 28863]
# ---------------------------------------------------------------

# O Tesoureiro altera a Energia Injetada para 9.999,00 kWh e seleciona
# cancelar.

# O sistema não persiste a alteração.

# O Tesoureiro consulta a fatura e verifica que a Energia Injetada continua
# com o valor anterior.

# 🟠 [A11] - ATUALIZAR - CAMPO OBRIGATÓRIO VAZIO [CA05 28861]
# ---------------------------------------------------------------

# O Tesoureiro apaga a Energia Consumida e tenta salvar.

# O sistema impede o salvamento. Exibe uma mensagem de erro informando
# que esse campo não pode ser vazio.

# 🟠 [A12] - ATUALIZAR - VALOR NUMÉRICO INVÁLIDO [CA06 28862]
# ---------------------------------------------------------------

# O Tesoureiro digita, em campos numéricos diferentes, "abc", "-10,00" e
# "1,234" e tenta salvar a cada vez.

# O sistema aceita apenas números maiores ou iguais a 0 com até 2 casas
# decimais: em cada tentativa gera erro, mostra uma mensagem de erro
# e impede o salvamento.

# 🟠 [A13] - ATUALIZAR - MÊS/ANO JÁ CADASTRADO [CA09 36312]
# ---------------------------------------------------------------

# O Tesoureiro edita a fatura 03/2026 e altera o Mês/Ano para 02/2026, já
# cadastrado na Usina Solar Alfa, e tenta salvar.

# O sistema impede o salvamento e exibe a mensagem "Já existe fatura
# cadastrada para este mês/ano e usina.".

# 🟠 [A14] - ATUALIZAR - FATURA EXCLUÍDA [CA01 28857]
# ---------------------------------------------------------------

# O ator tenta editar uma fatura com status Excluída.

# O sistema não permite a edição.

# 🟠 [A15] - ATUALIZAR - GESTOR NÃO EDITA [CA01 28857]
# ---------------------------------------------------------------

# O Gestor consulta a fatura e procura a opção de editar.

# O sistema não permite a edição ao Gestor: apenas o Tesoureiro tem acesso.

# 🟠 [A16] - EXCLUIR - TESOUREIRO NÃO EXCLUI [CA01 24920]
# ---------------------------------------------------------------

# O Tesoureiro consulta a fatura.

# O sistema não exibe a opção de exclusão para o Tesoureiro.

# 🟠 [A17] - EXCLUIR - CANCELAR A CONFIRMAÇÃO [CA06 36169]
# ---------------------------------------------------------------

# O Gestor seleciona "Excluir" e cancela a confirmação.

# O sistema não exclui a fatura, que permanece com o status anterior
# (Ativa).

# 🟣 [RN1] - VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------

# Na edição, Mês/Ano, Energia Injetada, Energia Consumida, Créditos de
# Energia e Valores Financeiros são obrigatórios e numéricos (maiores ou
# iguais a 0, até 2 casas decimais); o PDF é opcional. No cadastro, as
# regras não estão definidas.

# 🟣 [RN2] - UNICIDADE
# ---------------------------------------------------------------

# Não pode existir mais de uma fatura para o mesmo Mês/Ano e Usina, no
# cadastro (CA03 25771) e na edição (CA09 36312).

# 🟣 [RN3] - PERFIS
# ---------------------------------------------------------------

# Cadastro e edição: Tesoureiro. Consulta: Gestor, Tesoureiro e Operador de
# Usina. Exclusão: Gestor.

# 🟣 [RN4] - EXCLUSÃO LÓGICA
# ---------------------------------------------------------------

# A fatura excluída permanece no banco com a flag "excluída", não aparece na
# listagem padrão e só é exibida com o filtro "Exibir faturas excluídas",
# disponível apenas ao Gestor.

# 🟣 [RN5] - EDIÇÃO
# ---------------------------------------------------------------

# A Usina não pode ser alterada; o PDF anexado pode ser substituído; a
# edição não cria nova versão da fatura.

# 🟣 [RN6] - ESTADOS DA CONSULTA (CA07 36166)
# ---------------------------------------------------------------

# A consulta distingue o carregamento em andamento, a ausência de resultados
# e a falha na obtenção da lista. A falha nunca é apresentada como ausência
# de faturas.
