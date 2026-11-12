'''
UC011 - Sinalizar divergência acima da tolerância

Objetivo: Sinalizar visualmente a inconsistência quando a Diferença Percentual é maior
que o percentual de tolerância configurado, e não sinalizar enquanto a
tolerância não estiver configurada.

Requisitos:
- RF-23860 Comparação geração x injeção (Epic 23763)
- CA02 (24941) sinalização "Divergente" ou "Dentro da tolerância"
- CA10 (36176) tolerância não configurada
- RF-36181 Configuração do percentual de tolerância de divergência (apoio)

Ator:
- Gestor/Administrador
- Tesoureiro

Pré-condições:
- Usuário autenticado como Gestor/Administrador [D10].
- Tolerância configurada em 5% conforme o UC015 (valor apenas de teste).
- Fatura A: 03/2026 Alfa, Energia Medida 1.200,00 kWh e Energia Injetada
  1.230,00 kWh.
- Fatura B: 04/2026 Alfa, Energia Medida 1.000,00 kWh e Energia Injetada
  1.200,00 kWh.
- Fatura C: 05/2026 Alfa, Energia Medida 1.000,00 kWh e Energia Injetada
  1.050,00 kWh.

Dados de teste:
- Fatura A: diferença 30,00 kWh = 2,5% (menor que 5%)
- Fatura B: diferença 200,00 kWh = 20% (maior que 5%)
- Fatura C: diferença 50,00 kWh = 5% (igual a 5%)

Resultado esperado (resumo):
Somente a fatura com Diferença Percentual maior que a tolerância recebe o
ícone de alerta e o rótulo "Divergente"; as demais exibem "Dentro da
tolerância".

Versão dos requisitos: Work packages de 12/11/2026
Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D10] "Gestor/Administrador" é o mesmo perfil de "Gestor" (usado nas Features
      23834 e 23851) ou são perfis distintos?
[D16] Existe valor padrão para o percentual de tolerância e em que menu fica a
      configuração? Enquanto não configurado, as linhas exibem o rótulo
      "Dentro da tolerância"?
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de comparação geração x injeção.

# O ator localiza a fatura A (03/2026 Alfa) e verifica que a linha exibe o
# rótulo "Dentro da tolerância" e não exibe o ícone de alerta.

# O ator localiza a fatura B (04/2026 Alfa) e verifica que a linha exibe o
# ícone de alerta e o rótulo "Divergente". [A1][A2][A3] [RN1]

# 🟠 [A1] - DIVERGÊNCIA IGUAL À TOLERÂNCIA
# ---------------------------------------------------------------

# O ator localiza a fatura C (05/2026 Alfa), com Diferença Percentual de 5%
# e tolerância de 5%.

# O sistema exibe o rótulo "Dentro da tolerância", pois a divergência não é
# maior que a tolerância.

# 🟠 [A2] - ALTERAÇÃO DA TOLERÂNCIA
# ---------------------------------------------------------------

# O Gestor/Administrador altera a tolerância para 1% (UC015).

# O ator reabre a comparação.

# A fatura A (2,5%) passa a exibir o ícone de alerta e o rótulo
# "Divergente".

# 🟠 [A3] - TOLERÂNCIA NÃO CONFIGURADA [CA10 36176]
# ---------------------------------------------------------------

# Nenhum percentual de tolerância foi configurado [D16].

# O ator acessa a comparação.

# O sistema exibe a comparação, informa "Percentual de tolerância não
# configurado." e não exibe o ícone de alerta nem o rótulo "Divergente" em
# nenhuma fatura.

# 🟣 [RN1] - REGRA DA SINALIZAÇÃO
# ---------------------------------------------------------------

# Sinaliza-se quando a Diferença Percentual é maior que o percentual de
# tolerância configurado. O ícone de alerta e o rótulo "Divergente"
# identificam a inconsistência; caso contrário, o rótulo é "Dentro da
# tolerância".

# 🟣 [RN2] - TOLERÂNCIA
# ---------------------------------------------------------------

# Valor único, configurado pelo Gestor/Administrador (UC015). Não há valor
# padrão definido nos requisitos [D16].
