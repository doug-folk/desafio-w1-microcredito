# Sistema de Score de Microcredito Inclusivo

## Visao Geral

Este projeto propoe um modelo de triagem de microcredito mais inclusivo para pequenos empreendedores e trabalhadores informais, como costureiras, feirantes, mecanicos, vendedores autonomos e outros profissionais sem vinculo formal CLT.

O problema central do sistema antigo era usar a ausencia de renda formal comprovada como criterio de reprovacao automatica. Esse modelo gerava exclusao financeira, mesmo quando o solicitante apresentava bom historico de pagamento, estabilidade na atividade economica e capacidade real de honrar o credito.

O novo modelo substitui essa logica por uma avaliacao baseada em **Score Social Alternativo**, reduzindo vies algoritmico e ampliando o acesso ao microcredito com controle de risco.

## Objetivo

Permitir uma analise de credito mais justa, transparente e aderente a realidade economica das periferias, sem usar a falta de renda formal CLT como criterio excludente inicial.

O sistema deve:

- reconhecer a capacidade de pagamento de trabalhadores informais;
- priorizar comportamento financeiro e estabilidade da atividade economica;
- manter um criterio minimo de risco para concessao;
- proteger os dados pessoais dos solicitantes de acordo com principios de compliance e LGPD.

## Problema de Negocio

No cenario apresentado, 95% das mulheres chefes de familia da comunidade sao rejeitadas pelo sistema anterior por nao possuirem renda formal comprovada, mesmo mantendo contas em dia e operando atividades economicas estaveis.

Esse comportamento cria tres falhas graves:

- exclusao de clientes com capacidade real de pagamento;
- reforco de vies estrutural contra trabalhadores informais;
- perda de oportunidade financeira para a cooperativa de microcredito.

## Proposta de Solucao

O sistema utiliza um **Score Social Alternativo** de 0 a 100 para orientar a triagem inicial do solicitante.

A renda formal CLT ainda pode ser registrada no sistema, mas nao deve funcionar como filtro automatico de reprovacao. A decisao deve analisar primeiro o score social, que representa um retrato mais fiel da realidade financeira do cliente.

## Variaveis de Avaliacao

O score social e construido a partir de indicadores alternativos relacionados ao comportamento financeiro e a estabilidade da atividade produtiva:

- despesas mensais;
- renda estimada;
- emprestimos atuais;
- historico de pagamento e fidelidade;
- tempo de atividade profissional.

## Regras de Pontuacao

### 1. Renda Estimada (R)

A renda estimada representa o valor medio mensal recebido pelo solicitante em sua atividade profissional, independentemente de possuir CLT.

Exemplo:

`Renda estimada = R$ 2.000,00`

Essa informacao serve como base para comparar despesas e comprometimento com emprestimos.

### 2. Despesas Mensais (D)

Quanto menor o comprometimento da renda com despesas, menor o risco financeiro.

| Situacao | Pontuacao |
| --- | ---: |
| Despesas de ate 70% da renda | 100 |
| Despesas entre 71% e 100% da renda | 50 |
| Despesas superiores a renda | 0 |

### 3. Emprestimos Atuais (E)

O sistema analisa o peso das parcelas ja existentes em relacao a renda estimada.

| Situacao | Pontuacao |
| --- | ---: |
| Nao possui emprestimos ativos | 100 |
| Parcelas de emprestimos de ate 30% da renda | 50 |
| Parcelas superiores a 30% da renda | 0 |

Regra de seguranca:

Um novo emprestimo nao deve fazer o comprometimento total superar `30%` da renda estimada do solicitante.

### 4. Historico de Pagamento e Fidelidade (EF)

Esse criterio reconhece clientes que honram compromissos financeiros mesmo sem renda formal.

| Situacao | Pontuacao |
| --- | ---: |
| Pagamentos realizados em dia | 100 |
| Existencia de atrasos relevantes | 0 |

### 5. Tempo de Atividade Profissional (A)

Esse fator mede estabilidade da fonte de renda.

| Tempo de atividade | Pontuacao |
| --- | ---: |
| Ate 6 meses | 0 |
| Acima de 6 meses ate 1 ano | 50 |
| Acima de 1 ano | 100 |

## Pontuacao Maxima

A pontuacao maxima do modelo e de `400 pontos`:

- despesas: `100`;
- emprestimos: `100`;
- historico/fidelidade: `100`;
- tempo de atividade: `100`.

## Conversao Para Score Social

O sistema converte a pontuacao total para uma escala de 0 a 100 com a formula:

`Score Social = (Pontuacao obtida / 400) x 100`

Exemplo:

- pontuacao obtida: `300`;
- score social: `(300 / 400) x 100 = 75`.

## Regra de Triagem

A triagem deve analisar primeiro o **Score Social Alternativo**.

