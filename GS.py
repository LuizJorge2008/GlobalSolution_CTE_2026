
# ============================================================
# GLOBAL SOLUTION 2026 - COMPUTATIONAL THINKING FOR ENGINEERING
# Central de Monitoramento Ambiental
# Ambiente: sala de estudos comunitaria climatizada
# ============================================================

# LIMITES DE REFERENCIA
#
# Temperatura: 24 a 27 °C
# Faixa DIDATICA adaptada de referencias de conforto termico
# para ambientes educacionais climatizados em condicoes de verao
# Fonte: ASHRAE Handbook - Educational Facilities
# https://handbook.ashrae.org/handbooks/A19/SI/A19_Ch08/a19_ch08_si.aspx
TEMP_MIN = 24.0
TEMP_MAX = 27.0

# PM2.5: 15 ug/m3, media de 24 horas
# Cada valor digitado de PM2.5 representa a MEDIA DE 24 HORAS
# de um dia simulado, e NAO uma leitura instantanea
# Fonte: OMS - Global Air Quality Guidelines (2021)
# https://www.who.int/publications/i/item/9789240034228
LIMITE_PM25 = 15.0

# Ruido: 35 dB(A), referencia para salas de aula durante o ensino
# Cada valor digitado representa o nivel sonoro medio equivalente
# durante a atividade de estudos do dia simulado
# Fonte: OMS - Guidelines for Community Noise (1999)
# https://www.who.int/publications-detail-redirect/a68672
LIMITE_RUIDO = 35.0

AMBIENTE = "Sala de estudos comunitaria climatizada"

# Guarda os ciclos apenas enquanto o programa estiver aberto
ciclos = []


def ler_quantidade():
    """Solicita uma quantidade inteira maior que zero."""
    while True:
        try:
            quantidade = int(input("Quantas leituras deseja realizar? "))
            if quantidade > 0:
                return quantidade
            print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Digite um numero inteiro valido.")


def ler_valor(mensagem, nao_negativo=False):
    """Le um numero finito e, quando necessario, nao negativo."""
    while True:
        try:
            entrada = input(mensagem).strip().replace(",", ".")
            valor = float(entrada)

            if valor != valor or valor in (float("inf"), float("-inf")):
                print("Digite um numero finito.")
                continue

            if nao_negativo and valor < 0:
                print("Este valor nao pode ser negativo.")
                continue

            return valor
        except ValueError:
            print("Digite um numero valido, por exemplo 25.5.")


def calcular_estatisticas(valores):
    """Retorna media aritmetica, maior valor e menor valor."""
    media = sum(valores) / len(valores)
    maior = max(valores)
    menor = min(valores)
    return media, maior, menor


def verificar_alertas(temperatura, pm25, ruido):
    """Verifica os tres parametros de forma independente."""
    alertas = []

    if temperatura < TEMP_MIN or temperatura > TEMP_MAX:
        alertas.append("Temperatura fora dos limites estabelecidos")

    if pm25 > LIMITE_PM25:
        alertas.append("Concentracao de PM2.5 acima do limite adotado")

    if ruido > LIMITE_RUIDO:
        alertas.append("Nivel de ruido elevado em relacao ao limite definido")

    return alertas


