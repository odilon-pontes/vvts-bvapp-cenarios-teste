# Dúvidas para esclarecimento com os stakeholders

Autor: Odilon Francelino de Pontes Neto. Regras ausentes ou contraditórias que restaram nos requisitos (Work packages de 12/11/2026). Nenhuma regra foi inventada: os cenários afetados indicam "NÃO DEFINIDO" e o código da dúvida.

As dúvidas da versão anterior dos cenários sobre mensagens, perfis da comparação, fórmulas, tolerância e período foram resolvidas pelos novos requisitos e removidas.

| Código | Requisito | Dúvida | Cenários |
|---|---|---|---|
| D01 | 23834 / CA01 24993 e CA07 36163 | As Datas de Início e de Fim são obrigatórias, mas o requisito não diz o que o sistema faz (mensagem, destaque do campo) quando a consulta é acionada sem uma delas. | UC001 |
| D02 | 23834 / CA02 24994 | Quantos registros por página a listagem de medições exibe por padrão, e o usuário pode alterar essa quantidade? | UC001 |
| D03 | 23834 / CA03 24995 | Sob quais condições de carga (volume de registros, usuários simultâneos, ambiente) vale o limite de 3 s? O RNF-02 não foi fornecido. Qual o comportamento para períodos acima de 12 meses? | UC001 |
| D04 | 24997, 24919, 24920, 36177, 36187 e 25772 / 28857 | Como o sistema recusa o acesso direto de um perfil não autorizado (mensagem, redirecionamento)? O que acontece com o usuário não autenticado? Os critérios só dizem que é "recusado". | UC002, UC003, UC007, UC009, UC010, UC015 |
| D05 | 23834 / CA08 36164 | Qual a grandeza e a unidade do "valor medido" exibido em cada medição (kW, kWh)? | UC001 |
| D06 | 23851 / CA01 24913 | O filtro Mês/Ano é um mês único ou um intervalo de meses? O que a consulta exibe quando é acionada sem nenhum filtro? | UC004 |
| D07 | 23851 / CA02 24914 e CA08 36167 | O que significa o status "Substituída" e como uma fatura passa a tê-lo? Como o PDF é anexado na criação (o cadastro 25769 não prevê PDF, a edição 28858 prevê substituição) e qual a forma do indicador de PDF anexado? | UC003, UC004, UC013 |
| D08 | 23853 / CA02 24921 | O motivo da exclusão é texto livre? Há tamanho mínimo e máximo? Qual a mensagem exibida quando o motivo não é informado? | UC008 |
| D09 | 23853 / CA04 24923 e 36181 / CA04 36186 | Onde e por quem o registro de auditoria e o log da alteração de tolerância podem ser consultados? O RF-4.2.05 não foi fornecido. | UC003, UC014, UC015 |
| D10 | 23853 / CA01 24920, 23860 / CA11 36177 e 36181 / CA05 36187 | "Gestor/Administrador" é o mesmo perfil de "Gestor" (usado nas Features 23834 e 23851) ou são perfis distintos? | UC003, UC009, UC010, UC011, UC015 |
| D11 | 23849 / CA01 a CA03 25769-25771 | O cadastro não lista os campos obrigatórios nem os valores válidos (a edição define). Quais mensagens o sistema exibe no sucesso e nos erros do cadastro (duplicidade, campo obrigatório, valor inválido)? Uma fatura Excluída impede novo cadastro do mesmo Mês/Ano e Usina? | UC003 |
| D12 | 28855 / CA01 28857, CA05 28861 e CA06 28862 | Quais mensagens de erro o sistema exibe na edição (campo obrigatório vazio, valor inválido) e como é recusada a edição de uma fatura Excluída ou Substituída? | UC003 |
| D13 | 23860 / CA01 24939 e CA06 36172 | Quantas casas decimais e qual arredondamento são usados na Diferença Absoluta e na Diferença Percentual? | UC010 |
| D14 | 23860 / CA03 24942 | Como uma leitura de inversor passa a ser "inválida" e quem a sinaliza? | UC010 |
| D15 | 23860 / CA07 36173 e CA09 36175 | Quando há leituras em apenas parte do mês, o sistema calcula a comparação com as leituras existentes ou avisa a cobertura parcial? Quando a Energia Medida é zero e a Energia Injetada é maior que zero, a fatura é sinalizada? | UC012 |
| D16 | 23860 / CA10 36176 e 36181 / CA01 36183 | Existe valor padrão para o percentual de tolerância e em que menu fica a configuração? Enquanto não configurado, as linhas exibem o rótulo "Dentro da tolerância"? | UC011, UC015 |
| D17 | 36165, 36166 e 36180 | Como é indicado o carregamento em andamento (texto, ícone)? Qual o texto da mensagem de falha na comparação geração x injeção (CA14 36180 não define)? | UC001, UC005, UC010 |
