'''
UC001 - Consultar histórico de medições

Objetivo: Permitir que o usuário autorizado consulte as medições coletadas dos
inversores filtrando por período obrigatório, usina e inversor, com resultados
paginados e ordenados do mais recente para o mais antigo.

Requisitos:
- RF-23834 Consulta histórica de medições (Epic 23761)
- CA01 (24993) filtros Data de Início, Data de Fim, Usina e Inversor
- CA02 (24994) resultados paginados com controle de navegação
- CA03 (24995) primeira página em até 3 segundos para períodos de até 12 meses
- CA04 (24996) mensagem quando não há resultados
- CA06 (36162) listas de Usina e de Inversor
- CA07 (36163) limites do período e Data de Fim anterior à Data de Início
- CA08 (36164) colunas e ordenação padrão
- CA09 (36165) carregamento, ausência de resultados e falha
- US 24902 - Filtrar e Buscar medições de Inversores (Sprint 03)

Ator:
- Gestor (também Operador de Usina e Técnico de Manutenção, ver UC002)

Pré-condições:
- Usuário autenticado como Gestor, com acesso às usinas Usina Solar Alfa e
  Usina Solar Beta.
- Existem medições coletadas em 03/2026 para a Usina Solar Alfa (INV-01 e
  INV-02) e para a Usina Solar Beta (INV-03).
- Existem mais medições de INV-01 em 03/2026 do que cabem em uma página.
- Existe medição de INV-01 em 31/03/2026 às 23h45min e em 01/04/2026 às
  00h00min.

Dados de teste:
- Data de Início: 01/03/2026 | Data de Fim: 31/03/2026
- Usina: Usina Solar Alfa | Inversor: INV-01
- Período sem medições (negativo): 01/01/2020 a 31/01/2020
- Datas invertidas: Data de Início 31/03/2026 e Data de Fim 01/03/2026

Resultado esperado (resumo):
Somente as medições que atendem a todos os filtros são listadas, de forma
paginada e da mais recente para a mais antiga; sem resultados ou com falha, o
sistema exibe a mensagem definida.

Autor: Odilon Francelino de Pontes Neto
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de consulta histórica de medições. Ele verifica que
# existem os campos de filtro:
# - Data de Início
# - Data de Fim
# - Usina
# - Inversor
# - Nível Severidade
# - Opção para aplicar os filtros

# O ator verifica que o campo Usina lista, em ordem alfabética, apenas as
# usinas às quais ele tem acesso: Usina Solar Alfa e Usina Solar Beta. [A7]

# O ator preenche a Data de Início com 01/03/2026 e a Data de Fim com
# 31/03/2026 e seleciona a Usina Solar Alfa. [A1][A2][A5][A6][A8]

# O sistema passa a listar no campo Inversor apenas os inversores da Usina
# Solar Alfa: INV-01 e INV-02. O ator seleciona INV-01. [RN3]

# O ator seleciona a opção para aplicar os filtros. [A3][A4][A9] [RN1][RN2]

# O sistema indica o carregamento em andamento e exibe a lista de
# medições correspondentes aos filtros.

# O ator verifica que cada linha exibe o timestamp da medição (data e hora),
# o Inversor, a Usina e o valor medido (kWh), e que todas as
# linhas são do inversor INV-01, da Usina Solar Alfa, com timestamp entre
# 01/03/2026 e 31/03/2026.

# O ator verifica que a lista está ordenada pelo timestamp em ordem
# decrescente, da medição mais recente para a mais antiga.

# O ator verifica que nenhuma medição de outro inversor ou de outro período
# está na lista.

# 🟠 [A1] - FILTRAR POR PERÍODO E USINA, SEM INVERSOR
# ---------------------------------------------------------------

# O ator preenche o período e a Usina Solar Alfa, sem selecionar inversor, e
# aplica os filtros.

# O sistema exibe medições de INV-01 e INV-02 e nenhuma medição de INV-03.

# 🟠 [A2] - FILTRAR SOMENTE POR PERÍODO
# ---------------------------------------------------------------

# O ator preenche somente a Data de Início e a Data de Fim, sem usina nem
# inversor, e aplica os filtros.

# O sistema exibe medições de todas as usinas e inversores às quais o ator
# tem acesso, dentro do período.

# 🟠 [A3] - NAVEGAR ENTRE PÁGINAS [CA02]
# ---------------------------------------------------------------

# O ator executa o fluxo principal com um filtro que retorna mais registros
# do que cabem em uma página.

# O sistema exibe a primeira página e um controle de navegação entre
# páginas.

# O ator seleciona a próxima página.

# O sistema exibe a segunda página, sem repetir registros da primeira e
# mantendo os filtros aplicados.

# O ator retorna à primeira página e verifica que os registros iniciais
# continuam os mesmos.

# 🟠 [A4] - NENHUM RESULTADO [CA04]
# ---------------------------------------------------------------

# O ator informa o período de 01/01/2020 a 31/01/2020 e aplica os filtros.

# O sistema exibe a mensagem "Nenhuma medição encontrada para os filtros
# informados." e não exibe linhas de resultado.

# 🟠 [A5] - DATA DE FIM ANTERIOR À DATA DE INÍCIO [CA07]
# ---------------------------------------------------------------

# O ator informa Data de Início 31/03/2026 e Data de Fim 01/03/2026 e tenta
# aplicar os filtros.

# O sistema não executa a consulta e exibe a mensagem "A Data de Fim não
# pode ser anterior à Data de Início.".

# 🟠 [A6] - LIMITES DO PERÍODO INCLUEM AS DATAS INFORMADAS [CA07]
# ---------------------------------------------------------------

# O ator informa Data de Início 01/03/2026 e Data de Fim 31/03/2026,
# seleciona INV-01 e aplica os filtros.

# O sistema exibe a medição de INV-01 de 31/03/2026 às 23h45min.

# O sistema não exibe a medição de INV-01 de 01/04/2026 às 00h00min.

# 🟠 [A7] - USUÁRIO COM ACESSO A UMA ÚNICA USINA [CA06]
# ---------------------------------------------------------------

# O ator autentica com um usuário que tem acesso apenas à Usina Solar Alfa e
# acessa a consulta.

# O campo Usina lista somente a Usina Solar Alfa e o campo Inversor não
# oferece INV-03.

# 🟠 [A8] - PERÍODO NÃO INFORMADO [CA01]
# ---------------------------------------------------------------

# O ator preenche somente a Usina Solar Alfa, deixando Data de Início e Data
# de Fim em branco, e tenta aplicar os filtros.

# Resultado esperado: o sistema não executa a consulta, pois as datas são
# obrigatórias. A forma como o sistema informa é exibindo a mensagem 
# "Data de início e Data de fim são obrigatórios.".

# 🟠 [A9] - FALHA NA OBTENÇÃO DA LISTA [CA09]
# ---------------------------------------------------------------

# O ator aplica os filtros em um momento em que a obtenção das medições
# falha.

# O sistema exibe a mensagem "Não foi possível obter as medições. Tente
# novamente.".

# O sistema não informa que não existem medições e não exibe a mensagem de
# ausência de resultados do A4.

# 🟣 [RN1] - FILTROS
# ---------------------------------------------------------------

# Data de Início e Data de Fim são obrigatórias; Usina e Inversor são
# opcionais. A consulta retorna somente as medições que atendem a todos os
# filtros informados, com os limites do período incluídos.

# 🟣 [RN2] - DESEMPENHO (CA03 24995)
# ---------------------------------------------------------------

# Consultas com período de até 12 meses exibem a primeira página em até 3
# segundos, contados do acionamento da consulta. As condições de carga e o
# comportamento acima de 12 meses não estão definidos; a verificação
# fica para testes não funcionais.

# 🟣 [RN3] - LISTAS DEPENDENTES (CA06 36162)
# ---------------------------------------------------------------

# O campo Usina lista só as usinas acessíveis ao usuário, em ordem
# alfabética; o campo Inversor lista só os inversores da usina selecionada.
