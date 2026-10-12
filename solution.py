import datetime
import requests


def cotar():
    hoje = datetime.date.today()

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)
        data_formatada = dia.strftime("%m-%d-%Y")

        url = (
            "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
            f"CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_formatada}'"
            "&$top=100&$format=json"
        )

        try:
            resposta = requests.get(url, timeout=10)
            resposta.raise_for_status()
            dados = resposta.json()["value"]

            if dados:
                for cotacao in dados:
                    print(
                        dia,
                        "Compra:",
                        cotacao["cotacaoCompra"]
                    )
            else:
                print(dia, "Sem cotação disponível")

        except requests.RequestException as erro:
            print(dia, "Erro na consulta:", erro)


if __name__ == "__main__":
    cotar()