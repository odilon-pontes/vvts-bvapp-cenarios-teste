'''
UC009 - Restringir a exclusão de injeção de energia ao Gestor/Administrador

Objetivo: Garantir que somente o Gestor/Administrador visualize a opção de exclusão de
fatura e consiga acioná-la, e que a tentativa de outro perfil seja recusada.

Requisitos:
- RF-23853 Exclusão de Injeção de Energia mensal (Epic 23763)
- CA01 (24920) somente o Gestor/Administrador visualiza e aciona a exclusão; tentativa de outro perfil é recusada e a fatura permanece inalterada

Ator:
- Gestor/Administrador
- Tesoureiro
- Operador de Usina

Pré-condições:
- Usuários de teste: Gestor, Tesoureiro e Operador de Usina.
- Existe a fatura ativa 05/2026 da Usina Solar Alfa.

Dados de teste:
- Fatura: 05/2026 | Usina Solar Alfa

Resultado esperado (resumo):
A opção de exclusão só é exibida e aceita para o Gestor/Administrador; as
tentativas de outros perfis são recusadas e a fatura permanece inalterada.

Versão dos requisitos: Work packages de 12/11/2026
Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D04] Como o sistema recusa o acesso direto de um perfil não autorizado
      (mensagem, redirecionamento)? O que acontece com o usuário não
      autenticado? Os critérios só dizem que é "recusado".
[D10] "Gestor/Administrador" é o mesmo perfil de "Gestor" (usado nas Features
      23834 e 23851) ou são perfis distintos?
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator, autenticado como Gestor, acessa a consulta histórica e localiza a
# fatura 05/2026 da Usina Solar Alfa.

# O ator verifica que a opção "Excluir" está visível. [D10]

# O ator seleciona a opção e verifica que o sistema inicia o fluxo de
# exclusão (confirmação e motivo).

# 🟠 [A1] - TESOUREIRO
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro, acessa a consulta e localiza a fatura.

# O sistema não exibe a opção de exclusão.

# 🟠 [A2] - OPERADOR DE USINA
# ---------------------------------------------------------------

# O ator autentica como Operador de Usina, acessa a consulta e localiza a
# fatura.

# O sistema não exibe a opção de exclusão.

# 🟠 [A3] - ACESSO DIRETO À EXCLUSÃO SEM PERMISSÃO
# ---------------------------------------------------------------

# O ator autenticado como Tesoureiro tenta acionar a exclusão diretamente
# (endereço ou requisição da exclusão), sem usar o botão.

# O sistema recusa a tentativa. A forma da recusa é NÃO DEFINIDA [D04].

# A fatura permanece inalterada, com status Ativa.

# 🟣 [RN1] - PERFIL
# ---------------------------------------------------------------

# Exclusão restrita ao Gestor/Administrador; a equivalência entre Gestor e
# Administrador não está definida [D10].
