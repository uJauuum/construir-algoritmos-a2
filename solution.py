import datetime
import requests


def cotar():
    hoje = datetime.date.today()
    cotacoes = []
    ultima_cotacao = None

    url_base = (
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        "CotacaoDolarDia(dataCotacao=@dataCotacao)"
    )

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)
        data_formatada = dia.strftime("%m-%d-%Y")

        parametros = {
            "@dataCotacao": f"'{data_formatada}'",
            "$format": "json"
        }

        try:
            resposta = requests.get(
                url_base,
                params=parametros,
                timeout=15
            )
            resposta.raise_for_status()
            dados = resposta.json()["value"]

            if dados:
                ultima_cotacao = dados[0]["cotacaoCompra"]

            if ultima_cotacao is not None:
                cotacoes.append(ultima_cotacao)

        except requests.RequestException as erro:
            print(f"Erro ao consultar {dia}: {erro}")
            return []

    return cotacoes


if __name__ == "__main__":
    print("Consultando cotações do dólar...")
    resultado = cotar()
    print(resultado)
    print("Quantidade de valores:", len(resultado))