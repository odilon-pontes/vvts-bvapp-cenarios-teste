'''
UC002 - Controlar acesso à consulta histórica de medições por perfil

Objetivo: Garantir que os perfis Gestor, Operador de Usina e Técnico de Manutenção
acessem a consulta histórica de medições e que os demais perfis não a
visualizem nem a acessem diretamente.

Requisitos:
- RF-23834 Consulta histórica de medições (Epic 23761)
- CA05 (24997) perfis com acesso; demais perfis não visualizam e têm o acesso direto recusado

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
- Filtro: Usina Solar Alfa, de 01/03/2026 a 31/03/2026.

Resultado esperado (resumo):
Os três perfis autorizados acessam a consulta e visualizam as medições; o
Tesoureiro não vê a funcionalidade e tem o acesso direto recusado.

Autor: Odilon Francelino de Pontes Neto
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator, autenticado como Gestor, verifica que o menu exibe a consulta
# histórica de medições e a seleciona.

# O sistema exibe a página de consulta histórica de medições com os campos
# de filtro.

# O ator aplica o período de 01/03/2026 a 31/03/2026 e a Usina Solar Alfa.
# [RN1]

# O sistema exibe as medições da usina.

# 🟠 [A1] - ACESSO COMO OPERADOR DE USINA
# ---------------------------------------------------------------

# O ator autentica como Operador de Usina e executa o fluxo principal.

# O sistema permite o acesso e exibe os mesmos resultados.

# 🟠 [A2] - ACESSO COMO TÉCNICO DE MANUTENÇÃO
# ---------------------------------------------------------------

# O ator autentica como Técnico de Manutenção e executa o fluxo principal.

# O sistema permite o acesso e exibe os mesmos resultados.

# 🟠 [A3] - MENU DO TESOUREIRO
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro e examina o menu.

# O sistema não exibe a consulta histórica de medições no menu.

# 🟠 [A4] - ACESSO DIRETO PELO TESOUREIRO
# ---------------------------------------------------------------

# O ator, autenticado como Tesoureiro, tenta abrir diretamente o endereço da
# consulta histórica de medições.

# O sistema recusa o acesso e não exibe medições.

# 🟣 [RN1] - PERFIS AUTORIZADOS
# ---------------------------------------------------------------

# Têm acesso: Gestor, Operador de Usina e Técnico de Manutenção. Os demais
# perfis não visualizam a funcionalidade e têm o acesso direto recusado.
