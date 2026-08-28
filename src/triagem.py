def ler_float(mensagem, minimo=0):
    while True:
        try:
            valor = input(mensagem).strip()

            if valor == "":
                print("Erro: este campo não pode ficar vazio.")
                continue

            
            valor = valor.replace(",", ".")
            numero = float(valor)

            if numero < minimo:
                print(f"Erro: informe um valor maior ou igual a {minimo}.")
                continue

            return numero

        except ValueError:
            print("Erro: informe apenas um número válido.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            return None


def ler_int(mensagem, minimo=0):
    while True:
        try:
            valor = input(mensagem).strip()

            if valor == "":
                print("Erro: este campo não pode ficar vazio.")
                continue

            numero = int(valor)

            if numero < minimo:
                print(
                    f"Erro: informe um número inteiro "
                    f"maior ou igual a {minimo}."
                )
                continue

            return numero

        except ValueError:
            print("Erro: informe um número inteiro válido.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            return None


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

def ler_historico():
    while True:
        try:
            resposta = input(
                "Historico de pagamento em dia? (s/n): "
            )

            try:
                return converter_historico_pagamento(resposta)

            except ValueError as erro:
                print(erro)

        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            return None

def calcular_triagem():
    print("--- SISTEMA DE MICROCRÉDITO INCLUSIVO UniFAP ---")

    renda_formal = ler_float(
        "Digite a Renda Formal CLT (R$): "
    )

    if renda_formal is None:
        return


    renda_estimada = ler_float(
        "Digite a Renda Estimada (R$): ",
        minimo=0.01
    )

    if renda_estimada is None:
        return


    despesas = ler_float(
        "Digite o valor das Despesas Mensais (R$): "
    )

    if despesas is None:
        return


    parcela_emprestimo_atual = ler_float(
        "Digite a Parcela de Emprestimos Atuais (R$): "
    )

    if parcela_emprestimo_atual is None:
        return


    historico_pagamento_em_dia = ler_historico()

    if historico_pagamento_em_dia is None:
        return


    tempo_atividade_meses = ler_int(
        "Digite o Tempo de Atividade (em meses): "
    )

    if tempo_atividade_meses is None:
        return


    parcela_novo_emprestimo = ler_float(
        "Digite a Parcela do Novo Emprestimo (R$): "
    )

    if parcela_novo_emprestimo is None:
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
