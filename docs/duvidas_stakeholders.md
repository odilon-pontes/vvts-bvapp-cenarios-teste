# Dúvidas para esclarecimento com os stakeholders

Autor: Odilon. Regras ausentes ou contraditórias encontradas ao escrever os cenários. Nenhuma regra foi inventada: os cenários afetados indicam "NÃO DEFINIDO" e o código da dúvida.

Várias dúvidas confirmam problemas já registrados no walkthrough de requisitos (checklist C1–C5, T6–T7).

| Código | Requisito | Dúvida | Cenários |
|---|---|---|---|
| D01 | 23834 / CA01 24993 | Algum filtro é obrigatório? O que acontece sem nenhum filtro e quando a data de fim é anterior à data de início? | UC001 |
| D02 | 23834 / CA02 24994 | Quantos itens por página a listagem de medições deve exibir? | UC001 |
| D03 | 23834 / CA04 24996 | Qual o texto exato da mensagem quando nenhuma medição é encontrada? ("clara" é subjetivo) | UC001 |
| D04 | 23834 / CA03 24995 | RNF-02 não foi fornecido. Sob quais condições (volume de registros, usuários simultâneos, ambiente) vale o limite de 3 s? Qual o comportamento para períodos acima de 12 meses? | UC001 |
| D05 | 23834 / CA05 24997 e 23851 / CA05 24919 | Os perfis não listados nos critérios (ex.: Tesoureiro na consulta de medições; Técnico de Manutenção na consulta de faturas) devem ter o acesso negado? De que forma (menu oculto, mensagem, redirecionamento)? E o usuário não autenticado? | UC002, UC003, UC007, UC009 |
| D06 | 23851 / CA01 24913 | O filtro por mês/ano é um único mês ou um intervalo de meses? | UC004 |
| D07 | 23851 / CA02 24914 | O que significa o status "substituída" e como uma fatura passa a tê-lo? Como o PDF é anexado (o cadastro 25769 não prevê PDF)? | UC003, UC004 |
| D08 | 23851 / CA03 24916 | Qual o nome e a localização do "filtro específico" para faturas excluídas? Perfis diferentes de Gestor podem usá-lo? | UC003, UC006, UC008 |
| D09 | 23851 / CA04 24917 e CA06 25776 | Qual o texto da mensagem quando nenhuma fatura é encontrada? Os critérios 24917 e 25776 são duplicados: manter só um? | UC005 |
| D10 | 23853 / CA01 24920 | "Gestor/Administrador" é o mesmo perfil de "Gestor" ou são perfis distintos? | UC009 |
| D11 | 23853 / CA02 24921 | O motivo da exclusão é texto livre? Há tamanho mínimo/máximo? | UC008 |
| D12 | 23853 / CA02 24921 | O que acontece se o usuário cancelar a confirmação de exclusão? (comportamento não descrito) | UC003, UC008 |
| D13 | 23853 / CA04 24923 | RF-4.2.05 não foi fornecido: o que o registro de auditoria contém (usuário, data/hora, motivo, fatura?) e onde ele é consultado? (O CA 25778 "log imutável" está Rejected e não será testado.) | UC003 |
| D14 | 23849 / CA03 25771 | Uma fatura excluída logicamente impede novo cadastro do mesmo mês/ano e usina? | UC003 |
| D15 | 23860 / CA01 24939 | Qual a fórmula da diferença percentual (base: energia medida ou energia da fatura)? Qual o sinal da diferença absoluta? Qual campo da fatura é comparado (Energia Injetada ou Energia Consumida)? Como o período da fatura é definido? | UC011, UC012 |
| D16 | 23860 / CA02 24941 | Quem configura o percentual de tolerância, onde, e qual o valor padrão? Divergência "supera" significa > ou >=? | UC012 |
| D17 | 23860 / CA03 24942 | Como uma leitura de inversor passa a ser "inválida" e quem a sinaliza? | UC011 |
| D18 | 23860 / CA04 24943 | Se só parte do período da fatura tem dados de inversores, a divergência é calculada? (Os critérios 24943 e 28866 são duplicados.) | UC013 |
| D19 | 23860 / CA02 24941 | Qual a forma da sinalização visual da divergência (cor, ícone, rótulo)? | UC012 |
| D20 | 23860 | Quais perfis têm acesso à comparação geração x injeção? (a feature não define) | UC011, UC012, UC013 |
| D21 | 23849 / CA01-CA02 25769-25770 e 28855 / CA05-CA06 | Usina e PDF fazem parte do cadastro? Quais campos são obrigatórios e o que é "valor válido" em cada campo numérico (negativo, zero, casas decimais)? | UC003 |
| D22 | 23849 e 23853 | Quais mensagens o sistema exibe no sucesso do cadastro e da exclusão (só a edição tem CA de sucesso, 28864) e nos erros (duplicidade, campo obrigatório, valor inválido)? | UC003, UC008 |
| D23 | 28855 / CA01-CA02 | Alterar Mês/Ano para um mês já cadastrado na mesma usina é bloqueado? Faturas excluídas/substituídas podem ser editadas? O Gestor também edita? Usina e PDF são editáveis? | UC003 |
| D24 | 23860 / CA01 24939 | Faturas excluídas logicamente aparecem na comparação geração x injeção? | UC011 |