def montar_relatorio(numero_ciclo, ciclo):
    """Monta o texto exibido na tela e gravado no arquivo TXT."""
    temp = ciclo["estatisticas"]["temperatura"]
    pm = ciclo["estatisticas"]["pm25"]
    ruido = ciclo["estatisticas"]["ruido"]

    linhas = [
        "=" * 60,
        "CENTRAL DE MONITORAMENTO AMBIENTAL",
        f"Ciclo: {numero_ciclo}",
        f"Ambiente: {AMBIENTE}",
        f"Quantidade de leituras: {len(ciclo['leituras'])}",
        "",
        "LIMITES DE REFERENCIA ADOTADOS",
        f"Temperatura: {TEMP_MIN:.1f} a {TEMP_MAX:.1f} °C",
        f"PM2.5: ate {LIMITE_PM25:.1f} ug/m3 (media de 24 horas)",
        f"Ruido: ate {LIMITE_RUIDO:.1f} dB(A) (periodo de estudos)",
        "",
        "ESTATISTICAS",
        f"Temperatura: media={temp[0]:.2f} °C; maior={temp[1]:.2f} °C; menor={temp[2]:.2f} °C",
        f"PM2.5: media={pm[0]:.2f} ug/m3; maior={pm[1]:.2f} ug/m3; menor={pm[2]:.2f} ug/m3",
        f"Ruido: media aritmetica simplificada={ruido[0]:.2f} dB(A); maior={ruido[1]:.2f}; menor={ruido[2]:.2f}",
        "",
        "OCORRENCIAS CRITICAS POR PARAMETRO",
        f"Temperatura: {ciclo['criticas_temperatura']}",
        f"PM2.5: {ciclo['criticas_pm25']}",
        f"Ruido: {ciclo['criticas_ruido']}",
        f"Leituras com pelo menos uma condicao critica: {ciclo['leituras_criticas_totais']}",
        f"Percentual de leituras criticas: {ciclo['percentual_critico']:.2f}%",
        "",
        ciclo["classificacao"],
        "",
        "DETALHAMENTO DAS LEITURAS E ALERTAS",
    ]

    for indice, leitura in enumerate(ciclo["leituras"], start=1):
        linhas.append(
            f"Leitura {indice}: {leitura['temperatura']:.2f} °C; "
            f"PM2.5={leitura['pm25']:.2f} ug/m3; "
            f"ruido={leitura['ruido']:.2f} dB(A)"
        )
        if leitura["alertas"]:
            for alerta in leitura["alertas"]:
                linhas.append(f"  ALERTA: {alerta}")
        else:
            linhas.append("  Leitura dentro dos limites de referencia estabelecidos")

    linhas.extend([
        "",
        "OBSERVACOES",
        "- Esta e uma simulacao didatica baseada nos criterios adotados.",
        "- A classificacao nao e certificacao de seguranca ambiental.",
        "- O criterio de 30% e didatico, nao um limite oficial.",
        "- A media aritmetica de valores de ruido em dB e apenas",
        "  estatistica descritiva simplificada; nao e nivel sonoro",
        "  equivalente nem avaliacao de exposicao acustica.",
        "- Cada valor de PM2.5 representa uma media de 24 horas.",
        "=" * 60,
    ])

    return "\n".join(linhas)


def salvar_relatorio(numero_ciclo, texto):
    """Cria um TXT sem sobrescrever relatorios anteriores."""
    sufixo = 1

    while True:
        nome = f"relatorio_ciclo_{numero_ciclo}_{sufixo}.txt"
        try:
            with open(nome, "x", encoding="utf-8") as arquivo:
                arquivo.write(texto + "\n")
            return nome
        except FileExistsError:
            sufixo += 1


