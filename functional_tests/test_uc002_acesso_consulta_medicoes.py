'''
UC002 - Controlar acesso à consulta histórica de medições por perfil

Objetivo: Garantir que os perfis Gestor, Operador de Usina e Técnico de Manutenção
acessem a consulta histórica de medições.

Requisitos:
- RF-23834 Consulta histórica de medições (Epic 23761)
- CA05 (24997) acesso dos perfis Gestor, Operador de Usina e Técnico de Manutenção

Ator:
- Gestor
- Operador de Usina
- Técnico de Manutenção
- Tesoureiro (verificação de acesso negado)

Pré-condições:
- Existem usuários de teste, um para cada perfil acima.
- Existem medições coletadas para a Usina Solar Alfa.

Dados de teste:
- Um usuário por perfil: Gestor, Operador de Usina, Técnico de Manutenção,
  Tesoureiro.

Resultado esperado (resumo):
Os três perfis autorizados acessam a consulta e visualizam os filtros e
resultados; o perfil não listado tem o comportamento definido após
esclarecimento.

Autor:  Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D05] Os perfis não listados nos critérios (ex.: Tesoureiro na consulta de
      medições; Técnico de Manutenção na consulta de faturas) devem ter o
      acesso negado? De que forma (menu oculto, mensagem, redirecionamento)? E
      o usuário não autenticado?
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator, autenticado como Gestor, acessa o menu e seleciona a consulta
# histórica de medições.

# O sistema exibe a página de consulta histórica de medições com os campos
# de filtro.

# O ator aplica o filtro por usina "Usina Solar Alfa". [RN1]

# O sistema exibe as medições da usina.

# [A1] - ACESSO COMO OPERADOR DE USINA
# ---------------------------------------------------------------

# O ator autentica como Operador de Usina e executa o fluxo principal.

# O sistema permite o acesso e exibe os mesmos resultados.

# [A2] - ACESSO COMO TÉCNICO DE MANUTENÇÃO
# ---------------------------------------------------------------

# O ator autentica como Técnico de Manutenção e executa o fluxo principal.

# O sistema permite o acesso e exibe os mesmos resultados.

# [A3] - ACESSO COMO TESOUREIRO
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro e tenta acessar a consulta de medições.

# Resultado esperado: NÃO DEFINIDO nos requisitos [D05]. Os critérios só
# listam os três perfis autorizados e não dizem como o acesso é negado.

# [RN1] - PERFIS AUTORIZADOS
# ---------------------------------------------------------------

# Têm acesso: Gestor, Operador de Usina e Técnico de Manutenção.

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------