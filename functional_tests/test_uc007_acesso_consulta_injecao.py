'''
UC007 - Controlar acesso à consulta de injeção de energia por perfil

Objetivo: Garantir que os perfis Gestor, Tesoureiro e Operador de Usina acessem a
consulta histórica de injeção de energia mensal.

Requisitos:
- RF-23851 Consulta histórica de Injeção de Energia mensal (Epic 23763)
- CA05 (24919) acesso dos perfis Gestor, Tesoureiro e Operador de Usina

Ator:
- Gestor
- Tesoureiro
- Operador de Usina
- Técnico de Manutenção (verificação de acesso negado)

Pré-condições:
- Existem usuários de teste, um para cada perfil.
- Existe ao menos uma fatura ativa cadastrada.

Dados de teste:
- Um usuário por perfil: Gestor, Tesoureiro, Operador de Usina, Técnico de
  Manutenção.

Resultado esperado (resumo):
Os três perfis autorizados acessam a consulta e visualizam as faturas.

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
# histórica de faturas.

# O sistema exibe a página de consulta com os filtros.

# O ator aplica o filtro por usina "Usina Solar Alfa". [RN1]

# O sistema exibe as faturas da usina.

# [A1] - ACESSO COMO TESOUREIRO
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro e executa o fluxo principal.

# O sistema permite o acesso e exibe as faturas.

# [A2] - ACESSO COMO OPERADOR DE USINA
# ---------------------------------------------------------------

# O ator autentica como Operador de Usina e executa o fluxo principal.

# O sistema permite o acesso e exibe as faturas.

# [A3] - ACESSO COMO TÉCNICO DE MANUTENÇÃO
# ---------------------------------------------------------------

# O ator autentica como Técnico de Manutenção e tenta acessar a consulta de
# faturas.

# Resultado esperado: NÃO DEFINIDO [D05].

# [RN1] - PERFIS AUTORIZADOS
# ---------------------------------------------------------------

# Têm acesso: Gestor, Tesoureiro e Operador de Usina.

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------