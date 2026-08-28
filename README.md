# Sistema de Score de Microcredito Inclusivo

## Visao Geral

Este projeto propoe um modelo de triagem de microcredito mais inclusivo para pequenos empreendedores e trabalhadores informais, como costureiras, feirantes, mecanicos, vendedores autonomos e outros profissionais sem vinculo formal CLT.

O sistema anterior utilizava a ausencia de renda formal comprovada como criterio de reprovacao automatica. Isso gerava exclusao financeira mesmo quando o solicitante apresentava bom historico de pagamento, estabilidade na atividade economica e capacidade real de honrar o credito.

O novo modelo substitui essa logica por uma avaliacao baseada em **Score Social Alternativo**, reduzindo vies algoritmico e ampliando o acesso ao microcredito com controle de risco.

## Objetivo

Permitir uma analise de credito mais justa, transparente e aderente a realidade economica das periferias, sem usar a falta de renda formal CLT como criterio excludente inicial.

O sistema deve:

- reconhecer a capacidade de pagamento de trabalhadores informais;
- priorizar comportamento financeiro e estabilidade da atividade economica;
- manter criterio minimo de risco para concessao;
- proteger os dados pessoais dos solicitantes de acordo com principios de compliance e LGPD.

## Problema de Negocio

No cenario apresentado, 95% das mulheres chefes de familia da comunidade sao rejeitadas pelo sistema anterior por nao possuirem renda formal comprovada, mesmo mantendo contas em dia e operando atividades economicas estaveis.

Esse comportamento cria tres falhas principais:

- exclusao de clientes com capacidade real de pagamento;
- reforco de vies estrutural contra trabalhadores informais;
- perda de oportunidade financeira para a cooperativa de microcredito.

## Proposta de Solucao

O sistema passa a calcular um **Score Social Alternativo** com base em variaveis de comportamento financeiro e estabilidade profissional. A renda formal CLT continua sendo registrada, mas nao funciona como filtro automatico de reprovacao.

A decisao final considera dois eixos:

- o score social calculado a partir de variaveis alternativas;
- a regra de seguranca que limita a parcela total do credito a `30%` da renda estimada.

## Entradas do Sistema

O programa coleta as seguintes informacoes pelo terminal:

- renda formal CLT;
- renda estimada da atividade economica;
- despesas mensais;
- valor da parcela de emprestimos atuais;
- historico de pagamento e fidelidade;
- tempo de atividade profissional em meses;
- valor da parcela do novo emprestimo solicitado.

## Avaliacao Social

Para facilitar o credito, o solicitante deve apresentar um comportamento financeiro e social que indique responsabilidade com compromissos assumidos. O sistema considera:

- pagamentos;
- renda estimada;
- despesas;
- emprestimos atuais;
- historico de fidelidade;
- tempo de atividade.

## Regras de Pontuacao

### 1. Renda Estimada (R)

A renda estimada representa o valor medio mensal recebido pelo solicitante em sua atividade profissional, independentemente de possuir CLT.

Exemplo:

`Renda estimada = R$ 2.000,00`

Essa informacao serve como base para comparar despesas e comprometimento com emprestimos. Ela nao gera pontos de forma isolada.

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

Observacao:

Quando nao existe emprestimo atual, o criterio recebe `100 pontos`. O projeto nao remove essa variavel do calculo, porque ausencia de endividamento representa menor risco.

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
| Mais de 6 meses ate 1 ano | 50 |
| Mais de 1 ano | 100 |

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

## Regra de Credito

O sistema aprova o solicitante somente quando as duas condicoes abaixo sao atendidas:

1. `Score Social >= 70`
2. A parcela do novo emprestimo nao ultrapassa `30%` da renda estimada e a soma das parcelas atuais com a nova parcela tambem nao ultrapassa `30%` da renda estimada

Quando qualquer uma dessas condicoes falha, o resultado e de reprovacao.

### Regra de Seguranca da Parcela

Seja:

- `limite_parcela = renda_estimada x 0,30`

Entao:

- se `parcela_novo_emprestimo > limite_parcela`, o credito nao pode ser aprovado;
- se `parcela_emprestimo_atual + parcela_novo_emprestimo > limite_parcela`, o credito nao pode ser aprovado.

## Regra de Saida

Para manter aderencia ao criterio de aceite do projeto, o sistema exibe:

- `Resultado: Aprovado`
- `Resultado: Reprovado`

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
10. verificacao da regra de comprometimento maximo de `30%` da renda;
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
- a decisao depende primeiro do score social calculado;
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
