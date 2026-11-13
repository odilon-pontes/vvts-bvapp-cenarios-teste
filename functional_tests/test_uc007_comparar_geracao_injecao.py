'''
UC007 - Comparar geração dos inversores e injeção da fatura

Objetivo: Exibir, para cada fatura ativa, a Energia Medida pelos inversores, a Energia
Injetada informada na fatura, a Diferença Absoluta e a Diferença Percentual,
usando apenas leituras válidas.

Requisitos:
- RF-23860 Comparação geração x injeção (Epic 23763)
- CA01 (24939) valores exibidos por fatura
- CA03 (24942) apenas leituras válidas
- CA06 (36172) fórmulas das diferenças
- CA07 (36173) período da Energia Medida
- CA08 (36174) uso da Energia Injetada
- CA11 (36177) perfis com acesso
- CA12 (36178) faturas Excluídas fora da comparação
- CA13 (36179) ordenação e paginação
- CA14 (36180) carregamento, ausência de faturas e falha
- US 24978 - Comparar geração e injeção de energia com sinalização de divergência (Sprint 05)

Ator:
- Gestor
- Tesoureiro

Pré-condições:
- Usuário autenticado como Gestor.
- Fatura ativa 03/2026 Alfa com Energia Injetada 1.230,00 kWh, Energia
  Consumida 980,00 kWh e Créditos de Energia 270,00 kWh.
- Inversores da Usina Solar Alfa com 1.200,00 kWh de leituras válidas em
  03/2026.

Dados de teste:
- Energia Medida: 1.200,00 kWh | Energia Injetada: 1.230,00 kWh
- Diferença Absoluta: |1.230,00 - 1.200,00| = 30,00 kWh
- Diferença Percentual: 30,00 / 1.200,00 x 100 = 2,5% (casas decimais conforme)
- A1: mais 100,00 kWh de leituras sinalizadas como inválidas em 03/2026
- A4: leitura de 50,00 kWh em 01/04/2026 às 00h00min e leitura em 31/03/2026
  às 23h59min59s
- A3: fatura 05/2026 Alfa com status Excluída

Resultado esperado (resumo):
A linha de cada fatura exibe os quatro valores corretos, calculados com a
Energia Injetada e as leituras válidas do mês da fatura; faturas Excluídas não
aparecem.

Autor: Odilon Francelino de Pontes Neto
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de comparação geração x injeção.

# O sistema exibe uma linha para cada fatura ativa. [A2][A3][A6][A7][A8][A9]

# O ator localiza a fatura 03/2026 da Usina Solar Alfa.

# O ator verifica que a linha exibe:
# - Mês/Ano 03/2026 e Usina Solar Alfa
# - Energia Medida: 1.200,00 kWh
# - Energia Injetada: 1.230,00 kWh
# - Diferença Absoluta: 30,00 kWh
# - Diferença Percentual: 2,5%. [A1][A4][A5] [RN1]

# 🟠 [A1] - LEITURAS INVÁLIDAS IGNORADAS [CA03 24942]
# ---------------------------------------------------------------

# Existem 100,00 kWh de leituras sinalizadas como inválidas em 03/2026.

# O ator abre a comparação da fatura 03/2026 Alfa.

# O sistema exibe Energia Medida de 1.200,00 kWh, sem somar as leituras
# inválidas.

# 🟠 [A2] - VÁRIAS FATURAS, ORDENAÇÃO E PAGINAÇÃO [CA13 36179]
# ---------------------------------------------------------------

# Existem faturas 03/2026 e 04/2026 da Usina Solar Alfa e mais faturas que
# excedem a primeira página.

# O sistema exibe as faturas ordenadas por Mês/Ano em ordem decrescente,
# cada uma com seus próprios valores.

# O sistema exibe 10 registros por página por padrão e oferece as opções 50,
# 100 e Todos.

# O sistema informa a página atual, o total de páginas e o total de
# registros, e os mantém ao trocar de página.

# 🟠 [A3] - FATURA EXCLUÍDA NÃO ENTRA NA COMPARAÇÃO [CA12 36178]
# ---------------------------------------------------------------

# Existe a fatura 05/2026 Alfa com status Excluída.

# O ator procura essa fatura na comparação.

# O sistema não exibe a fatura 05/2026.

# 🟠 [A4] - PERÍODO DA ENERGIA MEDIDA [CA07 36173]
# ---------------------------------------------------------------

# O ator abre a comparação da fatura 03/2026 Alfa.

# O sistema soma as leituras do primeiro dia (00h00min00s) ao último dia
# (23h59min59s) de março, incluindo a de 31/03/2026 às 23h59min59s.

# O sistema não soma a leitura de 50,00 kWh de 01/04/2026 às 00h00min.

# 🟠 [A5] - ENERGIA CONSUMIDA E CRÉDITOS NÃO ENTRAM NO CÁLCULO [CA08 36174]
# ---------------------------------------------------------------

# O ator verifica que a fatura 03/2026 tem Energia Consumida 980,00 kWh e
# Créditos de Energia 270,00 kWh.

# A Diferença Absoluta continua 30,00 kWh, calculada somente com a Energia
# Injetada e a Energia Medida.

# 🟠 [A6] - NENHUMA FATURA CADASTRADA [CA14 36180]
# ---------------------------------------------------------------

# O ator acessa a comparação em um ambiente sem faturas cadastradas.

# O sistema exibe a mensagem "Nenhuma fatura cadastrada para comparação.".

# 🟠 [A7] - FALHA NA OBTENÇÃO DOS DADOS [CA14 36180]
# ---------------------------------------------------------------

# O ator acessa a comparação em um momento em que a obtenção dos dados
# falha.

# O sistema exibe a falha, com texto "Falha na obtenção dos dados", e não exibe a
# mensagem "Nenhuma fatura cadastrada para comparação.".

# 🟠 [A8] - ACESSO COMO TESOUREIRO [CA11 36177]
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro e acessa a comparação.

# O sistema permite o acesso e exibe os mesmos valores.

# 🟠 [A9] - ACESSO DE PERFIL NÃO AUTORIZADO [CA11 36177]
# ---------------------------------------------------------------

# O ator autentica como Operador de Usina e examina o menu.

# O sistema não exibe a comparação geração x injeção no menu.

# O ator tenta abrir diretamente o endereço da comparação.

# O sistema recusa o acesso.

# 🟣 [RN1] - FÓRMULAS (CA06 36172)
# ---------------------------------------------------------------

# Diferença Absoluta é o módulo da diferença entre a Energia Injetada e a
# Energia Medida, em kWh. Diferença Percentual é a Diferença Absoluta
# dividida pela Energia Medida e multiplicada por 100.

# 🟣 [RN2] - DADOS DE ENTRADA
# ---------------------------------------------------------------

# Energia Medida é a soma das leituras válidas dos inversores da Usina da
# fatura no mês da fatura. A comparação usa o campo Energia Injetada da
# fatura.

# 🟣 [RN3] - PERFIS
# ---------------------------------------------------------------

# Têm acesso Gestor e Tesoureiro.
