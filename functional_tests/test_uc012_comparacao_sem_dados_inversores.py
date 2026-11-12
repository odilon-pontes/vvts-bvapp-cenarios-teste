'''
UC012 - Informar ausência de dados de inversores na comparação

Objetivo: Informar a ausência de leituras válidas de inversores para a Usina e o Mês/Ano
da fatura, sem calcular diferenças nem sinalizar divergência, e tratar Energia
Medida igual a zero.

Requisitos:
- RF-23860 Comparação geração x injeção (Epic 23763)
- CA04 (24943) ausência de leituras válidas
- CA09 (36175) Energia Medida igual a zero

Ator:
- Gestor/Administrador
- Tesoureiro

Pré-condições:
- Usuário autenticado como Gestor/Administrador.
- Fatura ativa 06/2026 Alfa com Energia Injetada 1.100,00 kWh.
- Não existem leituras válidas de inversores da Usina Solar Alfa em 06/2026.
- Para o A1, fatura ativa 07/2026 Alfa com leituras válidas somando 0,00 kWh.

Dados de teste:
- Fatura: 06/2026 | Usina Solar Alfa | Energia Injetada 1.100,00 kWh
- Leituras válidas em 06/2026: nenhuma
- Fatura do A1: 07/2026 | Energia Medida 0,00 kWh

Resultado esperado (resumo):
Sem leituras válidas, o sistema exibe a mensagem de ausência e não calcula
diferenças nem sinaliza divergência; com Energia Medida igual a zero, exibe
"Não calculável" no percentual.

Versão dos requisitos: Work packages de 12/11/2026
Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D15] Quando há leituras em apenas parte do mês, o sistema calcula a
      comparação com as leituras existentes ou avisa a cobertura parcial?
      Quando a Energia Medida é zero e a Energia Injetada é maior que zero, a
      fatura é sinalizada?
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de comparação geração x injeção.

# O ator localiza a fatura 06/2026 da Usina Solar Alfa.

# O sistema exibe a mensagem "Sem dados de inversores para o período da
# fatura.".

# O ator verifica que a Diferença Absoluta e a Diferença Percentual não são
# calculadas (não exibem valor numérico, nem zero).

# O ator verifica que a fatura não recebe o ícone de alerta nem o rótulo
# "Divergente". [A1][A2]

# 🟠 [A1] - ENERGIA MEDIDA IGUAL A ZERO [CA09 36175]
# ---------------------------------------------------------------

# O ator localiza a fatura 07/2026 da Usina Solar Alfa, cuja Energia Medida
# é 0,00 kWh.

# O sistema exibe a Diferença Percentual como "Não calculável", sem exibir
# erro nem valor infinito.

# Se a fatura deve ser sinalizada quando a Energia Injetada é maior que zero
# é NÃO DEFINIDO [D15].

# 🟠 [A2] - DADOS PARCIAIS NO PERÍODO
# ---------------------------------------------------------------

# Existem leituras válidas apenas nos primeiros 10 dias de 06/2026.

# Resultado esperado: NÃO DEFINIDO [D15]. Pela regra da Energia Medida, a
# soma usaria as leituras existentes, mas o requisito não trata cobertura
# parcial.

# 🟣 [RN1] - AUSÊNCIA DE LEITURAS VÁLIDAS
# ---------------------------------------------------------------

# Sem leituras válidas para a Usina e o Mês/Ano da fatura, o sistema exibe a
# mensagem, não calcula as diferenças e não sinaliza divergência.

# 🟣 [RN2] - DIVISÃO POR ZERO
# ---------------------------------------------------------------

# Com Energia Medida igual a zero, a Diferença Percentual não é calculada e
# exibe "Não calculável".
