# BVapp didático: cenários de teste (Odilon)

Mini projeto individual de organização de cenários de teste do BVapp (atividade N3).

**Autor:**  Odilon Francelino de Pontes Neto
**Features sob minha responsabilidade:** 23834 Consulta histórica de medições, 23851 Consulta histórica de Injeção de Energia mensal, 23853 Exclusão de Injeção de Energia mensal e 23860 Comparação geração x injeção.

## Estrutura

```
bvapp-didatico/
├── pyproject.toml, manage.py     # configuração (uv) e entrada do Django
├── config/                       # configuração global do projeto Django
├── functional_tests/             # um arquivo por cenário (UC001 a UC013)
└── docs/
    ├── rastreabilidade.md        # critérios de aceitação x cenários
    └── duvidas_stakeholders.md   # regras ausentes ou contraditórias
```

Cada arquivo `functional_tests/test_ucNNN_*.py` segue o modelo do UC001 da Aula 06: cabeçalho (objetivo, requisitos, ator, dados, autor), fluxo principal `[FP]`, fluxos alternativos `[A#]` e regras de negócio `[RN#]`, mais um esqueleto de `unittest` marcado com `skip` para uso futuro.

Escopo desta entrega: somente documentação dos cenários. Nada foi implementado, automatizado ou executado.

## Cenários

| UC | Título |
|---|---|
| UC001 | Consultar histórico de medições |
| UC002 | Controlar acesso à consulta histórica de medições por perfil |
| UC003 | Manter injeção de energia mensal (fluxo CRUD completo) |
| UC004 | Consultar injeção de energia mensal com filtros |
| UC005 | Consultar injeção de energia mensal sem resultados |
| UC006 | Visualizar injeções de energia excluídas logicamente |
| UC007 | Controlar acesso à consulta de injeção de energia por perfil |
| UC008 | Excluir injeção de energia mensal com confirmação e motivo |
| UC009 | Restringir a exclusão de injeção de energia ao Gestor/Administrador |
| UC010 | Registrar auditoria na exclusão de injeção de energia |
| UC011 | Comparar geração dos inversores e injeção da fatura |
| UC012 | Sinalizar divergência acima da tolerância |
| UC013 | Informar ausência de dados de inversores na comparação |

O UC003 é o cenário CRUD completo (criar, consultar, atualizar e excluir). As partes de cadastro e edição pertencem aos colegas (RF-23849 e RF-28855) e foram incluídas só para fechar o fluxo.

