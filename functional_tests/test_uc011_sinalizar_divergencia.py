'''
UC012 - Sinalizar divergência acima da tolerância

Objetivo: Sinalizar visualmente a inconsistência quando a divergência entre geração e
injeção supera o percentual de tolerância configurado.

Requisitos:
- RF-23860 Comparação geração x injeção (Epic 23763)
- CA02 (24941) sinalização visual quando a divergência supera a tolerância

Ator:
- Gestor (perfis com acesso indefinidos [D20])

Pré-condições:
- Usuário autenticado como Gestor.
- Tolerância configurada em 5% (valor apenas de teste; quem configura e o
  valor padrão são indefinidos [D16]).
- Fatura A: 03/2026 Alfa, medida 1.200,00 kWh, informada 1.230,00 kWh
  (dentro).
- Fatura B: 04/2026 Alfa, medida 1.000,00 kWh, informada 1.200,00 kWh (fora).

Dados de teste:
- Fatura A: diferença 30,00 kWh (2,5% ou 2,44%) -> dentro de 5%
- Fatura B: diferença 200,00 kWh (20% ou 16,67%) -> acima de 5% em qualquer
  fórmula

Resultado esperado (resumo):
Somente a fatura acima da tolerância é sinalizada.

Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D15] Qual a fórmula da diferença percentual (base: energia medida ou energia
      da fatura)? Qual o sinal da diferença absoluta? Qual campo da fatura é
      comparado (Energia Injetada ou Energia Consumida)? Como o período da
      fatura é definido?
[D16] Quem configura o percentual de tolerância, onde, e qual o valor padrão?
      Divergência "supera" significa > ou >=?
[D19] Qual a forma da sinalização visual da divergência (cor, ícone, rótulo)?
[D20] Quais perfis têm acesso à comparação geração x injeção? (a feature não
      define)
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de comparação geração x injeção.

# O ator localiza a fatura A (03/2026 Alfa) e verifica que a linha não tem
# sinalização de inconsistência.

# O ator localiza a fatura B (04/2026 Alfa) e verifica que a linha exibe a
# sinalização visual de inconsistência [D19]. [A1][A2]

# [A1] - DIVERGÊNCIA IGUAL À TOLERÂNCIA
# ---------------------------------------------------------------

# Fatura C: medida 1.000,00 kWh e informada 1.050,00 kWh (5% se a base for a
# medida).

# Resultado esperado: NÃO DEFINIDO [D16][D15]. Depende de "supera" ser > ou
# >= e da base do percentual.

# [A2] - ALTERAÇÃO DA TOLERÂNCIA
# ---------------------------------------------------------------

# A tolerância é alterada para 1% (se existir tela de configuração [D16]).

# O sistema passa a sinalizar também a fatura A (2,5% ou 2,44% > 1%).

# [RN1] - TOLERÂNCIA
# ---------------------------------------------------------------

# Sinaliza-se quando a divergência supera a tolerância configurada; a regra
# de configuração é indefinida [D16].

# [RN2] - FORMA DA SINALIZAÇÃO
# ---------------------------------------------------------------

# Indefinida [D19]; o teste verifica a presença de algum indicador visual.

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------