Regra inicial proposta:

- `Score Social >= 60`: `Resultado: Aprovado`
- `Score Social < 60`: `Resultado: Reprovado`

### Exemplo

Solicitante informal:

- renda formal CLT: `R$ 0,00`;
- score social: `82`.

Resultado esperado:

`Resultado: Aprovado`

Essa regra garante que a ausencia de vinculo formal nao provoque exclusao automatica.

## Fluxo do Processo de Negocio

O processo de triagem segue as etapas abaixo:

1. cadastro do solicitante;
2. registro da renda formal CLT, caso exista;
3. levantamento da renda estimada da atividade informal;
4. levantamento das despesas mensais;
5. verificacao de emprestimos existentes;
6. verificacao do historico de pagamentos;
7. identificacao do tempo de atividade profissional;
8. calculo da pontuacao dos criterios;
9. conversao da pontuacao para score social de 0 a 100;
10. analise do score social;
11. exibicao do resultado final:

- `Resultado: Aprovado`
- `Resultado: Reprovado`

## Justificativa dos Pesos e das Variaveis Informais

O modelo da prioridade a variaveis que possuem relacao direta com capacidade de pagamento e estabilidade economica, em vez de privilegiar exclusivamente renda formal.

Justificativas:

- **despesas mensais** indicam o nivel de comprometimento da renda;
- **emprestimos atuais** medem endividamento e risco de sobrecarga financeira;
- **historico de pagamento** representa comportamento real diante de obrigacoes financeiras;
- **tempo de atividade profissional** funciona como sinal de estabilidade e continuidade da renda;
- **renda estimada** contextualiza a realidade economica do solicitante, mesmo sem CLT.

Essa estrutura reduz distorcao contra clientes do mercado informal e melhora a coerencia da decisao de credito.

## Combate ao Vies Algoritmico

O sistema foi projetado para evitar que a existencia ou ausencia de vinculo formal CLT seja usada como fator excludente.

Medidas adotadas:

- a renda formal nao e criterio inicial de reprovacao;
- a decisao depende primeiro do score social;
- o modelo considera indicadores concretos de comportamento financeiro;
- caracteristicas pessoais sem relacao com risco de credito nao devem influenciar a analise;
- a logica busca reduzir exclusao de grupos historicamente afetados pelo mercado informal.

## Compliance e LGPD

O sistema deve seguir principios de necessidade, finalidade, seguranca e acesso restrito no tratamento de dados pessoais.

Praticas recomendadas:

- coletar apenas os dados necessarios para analise do microcredito;
- informar claramente a finalidade da coleta;
- restringir o acesso aos dados a pessoas autorizadas;
- evitar exposicao de informacoes pessoais em relatorios e telas desnecessarias;
- nao usar atributos irrelevantes para a concessao do credito;
- proteger os dados contra acesso nao autorizado;
- usar os dados exclusivamente para analise, concessao e acompanhamento do microcredito.

### Dados sensiveis e protecao

Para proteger os dados dos clientes da periferia, o repositorio e o sistema devem adotar, no minimo:

- minimizacao de dados;
- controle de acesso por perfil;
- armazenamento seguro;
- registro de uso e auditoria;
- descarte adequado quando a finalidade terminar.

## Analise de Viabilidade

O novo modelo tambem tem potencial de gerar ganho financeiro para a cooperativa ao reduzir a rejeicao de clientes informais honestos.

Cenario de referencia:

- `1.000` solicitacoes de trabalhadores informais;
- sistema antigo: `95%` rejeitados;
- clientes potencialmente atendidos no modelo antigo: `50`.

Se o novo sistema aprovar `30%` dos solicitantes com bom score social:

- clientes aprovados: `300`;
- novos clientes em relacao ao modelo antigo: `250`.

Considerando operacoes medias de `R$ 1.000,00`:

`250 x R$ 1.000,00 = R$ 250.000,00`

Impactos esperados:

- ampliacao da carteira de microcredito;
- aumento do alcance social da cooperativa;
- reducao de exclusao financeira indevida;
- melhor equilibrio entre inclusao e controle de risco.

## Resultado Esperado

O projeto busca entregar um sistema de triagem mais justo, transparente e inclusivo, capaz de reconhecer a capacidade financeira de trabalhadores informais sem usar a ausencia de renda CLT como motivo automatico de reprovacao.

O equilibrio esperado do modelo e:

`Inclusao financeira + controle de risco + protecao de dados pessoais`

## Estrutura da Entrega

Nesta fase, o repositorio deve conter:

- `README.md` com documentacao do processo de negocio, score, vies, compliance e viabilidade;
- `src/triagem.py` como arquivo principal da logica de triagem.

As proximas fases envolvem a implementacao da regra de triagem no codigo e a validacao dos cenarios esperados.
