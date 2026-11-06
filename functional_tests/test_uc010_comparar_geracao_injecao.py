'''
UC011 - Comparar geração dos inversores e injeção da fatura

Objetivo: Exibir, para cada fatura cadastrada, a energia medida pelos inversores, a
energia informada na fatura, a diferença absoluta e a diferença percentual,
usando apenas leituras válidas.

Requisitos:
- RF-23860 Comparação geração x injeção (Epic 23763)
- CA01 (24939) energia medida, energia informada, diferença absoluta (kWh) e diferença percentual
- CA03 (24942) uso apenas de leituras válidas de inversores
- US 24978 - Comparar geração e injeção com sinalização de divergência (Sprint 05)

Ator:
- Gestor (perfis com acesso indefinidos [D20])

Pré-condições:
- Usuário autenticado como Gestor.
- Fatura ativa 03/2026 Alfa com 1.230,00 kWh de energia informada.
- Inversores da Usina Solar Alfa com 1.200,00 kWh de leituras válidas em
  03/2026.

Dados de teste:
- Energia medida: 1.200,00 kWh | Energia informada na fatura: 1.230,00 kWh
- Diferença absoluta: 30,00 kWh (sinal a definir [D15])
- Diferença percentual: 2,5% se a base for a energia medida; 2,44% se for a
  energia da fatura [D15]
- Para o A1: mais 100,00 kWh de leituras sinalizadas como inválidas em 03/2026

Resultado esperado (resumo):
A comparação mostra os quatro valores por fatura e ignora leituras inválidas.

Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders (não foi inventada nenhuma regra):
[D15] Qual a fórmula da diferença percentual (base: energia medida ou energia
      da fatura)? Qual o sinal da diferença absoluta? Qual campo da fatura é
      comparado (Energia Injetada ou Energia Consumida)? Como o período da
      fatura é definido?
[D17] Como uma leitura de inversor passa a ser "inválida" e quem a sinaliza?
[D20] Quais perfis têm acesso à comparação geração x injeção? (a feature não
      define)
[D24] Faturas excluídas logicamente aparecem na comparação geração x injeção?
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de comparação geração x injeção.

# O sistema exibe uma linha para cada fatura cadastrada. [A2][A3]

# O ator localiza a fatura 03/2026 da Usina Solar Alfa.

# O ator verifica que a linha exibe:
# - Energia medida pelos inversores: 1.200,00 kWh
# - Energia informada na fatura: 1.230,00 kWh [D15]
# - Diferença absoluta: 30,00 kWh
# - Diferença percentual: 2,5% ou 2,44% conforme a fórmula [D15]. [A1]

# [A1] - LEITURAS INVÁLIDAS IGNORADAS [CA03]
# ---------------------------------------------------------------

# Existem 100,00 kWh de leituras sinalizadas como inválidas em 03/2026
# [D17].

# O ator abre a comparação da fatura 03/2026 Alfa.

# O sistema exibe energia medida de 1.200,00 kWh, sem somar as leituras
# inválidas.

# [A2] - VÁRIAS FATURAS
# ---------------------------------------------------------------

# Existem faturas 03/2026 Alfa e 04/2026 Alfa.

# O sistema exibe uma linha de comparação para cada uma, com seus próprios
# valores.

# [A3] - FATURA EXCLUÍDA LOGICAMENTE
# ---------------------------------------------------------------

# Existe uma fatura excluída logicamente.

# Resultado esperado: NÃO DEFINIDO [D24].

# [RN1] - DADOS VÁLIDOS
# ---------------------------------------------------------------

# A energia medida usa apenas leituras válidas de inversores.

# [RN2] - FÓRMULA
# ---------------------------------------------------------------

# Fórmula da diferença percentual e campo da fatura comparado indefinidos
# [D15].

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------