def cadastrar_ciclo():
    """Recebe leituras, emite alertas e calcula os resultados."""
    print("\n=== CADASTRAR NOVO CICLO ===")
    print(f"Ambiente: {AMBIENTE}")
    print(f"Temperatura: {TEMP_MIN:.1f} a {TEMP_MAX:.1f} °C")
    print(f"PM2.5: ate {LIMITE_PM25:.1f} ug/m3 (media de 24h)")
    print(f"Ruido: ate {LIMITE_RUIDO:.1f} dB(A) (periodo de estudos)")

    quantidade = ler_quantidade()
    leituras = []

    criticas_temperatura = 0
    criticas_pm25 = 0
    criticas_ruido = 0
    leituras_criticas_totais = 0

    for numero in range(1, quantidade + 1):
        print(f"\n=== LEITURA {numero} DE {quantidade} ===")

        temperatura = ler_valor("Temperatura (°C): ")
        pm25 = ler_valor("PM2.5 (ug/m3, media de 24h): ", nao_negativo=True)
        ruido = ler_valor("Ruido (dB(A), periodo de estudos): ", nao_negativo=True)

        alertas = verificar_alertas(temperatura, pm25, ruido)

        # Cada parametro critico tem seu proprio contador
        if temperatura < TEMP_MIN or temperatura > TEMP_MAX:
            criticas_temperatura += 1
        if pm25 > LIMITE_PM25:
            criticas_pm25 += 1
        if ruido > LIMITE_RUIDO:
            criticas_ruido += 1

        # Mesmo com tres alertas, a leitura eh contada uma vez
        if alertas:
            leituras_criticas_totais += 1
            for alerta in alertas:
                print("ALERTA:", alerta)
        else:
            print("Leitura dentro dos limites de referencia estabelecidos")

        leituras.append({
            "temperatura": temperatura,
            "pm25": pm25,
            "ruido": ruido,
            "alertas": alertas,
        })

    temperaturas = [leitura["temperatura"] for leitura in leituras]
    concentracoes = [leitura["pm25"] for leitura in leituras]
    ruidos = [leitura["ruido"] for leitura in leituras]

    estatisticas = {
        "temperatura": calcular_estatisticas(temperaturas),
        "pm25": calcular_estatisticas(concentracoes),
        "ruido": calcular_estatisticas(ruidos),
    }

    percentual_critico = (leituras_criticas_totais / quantidade) * 100

    if percentual_critico > 30:
        classificacao = (
            "Estado geral: condicoes ambientais de atencao, com "
            "frequencia de ocorrencias acima do criterio estabelecido"
        )
    else:
        classificacao = (
            "Estado geral: frequencia de ocorrencias dentro do "
            "criterio estabelecido para a simulacao"
        )

    return {
        "leituras": leituras,
        "criticas_temperatura": criticas_temperatura,
        "criticas_pm25": criticas_pm25,
        "criticas_ruido": criticas_ruido,
        "leituras_criticas_totais": leituras_criticas_totais,
        "estatisticas": estatisticas,
        "percentual_critico": percentual_critico,
        "classificacao": classificacao,
    }


def visualizar_ciclos():
    """Exibe os ciclos mantidos em memoria durante a execucao."""
    print("\n=== VISUALIZAR CICLOS ===")

    if not ciclos:
        print("Nenhum ciclo cadastrado.")
        return

    for numero_ciclo, ciclo in enumerate(ciclos, start=1):
        print(f"\nCiclo {numero_ciclo}: {len(ciclo['leituras'])} leituras")
        print(f"Leituras criticas: {ciclo['leituras_criticas_totais']}")
        print(f"Percentual critico: {ciclo['percentual_critico']:.2f}%")
        print(ciclo["classificacao"])

        for numero_leitura, leitura in enumerate(ciclo["leituras"], start=1):
            print(
                f"  Leitura {numero_leitura}: "
                f"{leitura['temperatura']:.2f} °C; "
                f"PM2.5={leitura['pm25']:.2f} ug/m3; "
                f"ruido={leitura['ruido']:.2f} dB(A)"
            )


def perguntar_nova_analise():
    """Pergunta se o usuario deseja iniciar outra sequencia."""
    while True:
        resposta = input("\nDeseja realizar uma nova sequencia? (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("Responda com s ou n.")


def main():
    """Exibe o menu e controla a continuidade do programa."""
    while True:
        print("\n=== CENTRAL DE MONITORAMENTO AMBIENTAL ===")
        print(f"Ambiente: {AMBIENTE}")
        print("1 - Cadastrar informacoes")
        print("2 - Visualizar ciclos")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            print("Digite uma opcao numerica valida.")
            continue

        match opcao:
            case 1:
                ciclo = cadastrar_ciclo()
                ciclos.append(ciclo)

                numero_ciclo = len(ciclos)
                relatorio = montar_relatorio(numero_ciclo, ciclo)
                print("\n" + relatorio)

                nome_arquivo = salvar_relatorio(numero_ciclo, relatorio)
                print(f"Relatorio salvo no arquivo: {nome_arquivo}")

                if not perguntar_nova_analise():
                    print("Programa encerrado.")
                    break

                print("Retornando ao menu. Escolha 1 para iniciar a nova sequencia.")

            case 2:
                visualizar_ciclos()

            case 0:
                print("Programa encerrado.")
                break

            case _:
                print("Opcao invalida.")


if __name__ == "__main__":
    main()
