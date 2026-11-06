'''
UC009 - Restringir a exclusão de injeção de energia ao Gestor/Administrador

Objetivo: Garantir que somente o Gestor/Administrador visualize e acesse a opção de
exclusão de fatura.

Requisitos:
- RF-23853 Exclusão de Injeção de Energia mensal (Epic 23763)
- CA01 (24920) somente o Gestor/Administrador visualiza e acessa a exclusão

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
A opção de exclusão só é exibida e aceita para o Gestor/Administrador.

Autor: Odilon Francelino de Pontes Neto

Dúvidas para os stakeholders:
[D05] Os perfis não listados nos critérios (ex.: Tesoureiro na consulta de
      medições; Técnico de Manutenção na consulta de faturas) devem ter o
      acesso negado? De que forma (menu oculto, mensagem, redirecionamento)? E
      o usuário não autenticado?
[D10] "Gestor/Administrador" é o mesmo perfil de "Gestor" ou são perfis
      distintos?
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator, autenticado como Gestor, acessa a consulta histórica e localiza a
# fatura 05/2026 da Usina Solar Alfa.

# O ator verifica que a opção "Excluir" está visível. [D10]

# O ator seleciona a opção e verifica que o sistema inicia o fluxo de
# exclusão (confirmação e motivo).

# [A1] - TESOUREIRO
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro, acessa a consulta e localiza a fatura.

# O sistema não exibe a opção de exclusão.

# [A2] - OPERADOR DE USINA
# ---------------------------------------------------------------

# O ator autentica como Operador de Usina, acessa a consulta e localiza a
# fatura.

# O sistema não exibe a opção de exclusão.

# [A3] - ACESSO DIRETO À EXCLUSÃO SEM PERMISSÃO
# ---------------------------------------------------------------

# O ator autenticado como Tesoureiro tenta acionar a exclusão diretamente
# (endereço/requisição da exclusão), sem usar o botão.

# O sistema não efetiva a exclusão (o CA diz que o perfil "acessa" a opção).
# A forma da negação não é definida [D05]; a fatura continua ativa.

# [RN1] - PERFIL
# ---------------------------------------------------------------

# Exclusão restrita ao Gestor/Administrador; equivalência entre Gestor e
# Administrador indefinida [D10].

# ESQUELETO PARA ETAPAS FUTURAS (não implementado nesta atividade)
# ---------------------------------------------------------------
