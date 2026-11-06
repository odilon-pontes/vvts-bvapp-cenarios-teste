'''
UC013 - Informar ausência de dados de inversores na comparação

Objetivo: Informar explicitamente a ausência de dados de inversores para o período da
fatura, sem calcular divergência.

Requisitos:
- RF-23860 Comparação geração x injeção (Epic 23763)
- CA04 (24943) informar a ausência de dados, sem calcular divergência
- CA05 (28866) informar ausência de dados de inversores (duplica o CA04)

Ator:
- Gestor (perfis com acesso indefinidos [D20])

Pré-condições:
- Usuário autenticado como Gestor.
- Fatura ativa 06/2026 Alfa com 1.100,00 kWh informados.
- Não existem medições de inversores da Usina Solar Alfa em 06/2026.

Dados de teste:
- Fatura: 06/2026 | Usina Solar Alfa | Energia informada 1.100,00 kWh
- Medições em 06/2026: nenhuma

Resultado esperado (resumo):
O sistema informa a ausência de dados e não exibe divergência, nem diferenças
calculadas, nem sinalização de inconsistência.

Autor:  Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D18] Se só parte do período da fatura tem dados de inversores, a divergência
      é calculada? (Os critérios 24943 e 28866 são duplicados.)
[D20] Quais perfis têm acesso à comparação geração x injeção? (a feature não
      define)
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de comparação geração x injeção.

# O ator localiza a fatura 06/2026 da Usina Solar Alfa.

# O sistema informa explicitamente que não há dados de inversores para o
# período da fatura (texto não definido).

# O ator verifica que a diferença absoluta e a diferença percentual não são
# calculadas (não exibem valor numérico, nem zero).

# O ator verifica que a fatura não recebe a sinalização de inconsistência
# (UC012). [A1]

# [A1] - DADOS PARCIAIS NO PERÍODO
# ---------------------------------------------------------------

# Existem medições só em parte de 06/2026 (ex.: primeiros 10 dias).

# Resultado esperado: NÃO DEFINIDO [D18].

# [RN1] - CRITÉRIOS DUPLICADOS
# ---------------------------------------------------------------

# Os CAs 24943 e 28866 descrevem o mesmo comportamento; um único cenário os
# cobre [D18].

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------