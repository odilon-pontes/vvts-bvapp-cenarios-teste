# Rastreabilidade: critérios de aceitação x cenários

Features sob responsabilidade: 23834, 23851, 23853 e 23860 (20 CAs, excluindo o CA 25778 Rejected).

| Feature | CA (ID) | Critério | Coberto em |
|---|---|---|---|
| 23834 | 24993 | CA01 filtros | UC001 (FP, A1, A2, A5, A6) |
| 23834 | 24994 | CA02 paginação | UC001 (A3) |
| 23834 | 24995 | CA03 desempenho 3 s | UC001 (RN2), pendente de RNF-02 [D04] |
| 23834 | 24996 | CA04 sem resultados | UC001 (A4) |
| 23834 | 24997 | CA05 perfis | UC002 |
| 23851 | 24913 | CA01 filtro mês/ano e/ou usina | UC004, UC003 |
| 23851 | 24914 | CA02 itens da lista | UC004, UC003 |
| 23851 | 24916 | CA03 excluídas / filtro do Gestor | UC006, UC003, UC008 |
| 23851 | 24917 | CA04 mensagem sem fatura | UC005 |
| 23851 | 24919 | CA05 perfis | UC007 |
| 23851 | 25776 | CA06 mensagem (duplica CA04) | UC005 |
| 23853 | 24920 | CA01 só Gestor | UC009, UC003 (A7) |
| 23853 | 24921 | CA02 confirmação e motivo | UC008, UC003 |
| 23853 | 24922 | CA03 exclusão lógica | UC008, UC003 |
| 23853 | 24923 | CA04 auditoria | UC010 |
| 23853 | 25778 | CA05 log imutável (Rejected) | Fora do escopo |
| 23860 | 24939 | CA01 valores e diferenças | UC011 |
| 23860 | 24941 | CA02 sinalização | UC012 |
| 23860 | 24942 | CA03 apenas dados válidos | UC011 (A1) |
| 23860 | 24943 | CA04 ausência de dados | UC013 |
| 23860 | 28866 | CA05 ausência de dados (duplica CA04) | UC013 |

## Cenários

| UC | Título | Arquivo |
|---|---|---|
| UC001 | Consultar histórico de medições | `functional_tests/test_uc001_consultar_medicoes.py` |
| UC002 | Controlar acesso à consulta histórica de medições por perfil | `functional_tests/test_uc002_acesso_consulta_medicoes.py` |
| UC003 | Manter injeção de energia mensal (fluxo CRUD completo) | `functional_tests/test_uc003_manter_injecao_energia_crud.py` |
| UC004 | Consultar injeção de energia mensal com filtros | `functional_tests/test_uc004_consultar_injecao_filtros.py` |
| UC005 | Consultar injeção de energia mensal sem resultados | `functional_tests/test_uc005_consultar_injecao_sem_resultado.py` |
| UC006 | Visualizar injeções de energia excluídas logicamente | `functional_tests/test_uc006_visualizar_injecoes_excluidas.py` |
| UC007 | Controlar acesso à consulta de injeção de energia por perfil | `functional_tests/test_uc007_acesso_consulta_injecao.py` |
| UC008 | Excluir injeção de energia mensal com confirmação e motivo | `functional_tests/test_uc008_excluir_injecao_confirmacao_motivo.py` |
| UC009 | Restringir a exclusão de injeção de energia ao Gestor | `functional_tests/test_uc009_restringir_exclusao_gestor.py` |
| UC010 | Comparar geração dos inversores e injeção da fatura | `functional_tests/test_uc010_comparar_geracao_injecao.py` |
| UC011 | Sinalizar divergência acima da tolerância | `functional_tests/test_uc011_sinalizar_divergencia.py` |
| UC012 | Informar ausência de dados de inversores na comparação | `functional_tests/test_uc012_comparacao_sem_dados_inversores.py` |
