'''
UC011 - Configurar o percentual de tolerância de divergência

Objetivo: Permitir que o Gestor defina o percentual de tolerância de
divergência, único para todas as usinas, e que apenas ele acesse essa
configuração.

Requisitos:
- RF-36181 Configuração do percentual de tolerância de divergência (Epic 23763)
- CA01 (36183) informar e salvar o percentual único
- CA02 (36184) validação do campo
- CA03 (36185) mensagem de sucesso e aplicação do novo valor
- CA04 (36186) log da alteração
- CA05 (36187) acesso restrito ao Gestor

Ator:
- Gestor
- Tesoureiro (verificação de acesso negado)

Pré-condições:
- Usuário autenticado como Gestor.
- Fatura B (UC008): 04/2026 Alfa com Diferença Percentual de 20%.
- O menu da configuração não está definido.

Dados de teste:
- Percentual válido: 5
- Limites: 0 e 100
- Valores inválidos: vazio, "abc", "-1", "100,01" e "5,123"

Resultado esperado (resumo):
O percentual válido é salvo com a mensagem de sucesso, passa a valer nas
comparações seguintes e gera log; valores inválidos são recusados; outros
perfis não acessam.

Autor: Odilon Francelino de Pontes Neto
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de configuração do percentual de tolerância de
# divergência.

# O ator informa o percentual 5 e seleciona a opção de salvar.
# [A1][A2][A3][A4]

# O sistema salva o percentual e exibe a mensagem "Percentual de tolerância
# atualizado com sucesso.".

# O ator acessa a comparação geração x injeção (UC008) e verifica que a
# fatura B (20%) é sinalizada como "Divergente" com base no percentual de
# 5%.

# O responsável pela verificação consulta o log e verifica o registro da
# alteração com o usuário responsável, a data e a hora e os valores anterior
# e novo do percentual. [A5]

# 🟠 [A1] - VALOR VAZIO [CA02 36184]
# ---------------------------------------------------------------

# O ator deixa o campo em branco e tenta salvar.

# O sistema impede o salvamento e exibe mensagem de erro junto ao campo.

# O percentual anterior permanece.

# 🟠 [A2] - VALORES INVÁLIDOS [CA02 36184]
# ---------------------------------------------------------------

# O ator informa, em tentativas separadas, "abc", "-1", "100,01" e "5,123"
# (3 casas decimais).

# Em cada tentativa o sistema impede o salvamento e exibe mensagem de erro
# junto ao campo.

# O percentual anterior permanece.

# 🟠 [A3] - LIMITES DA FAIXA [CA02 36184]
# ---------------------------------------------------------------

# O ator informa 0 e salva. Depois informa 100 e salva. Depois informa 2,5
# (1 casa decimal) e salva.

# O sistema aceita os três valores e exibe a mensagem de sucesso em cada
# salvamento.

# 🟠 [A4] - VALOR ÚNICO PARA TODAS AS USINAS [CA01 36183]
# ---------------------------------------------------------------

# O ator salva o percentual 5.

# O ator verifica na comparação que as faturas da Usina Solar Alfa e da
# Usina Solar Beta usam o mesmo percentual.

# 🟠 [A5] - ACESSO DE OUTROS PERFIS [CA05 36187]
# ---------------------------------------------------------------

# O ator autentica como Tesoureiro e examina o menu.

# O sistema não exibe a configuração do percentual.

# O ator tenta abrir diretamente o endereço da configuração.

# O sistema recusa o acesso.

# 🟣 [RN1] - FAIXA
# ---------------------------------------------------------------

# O campo aceita somente números maiores ou iguais a 0 e menores ou iguais a
# 100, com até 2 casas decimais.

# 🟣 [RN2] - VALOR ÚNICO
# ---------------------------------------------------------------

# Há um único percentual de tolerância para todas as usinas.

# 🟣 [RN3] - PERFIL
# ---------------------------------------------------------------

# Somente o Gestor visualiza e acessa a configuração.
