# BVapp didático: cenários de teste (Odilon)

Mini projeto individual de organização de cenários de teste do BVapp (atividade N3).

**Autor:** Odilon Francelino de Pontes Neto
**Requisitos de referência:** Work packages de 12/11/2026
**Features sob minha responsabilidade:** 23834 Consulta histórica de medições, 23851 Consulta histórica de Injeção de Energia mensal, 23853 Exclusão de Injeção de Energia mensal, 23860 Comparação geração x injeção e 36181 Configuração do percentual de tolerância de divergência.

## Estrutura

```
vvts-bvapp-cenarios-teste/
├── pyproject.toml, manage.py     # configuração (uv) e entrada do Django
├── config/                       # configuração global do projeto Django
├── functional_tests/             # um arquivo por cenário (UC001 a UC011)
└── docs/
    ├── rastreabilidade.md        # critérios de aceitação x cenários
```

Cada arquivo `functional_tests/test_ucNNN_*.py` segue o modelo do UC001 da Aula 06: cabeçalho (objetivo, requisitos, ator, pré-condições, dados de teste, autor, dúvidas), fluxo principal `[FP]`, fluxos alternativos `[A#]` e regras de negócio `[RN#]`, todos escritos como comentários.

Escopo desta entrega: somente a documentação dos cenários e a organização dos arquivos. Nada foi implementado, automatizado ou executado.

## Cenários

| UC | Título |
|---|---|
| UC001 | Consultar histórico de medições |
| UC002 | Controlar acesso à consulta histórica de medições por perfil |
| UC003 | Manter injeção de energia mensal (fluxo CRUD completo) |
| UC004 | Controlar acesso à consulta de injeção de energia por perfil |
| UC005 | Excluir injeção de energia mensal com confirmação e motivo |
| UC006 | Restringir a exclusão de injeção de energia ao Gestor/Administrador |
| UC007 | Comparar geração dos inversores e injeção da fatura |
| UC008 | Sinalizar divergência acima da tolerância |
| UC009 | Informar ausência de dados de inversores na comparação |
| UC010 | Registrar auditoria na exclusão de injeção de energia |
| UC011 | Configurar o percentual de tolerância de divergência |

O UC003 é o cenário CRUD completo (criar, consultar, editar e excluir) e concentra os fluxos de consulta da injeção (filtros, ausência de resultados, falha, faturas excluídas e detalhe), em vez de cenários separados, como no exemplo da Aula 06. As partes de cadastro e de edição pertencem aos colegas (RF-23849 e RF-28855) e foram incluídas só para fechar o fluxo.
