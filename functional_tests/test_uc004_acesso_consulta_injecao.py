'''
UC004 - Controlar acesso à consulta de injeção de energia por perfil

Objetivo: Garantir que os perfis Gestor, Tesoureiro e Operador de Usina acessem a
consulta histórica de faturas e que os demais perfis não a visualizem nem a
acessem diretamente.

Requisitos:
- RF-23851 Consulta histórica de Injeção de Energia mensal (Epic 23763)
- CA05 (24919) perfis com acesso; demais perfis não visualizam e têm o acesso direto recusado

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
Os três perfis autorizados acessam a consulta e visualizam as faturas; o
Técnico de Manutenção não vê a funcionalidade e tem o acesso direto recusado.

Autor: Odilon Francelino de Pontes Neto
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator, autenticado como Gestor, verifica que o menu exibe a consulta
# histórica de faturas e a seleciona.

# O sistema exibe a página de consulta com os filtros.

# O ator aplica o filtro por Usina Solar Alfa. [RN1]

# O sistema exibe as faturas da usina.

# 🟠 [A1] - ACESSO COMO TESOUREIRO
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro e executa o fluxo principal.

# O sistema permite o acesso e exibe as faturas.

# 🟠 [A2] - ACESSO COMO OPERADOR DE USINA
# ---------------------------------------------------------------

# O ator autentica como Operador de Usina e executa o fluxo principal.

# O sistema permite o acesso e exibe as faturas.

# 🟠 [A3] - MENU DO TÉCNICO DE MANUTENÇÃO
# ---------------------------------------------------------------

# O ator autentica como Técnico de Manutenção e examina o menu.

# O sistema não exibe a consulta histórica de faturas no menu.

# 🟠 [A4] - ACESSO DIRETO PELO TÉCNICO DE MANUTENÇÃO
# ---------------------------------------------------------------

# O ator, autenticado como Técnico de Manutenção, tenta abrir diretamente o
# endereço da consulta histórica de faturas.

# O sistema recusa o acesso e não exibe faturas.

# 🟣 [RN1] - PERFIS AUTORIZADOS
# ---------------------------------------------------------------

# Têm acesso: Gestor, Tesoureiro e Operador de Usina. Os demais perfis não
# visualizam a funcionalidade e têm o acesso direto recusado.
