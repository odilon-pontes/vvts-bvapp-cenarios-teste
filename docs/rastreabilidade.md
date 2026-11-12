# Rastreabilidade: critérios de aceitação x cenários

Base: Work packages de 12/11/2026. Features sob responsabilidade: 23834, 23851, 23853, 23860 e 36181 (42 critérios de aceitação).

Os critérios 25776 (duplicava o CA04 de 24917), 25778 (Rejected) e 28866 (duplicava o CA04 de 24943) não constam mais no backlog e, por isso, saíram da cobertura.

| Feature | CA (ID) | Critério | Coberto em |
|---|---|---|---|
| 23834 | 24993 | CA01 filtros (período obrigatório) | UC001 (FP, A1, A2, A8) |
| 23834 | 24994 | CA02 paginação | UC001 (A3) |
| 23834 | 24995 | CA03 3 segundos até 12 meses | UC001 (RN2), pendente de condições [D03] |
| 23834 | 24996 | CA04 sem resultados | UC001 (A4) |
| 23834 | 24997 | CA05 perfis | UC002 |
| 23834 | 36162 | CA06 listas de Usina e Inversor | UC001 (FP, A7) |
| 23834 | 36163 | CA07 limites e datas invertidas | UC001 (A5, A6) |
| 23834 | 36164 | CA08 colunas e ordenação | UC001 (FP) |
| 23834 | 36165 | CA09 carregamento, vazio e falha | UC001 (A4, A9) |
| 23851 | 24913 | CA01 filtro Mês/Ano e/ou Usina | UC004, UC003 |
| 23851 | 24914 | CA02 itens da lista | UC004, UC003 |
| 23851 | 24916 | CA03 excluídas e filtro do Gestor | UC006, UC003, UC008 |
| 23851 | 24917 | CA04 mensagem sem fatura | UC005 |
| 23851 | 24919 | CA05 perfis | UC007 |
| 23851 | 36166 | CA07 carregamento, vazio e falha | UC005 (A2) |
| 23851 | 36167 | CA08 visualização detalhada | UC013, UC003 |
| 23851 | 36168 | CA09 dados da exclusão no detalhe | UC013 (A2), UC003 |
| 23853 | 24920 | CA01 só Gestor/Administrador | UC009, UC003 (A7) |
| 23853 | 24921 | CA02 confirmação e motivo | UC008, UC003 |
| 23853 | 24922 | CA03 exclusão lógica | UC008, UC003 |
| 23853 | 24923 | CA04 auditoria | UC014 |
| 23853 | 36169 | CA06 cancelar a confirmação | UC008 (A2), UC003 (A11) |
| 23853 | 36170 | CA07 mensagem de sucesso | UC008, UC003 |
| 23853 | 36171 | CA08 fatura já excluída ou inexistente | UC008 (A4) |
| 23860 | 24939 | CA01 valores e diferenças | UC010 |
| 23860 | 24941 | CA02 sinalização | UC011 |
| 23860 | 24942 | CA03 apenas leituras válidas | UC010 (A1) |
| 23860 | 24943 | CA04 ausência de dados | UC012 |
| 23860 | 36172 | CA06 fórmulas | UC010 (FP) |
| 23860 | 36173 | CA07 período da Energia Medida | UC010 (A4) |
| 23860 | 36174 | CA08 uso da Energia Injetada | UC010 (A5) |
| 23860 | 36175 | CA09 Energia Medida zero | UC012 (A1) |
| 23860 | 36176 | CA10 tolerância não configurada | UC011 (A3) |
| 23860 | 36177 | CA11 perfis | UC010 (A8, A9) |
| 23860 | 36178 | CA12 faturas Excluídas | UC010 (A3) |
| 23860 | 36179 | CA13 ordenação e paginação | UC010 (A2) |
| 23860 | 36180 | CA14 vazio e falha | UC010 (A6, A7) |
| 36181 | 36183 | CA01 percentual único | UC015, UC011 (A2) |
| 36181 | 36184 | CA02 validação do campo | UC015 (A1, A2, A3) |
| 36181 | 36185 | CA03 mensagem e aplicação | UC015 |
| 36181 | 36186 | CA04 log da alteração | UC015 |
| 36181 | 36187 | CA05 acesso restrito | UC015 (A5) |

## Cenários

| UC | Título | Arquivo |
|---|---|---|
| UC001 | Consultar histórico de medições | `functional_tests/test_uc001_consultar_medicoes.py` |
| UC002 | Controlar acesso à consulta histórica de medições por perfil | `functional_tests/test_uc002_acesso_consulta_medicoes.py` |
| UC003 | Manter injeção de energia mensal (fluxo CRUD completo) | `functional_tests/test_uc003_manter_injecao_energia_crud.py` |
| UC004 | Consultar injeção de energia mensal com filtros | `functional_tests/test_uc004_consultar_injecao_filtros.py` |
| UC005 | Consultar injeção de energia mensal sem resultados ou com falha | `functional_tests/test_uc005_consultar_injecao_sem_resultado.py` |
| UC006 | Visualizar injeções de energia excluídas logicamente | `functional_tests/test_uc006_visualizar_injecoes_excluidas.py` |
| UC007 | Controlar acesso à consulta de injeção de energia por perfil | `functional_tests/test_uc007_acesso_consulta_injecao.py` |
| UC008 | Excluir injeção de energia mensal com confirmação e motivo | `functional_tests/test_uc008_excluir_injecao_confirmacao_motivo.py` |
| UC009 | Restringir a exclusão de injeção de energia ao Gestor/Administrador | `functional_tests/test_uc009_restringir_exclusao_gestor.py` |
| UC010 | Comparar geração dos inversores e injeção da fatura | `functional_tests/test_uc010_comparar_geracao_injecao.py` |
| UC011 | Sinalizar divergência acima da tolerância | `functional_tests/test_uc011_sinalizar_divergencia.py` |
| UC012 | Informar ausência de dados de inversores na comparação | `functional_tests/test_uc012_comparacao_sem_dados_inversores.py` |
| UC013 | Visualizar os detalhes de uma injeção de energia mensal | `functional_tests/test_uc013_visualizar_detalhe_injecao.py` |
| UC014 | Registrar auditoria na exclusão de injeção de energia | `functional_tests/test_uc014_auditoria_exclusao_injecao.py` |
| UC015 | Configurar o percentual de tolerância de divergência | `functional_tests/test_uc015_configurar_tolerancia_divergencia.py` |
