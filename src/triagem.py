def pontuar_despesas(despesas, renda_estimada):
    percentual = despesas / renda_estimada

    if percentual <= 0.70:
        return 100
    if percentual <= 1:
        return 50
    return 0


def pontuar_emprestimos(parcela_emprestimo_atual, renda_estimada):
    if parcela_emprestimo_atual == 0:
        return 100
    if parcela_emprestimo_atual <= renda_estimada * 0.30:
        return 50
    return 0


def pontuar_historico(historico_pagamento_em_dia):
    return 100 if historico_pagamento_em_dia else 0


def pontuar_atividade(tempo_atividade_meses):
    if tempo_atividade_meses <= 6:
        return 0
    if tempo_atividade_meses <= 12:
        return 50
    return 100


def calcular_score_social(
    renda_estimada,
    despesas,
    parcela_emprestimo_atual,
    historico_pagamento_em_dia,
    tempo_atividade_meses,
):
    pontos_despesas = pontuar_despesas(despesas, renda_estimada)
    pontos_emprestimos = pontuar_emprestimos(parcela_emprestimo_atual, renda_estimada)
    pontos_historico = pontuar_historico(historico_pagamento_em_dia)
    pontos_atividade = pontuar_atividade(tempo_atividade_meses)

    pontuacao_total = (
        pontos_despesas
        + pontos_emprestimos
        + pontos_historico
        + pontos_atividade
    )
    return (pontuacao_total / 400) * 100


def converter_historico_pagamento(resposta):
    resposta_normalizada = resposta.strip().lower()
    respostas_positivas = {"s", "sim", "em dia", "emdia"}
    respostas_negativas = {"n", "nao", "não", "atrasado", "atraso"}

    if resposta_normalizada in respostas_positivas:
        return True
    if resposta_normalizada in respostas_negativas:
        return False

    raise ValueError("Resposta invalida para historico de pagamento.")


def calcular_triagem():
    print("--- SISTEMA DE MICROCRÉDITO INCLUSIVO UniFAP ---")

    renda_formal = float(input("Digite a Renda Formal CLT (R$): "))
    renda_estimada = float(input("Digite a Renda Estimada (R$): "))
    despesas = float(input("Digite o valor das Despesas Mensais (R$): "))
    parcela_emprestimo_atual = float(
        input("Digite a Parcela de Emprestimos Atuais (R$): ")
    )
    historico_pagamento = input("Historico de pagamento em dia? (s/n): ")
    tempo_atividade_meses = int(input("Digite o Tempo de Atividade (em meses): "))
    parcela_novo_emprestimo = float(
        input("Digite a Parcela do Novo Emprestimo (R$): ")
    )

    _ = renda_formal

    if renda_estimada <= 0:
        print("Renda estimada invalida. Informe um valor maior que zero.")
        return

    if (
        renda_formal < 0
        or despesas < 0
        or parcela_emprestimo_atual < 0
        or tempo_atividade_meses < 0
        or parcela_novo_emprestimo < 0
    ):
        print("Valores invalidos. Informe apenas numeros maiores ou iguais a zero.")
        return

    try:
        historico_pagamento_em_dia = converter_historico_pagamento(
            historico_pagamento
        )
    except ValueError as erro:
        print(erro)
        return

    score_social = calcular_score_social(
        renda_estimada,
        despesas,
        parcela_emprestimo_atual,
        historico_pagamento_em_dia,
        tempo_atividade_meses,
    )

    limite_parcela = renda_estimada * 0.30
    parcela_total = parcela_emprestimo_atual + parcela_novo_emprestimo

    print(f"Score Social Calculado: {score_social:.2f}")

    if (
        score_social >= 70
        and parcela_novo_emprestimo <= limite_parcela
        and parcela_total <= limite_parcela
    ):
        print("Resultado: Aprovado")
    else:
        print("Resultado: Reprovado")


if __name__ == "__main__":
    calcular_triagem()
